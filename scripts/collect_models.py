"""
collect_models.py — AIモデル情報の収集

情報ソース:
  1. 既存の日報 Markdown からモデル関連記事を抽出
  2. 各社公式ページからモデル・料金情報をスクレイピング
  3. Artificial Analysis からベンチマーク/ランキング情報を取得
"""

import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "news"

FETCH_TIMEOUT = 15

# モデル関連記事を抽出するためのキーワード
MODEL_KEYWORDS = [
    "gpt-4", "gpt-5", "gpt4", "gpt5", "o1", "o3", "o4-mini",
    "claude", "sonnet", "opus", "haiku",
    "gemini", "gemma",
    "llama", "meta ai",
    "mistral", "mixtral",
    "deepseek",
    "qwen",
    "grok",
    "phi-", "phi4",
    "command-r", "command r",
    "stable diffusion", "dall-e", "midjourney", "imagen",
    "sora", "veo",
    "whisper",
    "codex",
]

# 主要プロバイダーの料金ページ
PRICING_SOURCES = [
    {
        "provider": "Anthropic",
        "url": "https://docs.anthropic.com/en/docs/about-claude/models",
    },
    {
        "provider": "Google",
        "url": "https://ai.google.dev/pricing",
    },
    {
        "provider": "Artificial Analysis (総合比較)",
        "url": "https://artificialanalysis.ai/leaderboards/models",
    },
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}


def _request_html(url: str) -> str:
    r = requests.get(url, timeout=FETCH_TIMEOUT, headers=HEADERS)
    r.raise_for_status()
    return r.text


def _extract_text(html: str) -> str:
    """HTML からテキストを抽出する。"""
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return soup.get_text("\n", strip=True)


# ---------------------------------------------------------------------------
# 1. 既存日報からモデル関連記事を抽出
# ---------------------------------------------------------------------------

def _parse_daily_report(filepath: Path) -> list[dict]:
    """日報 Markdown から記事情報を抽出する。"""
    text = filepath.read_text(encoding="utf-8")
    articles = []

    # フロントマターから日付を取得
    date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    report_date = date_match.group(1) if date_match else filepath.stem

    # ### で始まる記事ブロックを抽出
    blocks = re.split(r"^### \d+\.\s+", text, flags=re.MULTILINE)

    for block in blocks[1:]:  # 最初の空ブロックをスキップ
        lines = block.strip().splitlines()
        if not lines:
            continue

        title = lines[0].strip()
        source = ""
        link = ""
        summary = ""
        tags = []
        importance = 0

        for line in lines[1:]:
            line = line.strip()
            if line.startswith("- Source:"):
                source = line.replace("- Source:", "").strip()
            elif line.startswith("- Link:"):
                link_match = re.search(r"\[(.+?)\]\((.+?)\)", line)
                if link_match:
                    link = link_match.group(2)
                else:
                    link = line.replace("- Link:", "").strip()
            elif line.startswith("- Summary:"):
                summary = line.replace("- Summary:", "").strip()
            elif line.startswith("- Tags:"):
                tags = [t.strip() for t in line.replace("- Tags:", "").split(",")]
            elif line.startswith("- Importance:"):
                try:
                    importance = int(line.replace("- Importance:", "").strip())
                except ValueError:
                    pass

        if title and link:
            articles.append({
                "title": title,
                "link": link,
                "source": source,
                "summary_ja": summary,
                "tags": tags,
                "importance_score": importance,
                "report_date": report_date,
            })

    return articles


def _is_model_related(article: dict) -> bool:
    """記事がモデルリリース/アップデートに関連するか判定する。"""
    text = f"{article.get('title', '')} {article.get('summary_ja', '')}".lower()
    return any(kw in text for kw in MODEL_KEYWORDS)


def collect_model_articles_from_reports(days: int = 14) -> list[dict]:
    """直近 N 日間の日報からモデル関連記事を収集する。"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    cutoff_str = cutoff.strftime("%Y-%m-%d")

    all_articles = []
    for md_file in sorted(NEWS_DIR.glob("*/*/*.md"), reverse=True):
        # prev- ファイルも含める
        stem = md_file.stem.replace("prev-", "")
        if stem < cutoff_str:
            continue

        try:
            articles = _parse_daily_report(md_file)
            model_articles = [a for a in articles if _is_model_related(a)]
            all_articles.extend(model_articles)
        except Exception as e:
            print(f"[warn] parse failed: {md_file.name}: {e}")

    # URL で重複排除（最新の記事を優先）
    seen_links = set()
    deduped = []
    for a in all_articles:
        if a["link"] not in seen_links:
            seen_links.add(a["link"])
            deduped.append(a)

    print(f"[info] collected {len(deduped)} model-related articles from reports")
    return deduped


# ---------------------------------------------------------------------------
# 2. 公式ページからの料金・モデル情報スクレイピング
# ---------------------------------------------------------------------------

def _scrape_page_text(url: str) -> str:
    """URL からページテキストを取得する。失敗時は空文字列を返す。"""
    try:
        html_text = _request_html(url)
        return _extract_text(html_text)
    except Exception as e:
        print(f"[warn] scrape failed: {url}: {e}")
        return ""


def scrape_pricing_pages() -> list[dict]:
    """各社の料金ページからテキストを取得し、プロバイダー情報として返す。"""
    results = []
    for src in PRICING_SOURCES:
        text = _scrape_page_text(src["url"])
        if text:
            results.append({
                "provider": src["provider"],
                "url": src["url"],
                "raw_text": text[:5000],  # Claude に渡す上限
            })
            print(f"[info] scraped pricing: {src['provider']} ({len(text)} chars)")
        else:
            print(f"[warn] no pricing data: {src['provider']}")

    return results


# ---------------------------------------------------------------------------
# 3. Artificial Analysis からランキング情報を取得
# ---------------------------------------------------------------------------

def scrape_leaderboard() -> str:
    """Artificial Analysis のリーダーボードページのテキストを取得する。"""
    url = "https://artificialanalysis.ai/leaderboards/models"
    text = _scrape_page_text(url)
    if text:
        print(f"[info] scraped leaderboard ({len(text)} chars)")
    else:
        print("[warn] leaderboard scrape failed")
    return text[:8000] if text else ""
