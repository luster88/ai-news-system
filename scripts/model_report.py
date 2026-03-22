"""
model_report.py — 最新AIモデルまとめパイプライン

既存の日報データ + 公式ページスクレイピング + ベンチマークサイトから
モデル情報を収集し、Claude API で構造化して Markdown レポートを生成する。

実行: python -m scripts.model_report
"""

import json
import os

from anthropic import Anthropic
from dotenv import load_dotenv

from scripts.collect_models import (
    collect_model_articles_from_reports,
    scrape_pricing_pages,
    scrape_leaderboard,
)
from scripts.render_model_report import render_model_report

load_dotenv()

MODEL = "claude-sonnet-4-5"


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


def _safe_parse_json(text: str) -> dict | list:
    cleaned = _clean_json_text(text)
    try:
        return json.loads(cleaned)
    except Exception:
        print(f"[warn] JSON parse failed, raw text: {cleaned[:200]}")
        return {}


def _build_articles_text(articles: list[dict]) -> str:
    """記事リストをプロンプト用テキストにする。"""
    lines = []
    for i, a in enumerate(articles, start=1):
        lines.append(
            f"{i}. タイトル: {a.get('title', '')}\n"
            f"   ソース: {a.get('source', '')}\n"
            f"   URL: {a.get('link', '')}\n"
            f"   要約: {a.get('summary_ja', '')}\n"
            f"   日付: {a.get('report_date', '')}"
        )
    return "\n\n".join(lines)


def _build_pricing_text(pricing_data: list[dict]) -> str:
    """料金ページのテキストをプロンプト用にまとめる。"""
    parts = []
    for p in pricing_data:
        parts.append(
            f"=== {p['provider']} ({p['url']}) ===\n"
            f"{p['raw_text'][:3000]}"
        )
    return "\n\n".join(parts)


def structure_model_info(
    client: Anthropic,
    articles: list[dict],
    pricing_data: list[dict],
    leaderboard_text: str,
) -> dict:
    """Claude API を使ってモデル情報を構造化する。"""
    articles_text = _build_articles_text(articles)
    pricing_text = _build_pricing_text(pricing_data)

    prompt = f"""
あなたはAIモデルの専門アナリストです。以下の情報源から最新のAIモデル情報を構造化してください。

## 情報源1: 直近のAIニュース記事（モデル関連）
{articles_text if articles_text else "（記事なし）"}

## 情報源2: 各社の料金ページ
{pricing_text if pricing_text else "（料金情報なし）"}

## 情報源3: ベンチマーク/リーダーボード
{leaderboard_text if leaderboard_text else "（リーダーボード情報なし）"}

## 出力形式
以下のJSON形式で返してください。必ずJSONのみ返してください。

{{
    "overview": [
        "直近のAIモデル動向の要約（3〜5行の配列）"
    ],
    "ranking": [
        {{
            "model_name": "モデル名",
            "provider": "提供元",
            "score": "ベンチマークスコアまたはArenaスコア（数値または文字列）",
            "note": "備考（特徴を簡潔に）"
        }}
    ],
    "pricing": [
        {{
            "model_name": "モデル名",
            "provider": "提供元",
            "input_cost": "入力コスト（$/1M tokens）",
            "output_cost": "出力コスト（$/1M tokens）",
            "cost_rating": "コスパ評価（★1〜5個）"
        }}
    ],
    "categories": {{
        "llm": [
            {{
                "model_name": "モデル名",
                "provider": "提供元",
                "release_date": "リリース日（YYYY-MM-DD または YYYY-MM、不明なら空文字）",
                "summary": "特徴を1行で"
            }}
        ],
        "image": [],
        "audio": [],
        "multimodal": [],
        "other": []
    }},
    "new_updates": [
        {{
            "model_name": "モデル名",
            "provider": "提供元",
            "summary": "アップデート内容の要約（2〜3行）",
            "link": "参照URL（あれば）"
        }}
    ]
}}

注意:
- ranking は性能順（高い順）で最大15件
- pricing は主要モデルを網羅し、入力/出力の料金を明記。最大20件
- コスパ評価は性能と料金のバランスで判断（★が多いほどコスパが良い）
- categories は各カテゴリの代表的なモデルを含める
- new_updates は直近1〜2週間の新モデル/アップデートのみ
- 情報が不足している場合は、確認できた範囲のみ記載し、推測は最小限にする
- 料金は可能な限り正確な数値を使い、不明な場合は "不明" とする
"""

    print("[info] calling Claude API for model structuring...")
    msg = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}],
    )

    text = _extract_text_from_message(msg)
    parsed = _safe_parse_json(text)

    if not isinstance(parsed, dict):
        print("[error] unexpected response format from Claude API")
        return {}

    return parsed


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    client = Anthropic(api_key=api_key)

    # 1. 既存日報からモデル関連記事を収集
    print("[info] === Phase 1: collecting model articles from reports ===")
    model_articles = collect_model_articles_from_reports(days=14)

    # 2. 料金ページをスクレイピング
    print("[info] === Phase 2: scraping pricing pages ===")
    pricing_data = scrape_pricing_pages()

    # 3. リーダーボード情報を取得
    print("[info] === Phase 3: scraping leaderboard ===")
    leaderboard_text = scrape_leaderboard()

    # 4. Claude API でモデル情報を構造化
    print("[info] === Phase 4: structuring with Claude API ===")
    report = structure_model_info(
        client=client,
        articles=model_articles,
        pricing_data=pricing_data,
        leaderboard_text=leaderboard_text,
    )

    if not report:
        print("[error] failed to structure model info")
        return

    # 情報源 URL を追加（重複除去）
    source_urls = []
    seen = set()
    for url in (
        [s["url"] for s in pricing_data]
        + ["https://artificialanalysis.ai/leaderboards/models"]
        + [a.get("link", "") for a in model_articles[:10] if a.get("link")]
    ):
        if url and url not in seen:
            seen.add(url)
            source_urls.append(url)
    report["sources"] = source_urls

    # 5. Markdown レポート生成
    print("[info] === Phase 5: rendering model report ===")
    output_path = render_model_report(report)

    print(f"[info] done: {output_path}")


if __name__ == "__main__":
    main()
