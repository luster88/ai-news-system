"""
claude_main.py — Claude エコシステム情報収集パイプライン

使い方:
  python -m scripts.claude_main

実行フロー:
  1. claude_feeds.yaml からソース定義を読み込み
  2. 各ソースから記事を収集
  3. claude_seen_urls.json と照合（URL 重複排除）
  4. 記事本文を取得（fetch_body.py を再利用）
  5. Claude API で要約 + カテゴリ分類
  6. カテゴリ別 Markdown に書き出し
  7. seen_urls を更新
"""

import os
import time
from datetime import datetime, timezone
from pathlib import Path

from scripts.claude_collect import collect_claude_articles
from scripts.claude_summarize import summarize_claude_articles
from scripts.claude_render import render_claude_articles
from scripts.fetch_body import fetch_article_bodies
from scripts.metrics import save_metrics, CLAUDE_METRICS_FILE
from scripts.seen_urls import (
    load_seen_data,
    filter_seen_articles,
    apply_source_penalties,
    compute_source_penalties,
    update_seen_urls,
)

BASE_DIR = Path(__file__).resolve().parent.parent
CLAUDE_SEEN_FILE = BASE_DIR / "data" / "claude_seen_urls.json"


def _save_claude_metrics(
    start_time: float,
    source_stats: dict,
    raw_articles: list,
    new_articles: list,
    seen_articles: list,
    skipped_by_penalty: int,
    fetched_articles: list,
    summarized: list,
    seen_data: dict,
) -> None:
    """Claude パイプラインの実行メトリクスを data/claude_metrics.json に保存する。"""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    body_total = len(fetched_articles)
    body_success = len([a for a in fetched_articles if a.get("body", "").strip()])

    parse_failure_count = sum(
        1 for a in summarized
        if "[解析失敗]" in a.get("summary_ja", "") or "[要約失敗]" in a.get("summary_ja", "")
    )

    active_penalties = sum(
        1 for d in seen_data.get("source_penalties", {}).values()
        if d > today
    )

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(time.time() - start_time, 1),
        "collection": {
            "total_raw": len(raw_articles),
            "total_new": len(new_articles),
            "total_seen": len(seen_articles),
            "total_penalized": skipped_by_penalty,
            "by_source": source_stats,
            "sources_zero": [name for name, count in source_stats.items() if count == 0],
        },
        "body_fetch": {
            "total": body_total,
            "success": body_success,
            "empty": body_total - body_success,
            "skipped": 0,
            "success_rate": round(body_success / body_total, 2) if body_total > 0 else 0,
        },
        "summarization": {
            "selected": len(summarized),
            "parse_failure_count": parse_failure_count,
        },
        "output": {
            "total_items": len(summarized),
            "active_penalties": active_penalties,
        },
    }

    save_metrics(today, entry, file_path=CLAUDE_METRICS_FILE)
    print(f"[info] metrics saved to {CLAUDE_METRICS_FILE.name}")


def main():
    start_time = time.time()
    print(f"[info] claude pipeline started at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # 0. API キー早期チェック
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY is not set — aborting before collection")

    # 1. 収集
    raw_articles, source_stats = collect_claude_articles()
    print(f"[info] collected {len(raw_articles)} raw claude articles")

    # 途中終了時も含めて必ずメトリクスを記録する（0件の日も健全性チェックの対象にする）
    new_articles: list = []
    seen_articles: list = []
    skipped_by_penalty = 0
    filtered_articles: list = []
    summarized: list = []
    seen_data = load_seen_data(file_path=CLAUDE_SEEN_FILE)

    def record_metrics():
        _save_claude_metrics(
            start_time=start_time,
            source_stats=source_stats,
            raw_articles=raw_articles,
            new_articles=new_articles,
            seen_articles=seen_articles,
            skipped_by_penalty=skipped_by_penalty,
            fetched_articles=filtered_articles,
            summarized=summarized,
            seen_data=seen_data,
        )

    if not raw_articles:
        print("[info] no articles collected, pipeline done")
        record_metrics()
        return

    # 2. 既出URLフィルタ（claude_seen_urls.json を使用）
    new_articles, seen_articles = filter_seen_articles(raw_articles, seen_data)
    print(f"[info] {len(seen_articles)} articles skipped (seen), {len(new_articles)} new")

    if not new_articles:
        print("[info] no new articles, pipeline done")
        record_metrics()
        return

    # 3. ペナルティ計算
    seen_data = compute_source_penalties(seen_articles, seen_data)

    # 4. ペナルティ中ソースを除外
    filtered_articles = apply_source_penalties(new_articles, seen_data)
    skipped_by_penalty = len(new_articles) - len(filtered_articles)
    if skipped_by_penalty:
        print(f"[info] {skipped_by_penalty} articles skipped (source penalty)")

    if not filtered_articles:
        print("[info] no articles after penalty filter, pipeline done")
        # seen_urls は更新して記録
        update_seen_urls([], seen_data, file_path=CLAUDE_SEEN_FILE)
        record_metrics()
        return

    # 5. 記事本文を取得（fetch_body.py を再利用）
    filtered_articles = fetch_article_bodies(filtered_articles)

    # 6. 要約・カテゴリ分類
    summarized = summarize_claude_articles(filtered_articles)
    print(f"[info] {len(summarized)} articles after summarization")

    if not summarized:
        print("[info] no articles above importance threshold, pipeline done")
        update_seen_urls(filtered_articles, seen_data, file_path=CLAUDE_SEEN_FILE)
        record_metrics()
        return

    # 7. カテゴリ別 Markdown に書き出し
    written_files = render_claude_articles(summarized)
    print(f"[info] wrote {len(written_files)} file(s)")

    # 8. 今日の新規URLを claude_seen_urls.json に記録
    update_seen_urls(filtered_articles, seen_data, file_path=CLAUDE_SEEN_FILE)

    elapsed = time.time() - start_time
    print(f"[info] claude pipeline finished at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} ({elapsed:.1f}s)")
    print(f"[info] summary: {len(raw_articles)} collected → {len(new_articles)} new → {len(summarized)} published")

    # 9. メトリクス保存
    record_metrics()


if __name__ == "__main__":
    main()
