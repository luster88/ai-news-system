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

BASE_DIR = Path(__file__).resolve().parent.parent
SEEN_URLS_FILE = BASE_DIR / "data" / "seen_urls.json"

PENALTY_THRESHOLD = 2    # このURL件数以上既出 → ペナルティ発動
PENALTY_DAYS = 3         # ペナルティ継続日数
URL_EXPIRY_DAYS = 90     # seen_urls の保持期間（古いエントリを自動削除）


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _expiry_cutoff() -> str:
    cutoff = datetime.now(timezone.utc) - timedelta(days=URL_EXPIRY_DAYS)
    return cutoff.strftime("%Y-%m-%d")


def load_seen_data() -> dict:
    """seen_urls.json を読み込む。ファイルが存在しない場合は空の構造を返す。"""
    if not SEEN_URLS_FILE.exists():
        return {"urls": {}, "source_penalties": {}}

    try:
        with open(SEEN_URLS_FILE, "r", encoding="utf-8") as f:
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
) -> None:
    """
    今日収集した新規記事のURLを seen_urls.json に記録して保存する。
    URL_EXPIRY_DAYS を超えた古いエントリはこのタイミングで削除する。
    """
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
            dir=SEEN_URLS_FILE.parent, suffix=".tmp"
        )
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                json.dump(seen_data, f, ensure_ascii=False, indent=2)
            os.replace(tmp_path, SEEN_URLS_FILE)
        except Exception:
            os.unlink(tmp_path)
            raise
        print(f"[info] seen_urls.json を更新しました（新規URL +{added}件、合計 {len(urls)}件）")
    except Exception as e:
        print(f"[warn] seen_urls.json の書き込みに失敗しました: {e}")
