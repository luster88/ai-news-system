"""
claude_collect.py — Claude エコシステム情報の収集

data/claude_feeds.yaml に定義されたソースから、
Claude 関連の記事を RSS / サイトスクレイピングで収集する。

既存の collect.py のユーティリティ関数を再利用する。
"""

from pathlib import Path

import feedparser
import yaml
from bs4 import BeautifulSoup

from scripts.collect import (
    _request_html,
    _extract_links,
    _resolve_href,
    canonicalize_url,
    clean_title,
    is_bad_title,
    is_bad_url,
    is_recent_enough,
)
from scripts.config import get as cfg

BASE_DIR = Path(__file__).resolve().parent.parent
CLAUDE_FEEDS_FILE = BASE_DIR / "data" / "claude_feeds.yaml"

MAX_AGE_DAYS = cfg("max_age_days", 14)

# Claude 関連キーワード（filter_keywords が未設定のソースで使用）
CLAUDE_KEYWORDS = [
    "claude", "anthropic", "claude code", "claude console",
    "sonnet", "opus", "haiku", "mcp", "model context protocol",
    "artifacts", "claude api", "claude desktop",
    "cowork", "prompt engineering",
    "claude max", "claude pro", "claude team",
]

# Anthropic サイト用のリンク抽出セレクタ
CLAUDE_SOURCE_SELECTORS = {
    "Anthropic News": [
        "a[href*='/news/']",
        "article a",
        "h2 a",
        "h3 a",
        "main a",
    ],
}


def load_claude_feeds() -> dict:
    """data/claude_feeds.yaml を読み込む。"""
    with open(CLAUDE_FEEDS_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _matches_keywords(text: str, keywords: list[str]) -> bool:
    """テキストにキーワードのいずれかが含まれるか判定する。"""
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def _fetch_rss_claude(url: str, max_items: int, filter_keywords: list[str] | None = None) -> list[dict]:
    """RSS からエントリを取得し、Claude 関連フィルタを適用する。"""
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
        summary = entry.get("summary", "").strip()

        if not title or not link:
            continue

        if is_bad_title(title) or is_bad_url(link):
            continue

        if not is_recent_enough(published, url=link):
            continue

        # filter_keywords によるフィルタ
        keywords = filter_keywords or CLAUDE_KEYWORDS
        search_text = f"{title} {summary}"
        if not _matches_keywords(search_text, keywords):
            continue

        items.append({
            "title": title,
            "link": link,
            "published": published,
            "summary": summary,
        })

        if len(items) >= max_items:
            break

    return items


def _fetch_site_claude(source_name: str, url: str, max_items: int, filter_keywords: list[str] | None = None) -> list[dict]:
    """サイトスクレイピングで記事リンクを取得する。"""
    try:
        html_text = _request_html(url)
    except Exception as e:
        print(f"[warn] {source_name}: サイト取得失敗: {e}")
        return []

    soup = BeautifulSoup(html_text, "lxml")

    # ソース固有のセレクタがあればそれを使う
    selectors = CLAUDE_SOURCE_SELECTORS.get(source_name)
    if selectors:
        def _iter_a_tags():
            for selector in selectors:
                for node in soup.select(selector):
                    a_tag = node if getattr(node, "name", "") == "a" else node.find("a")
                    if a_tag is None:
                        continue
                    yield a_tag.get_text(" ", strip=True), a_tag.get("href")

        items = _extract_links(_iter_a_tags(), url, max_items * 2, check_domain=True)
    else:
        # デフォルト: <a> タグを全探索
        def _iter_all_a():
            for a in soup.select("a"):
                yield a.get_text(" ", strip=True), a.get("href")

        items = _extract_links(_iter_all_a(), url, max_items * 2, check_domain=True)

    # filter_keywords でフィルタ
    keywords = filter_keywords or CLAUDE_KEYWORDS
    filtered = [
        item for item in items
        if _matches_keywords(f"{item['title']} {item.get('summary', '')}", keywords)
    ]

    return filtered[:max_items]


def collect_claude_articles() -> tuple[list[dict], dict[str, int]]:
    """Claude 関連の記事を全ソースから収集する。

    戻り値:
        (articles, source_stats)
        - articles: 収集した記事リスト
        - source_stats: ソース名 → 収集件数
    """
    feeds_cfg = load_claude_feeds()
    all_items: list[dict] = []
    source_stats: dict[str, int] = {}

    for group, sources in feeds_cfg.items():
        for src in sources:
            name = src["name"]
            try:
                item_limit = int(src.get("max_items", 10))
                source_type = src["type"]
                filter_kw = src.get("filter_keywords")

                if source_type == "rss":
                    items = _fetch_rss_claude(src["url"], max_items=item_limit, filter_keywords=filter_kw)
                else:
                    items = _fetch_site_claude(
                        source_name=name,
                        url=src["url"],
                        max_items=item_limit,
                        filter_keywords=filter_kw,
                    )

                # group と source メタデータを付与
                for item in items:
                    item["group"] = group
                    item["source"] = name

                source_stats[name] = len(items)
                all_items.extend(items)
                print(f"[info] {name}: {len(items)} articles")

            except Exception as e:
                print(f"[warn] {name}: 収集失敗: {e}")
                source_stats[name] = 0

    print(f"[info] claude collect total: {len(all_items)} articles from {len(source_stats)} sources")
    return all_items, source_stats
