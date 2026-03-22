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
from scripts.seen_urls import (
    load_seen_data,
    filter_seen_articles,
    apply_source_penalties,
    compute_source_penalties,
    update_seen_urls,
)

BASE_DIR = Path(__file__).resolve().parent.parent
CLAUDE_SEEN_FILE = BASE_DIR / "data" / "claude_seen_urls.json"


def main():
    start_time = time.time()
    print(f"[info] claude pipeline started at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # 0. API キー早期チェック
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY is not set — aborting before collection")

    # 1. 収集
    raw_articles, source_stats = collect_claude_articles()
    print(f"[info] collected {len(raw_articles)} raw claude articles")

    if not raw_articles:
        print("[info] no articles collected, pipeline done")
        return

    # 2. 既出URLフィルタ（claude_seen_urls.json を使用）
    seen_data = load_seen_data(file_path=CLAUDE_SEEN_FILE)
    new_articles, seen_articles = filter_seen_articles(raw_articles, seen_data)
    print(f"[info] {len(seen_articles)} articles skipped (seen), {len(new_articles)} new")

    if not new_articles:
        print("[info] no new articles, pipeline done")
        return

    # 3. ペナルティ計算
    updated_seen_data = compute_source_penalties(seen_articles, seen_data)

    # 4. ペナルティ中ソースを除外
    filtered_articles = apply_source_penalties(new_articles, updated_seen_data)
    skipped_by_penalty = len(new_articles) - len(filtered_articles)
    if skipped_by_penalty:
        print(f"[info] {skipped_by_penalty} articles skipped (source penalty)")

    if not filtered_articles:
        print("[info] no articles after penalty filter, pipeline done")
        # seen_urls は更新して記録
        update_seen_urls([], updated_seen_data, file_path=CLAUDE_SEEN_FILE)
        return

    # 5. 記事本文を取得（fetch_body.py を再利用）
    # group フィールドを region として扱えるよう一時的に設定
    for article in filtered_articles:
        article.setdefault("region", article.get("group", ""))

    filtered_articles = fetch_article_bodies(filtered_articles)

    # 6. 要約・カテゴリ分類
    summarized = summarize_claude_articles(filtered_articles)
    print(f"[info] {len(summarized)} articles after summarization")

    if not summarized:
        print("[info] no articles above importance threshold, pipeline done")
        update_seen_urls(filtered_articles, updated_seen_data, file_path=CLAUDE_SEEN_FILE)
        return

    # 7. カテゴリ別 Markdown に書き出し
    written_files = render_claude_articles(summarized)
    print(f"[info] wrote {len(written_files)} file(s)")

    # 8. 今日の新規URLを claude_seen_urls.json に記録
    update_seen_urls(filtered_articles, updated_seen_data, file_path=CLAUDE_SEEN_FILE)

    elapsed = time.time() - start_time
    print(f"[info] claude pipeline finished at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} ({elapsed:.1f}s)")
    print(f"[info] summary: {len(raw_articles)} collected → {len(new_articles)} new → {len(summarized)} published")


if __name__ == "__main__":
    main()
