"""
metrics.py — パイプライン実行メトリクスの保存・表示

data/metrics.json に日付キーで実行メトリクスを蓄積する。
python -m scripts.metrics で直近の実行状況を表示する。

使い方:
  python -m scripts.metrics              # 直近14件のサマリ + 最新回の詳細
  python -m scripts.metrics --latest     # 最新回の詳細のみ
  python -m scripts.metrics --days 7     # 直近7件のサマリ
"""

import json
import os
import sys
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


def _show_summary(data: dict, days: int = 14) -> None:
    """直近 N 日分のメトリクスをサマリテーブルで表示する。"""
    keys = sorted(data.keys(), reverse=True)[:days]

    print(f"=== 日次サマリ (直近{len(keys)}件) ===")
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


def _show_latest_detail(data: dict) -> None:
    """最新回のメトリクスを詳細表示する。"""
    keys = sorted(data.keys(), reverse=True)
    if not keys:
        return

    key = keys[0]
    e = data[key]
    coll = e.get("collection", {})
    body = e.get("body_fetch", {})
    summ = e.get("summarization", {})
    output = e.get("output", {})

    print(f"=== 最新実行の詳細 ({key}) ===")
    print(f"実行日時:     {e.get('timestamp', '?')}")
    print(f"実行時間:     {e.get('elapsed_seconds', '?')}s")
    print()

    # 収集
    print(f"--- 収集 ---")
    print(f"総収集:       {coll.get('total_raw', '?')}件")
    print(f"新規:         {coll.get('total_new', '?')}件")
    print(f"既出(seen):   {coll.get('total_seen', '?')}件")
    print(f"ペナルティ除外: {coll.get('total_penalized', '?')}件")
    print()

    # ソース別件数
    by_source = coll.get("by_source", {})
    if by_source:
        print(f"--- ソース別件数 ({len(by_source)}ソース) ---")
        for name, count in sorted(by_source.items(), key=lambda x: x[1], reverse=True):
            marker = " *** 0件" if count == 0 else ""
            print(f"  {count:>3} | {name}{marker}")
        print()

    # 0件ソース
    sources_zero = coll.get("sources_zero", [])
    if sources_zero:
        print(f"--- 0件ソース警告 ({len(sources_zero)}件) ---")
        for src in sources_zero:
            print(f"  - {src}")
        print()

    # 本文取得
    print(f"--- 本文取得 ---")
    print(f"対象:         {body.get('total', '?')}件")
    print(f"成功:         {body.get('success', '?')}件")
    print(f"失敗(empty):  {body.get('empty', '?')}件")
    print(f"スキップ:     {body.get('skipped', '?')}件 (research)")
    success_rate = body.get("success_rate", 0)
    rate_str = f"{success_rate:.0%}" if isinstance(success_rate, float) else "?"
    print(f"成功率:       {rate_str}")
    print()

    # 要約
    print(f"--- 要約 ---")
    print(f"要約対象:     {summ.get('selected', '?')}件")
    print(f"[暫定]:       {summ.get('tentative_count', '?')}件")
    print(f"[解析失敗]:   {summ.get('parse_failure_count', '?')}件")

    dist = summ.get("importance_distribution", {})
    if dist:
        dist_str = "  ".join(f"{k}:{v}" for k, v in dist.items())
        print(f"importance分布: {dist_str}")
    print()

    # 出力
    print(f"--- 出力 ---")
    print(f"日報記事数:   {output.get('total_items', '?')}件")
    print(f"ペナルティ中: {output.get('active_penalties', '?')}ソース")


# ---------------------------------------------------------------------------
# 異常検知
# ---------------------------------------------------------------------------

# 閾値（conservative に設定）
ZERO_STREAK_THRESHOLD = 3       # N日連続0件で警告
BODY_RATE_THRESHOLD = 0.50      # 本文取得成功率がこの値未満で警告
COUNT_DROP_RATIO = 0.30         # 直近平均の30%以下に落ちたら警告


def check_health(data: dict | None = None) -> list[dict]:
    """
    蓄積されたメトリクスからソース健全性を判定し、警告リストを返す。

    戻り値: [{"level": "warn", "type": "...", "source": "...", "message": "..."}, ...]
    """
    if data is None:
        data = _load_metrics()
    if not data:
        return []

    warnings = []
    keys = sorted(data.keys(), reverse=True)

    # --- 0件連続ソースの検知 ---
    if len(keys) >= ZERO_STREAK_THRESHOLD:
        recent_keys = keys[:ZERO_STREAK_THRESHOLD]
        # 最新回に by_source があるソース名を基準にする
        latest_sources = data[keys[0]].get("collection", {}).get("by_source", {})

        for source in latest_sources:
            streak = 0
            for k in recent_keys:
                by_source = data[k].get("collection", {}).get("by_source", {})
                if by_source.get(source, 0) == 0:
                    streak += 1
                else:
                    break
            if streak >= ZERO_STREAK_THRESHOLD:
                warnings.append({
                    "level": "warn",
                    "type": "zero_streak",
                    "source": source,
                    "message": f"{source}: {streak}日連続0件",
                })

    # --- 本文取得成功率の低下 ---
    if keys:
        latest = data[keys[0]]
        body = latest.get("body_fetch", {})
        rate = body.get("success_rate", 1.0)
        if isinstance(rate, (int, float)) and rate < BODY_RATE_THRESHOLD:
            warnings.append({
                "level": "warn",
                "type": "body_rate_low",
                "source": "",
                "message": f"本文取得成功率が {rate:.0%} に低下（閾値 {BODY_RATE_THRESHOLD:.0%}）",
            })

    # --- 収集件数の急激な低下 ---
    if len(keys) >= 4:
        latest_raw = data[keys[0]].get("collection", {}).get("total_raw", 0)
        recent_raws = [
            data[k].get("collection", {}).get("total_raw", 0)
            for k in keys[1:4]
        ]
        avg = sum(recent_raws) / len(recent_raws) if recent_raws else 0
        if avg > 0 and latest_raw < avg * COUNT_DROP_RATIO:
            warnings.append({
                "level": "warn",
                "type": "count_drop",
                "source": "",
                "message": f"総収集件数が急落（{latest_raw}件、直近平均 {avg:.0f}件）",
            })

    return warnings


def _show_health(warnings: list[dict]) -> None:
    """警告を CLI に表示する。"""
    if not warnings:
        print("=== 健全性チェック: 問題なし ===")
        return

    print(f"=== 健全性チェック: {len(warnings)}件の警告 ===")
    for w in warnings:
        print(f"  [{w['level']}] {w['message']}")


def show_metrics(days: int = 14, latest_only: bool = False) -> None:
    """メトリクスを表示する。"""
    data = _load_metrics()
    if not data:
        print("メトリクスがありません。python -m scripts.main を実行してください。")
        return

    if latest_only:
        _show_latest_detail(data)
    else:
        _show_summary(data, days=days)
        print()
        _show_latest_detail(data)

    print()
    warnings = check_health(data)
    _show_health(warnings)


if __name__ == "__main__":
    args = sys.argv[1:]
    latest_only = "--latest" in args
    days = 14
    for i, a in enumerate(args):
        if a == "--days" and i + 1 < len(args):
            try:
                days = int(args[i + 1])
            except ValueError:
                pass

    show_metrics(days=days, latest_only=latest_only)
