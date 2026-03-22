"""
fetch_body.py — 記事本文の取得とキャッシュ

各記事URLにHTTPリクエストして本文テキストを抽出する。
取得結果は data/cache/ にその日限りのキャッシュとして保存し、
再実行時のAPI・HTTP負荷を削減する。

対象外リージョン:
  - "research": arXiv のアブストラクトは RSS の summary に既に含まれているため
    本文フェッチは行わない。
"""

import hashlib
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "data" / "cache"

FETCH_TIMEOUT = 10        # HTTP タイムアウト（秒）
MAX_BODY_CHARS = 2000     # Claude に渡す本文の最大文字数

# 本文として優先するセレクタ（順に試行）
BODY_SELECTORS = [
    "article",
    "main article",
    '[class*="article-body"]',
    '[class*="post-content"]',
    '[class*="entry-content"]',
    '[class*="article-content"]',
    '[class*="blog-content"]',
    "main",
    ".content",
]

# 除去対象の要素タグ
NOISE_TAGS = [
    "script", "style", "nav", "header", "footer",
    "aside", "figure", "figcaption", "noscript",
    "iframe", "form", "button", "input",
]

# 本文フェッチをスキップするリージョン
SKIP_REGIONS = {"research"}


def _cache_path(url: str) -> Path:
    """URLのMD5ハッシュをファイル名としたキャッシュパスを返す。"""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    url_hash = hashlib.md5(url.encode()).hexdigest()
    return CACHE_DIR / f"{today}_{url_hash}.txt"


def _load_cache(url: str) -> str | None:
    path = _cache_path(url)
    if path.exists():
        try:
            return path.read_text(encoding="utf-8")
        except Exception:
            return None
    return None


def _save_cache(url: str, body: str) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        _cache_path(url).write_text(body, encoding="utf-8")
    except Exception:
        pass


def _extract_body_text(html: str) -> str:
    """HTML から本文テキストを抽出して返す。"""
    soup = BeautifulSoup(html, "lxml")

    # ノイズ要素を除去
    for tag in soup(NOISE_TAGS):
        tag.decompose()

    # 優先セレクタで本文エリアを探す
    body_node = None
    for selector in BODY_SELECTORS:
        node = soup.select_one(selector)
        if node:
            body_node = node
            break

    target = body_node if body_node else soup.body or soup

    # テキスト抽出：段落ごとに改行を入れて読みやすくする
    paragraphs = []
    for elem in target.find_all(["p", "li", "h1", "h2", "h3", "h4"]):
        text = elem.get_text(" ", strip=True)
        if len(text) > 30:  # 短すぎる断片は無視
            paragraphs.append(text)

    full_text = "\n".join(paragraphs)

    # 連続空白・改行を正規化
    full_text = re.sub(r"\n{3,}", "\n\n", full_text).strip()

    return full_text[:MAX_BODY_CHARS]


def fetch_article_body(url: str) -> str:
    """
    記事URLにHTTPリクエストし、本文テキストを最大 MAX_BODY_CHARS 文字で返す。
    キャッシュがあればそちらを返す。失敗時は空文字列を返す。
    """
    if not url:
        return ""

    # キャッシュ確認
    cached = _load_cache(url)
    if cached is not None:
        return cached

    _RETRY_STATUS = (429, 503)
    _MAX_RETRIES = 2

    try:
        resp = None
        for attempt in range(_MAX_RETRIES + 1):
            resp = requests.get(
                url,
                timeout=FETCH_TIMEOUT,
                headers={
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/122.0.0.0 Safari/537.36"
                    )
                },
            )
            if resp.status_code in _RETRY_STATUS and attempt < _MAX_RETRIES:
                print(f"[warn] fetch_body {resp.status_code} for {url}, retrying ({attempt + 1}/{_MAX_RETRIES})")
                time.sleep(1)
                continue
            break

        resp.raise_for_status()
        body = _extract_body_text(resp.text)
        _save_cache(url, body)
        return body

    except Exception as e:
        print(f"[warn] fetch_body failed for {url}: {e}")
        return ""


def fetch_article_bodies(articles: list[dict]) -> list[dict]:
    """
    記事リストの各記事に body フィールドを付与して返す。
    research リージョンはスキップ（アブストラクトが summary に入っているため）。
    """
    total = len(articles)
    skipped = 0

    for i, article in enumerate(articles, start=1):
        region = article.get("region", "")
        if region in SKIP_REGIONS:
            article["body"] = ""
            skipped += 1
            continue

        url = article.get("link", "")
        body = fetch_article_body(url)
        article["body"] = body

        status = "cached" if _load_cache(url) == body and body else "fetched" if body else "empty"
        print(f"[info] body {i}/{total} ({status}): {article.get('title', '')[:40]}")

    print(f"[info] fetch_bodies complete: {total - skipped} fetched, {skipped} skipped (research)")
    return articles
