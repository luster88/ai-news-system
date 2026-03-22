import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from datetime import datetime, timezone, timedelta
import re

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

from scripts.config import get as cfg

BASE_DIR = Path(__file__).resolve().parent.parent
FEEDS_FILE = BASE_DIR / "data" / "feeds.yaml"

MAX_AGE_DAYS = cfg("max_age_days", 14)

BAD_TITLE_EXACT = {
    "sign in to an existing account",
    "by signing up, you agree to our privacy policy.",
    "download press kit",
    "semiconductor",
    "economic futures",
    "business",
    "business business",
    "learning",
    "learning learning",
    "engineering",
    "engineering engineering",
    "dynamiclake",
}

BAD_TITLE_CONTAINS = [
    "sign in",
    "privacy policy",
    "press kit",
    "cookie",
    "subscribe",
    "subscription",
    "log in",
    "login",
    "register",
    "terms of service",
    "newsletter",
    "advertise",
    "contact us",
    "about us",
]

BAD_URL_CONTAINS = [
    "/login",
    "/signin",
    "/signup",
    "/register",
    "/privacy",
    "/terms",
    "/cookies",
    "/press",
    "/account",
    "/subscription",
    "/advertising",
    "/tag/",
    "/tags/",
    "/category/",
    "/categories/",
    "/authors/",
    "/author/",
]

GOOD_AI_KEYWORDS = [
    "ai",
    "artificial intelligence",
    "llm",
    "gpt",
    "agent",
    "agents",
    "openai",
    "anthropic",
    "claude",
    "gemini",
    "deepseek",
    "qwen",
    "ernie",
    "minimax",
    "kimi",
    "moonshot",
    "zhipu",
    "glm",
    "baidu",
    "alibaba",
    "tencent",
    "bytedance",
    "model",
    "models",
    "bot",
    "chatbot",
    "生成ai",
    "生成ＡＩ",
    "人工知能",
    "大規模言語モデル",
    "エージェント",
    "半導体",
]

SITE_ONLY_MIN_TITLE_LEN = 18

# 先頭に付いてくるカテゴリ語を削る
CATEGORY_PREFIXES = [
    "公共",
    "ビジネス",
    "ラーニング",
    "エンジニアリング",
    "テクノロジー",
    "特集",
    "ニュース",
    "事例",
]

# CN系を中心に、媒体ごとの取りやすいセレクタを定義
# techblog リージョンでは RSS でも AI キーワードフィルタを適用する
AI_FILTER_REGIONS = {"techblog"}

SOURCE_SELECTORS = {
    "nyosegawa blog": [
        "article a",
        "h2 a",
        "h3 a",
        ".entry-title a",
        ".post-title a",
        "main a",
    ],
    "Qwen Research": [
        "a[href*='qwen.ai/blog?id=']",
        "a[href*='/blog?id=']",
        "article a",
        "main a",
    ],
    "ERNIE Blog": [
        "article",
        "main article",
        "main > div",
    ],
    "MiniMax News": [
        "article a",
        "main a",
        ".news a",
        ".blog a",
    ],
    "36Kr AI": [
        "a[href*='/p/']",
        "a[href*='/information/']",
    ],
    "TechNode News Feed": [
        "article a",
        "h2 a",
        "h3 a",
        ".entry-title a",
        ".post-title a",
        "main a",
    ],
    "36Kr English": [
        "article a",
        "h2 a",
        "h3 a",
        "main a",
    ],
    "KrASIA": [
        "article a",
        "h2 a",
        "h3 a",
        ".entry-title a",
        "main a",
    ],
}

def load_feeds():
    with open(FEEDS_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def clean_title(title: str) -> str:
    t = (title or "").strip()

    if not t:
        return ""

    # 連続空白を正規化
    t = re.sub(r"\s+", " ", t).strip()

    # Ledge系などの
    # 「公共 2026 / 3 / 9 [MON] タイトル」
    # 「ビジネス 2026 / 3 / 13 [FRI] タイトル」
    # のような先頭を削る
    category_pattern = "|".join(re.escape(x) for x in CATEGORY_PREFIXES)
    t = re.sub(
        rf"^(?:{category_pattern})\s+20\d{{2}}\s*/\s*\d{{1,2}}\s*/\s*\d{{1,2}}\s*\[[A-Z]{{3}}\]\s*",
        "",
        t,
        flags=re.IGNORECASE,
    ).strip()

    # カテゴリ語だけが先頭に単独で付く場合も削る
    t = re.sub(
        rf"^(?:{category_pattern})\s+",
        "",
        t,
        flags=re.IGNORECASE,
    ).strip()

    # 区切り記号だけ残るケースを軽く整形
    t = re.sub(r"^[\-–—:：/\|\]\[()\s]+", "", t).strip()

    return t


def canonicalize_url(url: str) -> str:
    u = (url or "").strip()
    if not u:
        return ""

    parsed = urlparse(u)
    path = parsed.path.rstrip("/")

    # query / fragment を捨てて URL の揺れを減らす
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def is_bad_title(title: str) -> bool:
    t = clean_title(title).lower()
    if not t:
        return True

    if t in BAD_TITLE_EXACT:
        return True

    return any(bad in t for bad in BAD_TITLE_CONTAINS)


def is_bad_url(url: str) -> bool:
    u = (url or "").strip().lower()
    if not u:
        return True

    return any(bad in u for bad in BAD_URL_CONTAINS)


def parse_datetime_safe(value: str):
    if not value:
        return None

    try:
        dt = dateparser.parse(value)
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def extract_date_from_url(url: str):
    if not url:
        return None

    patterns = [
        # /2025/08/21/
        r"/(20\d{2})/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/",
        # /articles/20260314/
        r"/(20\d{2})(0[1-9]|1[0-2])([0-3]\d)/",
        # 2026-03-14 / 2026_03_14
        r"(20\d{2})[_\-](0[1-9]|1[0-2])[_\-]([0-3]\d)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if not match:
            continue

        try:
            year, month, day = match.groups()
            return datetime(
                int(year),
                int(month),
                int(day),
                tzinfo=timezone.utc,
            )
        except Exception:
            continue

    return None


def is_recent_enough(published: str, url: str = "") -> bool:
    dt = parse_datetime_safe(published)

    if dt is None and url:
        dt = extract_date_from_url(url)

    if dt is None:
        return True

    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_AGE_DAYS)
    return dt >= cutoff


def looks_like_real_article(
    title: str,
    url: str,
    source_type: str,
    published: str = "",
) -> bool:
    cleaned_title = clean_title(title)

    if is_bad_title(cleaned_title) or is_bad_url(url):
        return False

    if source_type == "site" and len(cleaned_title) < SITE_ONLY_MIN_TITLE_LEN:
        return False

    if source_type == "site":
        text = f"{cleaned_title} {url}".lower()
        if not any(keyword in text for keyword in GOOD_AI_KEYWORDS):
            return False

    if not is_recent_enough(published, url=url):
        return False

    return True


def fetch_rss(url: str, max_items: int = 20):
    parsed = feedparser.parse(url)
    if parsed.bozo:
        print(f"[warn] RSS parse issue ({url}): {parsed.bozo_exception}")
    items = []

    for entry in parsed.entries[: max_items * 5]:
        published = (
            entry.get("published", "")
            or entry.get("updated", "")
            or entry.get("created", "")
        )

        title = clean_title(entry.get("title", "").strip())
        link = canonicalize_url(entry.get("link", "").strip())

        item = {
            "title": title,
            "link": link,
            "published": published,
            "summary": entry.get("summary", "").strip(),
        }

        if looks_like_real_article(
            item["title"],
            item["link"],
            "rss",
            published=item["published"],
        ):
            items.append(item)

        if len(items) >= max_items:
            break

    return items


def _request_html(url: str):
    _RETRY_STATUS = (429, 503)
    _MAX_RETRIES = 2

    r = None
    for attempt in range(_MAX_RETRIES + 1):
        r = requests.get(
            url,
            timeout=30,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
                )
            },
        )
        if r.status_code in _RETRY_STATUS and attempt < _MAX_RETRIES:
            print(f"[warn] _request_html {r.status_code} for {url}, retrying ({attempt + 1}/{_MAX_RETRIES})")
            time.sleep(1)
            continue
        break

    r.raise_for_status()
    return r.text


def extract_links_by_selectors(
    soup: BeautifulSoup,
    base_url: str,
    selectors: list[str],
    max_items: int,
):
    items = []
    seen_links = set()

    for selector in selectors:
        for node in soup.select(selector):
            a_tag = node if getattr(node, "name", "") == "a" else node.find("a")
            if a_tag is None:
                continue

            raw_title = a_tag.get_text(" ", strip=True)
            title = clean_title(raw_title)
            href = a_tag.get("href")

            if not title or not href:
                continue

            if href.startswith("/"):
                href = urljoin(base_url, href)

            href = canonicalize_url(href)

            if not href.startswith("http"):
                continue

            try:
                src_netloc = urlparse(base_url).netloc
                dst_netloc = urlparse(href).netloc
                if src_netloc and dst_netloc and src_netloc not in dst_netloc:
                    continue
            except Exception:
                pass

            if not looks_like_real_article(title, href, "site"):
                continue

            if href in seen_links:
                continue
            seen_links.add(href)

            items.append({
                "title": title,
                "link": href,
                "published": "",
                "summary": "",
            })

            if len(items) >= max_items:
                return items

    return items

def extract_ernie_blog_items(soup: BeautifulSoup, base_url: str, max_items: int):
    items = []
    seen_links = set()

    for a in soup.select("a"):
        href = a.get("href")
        if not href:
            continue

        if href.startswith("/"):
            href = urljoin(base_url, href)
        href = canonicalize_url(href)

        if not href.startswith("http"):
            continue

        # ERNIE blog 配下の記事っぽいURLだけを優先
        if "/blog/" not in href and "/publication/" not in href:
            continue

        # タイトルは a テキストが空のことがあるので、近くの見出しを探す
        title = clean_title(a.get_text(" ", strip=True))

        if not title:
            parent = a.parent
            if parent:
                heading = parent.find_next(["h1", "h2", "h3"])
                if heading:
                    title = clean_title(heading.get_text(" ", strip=True))

        if not title:
            continue

        if not looks_like_real_article(title, href, "site"):
            continue

        if href in seen_links:
            continue
        seen_links.add(href)

        items.append({
            "title": title,
            "link": href,
            "published": "",
            "summary": "",
        })

        if len(items) >= max_items:
            break

    return items

def extract_36kr_ai_items(soup: BeautifulSoup, base_url: str, max_items: int):
    items = []
    seen_links = set()

    # 36Kr AIページは本文エリアに記事リンクが並ぶ
    selectors = [
        "a[href*='/p/']",
        "a[href*='/information/']",
    ]

    for selector in selectors:
        for a in soup.select(selector):
            href = a.get("href")
            if not href:
                continue

            if href.startswith("/"):
                href = urljoin(base_url, href)

            href = canonicalize_url(href)

            if not href.startswith("http"):
                continue

            # 36kr.com ドメインだけ
            if "36kr.com" not in href:
                continue

            title = clean_title(a.get_text(" ", strip=True))
            if not title:
                continue

            # 明らかなナビやカテゴリを除外
            if len(title) < 10:
                continue
            if title in {"AI", "推荐", "最新", "财经", "科技", "查看更多"}:
                continue

            if not looks_like_real_article(title, href, "site"):
                continue

            if href in seen_links:
                continue
            seen_links.add(href)

            items.append({
                "title": title,
                "link": href,
                "published": "",
                "summary": "",
            })

            if len(items) >= max_items:
                return items

    return items

def fetch_site_source_specific(source_name: str, url: str, max_items: int = 20):
    html = _request_html(url)
    soup = BeautifulSoup(html, "lxml")

    if source_name == "ERNIE Blog":
        return extract_ernie_blog_items(soup, url, max_items)

    if source_name == "36Kr AI":
        return extract_36kr_ai_items(soup, url, max_items)

    selectors = SOURCE_SELECTORS.get(source_name, [])
    if not selectors:
        return []

    return extract_links_by_selectors(
        soup=soup,
        base_url=url,
        selectors=selectors,
        max_items=max_items,
    )


def fetch_site_simple(url: str, max_items: int = 20):
    html = _request_html(url)
    soup = BeautifulSoup(html, "lxml")

    items = []
    seen_links = set()

    for a in soup.select("a"):
        raw_title = a.get_text(" ", strip=True)
        title = clean_title(raw_title)
        href = a.get("href")

        if not title or not href:
            continue

        if href.startswith("/"):
            href = urljoin(url, href)

        href = canonicalize_url(href)

        if not href.startswith("http"):
            continue

        try:
            src_netloc = urlparse(url).netloc
            dst_netloc = urlparse(href).netloc
            if src_netloc and dst_netloc and src_netloc not in dst_netloc:
                continue
        except Exception:
            pass

        if not looks_like_real_article(title, href, "site"):
            continue

        # URL単位で重複除去
        if href in seen_links:
            continue
        seen_links.add(href)

        items.append({
            "title": title,
            "link": href,
            "published": "",
            "summary": "",
        })

        if len(items) >= max_items:
            break

    return items


def fetch_site(source_name: str, url: str, max_items: int = 20):
    if source_name in SOURCE_SELECTORS:
        try:
            items = fetch_site_source_specific(
                source_name=source_name,
                url=url,
                max_items=max_items,
            )
            if items:
                return items
        except Exception as e:
            print(f"[warn] source-specific fallback to generic for {source_name}: {e}")

    return fetch_site_simple(url=url, max_items=max_items)


def normalize_items(region: str, source_name: str, items: list):
    out = []
    seen_links = set()

    for item in items:
        link = canonicalize_url(item.get("link", "").strip())
        title = clean_title(item.get("title", "").strip())

        if not link or not title:
            continue

        # URL単位で優先して重複除去
        if link in seen_links:
            continue
        seen_links.add(link)

        out.append({
            "region": region,
            "source": source_name,
            "title": title,
            "link": link,
            "published": item.get("published", ""),
            "summary": item.get("summary", ""),
        })

    return out


def dedupe_articles(items: list):
    out = []
    seen_links = set()

    for item in items:
        link = canonicalize_url(item.get("link", "").strip())
        if not link:
            continue

        # URL単位で最終重複除去
        if link in seen_links:
            continue
        seen_links.add(link)

        item["title"] = clean_title(item.get("title", ""))
        item["link"] = link
        out.append(item)

    return out


def collect_articles():
    cfg = load_feeds()
    all_items = []

    for region, sources in cfg.items():
        for src in sources:
            try:
                item_limit = int(src.get("max_items", 20))
                source_type = src["type"]

                if source_type == "rss":
                    items = fetch_rss(src["url"], max_items=item_limit)
                else:
                    items = fetch_site(
                        source_name=src["name"],
                        url=src["url"],
                        max_items=item_limit,
                    )

                normalized = normalize_items(region, src["name"], items)

                # techblog リージョンの RSS は AI キーワードフィルタを追加適用
                if region in AI_FILTER_REGIONS and source_type == "rss":
                    normalized = [
                        a for a in normalized
                        if any(
                            kw in f"{a.get('title', '')} {a.get('summary', '')}".lower()
                            for kw in GOOD_AI_KEYWORDS
                        )
                    ]

                all_items.extend(normalized)
                print(f"[info] collected {len(normalized)} from {src['name']}")

            except Exception as e:
                print(f"[warn] {src['name']}: {e}")

    return dedupe_articles(all_items)