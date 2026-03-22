"""
test_pipeline.py — テスト用パイプライン

ペナルティ/seen_urls 更新をスキップして全件収集し、
テスト出力として news/YYYY/MM/test-{model}-{date}-{HHMM}.md に保存する。

実行:
  python -m scripts.test_pipeline
  python -m scripts.test_pipeline --model claude-opus-4-6
"""

import os
import sys
import time
from datetime import datetime, timezone

from scripts.collect import collect_articles
from scripts.fetch_body import fetch_article_bodies
from scripts.summarize import summarize_articles
from scripts.cluster_topics import cluster_articles
from scripts.render_markdown import render_daily_markdown
from scripts.config import get as cfg


MODEL_SHORT_NAMES = {
    "claude-sonnet-4-5": "sonnet",
    "claude-opus-4-6": "opus",
    "claude-haiku-4-5": "haiku",
}


def _short_model_name(model: str) -> str:
    return MODEL_SHORT_NAMES.get(model, model.split("-")[-1])


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    # --model 引数の解析
    model = cfg("model", "claude-sonnet-4-5")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for i, a in enumerate(sys.argv[1:], 1):
        if a == "--model" and i < len(sys.argv) - 1:
            model = sys.argv[i + 1]

    short_name = _short_model_name(model)
    now = datetime.now(timezone.utc)
    filename = f"test-{short_name}-{now.strftime('%Y-%m-%d-%H%M')}"

    start_time = time.time()
    print(f"[info] test pipeline started at {now.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"[info] model: {model} ({short_name})")
    print(f"[info] output: {filename}.md")

    # 1. 収集（ペナルティなし）
    raw_articles = collect_articles()
    print(f"[info] collected {len(raw_articles)} raw articles (no penalty filter)")

    # 2. 本文取得
    raw_articles = fetch_article_bodies(raw_articles)

    # 3. 要約（モデル指定）
    result = summarize_articles(raw_articles, model_override=model)
    clustered_articles = cluster_articles(result["articles"])
    result["articles"] = clustered_articles

    # 4. テスト出力（seen_urls 更新なし、index 更新なし）
    output_path = render_daily_markdown(result, filename_override=filename)

    elapsed = time.time() - start_time
    print(f"[info] generated: {output_path}")
    print(f"[info] test pipeline finished ({elapsed:.1f}s)")


if __name__ == "__main__":
    main()
