from scripts.collect import collect_articles
from scripts.fetch_body import fetch_article_bodies
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
    # 1. 収集
    raw_articles = collect_articles()
    print(f"[info] collected {len(raw_articles)} raw articles")

    # 2. 既出URLフィルタ
    seen_data = load_seen_data()
    new_articles, seen_articles = filter_seen_articles(raw_articles, seen_data)
    print(f"[info] {len(seen_articles)} articles skipped (seen), {len(new_articles)} new")

    # 3. ペナルティ計算（今日の既出状況から次回以降のペナルティを更新）
    updated_seen_data = compute_source_penalties(seen_articles, raw_articles, seen_data)

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

    output_path = render_daily_markdown(result)
    index_path = build_index()

    # 7. 今日の新規URLを seen_urls.json に記録
    update_seen_urls(filtered_articles, updated_seen_data)

    print(f"[info] generated: {output_path}")
    print(f"[info] updated index: {index_path}")


if __name__ == "__main__":
    main()
