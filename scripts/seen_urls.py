"""
seen_urls.py — 既出URL管理とソースペナルティ機能

data/seen_urls.json に収集済みURLとソースペナルティを永続化し、
毎日の実行で同じ記事が繰り返し出現しないようにする。

ペナルティロジック:
  - あるソースから既出URLが PENALTY_THRESHOLD 件以上出た場合、
    そのソースを PENALTY_DAYS 日間スキップする。
"""

import json
import os
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scripts.config import get as cfg

BASE_DIR = Path(__file__).resolve().parent.parent
SEEN_URLS_FILE = BASE_DIR / "data" / "seen_urls.json"

PENALTY_THRESHOLD = cfg("penalty_threshold", 2)    # このURL件数以上既出 → ペナルティ発動
PENALTY_DAYS = cfg("penalty_days", 3)               # ペナルティ継続日数
URL_EXPIRY_DAYS = cfg("url_expiry_days", 90)         # seen_urls の保持期間（古いエントリを自動削除）


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _expiry_cutoff() -> str:
    cutoff = datetime.now(timezone.utc) - timedelta(days=URL_EXPIRY_DAYS)
    return cutoff.strftime("%Y-%m-%d")


def load_seen_data(file_path: Path | None = None) -> dict:
    """seen_urls.json を読み込む。ファイルが存在しない場合は空の構造を返す。
    file_path を指定すると、デフォルトの SEEN_URLS_FILE の代わりにそのパスを使う。"""
    path = file_path or SEEN_URLS_FILE
    if not path.exists():
        return {"urls": {}, "source_penalties": {}}

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # 必須キーが欠けている場合は補完
        data.setdefault("urls", {})
        data.setdefault("source_penalties", {})
        return data
    except Exception as e:
        print(f"[warn] seen_urls.json の読み込みに失敗しました: {e}")
        return {"urls": {}, "source_penalties": {}}


def filter_seen_articles(
    articles: list[dict],
    seen_data: dict,
) -> tuple[list[dict], list[dict]]:
    """
    articles から seen_urls に含まれるURLを除去する。

    戻り値:
        (new_articles, seen_articles)
        - new_articles: 今日初めて収集した記事
        - seen_articles: 過去に収集済みの記事（ペナルティ計算に使用）
    """
    seen_urls: dict[str, str] = seen_data.get("urls", {})
    new_articles = []
    seen_articles = []

    for article in articles:
        url = article.get("link", "")
        if url in seen_urls:
            seen_articles.append(article)
        else:
            new_articles.append(article)

    return new_articles, seen_articles


def apply_source_penalties(
    articles: list[dict],
    seen_data: dict,
) -> list[dict]:
    """
    source_penalties に記録されたペナルティ中のソースを除外する。
    ペナルティ解除日を過ぎたソースは除外しない。
    """
    penalties: dict[str, str] = seen_data.get("source_penalties", {})
    today = _today()

    penalized_sources = {
        source
        for source, release_date in penalties.items()
        if release_date > today
    }

    if penalized_sources:
        print(f"[info] ペナルティ中のソース: {sorted(penalized_sources)}")

    return [
        a for a in articles
        if a.get("source", "") not in penalized_sources
    ]


def compute_source_penalties(
    seen_articles: list[dict],
    seen_data: dict,
) -> dict:
    """
    今日の収集結果をもとにソースペナルティを計算し、seen_data を更新して返す。

    条件:
        - あるソースの既出URL件数が PENALTY_THRESHOLD 以上の場合、
          そのソースを今日から PENALTY_DAYS 日後まで停止する。
        - 既にペナルティ中のソースは上書きしない（既存の解除日を保持）。

    引数:
        seen_articles: 今日の収集で「既出」と判定された記事リスト
        seen_data:     現在の seen_urls データ（変更して返す）

    戻り値:
        更新後の seen_data
    """
    # ソースごとの既出URL件数を集計
    seen_count_by_source: dict[str, int] = defaultdict(int)
    for article in seen_articles:
        source = article.get("source", "")
        if source:
            seen_count_by_source[source] += 1

    today = _today()
    release_date = (
        datetime.now(timezone.utc) + timedelta(days=PENALTY_DAYS)
    ).strftime("%Y-%m-%d")

    penalties: dict[str, str] = seen_data.get("source_penalties", {})

    for source, count in seen_count_by_source.items():
        if count < PENALTY_THRESHOLD:
            continue

        # 既にペナルティ中（解除日が未来）の場合は上書きしない
        existing_release = penalties.get(source, "")
        if existing_release > today:
            print(
                f"[info] {source}: ペナルティ継続中 (解除日: {existing_release})"
            )
            continue

        penalties[source] = release_date
        print(
            f"[info] {source}: 既出URL {count}件 → {release_date} までペナルティ"
        )

    seen_data["source_penalties"] = penalties
    return seen_data


def update_seen_urls(
    new_articles: list[dict],
    seen_data: dict,
    file_path: Path | None = None,
) -> None:
    """
    今日収集した新規記事のURLを seen_urls.json に記録して保存する。
    URL_EXPIRY_DAYS を超えた古いエントリはこのタイミングで削除する。
    file_path を指定すると、デフォルトの SEEN_URLS_FILE の代わりにそのパスを使う。
    """
    path = file_path or SEEN_URLS_FILE
    today = _today()
    cutoff = _expiry_cutoff()

    urls: dict[str, str] = seen_data.get("urls", {})

    # 期限切れURLを削除
    expired = [url for url, date in urls.items() if date < cutoff]
    for url in expired:
        del urls[url]
    if expired:
        print(f"[info] 期限切れURL {len(expired)}件を削除しました")

    # 今日の新規URLを追加
    added = 0
    for article in new_articles:
        url = article.get("link", "")
        if url and url not in urls:
            urls[url] = today
            added += 1

    seen_data["urls"] = urls

    try:
        tmp_fd, tmp_path = tempfile.mkstemp(
            dir=path.parent, suffix=".tmp"
        )
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                json.dump(seen_data, f, ensure_ascii=False, indent=2)
            os.replace(tmp_path, path)
        except Exception:
            os.unlink(tmp_path)
            raise
        print(f"[info] {path.name} を更新しました（新規URL +{added}件、合計 {len(urls)}件）")
    except Exception as e:
        print(f"[warn] {path.name} の書き込みに失敗しました: {e}")


def show_status() -> None:
    """ペナルティ状況と seen_urls の統計を表示する。"""
    data = load_seen_data()
    today = _today()
    urls = data.get("urls", {})
    penalties = data.get("source_penalties", {})

    active = {s: d for s, d in penalties.items() if d > today}
    expired = {s: d for s, d in penalties.items() if d <= today}

    print(f"=== seen_urls.json ステータス (today={today}) ===")
    print(f"URL件数: {len(urls)}")
    print(f"設定: PENALTY_THRESHOLD={PENALTY_THRESHOLD}, PENALTY_DAYS={PENALTY_DAYS}, URL_EXPIRY_DAYS={URL_EXPIRY_DAYS}")
    print()

    print(f"=== アクティブペナルティ ({len(active)}件) ===")
    if active:
        for source, release in sorted(active.items()):
            print(f"  {source}: {release} まで")
    else:
        print("  なし")
    print()

    print(f"=== 期限切れペナルティ ({len(expired)}件) ===")
    if expired:
        for source, release in sorted(expired.items()):
            print(f"  {source}: {release} で解除済み")
    else:
        print("  なし")


if __name__ == "__main__":
    show_status()
