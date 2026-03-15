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


def load_feeds():
    with open(FEEDS_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def is_bad_title(title: str) -> bool:
    t = (title or "").strip().lower()
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
        # /articles/260314/ のようなケースは今回は対象外
        # /articles/20260314/ のような YYYYMMDD
        r"/(20\d{2})(0[1-9]|1[0-2])([0-3]\d)/",
        # _2026_03_14_ など
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
        # 日付不明はここでは通す
        return True

    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_AGE_DAYS)
    return dt >= cutoff


def looks_like_real_article(
    title: str,
    url: str,
    source_type: str,
    published: str = "",
) -> bool:
    if is_bad_title(title) or is_bad_url(url):
        return False

    title_stripped = (title or "").strip()
    if source_type == "site" and len(title_stripped) < SITE_ONLY_MIN_TITLE_LEN:
        return False

    if source_type == "site":
        text = f"{title} {url}".lower()
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

        item = {
            "title": entry.get("title", "").strip(),
            "link": entry.get("link", "").strip(),
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
    seen = set()

    for a in soup.select("a"):
        title = a.get_text(" ", strip=True)
        href = a.get("href")

        if not title or not href:
            continue

        if href.startswith("/"):
            href = urljoin(url, href)

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

        key = (title.lower(), href)
        if key in seen:
            continue
        seen.add(key)

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
    seen = set()

    for item in items:
        link = item.get("link", "").strip()
        title = item.get("title", "").strip()

        if not link or not title:
            continue

        key = (title.lower(), link)
        if key in seen:
            continue
        seen.add(key)

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
    seen = set()

    for item in items:
        key = (
            item.get("title", "").strip().lower(),
            item.get("link", "").strip(),
        )
        if key in seen:
            continue
        seen.add(key)
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