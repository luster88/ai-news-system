from scripts.collect import collect_articles
from scripts.summarize import summarize_articles
from scripts.render_markdown import render_daily_markdown


def main():
    articles = collect_articles()
    print(f"[info] collected {len(articles)} raw articles")

    result = summarize_articles(articles)
    output_path = render_daily_markdown(result)

    print(f"[info] generated: {output_path}")


if __name__ == "__main__":
    main()