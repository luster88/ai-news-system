from pathlib import Path
from urllib.parse import urljoin, urlparse
from datetime import datetime, timezone, timedelta
import re

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

BASE_DIR = Path(__file__).resolve().parent.parent
FEEDS_FILE = BASE_DIR / "data" / "feeds.yaml"

MAX_AGE_DAYS = 14

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


def fetch_site_simple(url: str, max_items: int = 20):
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
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
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
                    items = fetch_site_simple(src["url"], max_items=item_limit)

                normalized = normalize_items(region, src["name"], items)
                all_items.extend(normalized)
                print(f"[info] collected {len(normalized)} from {src['name']}")

            except Exception as e:
                print(f"[warn] {src['name']}: {e}")

    return dedupe_articles(all_items)