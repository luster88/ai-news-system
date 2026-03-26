"""
favorites.py — お気に入り記事の管理CLI

使い方:
  python -m scripts.favorites add URL --tags tag1,tag2 [--memo "メモ"]
  python -m scripts.favorites remove URL
  python -m scripts.favorites list [--tag TAG]
  python -m scripts.favorites tags
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
FAV_FILE = BASE_DIR / "data" / "favorites.yaml"
NEWS_DIR = BASE_DIR / "news"


def _load() -> list[dict]:
    if not FAV_FILE.exists():
        return []
    with open(FAV_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("favorites", []) or []


def _save(favorites: list[dict]) -> None:
    FAV_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        yaml.dump(
            {"favorites": favorites},
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )


def _find_article_in_news(url: str) -> dict | None:
    """日報ファイルからURLに一致する記事情報を検索する。"""
    for md_file in sorted(NEWS_DIR.glob("*/*/*.md"), reverse=True):
        if md_file.name.startswith(("prev-", "test-")):
            continue
        text = md_file.read_text(encoding="utf-8")
        if url not in text:
            continue

        # 記事のタイトルを抽出
        lines = text.splitlines()
        title = None
        source_date = None

        # frontmatter から日付取得
        for line in lines:
            m = re.match(r"^date:\s*(.+)", line)
            if m:
                source_date = m.group(1).strip()
                break

        # URLを含むセクションのタイトルを取得
        for i, line in enumerate(lines):
            if url in line:
                # 上方向に ### を探す
                for j in range(i - 1, max(i - 5, -1), -1):
                    if lines[j].startswith("### "):
                        raw_title = lines[j].lstrip("# ").strip()
                        # "1. タイトル" の番号を除去
                        title = re.sub(r"^\d+\.\s*", "", raw_title)
                        break
                break

        if title:
            return {"title": title, "source_date": source_date or ""}

    return None


def cmd_add(args: argparse.Namespace) -> None:
    favorites = _load()

    # 重複チェック
    if any(f["url"] == args.url for f in favorites):
        print(f"[skip] 既に登録済みです: {args.url}")
        return

    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []

    # 日報から記事情報を検索
    info = _find_article_in_news(args.url)
    title = args.title or (info["title"] if info else args.url)
    source_date = info["source_date"] if info else ""

    entry = {
        "url": args.url,
        "title": title,
        "user_tags": tags,
        "added": str(date.today()),
        "source_date": source_date,
    }
    if args.memo:
        entry["memo"] = args.memo

    favorites.append(entry)
    _save(favorites)
    print(f"[add] {title}")
    if tags:
        print(f"  tags: {', '.join(tags)}")


def cmd_remove(args: argparse.Namespace) -> None:
    favorites = _load()
    before = len(favorites)
    favorites = [f for f in favorites if f["url"] != args.url]
    if len(favorites) == before:
        print(f"[skip] 見つかりません: {args.url}")
        return
    _save(favorites)
    print(f"[remove] {args.url}")


def cmd_list(args: argparse.Namespace) -> None:
    favorites = _load()
    if args.tag:
        favorites = [f for f in favorites if args.tag in f.get("user_tags", [])]

    if not favorites:
        print("お気に入りはありません。")
        return

    for i, f in enumerate(favorites, 1):
        tags_str = ", ".join(f.get("user_tags", []))
        print(f"{i}. [{f.get('source_date', '')}] {f['title']}")
        print(f"   URL: {f['url']}")
        if tags_str:
            print(f"   Tags: {tags_str}")
        if f.get("memo"):
            print(f"   Memo: {f['memo']}")
        print()


def cmd_tags(args: argparse.Namespace) -> None:
    favorites = _load()
    tag_counts: dict[str, int] = {}
    for f in favorites:
        for t in f.get("user_tags", []):
            tag_counts[t] = tag_counts.get(t, 0) + 1

    if not tag_counts:
        print("タグはまだありません。")
        return

    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {tag} ({count})")


def main() -> None:
    parser = argparse.ArgumentParser(description="お気に入り記事管理")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="記事をお気に入りに追加")
    p_add.add_argument("url", help="記事のURL")
    p_add.add_argument("--tags", "-t", default="", help="カンマ区切りのタグ")
    p_add.add_argument("--title", default="", help="タイトル（省略時は日報から自動取得）")
    p_add.add_argument("--memo", "-m", default="", help="メモ")

    p_rm = sub.add_parser("remove", help="お気に入りから削除")
    p_rm.add_argument("url", help="削除する記事のURL")

    p_list = sub.add_parser("list", help="お気に入り一覧")
    p_list.add_argument("--tag", "-t", default="", help="タグでフィルタ")

    sub.add_parser("tags", help="タグ一覧")

    args = parser.parse_args()
    if args.command == "add":
        cmd_add(args)
    elif args.command == "remove":
        cmd_remove(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "tags":
        cmd_tags(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
