"""
metrics.py — パイプライン実行メトリクスの保存・表示

data/metrics.json に日付キーで実行メトリクスを蓄積する。
python -m scripts.metrics で直近の実行状況を表示する。
"""

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
METRICS_FILE = BASE_DIR / "data" / "metrics.json"


def _load_metrics() -> dict:
    if not METRICS_FILE.exists():
        return {}
    try:
        with open(METRICS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[warn] metrics.json の読み込みに失敗しました: {e}")
        return {}


def save_metrics(date_key: str, entry: dict) -> None:
    """メトリクスを日付キーで保存する（アトミック書き込み）。"""
    data = _load_metrics()
    data[date_key] = entry

    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        tmp_fd, tmp_path = tempfile.mkstemp(
            dir=METRICS_FILE.parent, suffix=".tmp"
        )
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(tmp_path, METRICS_FILE)
        except Exception:
            os.unlink(tmp_path)
            raise
    except Exception as e:
        print(f"[warn] metrics.json の書き込みに失敗しました: {e}")


def show_metrics(days: int = 14) -> None:
    """直近 N 日分のメトリクスをテーブル表示する。"""
    data = _load_metrics()
    if not data:
        print("メトリクスがありません。python -m scripts.main を実行してください。")
        return

    keys = sorted(data.keys(), reverse=True)[:days]

    print(f"=== 収集精度メトリクス (直近{len(keys)}件) ===")
    print(f"{'日付':<12} | {'収集':>4} | {'新規':>4} | {'本文成功率':>8} | {'[暫定]':>6} | {'[解析失敗]':>8} | {'実行時間':>8}")
    print("-" * 75)

    for key in keys:
        e = data[key]
        coll = e.get("collection", {})
        body = e.get("body_fetch", {})
        summ = e.get("summarization", {})

        total_raw = coll.get("total_raw", "?")
        total_new = coll.get("total_new", "?")
        success_rate = body.get("success_rate", 0)
        tentative = summ.get("tentative_count", "?")
        parse_fail = summ.get("parse_failure_count", "?")
        elapsed = e.get("elapsed_seconds", 0)

        rate_str = f"{success_rate:.0%}" if isinstance(success_rate, float) else "?"
        elapsed_str = f"{elapsed:.0f}s" if isinstance(elapsed, (int, float)) else "?"

        print(f"{key:<12} | {total_raw:>4} | {total_new:>4} | {rate_str:>8} | {tentative:>6} | {parse_fail:>8} | {elapsed_str:>8}")

    # 0件ソース警告
    if keys:
        latest = data[keys[0]]
        zero_sources = latest.get("collection", {}).get("sources_zero", [])
        if zero_sources:
            print()
            print(f"=== 0件ソース警告（最新実行） ===")
            for src in zero_sources:
                print(f"  - {src}")


if __name__ == "__main__":
    show_metrics()
