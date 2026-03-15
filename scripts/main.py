from scripts.collect import collect_articles
from scripts.summarize import summarize_articles
from scripts.cluster_topics import cluster_articles
from scripts.render_markdown import render_daily_markdown
from scripts.build_index import build_index


def main():
    articles = collect_articles()
    print(f"[info] collected {len(articles)} raw articles")

    result = summarize_articles(articles)

    clustered_articles = cluster_articles(result["articles"])
    result["articles"] = clustered_articles

    output_path = render_daily_markdown(result)
    index_path = build_index()

    print(f"[info] generated: {output_path}")
    print(f"[info] updated index: {index_path}")


if __name__ == "__main__":
    main()