from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _group_by_region(articles: list):
    grouped = defaultdict(list)
    for article in articles:
        region = article.get("region", "other")
        grouped[region].append(article)

    for region in grouped:
        grouped[region].sort(
            key=lambda x: x.get("importance_score", 1),
            reverse=True
        )

    return grouped


def _top_stories(articles: list, limit: int = 3):
    return sorted(
        articles,
        key=lambda x: x.get("importance_score", 1),
        reverse=True
    )[:limit]


def _collect_all_tags(articles: list) -> list[str]:
    """全記事のタグを重複なしで収集して返す。"""
    seen = set()
    tags = []
    for a in articles:
        for t in a.get("tags", []):
            if t and t not in seen:
                seen.add(t)
                tags.append(t)
    return sorted(tags)


def _render_article_lines(a: dict, show_region: bool = False) -> list[str]:
    """1記事分の Markdown 行リストを返す（共通ヘルパー）。"""
    lines = []
    if show_region:
        lines.append(f"- Region: {a.get('region', '').upper()}")
    lines.append(f"- Source: {a['source']}")
    lines.append(f"- Link: [{a['link']}]({a['link']})")
    lines.append(f"- Importance: {a.get('importance_score', 1)}")

    tags = a.get("tags", [])
    if tags:
        lines.append(f"- Tags: {', '.join(tags)}")

    lines.append(f"- Summary: {a.get('summary_ja', '').strip()}")

    why = a.get("why_it_matters", "").strip()
    if why:
        lines.append(f"- Why it matters: {why}")

    related = a.get("related_articles", [])
    if related:
        lines.append("- Related:")
        for r in related[:3]:
            lines.append(
                f"  - {r.get('source', '').strip()}: "
                f"[{r.get('title', '').strip()}]({r.get('link', '').strip()})"
            )

    return lines


def render_daily_markdown(result: dict):
    articles = result.get("articles", [])
    overall_summary = result.get("overall_summary", [])

    today = datetime.now().strftime("%Y-%m-%d")
    year, month, _ = today.split("-")

    out_dir = BASE_DIR / "news" / year / month
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{today}.md"

    grouped = _group_by_region(articles)
    top_stories = _top_stories(articles, limit=3)
    all_tags = _collect_all_tags(articles)

    lines = []
    lines.append("---")
    lines.append(f"date: {today}")
    lines.append(f"total_items: {len(articles)}")
    if all_tags:
        lines.append(f"tags: [{', '.join(all_tags)}]")
    lines.append("---")
    lines.append("")
    lines.append(f"# AI News Daily - {today}")
    lines.append("")

    lines.append("## 今日の総括")
    if overall_summary:
        lines.extend(overall_summary)
    else:
        lines.append("- 総括は生成されませんでした。")
    lines.append("")

    lines.append("## 注目3件")
    if top_stories:
        for i, a in enumerate(top_stories, start=1):
            lines.append(f"### {i}. {a['title']}")
            lines.extend(_render_article_lines(a, show_region=True))
            lines.append("")
    else:
        lines.append("- 注目記事を生成できませんでした。")
        lines.append("")

    for region in ["us", "cn", "jp", "techblog", "research"]:
        region_items = grouped.get(region, [])

        region_labels = {
            "research": "RESEARCH（論文・技術ブログ）",
            "techblog": "TECHBLOG（技術ブログ）",
        }
        region_label = region_labels.get(region, region.upper())
        lines.append(f"## {region_label}")

        if not region_items:
            lines.append("- 今日は有効な記事を取得できませんでした。")
            lines.append("")
            continue

        for i, a in enumerate(region_items, start=1):
            lines.append(f"### {i}. {a['title']}")
            lines.extend(_render_article_lines(a))
            lines.append("")

    out_file.write_text("\n".join(lines), encoding="utf-8")
    return str(out_file)
