import sys
from pathlib import Path
import yaml

from scripts.collect import fetch_rss, fetch_site, normalize_items
from scripts.seen_urls import (
    load_seen_data,
    filter_seen_articles,
    apply_source_penalties,
)

ROOT = Path(__file__).resolve().parents[1]
FEEDS_FILE = ROOT / "data" / "feeds.yaml"

VALID_REGIONS = {"us", "cn", "jp", "techblog", "research"}


def load_feeds():
    with open(FEEDS_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize(text: str) -> str:
    return (text or "").lower().replace(" ", "").replace("_", "").replace("-", "")


def run_test(region: str, source: dict, seen_data: dict | None = None):
    name = source["name"]
    url = source["url"]
    typ = source["type"]
    max_items = int(source.get("max_items", 5))

    print("=" * 80)
    print(f"[region] {region}")
    print(f"[test] source: {name}")
    print(f"[type] {typ}")
    print(f"[url] {url}")

    try:
        if typ == "rss":
            items = fetch_rss(url, max_items=max_items)
        else:
            items = fetch_site(
                source_name=name,
                url=url,
                max_items=max_items,
            )

        normalized = normalize_items(region, name, items)
    except Exception as e:
        print("[error]", e)
        return

    print(f"[result] collected: {len(normalized)}")

    # --penalties: seen_urls フィルタ結果を表示（読み取り専用）
    if seen_data is not None:
        new_items, seen_items = filter_seen_articles(normalized, seen_data)
        penalized = apply_source_penalties(new_items, seen_data)
        skipped_penalty = len(new_items) - len(penalized)
        print(f"[penalties] new: {len(new_items)}, seen: {len(seen_items)}, penalized: {skipped_penalty}")
        normalized = penalized

    for i, item in enumerate(normalized[:10], start=1):
        print(f"  {i}. {item.get('title', '')}")
        print(f"     {item.get('link', '')}")


def run_region(region: str, feeds: dict, seen_data: dict | None = None):
    sources = feeds.get(region, [])

    print("\n" + "#" * 80)
    print(f"### REGION: {region}")
    print("#" * 80)

    if not sources:
        print("[warn] no sources found")
        return

    for src in sources:
        run_test(region, src, seen_data=seen_data)


def run_source_keyword(keyword: str, feeds: dict, seen_data: dict | None = None):
    found = False
    key = normalize(keyword)

    for region, sources in feeds.items():
        for src in sources:
            if key in normalize(src["name"]):
                run_test(region, src, seen_data=seen_data)
                found = True

    if not found:
        print("source not found:", keyword)


def main():
    feeds = load_feeds()

    # --penalties フラグの検出（seen_urls フィルタのドライラン）
    use_penalties = "--penalties" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--penalties"]

    seen_data = None
    if use_penalties:
        seen_data = load_seen_data()
        seen_urls = seen_data.get("urls", {})
        penalties = seen_data.get("source_penalties", {})
        print(f"[penalties] loaded seen_urls.json: {len(seen_urls)} URLs, {len(penalties)} source penalties")

    # 引数なし: 全region
    if not args:
        for region in feeds:
            run_region(region, feeds, seen_data=seen_data)
        return

    arg = args[0].strip().lower()

    # 国別指定
    if arg in VALID_REGIONS:
        run_region(arg, feeds, seen_data=seen_data)
        return

    # ソース名部分一致
    run_source_keyword(arg, feeds, seen_data=seen_data)


if __name__ == "__main__":
    main()