"""
weekly_report.py — 週次トレンドまとめの生成

直近 WEEKLY_LOOKBACK_DAYS 日分の日報 Markdown から記事情報を集約し、
Claude API で「今週のハイライト・トレンド分析」を含む週報を生成して
news/weekly/YYYY-Www.md に保存する。

使い方:
  python -m scripts.weekly_report

GitHub Actions (daily-news.yml) から毎週月曜に自動実行される。
"""

import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

from scripts.config import get as cfg
from scripts.utils import extract_text_from_message

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "news"
WEEKLY_DIR = NEWS_DIR / "weekly"

MODEL = cfg("model", "claude-sonnet-4-5")
WEEKLY_LOOKBACK_DAYS = cfg("weekly_lookback_days", 7)

SYSTEM_PROMPT = (
    "あなたはAIニュースの編集者です。1週間分の日報記事リストをもとに、"
    "読者が今週の動きを5分で把握できる週報を日本語のMarkdownで作成してください。"
    "見出し・箇条書き以外の余計な前置きや説明は出力しないでください。"
)


def _collect_week_files(today: datetime) -> list[Path]:
    """直近 WEEKLY_LOOKBACK_DAYS 日分の日報ファイルを日付順で返す。"""
    files = []
    for i in range(WEEKLY_LOOKBACK_DAYS - 1, -1, -1):
        d = today - timedelta(days=i)
        path = NEWS_DIR / d.strftime("%Y") / d.strftime("%m") / f"{d.strftime('%Y-%m-%d')}.md"
        if path.exists():
            files.append(path)
    return files


def _parse_daily_articles(text: str) -> list[dict]:
    """日報 Markdown から記事情報（タイトル・ソース・スコア・要約）を抽出する。"""
    articles = []
    current = None

    for line in text.splitlines():
        m = re.match(r"^### \d+\. (.+)$", line)
        if m:
            current = {"title": m.group(1).strip()}
            articles.append(current)
            continue
        if current is None:
            continue
        if line.startswith("- Source: "):
            current["source"] = line[len("- Source: "):].strip()
        elif line.startswith("- Importance: "):
            try:
                current["importance"] = int(line[len("- Importance: "):].strip())
            except ValueError:
                current["importance"] = 1
        elif line.startswith("- Tags: "):
            current["tags"] = line[len("- Tags: "):].strip()
        elif line.startswith("- Summary: "):
            current["summary"] = line[len("- Summary: "):].strip()

    # 注目3件はリージョン別セクションと重複するためタイトルで重複排除
    seen_titles = set()
    deduped = []
    for a in articles:
        if a["title"] in seen_titles:
            continue
        seen_titles.add(a["title"])
        deduped.append(a)

    return deduped


def _build_prompt(daily_data: list[tuple[str, list[dict]]], week_start: str, week_end: str) -> str:
    lines = [
        f"対象期間: {week_start} 〜 {week_end}",
        "",
        "以下は日付ごとのAIニュース記事一覧です（importance は 1〜10 の重要度）。",
        "",
    ]

    for date, articles in daily_data:
        lines.append(f"### {date}")
        for a in sorted(articles, key=lambda x: x.get("importance", 1), reverse=True):
            summary = a.get("summary", "")[:100]
            lines.append(
                f"- [{a.get('importance', 1)}] {a['title']}"
                f"（{a.get('source', '')}）{summary}"
            )
        lines.append("")

    lines.append("""上記をもとに、以下の構成の週報をMarkdownで出力してください:

## 今週のハイライト
最重要ニュース5件を選び、それぞれ「### タイトル」+ 2〜3行の解説（何が起きたか・なぜ重要か）。
同じトピックの続報はまとめて1件として扱う。

## トレンド分析
今週の流れ・注目領域の変化・複数日にまたがる動きを3〜5個の箇条書きで。

## 来週の注目点
今週の動きから予想される来週のウォッチポイントを2〜3個の箇条書きで。""")

    return "\n".join(lines)


def generate_weekly_report() -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    today = datetime.now(timezone.utc)
    files = _collect_week_files(today)
    if not files:
        raise RuntimeError("直近の日報が見つかりません")

    daily_data = []
    total_articles = 0
    for f in files:
        articles = _parse_daily_articles(f.read_text(encoding="utf-8"))
        if articles:
            daily_data.append((f.stem, articles))
            total_articles += len(articles)

    week_start = files[0].stem
    week_end = files[-1].stem
    print(f"[info] weekly_report: {len(files)} daily reports, {total_articles} articles ({week_start} 〜 {week_end})")

    client = Anthropic(api_key=api_key, timeout=180.0)
    msg = client.messages.create(
        model=MODEL,
        max_tokens=3000,
        temperature=0.3,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": _build_prompt(daily_data, week_start, week_end)}],
    )
    body = extract_text_from_message(msg)

    # ISO週番号でファイル名を決定（例: 2026-W28.md）
    iso_year, iso_week, _ = today.isocalendar()
    out_name = f"{iso_year}-W{iso_week:02d}.md"

    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    out_file = WEEKLY_DIR / out_name

    lines = [
        "---",
        f"date: {today.strftime('%Y-%m-%d')}",
        f"week_start: {week_start}",
        f"week_end: {week_end}",
        "---",
        "",
        f"# AI News Weekly - {week_start} 〜 {week_end}",
        "",
        body,
        "",
    ]
    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[info] weekly report generated: {out_file}")
    return str(out_file)


if __name__ == "__main__":
    generate_weekly_report()
