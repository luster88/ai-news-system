import os
import time
from collections import Counter
from datetime import datetime, timezone

from scripts.collect import collect_articles
from scripts.fetch_body import fetch_article_bodies
from scripts.metrics import save_metrics
from scripts.seen_urls import (
    load_seen_data,
    filter_seen_articles,
    apply_source_penalties,
    compute_source_penalties,
    update_seen_urls,
)
from scripts.summarize import summarize_articles
from scripts.cluster_topics import cluster_articles
from scripts.render_markdown import render_daily_markdown
from scripts.build_index import build_index


def main():
    start_time = time.time()
    print(f"[info] pipeline started at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # 0. API キー早期チェック（後段の summarize で使うため）
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY is not set — aborting before collection")

    # 1. 収集
    raw_articles = collect_articles()
    print(f"[info] collected {len(raw_articles)} raw articles")

    # 2. 既出URLフィルタ
    seen_data = load_seen_data()
    new_articles, seen_articles = filter_seen_articles(raw_articles, seen_data)
    print(f"[info] {len(seen_articles)} articles skipped (seen), {len(new_articles)} new")

    # 3. ペナルティ計算（今日の既出状況から次回以降のペナルティを更新）
    updated_seen_data = compute_source_penalties(seen_articles, seen_data)

    # 4. ペナルティ中ソースを除外
    filtered_articles = apply_source_penalties(new_articles, updated_seen_data)
    skipped_by_penalty = len(new_articles) - len(filtered_articles)
    if skipped_by_penalty:
        print(f"[info] {skipped_by_penalty} articles skipped (source penalty)")

    # 5. 記事本文を取得（キャッシュ優先、research リージョンはスキップ）
    filtered_articles = fetch_article_bodies(filtered_articles)

    # 6. 要約・クラスタリング・出力
    result = summarize_articles(filtered_articles)
    clustered_articles = cluster_articles(result["articles"])
    result["articles"] = clustered_articles

    output_path = render_daily_markdown(result, seen_data=updated_seen_data)
    index_path = build_index()

    # 7. 今日の新規URLを seen_urls.json に記録
    update_seen_urls(filtered_articles, updated_seen_data)

    print(f"[info] generated: {output_path}")
    print(f"[info] updated index: {index_path}")

    elapsed = time.time() - start_time
    print(f"[info] pipeline finished at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')} ({elapsed:.1f}s)")

    # 8. メトリクス集計・保存
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    articles = result.get("articles", [])

    # ソース別の収集件数（raw_articles から集計）
    source_counts = Counter(a.get("source", "") for a in raw_articles)
    from scripts.collect import load_feeds
    feeds = load_feeds()
    sources_zero = [
        src["name"]
        for region_sources in feeds.values()
        for src in region_sources
        if source_counts.get(src["name"], 0) == 0
    ]

    # 本文取得の統計（記事の body フィールドから集計）
    body_total = len([a for a in filtered_articles if a.get("region", "") not in {"research"}])
    body_success = len([a for a in filtered_articles if a.get("body", "").strip() and a.get("region", "") not in {"research"}])
    body_skipped = len([a for a in filtered_articles if a.get("region", "") in {"research"}])

    # 要約の統計
    tentative_count = sum(1 for a in articles if "[暫定]" in a.get("summary_ja", ""))
    parse_failure_count = sum(1 for a in articles if "[解析失敗]" in a.get("summary_ja", ""))

    # importance 分布
    scores = [a.get("importance_score", 0) for a in articles]
    importance_dist = {
        "1-2": sum(1 for s in scores if 1 <= s <= 2),
        "3-4": sum(1 for s in scores if 3 <= s <= 4),
        "5-6": sum(1 for s in scores if 5 <= s <= 6),
        "7-8": sum(1 for s in scores if 7 <= s <= 8),
        "9-10": sum(1 for s in scores if 9 <= s <= 10),
    }

    # ペナルティ件数
    active_penalties = sum(
        1 for d in updated_seen_data.get("source_penalties", {}).values()
        if d > today
    )

    metrics_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(elapsed, 1),
        "collection": {
            "total_raw": len(raw_articles),
            "total_new": len(new_articles),
            "total_seen": len(seen_articles),
            "total_penalized": skipped_by_penalty,
            "sources_zero": sources_zero,
        },
        "body_fetch": {
            "total": body_total,
            "success": body_success,
            "empty": body_total - body_success,
            "skipped": body_skipped,
            "success_rate": round(body_success / body_total, 2) if body_total > 0 else 0,
        },
        "summarization": {
            "selected": len(articles),
            "tentative_count": tentative_count,
            "parse_failure_count": parse_failure_count,
            "importance_distribution": importance_dist,
        },
        "output": {
            "total_items": len(articles),
            "active_penalties": active_penalties,
        },
    }

    save_metrics(today, metrics_entry)
    print(f"[info] metrics saved to data/metrics.json")


if __name__ == "__main__":
    main()
