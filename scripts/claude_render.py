"""
claude_render.py — カテゴリ別 Markdown への書き出し

要約済みの記事を、claude/{category}/{slug}.md に追記または新規作成する。
日報形式（日付ごとの1ファイル）ではなく、カテゴリ/サブカテゴリ別に蓄積する。

追記ルール:
  - 同じカテゴリ+サブカテゴリのファイルが既にあれば、日付セクションとして追記
  - 新しいサブカテゴリの場合は新規ファイルを作成
  - frontmatter の updated と sources を更新
"""

import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
CLAUDE_DIR = BASE_DIR / "claude"


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _slugify(text: str) -> str:
    """サブカテゴリ名をファイル名用の slug に変換する。"""
    slug = text.lower().strip()
    slug = re.sub(r"[^a-z0-9\-]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "general"


def _find_existing_file(category: str, subcategory: str) -> Path | None:
    """既存のファイルを subcategory ベースで探す。"""
    cat_dir = CLAUDE_DIR / category
    if not cat_dir.exists():
        return None

    slug = _slugify(subcategory)

    # まず完全一致
    candidate = cat_dir / f"{slug}.md"
    if candidate.exists():
        return candidate

    # slug を含むファイルを探す（例: claude-code → claude-code-updates.md）
    for md_file in cat_dir.glob("*.md"):
        if md_file.name.startswith("_"):
            continue
        if slug in md_file.stem:
            return md_file

    return None


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """YAML frontmatter をパースして (meta, body) を返す。"""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text

    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return {}, text

    raw_yaml = text[4:end_idx]
    body = text[end_idx + 5:]

    try:
        meta = yaml.safe_load(raw_yaml) or {}
    except Exception:
        meta = {}

    return meta, body


def _serialize_frontmatter(meta: dict) -> str:
    """frontmatter を YAML 文字列にシリアライズする。"""
    return "---\n" + yaml.dump(meta, allow_unicode=True, default_flow_style=False, sort_keys=False).strip() + "\n---\n"


def _render_article_section(article: dict) -> str:
    """1記事分の Markdown セクションを生成する。"""
    title = article.get("title", "無題")
    summary = article.get("summary_ja", "")
    source = article.get("source", "")
    link = article.get("link", "")
    score = article.get("importance_score", 0)
    tags = article.get("tags", [])

    tags_str = ", ".join(tags) if tags else ""

    lines = [
        f"### {title}",
        "",
        summary,
        "",
        f"- **ソース**: [{source}]({link})",
        f"- **重要度**: {score}/10",
    ]
    if tags_str:
        lines.append(f"- **タグ**: {tags_str}")
    lines.append("")

    return "\n".join(lines)


def _append_to_existing(file_path: Path, articles: list[dict], today: str) -> None:
    """既存ファイルに日付セクションとして追記する。"""
    raw = file_path.read_text(encoding="utf-8")
    meta, body = _parse_frontmatter(raw)

    # frontmatter の updated を更新
    meta["updated"] = today

    # sources リストに新しいソースを追加
    existing_sources = meta.get("sources", [])
    if not isinstance(existing_sources, list):
        existing_sources = []
    existing_urls = {s.get("url", "") for s in existing_sources if isinstance(s, dict)}

    for article in articles:
        link = article.get("link", "")
        if link and link not in existing_urls:
            existing_sources.append({
                "url": link,
                "title": article.get("title", ""),
                "date": today,
            })
            existing_urls.add(link)
    meta["sources"] = existing_sources

    # tags を統合
    existing_tags = meta.get("tags", [])
    if not isinstance(existing_tags, list):
        existing_tags = []
    new_tags = set(existing_tags)
    for article in articles:
        for tag in article.get("tags", []):
            new_tags.add(tag)
    meta["tags"] = sorted(new_tags)

    # 日付セクションを生成
    section_lines = [
        f"## {today}",
        "",
    ]
    for article in articles:
        section_lines.append(_render_article_section(article))
        section_lines.append("---")
        section_lines.append("")

    new_section = "\n".join(section_lines)

    # 本文の先頭（最初の ## の前、または本文末尾）に挿入
    # 「## 詳細」セクションの直後、または最初の「## YYYY-MM-DD」の前に挿入
    insertion_point = _find_insertion_point(body)
    if insertion_point is not None:
        updated_body = body[:insertion_point] + new_section + "\n" + body[insertion_point:]
    else:
        updated_body = body.rstrip() + "\n\n" + new_section

    file_path.write_text(
        _serialize_frontmatter(meta) + "\n" + updated_body,
        encoding="utf-8",
    )


def _find_insertion_point(body: str) -> int | None:
    """本文中の適切な挿入位置を見つける。
    既存の日付セクション（## YYYY-MM-DD）の直前、または
    「## 詳細」セクションの直後に挿入する。"""

    # 既存の日付セクションを探す（最も新しいものの前に挿入）
    date_pattern = re.compile(r"^## \d{4}-\d{2}-\d{2}", re.MULTILINE)
    match = date_pattern.search(body)
    if match:
        return match.start()

    # 「## 更新履歴」の前に挿入
    history_pattern = re.compile(r"^## 更新履歴", re.MULTILINE)
    match = history_pattern.search(body)
    if match:
        return match.start()

    # 「## 関連リンク」の前に挿入
    related_pattern = re.compile(r"^## 関連リンク", re.MULTILINE)
    match = related_pattern.search(body)
    if match:
        return match.start()

    return None


def _create_new_file(category: str, subcategory: str, articles: list[dict], today: str) -> Path:
    """新規ファイルを作成する。"""
    cat_dir = CLAUDE_DIR / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    slug = _slugify(subcategory)
    file_path = cat_dir / f"{slug}.md"

    # タイトルを生成
    # subcategory から見出し用のタイトルを作成
    display_title = subcategory.replace("-", " ").title()

    all_tags = set()
    sources = []
    for article in articles:
        for tag in article.get("tags", []):
            all_tags.add(tag)
        link = article.get("link", "")
        if link:
            sources.append({
                "url": link,
                "title": article.get("title", ""),
                "date": today,
            })

    meta = {
        "title": display_title,
        "category": category,
        "subcategory": subcategory,
        "tags": sorted(all_tags),
        "date": today,
        "updated": today,
        "sources": sources,
    }

    # 記事セクションを生成
    section_lines = [
        f"# {display_title}",
        "",
        "---",
        "",
        f"## {today}",
        "",
    ]
    for article in articles:
        section_lines.append(_render_article_section(article))
        section_lines.append("---")
        section_lines.append("")

    section_lines.extend([
        "## 関連リンク",
        "",
        f"- [Claude Info トップ](../README.md)",
        "",
        "---",
        "",
        "## 更新履歴",
        "",
        "| 日付 | 内容 |",
        "|------|------|",
        f"| {today} | 自動生成 |",
    ])

    body = "\n".join(section_lines)

    file_path.write_text(
        _serialize_frontmatter(meta) + "\n" + body + "\n",
        encoding="utf-8",
    )

    return file_path


def render_claude_articles(articles: list[dict]) -> list[Path]:
    """要約済み記事をカテゴリ別 Markdown に書き出す。

    引数:
        articles: 要約済みの記事リスト（category/subcategory が付与済み）

    戻り値:
        書き出したファイルパスのリスト
    """
    today = _today()
    written_files: list[Path] = []

    # カテゴリ+サブカテゴリでグループ化
    grouped: dict[tuple[str, str], list[dict]] = {}
    for article in articles:
        cat = article.get("category", "ecosystem")
        subcat = article.get("subcategory", "") or cat
        key = (cat, subcat)
        grouped.setdefault(key, []).append(article)

    for (category, subcategory), group_articles in grouped.items():
        # 既存ファイルを探す
        existing = _find_existing_file(category, subcategory)

        if existing:
            _append_to_existing(existing, group_articles, today)
            written_files.append(existing)
            print(f"[info] claude_render: appended {len(group_articles)} article(s) to {existing.relative_to(BASE_DIR)}")
        else:
            new_file = _create_new_file(category, subcategory, group_articles, today)
            written_files.append(new_file)
            print(f"[info] claude_render: created {new_file.relative_to(BASE_DIR)} with {len(group_articles)} article(s)")

    return written_files
