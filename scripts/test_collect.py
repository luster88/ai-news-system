import sys
from pathlib import Path
import yaml

from scripts.collect import fetch_rss, fetch_site, normalize_items

ROOT = Path(__file__).resolve().parents[1]
FEEDS_FILE = ROOT / "data" / "feeds.yaml"

VALID_REGIONS = {"us", "cn", "jp"}


def load_feeds():
    with open(FEEDS_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize(text: str) -> str:
    return (text or "").lower().replace(" ", "").replace("_", "").replace("-", "")


def run_test(region: str, source: dict):
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

    for i, item in enumerate(normalized[:10], start=1):
        print(f"  {i}. {item.get('title', '')}")
        print(f"     {item.get('link', '')}")


def run_region(region: str, feeds: dict):
    sources = feeds.get(region, [])

    print("\n" + "#" * 80)
    print(f"### REGION: {region}")
    print("#" * 80)

    if not sources:
        print("[warn] no sources found")
        return

    for src in sources:
        run_test(region, src)


def run_source_keyword(keyword: str, feeds: dict):
    found = False
    key = normalize(keyword)

    for region, sources in feeds.items():
        for src in sources:
            if key in normalize(src["name"]):
                run_test(region, src)
                found = True

    if not found:
        print("source not found:", keyword)


def main():
    feeds = load_feeds()

    # 引数なし: 全region
    if len(sys.argv) == 1:
        for region in feeds:
            run_region(region, feeds)
        return

    arg = sys.argv[1].strip().lower()

    # 国別指定
    if arg in VALID_REGIONS:
        run_region(arg, feeds)
        return

    # ソース名部分一致
    run_source_keyword(arg, feeds)


if __name__ == "__main__":
    main()