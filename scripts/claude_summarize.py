"""
claude_summarize.py — Claude エコシステム記事の要約・カテゴリ分類

記事を Claude API で日本語要約し、カテゴリ・サブカテゴリ・タグを自動分類する。
既存の summarize.py のパターンを踏襲しつつ、Claude エコシステム特化のプロンプトを使用。
"""

import json
import os
from collections import Counter

from anthropic import Anthropic
from dotenv import load_dotenv

from scripts.config import get as cfg

load_dotenv()

MODEL = cfg("claude_model", cfg("model", "claude-sonnet-4-5"))
MAX_ARTICLES = cfg("claude_max_articles", 20)
MAX_PER_SOURCE = cfg("claude_max_per_source", 4)
MIN_IMPORTANCE = cfg("claude_min_importance", 4)

# カテゴリ候補
CLAUDE_CATEGORIES = [
    "releases",
    "guides",
    "tools",
    "prompts",
    "troubleshooting",
    "ecosystem",
]

# タグ候補
CLAUDE_TAG_CANDIDATES = [
    "claude-code", "claude-console", "claude-api",
    "opus", "sonnet", "haiku",
    "mcp", "release", "bugfix", "新機能",
    "setup", "windows", "mac", "linux", "vscode",
    "prompt", "pricing", "performance",
    "cursor", "copilot", "cowork",
]

SYSTEM_PROMPT = """\
あなたは Claude エコシステムの専門情報アナリストです。
与えられた記事を分析し、必ず以下の JSON 形式のみで出力してください。
JSON 以外のテキスト（説明文やマークダウン）は絶対に含めないでください。

{
  "summary": "日本語で3-5文の要約",
  "category": "releases | guides | tools | prompts | troubleshooting | ecosystem",
  "subcategory": "カテゴリ内の細分類（kebab-case、例: claude-code, claude-api, setup-windows）",
  "tags": ["タグ1", "タグ2", "タグ3"],
  "importance_score": 1
}

カテゴリ判定基準:
- releases: 新バージョン、機能追加、API変更、モデルアップデート、リリースノート
- guides: セットアップ手順、使い方Tips、ワークフロー、ベストプラクティス
- tools: ツール比較、MCP サーバー、IDE連携、外部ツール情報
- prompts: プロンプトテンプレート、エンジニアリング技法、システムプロンプト
- troubleshooting: エラー対処、環境問題、バグ報告、FAQ
- ecosystem: 料金変更、コミュニティ動向、競合比較、業界ニュース

importance_score の基準:
- 9-10: Claude 公式の重大発表（新モデル・大幅な料金変更・新機能リリース）
- 7-8: 公式の機能追加・API変更・重要なアップデート
- 5-6: 有用な使い方Tips・ツール連携情報・ガイド
- 3-4: コミュニティの議論・マイナーな Tips
- 1-2: 既知情報の繰り返し・関連性の低い記事

tags は以下から最大3つ選択:
""" + ", ".join(CLAUDE_TAG_CANDIDATES)


def _extract_text_from_message(msg) -> str:
    return "".join(
        block.text for block in msg.content
        if getattr(block, "type", "") == "text"
    ).strip()


def _clean_json_text(text: str) -> str:
    text = text.strip()
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    elif text.startswith("```"):
        text = text[len("```"):].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text


def _safe_parse_claude_json(text: str) -> dict:
    """Claude API のレスポンスを安全にパースする。"""
    cleaned = _clean_json_text(text)

    try:
        parsed = json.loads(cleaned)

        # category バリデーション
        category = str(parsed.get("category", "ecosystem")).strip()
        if category not in CLAUDE_CATEGORIES:
            category = "ecosystem"

        # tags バリデーション
        raw_tags = parsed.get("tags", [])
        if isinstance(raw_tags, list):
            tags = [t for t in raw_tags if isinstance(t, str) and t in CLAUDE_TAG_CANDIDATES][:3]
        else:
            tags = []

        return {
            "summary": str(parsed.get("summary", "")).strip(),
            "category": category,
            "subcategory": str(parsed.get("subcategory", "")).strip().lower().replace(" ", "-"),
            "tags": tags,
            "importance_score": max(1, min(10, int(parsed.get("importance_score", 1)))),
        }
    except Exception:
        return {
            "summary": f"[解析失敗] {cleaned[:200]}",
            "category": "ecosystem",
            "subcategory": "",
            "tags": [],
            "importance_score": 1,
        }


def _select_articles(articles: list[dict]) -> list[dict]:
    """ソース偏りを防ぎながら記事を選択する。各ソース最大 MAX_PER_SOURCE 件。"""
    selected: list[dict] = []
    source_counts: Counter = Counter()

    for article in articles:
        if len(selected) >= MAX_ARTICLES:
            break
        source = article.get("source", "unknown")
        if source_counts[source] >= MAX_PER_SOURCE:
            continue
        selected.append(article)
        source_counts[source] += 1

    return selected


def summarize_claude_articles(articles: list[dict]) -> list[dict]:
    """Claude 関連記事を要約・カテゴリ分類する。

    引数:
        articles: 収集済みの記事リスト（各記事は title/link/summary/body 等を持つ）

    戻り値:
        要約済みの記事リスト（summary_ja/category/subcategory/tags/importance_score が追加済み）
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    client = Anthropic(api_key=api_key, timeout=120.0)

    # ソース偏り防止付きの記事選択
    target_articles = _select_articles(articles)
    print(f"[info] claude_summarize: {len(target_articles)}/{len(articles)} articles selected (model={MODEL})")

    api_calls = 0
    results = []

    for article in target_articles:
        title = article.get("title", "")
        body = article.get("body", "")
        summary = article.get("summary", "")
        source = article.get("source", "")
        link = article.get("link", "")

        # 本文がなければ summary をフォールバック
        content = body or summary or title

        user_prompt = f"""以下の記事を分析してください。

タイトル: {title}
ソース: {source}
URL: {link}

本文:
{content[:2000]}"""

        try:
            msg = client.messages.create(
                model=MODEL,
                max_tokens=1000,
                timeout=120,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
            )

            raw_text = _extract_text_from_message(msg)
            parsed = _safe_parse_claude_json(raw_text)
            api_calls += 1

        except Exception as e:
            print(f"[warn] claude_summarize: API error for '{title[:40]}': {e}")
            parsed = {
                "summary": f"[要約失敗] {title}",
                "category": "ecosystem",
                "subcategory": "",
                "tags": [],
                "importance_score": 1,
            }

        # 記事にマージ
        article["summary_ja"] = parsed["summary"]
        article["category"] = parsed["category"]
        article["subcategory"] = parsed["subcategory"]
        article["tags"] = parsed["tags"]
        article["importance_score"] = parsed["importance_score"]

        results.append(article)

    print(f"[info] claude_summarize: {api_calls} API calls, {len(results)} articles processed")

    # importance_score でフィルタ
    filtered = [a for a in results if a["importance_score"] >= MIN_IMPORTANCE]
    skipped = len(results) - len(filtered)
    if skipped:
        print(f"[info] claude_summarize: {skipped} articles below importance threshold ({MIN_IMPORTANCE})")

    return filtered
