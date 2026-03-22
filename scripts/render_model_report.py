"""
render_model_report.py — AIモデルまとめ Markdown 生成

Claude API で構造化されたモデル情報を受け取り、
models/latest.md と models/history/YYYY-MM-DD.md に出力する。
"""

import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
HISTORY_DIR = MODELS_DIR / "history"


def render_model_report(report: dict) -> str:
    """モデルまとめ Markdown を生成して latest.md と history に出力する。"""
    today = datetime.now().strftime("%Y-%m-%d")

    ranking = report.get("ranking", [])
    pricing = report.get("pricing", [])
    categories = report.get("categories", {})
    new_updates = report.get("new_updates", [])
    overview = report.get("overview", [])

    lines = []

    # フロントマター
    lines.append("---")
    lines.append(f"date: {today}")
    lines.append("type: model-report")
    lines.append("---")
    lines.append("")
    lines.append(f"# 最新AIモデルまとめ - {today}")
    lines.append("")

    # 概要
    lines.append("## 概要")
    if overview:
        for line in overview:
            lines.append(f"- {line}")
    else:
        lines.append("- モデル情報の概要を生成できませんでした。")
    lines.append("")

    # 性能ランキング
    lines.append("## 性能ランキング")
    if ranking:
        lines.append("")
        lines.append("| 順位 | モデル名 | 提供元 | スコア | 備考 |")
        lines.append("|---:|---|---|---:|---|")
        for i, m in enumerate(ranking, start=1):
            name = m.get("model_name", "")
            provider = m.get("provider", "")
            score = m.get("score", "")
            note = m.get("note", "")
            lines.append(f"| {i} | {name} | {provider} | {score} | {note} |")
    else:
        lines.append("- ランキング情報を取得できませんでした。")
    lines.append("")

    # コスト比較
    lines.append("## コスト比較")
    if pricing:
        lines.append("")
        lines.append("| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |")
        lines.append("|---|---|---:|---:|---|")
        for m in pricing:
            name = m.get("model_name", "")
            provider = m.get("provider", "")
            input_cost = m.get("input_cost", "")
            output_cost = m.get("output_cost", "")
            cost_rating = m.get("cost_rating", "")
            lines.append(f"| {name} | {provider} | {input_cost} | {output_cost} | {cost_rating} |")
    else:
        lines.append("- コスト情報を取得できませんでした。")
    lines.append("")

    # カテゴリ別モデル一覧
    category_labels = {
        "llm": "LLM（テキスト生成）",
        "image": "画像生成",
        "audio": "音声AI",
        "multimodal": "マルチモーダル",
        "other": "その他",
    }

    lines.append("## カテゴリ別モデル一覧")
    lines.append("")

    for cat_key, cat_label in category_labels.items():
        models = categories.get(cat_key, [])
        lines.append(f"### {cat_label}")
        if models:
            lines.append("")
            lines.append("| モデル名 | 提供元 | リリース日 | 特徴 |")
            lines.append("|---|---|---|---|")
            for m in models:
                name = m.get("model_name", "")
                provider = m.get("provider", "")
                release = m.get("release_date", "")
                feature = m.get("summary", "")
                lines.append(f"| {name} | {provider} | {release} | {feature} |")
        else:
            lines.append("- 該当なし")
        lines.append("")

    # 今週の新モデル・アップデート
    lines.append("## 今週の新モデル・アップデート")
    if new_updates:
        lines.append("")
        for m in new_updates:
            name = m.get("model_name", "")
            provider = m.get("provider", "")
            summary = m.get("summary", "")
            link = m.get("link", "")
            lines.append(f"### {name} ({provider})")
            lines.append(f"- {summary}")
            if link:
                lines.append(f"- 参照: [{link}]({link})")
            lines.append("")
    else:
        lines.append("- 今週の新モデル情報はありません。")
        lines.append("")

    # 情報源
    sources = report.get("sources", [])
    if sources:
        lines.append("## 情報源")
        for s in sources:
            lines.append(f"- [{s}]({s})")
        lines.append("")

    content = "\n".join(lines)

    # 出力
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    latest_path = MODELS_DIR / "latest.md"
    latest_path.write_text(content, encoding="utf-8")

    history_path = HISTORY_DIR / f"{today}.md"
    shutil.copy2(latest_path, history_path)

    print(f"[info] model report: {latest_path}")
    print(f"[info] model report history: {history_path}")
    return str(latest_path)
