import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scripts.config import get as cfg

BASE_DIR = Path(__file__).resolve().parent.parent

# クラスタリング設定
CLUSTER_THRESHOLD = cfg("cluster_threshold", 0.35)
WEIGHT_TITLE = cfg("cluster_weight_title", 0.40)
WEIGHT_SUMMARY = cfg("cluster_weight_summary", 0.35)
WEIGHT_TAGS = cfg("cluster_weight_tags", 0.25)


def normalize_text(text: str) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[^a-z0-9ぁ-んァ-ン一-龠 ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "for", "in", "on", "with",
    "from", "by", "at", "is", "are", "be", "this", "that",
    "ai", "news", "announcement", "announcements",
}

# 日本語ストップワード（助詞・助動詞など）
JA_STOPWORDS = {
    "の", "に", "は", "を", "た", "が", "で", "て", "と", "し", "れ",
    "さ", "ある", "いる", "する", "から", "こと", "この", "それ", "ため",
    "など", "なる", "への", "もの", "という", "として", "られ", "について",
    "また", "ない", "なっ", "でき", "これ", "その", "ここ", "まで",
}


def _split_japanese(text: str) -> list[str]:
    """日本語テキストを文字Nグラム（2-gram）に分割する。
    形態素解析ライブラリに依存せずに日本語の類似度を計算するための簡易手法。"""
    # 日本語文字の連続部分を抽出
    ja_chunks = re.findall(r"[ぁ-んァ-ン一-龠]+", text)
    ngrams = []
    for chunk in ja_chunks:
        if len(chunk) <= 2:
            if chunk not in JA_STOPWORDS:
                ngrams.append(chunk)
        else:
            for i in range(len(chunk) - 1):
                bigram = chunk[i:i+2]
                if bigram not in JA_STOPWORDS:
                    ngrams.append(bigram)
    return ngrams


def tokenize(text: str) -> set[str]:
    normalized = normalize_text(text)

    # 英数字トークン（スペース区切り）
    ascii_tokens = {
        t for t in normalized.split()
        if len(t) >= 2 and t not in STOPWORDS
        and re.match(r"^[a-z0-9]+$", t)
    }

    # 日本語 2-gram トークン
    ja_tokens = set(_split_japanese(normalized))

    return ascii_tokens | ja_tokens


def jaccard_similarity(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def tag_similarity(tags_a: list[str], tags_b: list[str]) -> float:
    """タグの一致率を計算する。"""
    set_a = set(tags_a or [])
    set_b = set(tags_b or [])
    if not set_a or not set_b:
        return 0.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union else 0.0


def composite_similarity(article_a: dict, article_b: dict,
                         tokens_a: dict, tokens_b: dict) -> float:
    """タイトル + 要約 + タグの加重スコアで複合類似度を計算する。
    要約やタグが片方でも空の場合、その分の重みをタイトルに再配分する。"""
    title_sim = jaccard_similarity(tokens_a["title"], tokens_b["title"])
    summary_sim = jaccard_similarity(tokens_a["summary"], tokens_b["summary"])
    tags_sim = tag_similarity(
        article_a.get("tags", []),
        article_b.get("tags", []),
    )

    w_title = WEIGHT_TITLE
    w_summary = WEIGHT_SUMMARY
    w_tags = WEIGHT_TAGS

    # 要約が片方でも空なら、その重みをタイトルに再配分
    has_summary = bool(tokens_a["summary"]) and bool(tokens_b["summary"])
    has_tags = bool(article_a.get("tags")) and bool(article_b.get("tags"))

    if not has_summary and not has_tags:
        w_title = 1.0
        w_summary = 0.0
        w_tags = 0.0
    elif not has_summary:
        w_title += w_summary
        w_summary = 0.0
    elif not has_tags:
        w_title += w_tags
        w_tags = 0.0

    return (
        w_title * title_sim
        + w_summary * summary_sim
        + w_tags * tags_sim
    )


def _tokenize_article(article: dict) -> dict:
    """記事からタイトルと要約のトークンセットを生成する。"""
    return {
        "title": tokenize(article.get("title", "")),
        "summary": tokenize(article.get("summary_ja", "") or article.get("summary", "")),
    }


def cluster_articles(articles: list[dict], threshold: float | None = None) -> list[dict]:
    """
    複合類似度（タイトル + 要約 + タグ）で記事をクラスタリングし、
    importanceが高いものを代表として残す。
    """
    threshold = threshold if threshold is not None else CLUSTER_THRESHOLD
    clusters: list[list[dict]] = []
    used: set[int] = set()

    tokenized = [_tokenize_article(a) for a in articles]

    for i, article in enumerate(articles):
        if i in used:
            continue

        cluster = [article]
        used.add(i)

        for j in range(i + 1, len(articles)):
            if j in used:
                continue

            sim = composite_similarity(
                articles[i], articles[j],
                tokenized[i], tokenized[j],
            )
            if sim >= threshold:
                cluster.append(articles[j])
                used.add(j)

        clusters.append(cluster)

    merged = []
    for cluster in clusters:
        cluster.sort(key=lambda x: x.get("importance_score", 1), reverse=True)
        representative = dict(cluster[0])

        if len(cluster) > 1:
            representative["related_articles"] = [
                {
                    "title": a.get("title", ""),
                    "source": a.get("source", ""),
                    "link": a.get("link", ""),
                }
                for a in cluster[1:]
            ]
        else:
            representative["related_articles"] = []

        merged.append(representative)

    merged.sort(key=lambda x: x.get("importance_score", 1), reverse=True)
    return merged


# ---------------------------------------------------------------------------
# 日をまたいだ重複検出
# ---------------------------------------------------------------------------

LOOKBACK_DAYS = cfg("cluster_lookback_days", 7)
CROSS_DAY_THRESHOLD = cfg("cluster_cross_day_threshold", 0.30)


def _parse_articles_from_markdown(md_text: str, date_str: str) -> list[dict]:
    """日報 Markdown から記事の title / summary / tags / link を抽出する。
    '## 注目3件' セクションはスキップし、地域セクションのみパースする。"""
    articles: list[dict] = []
    lines = md_text.splitlines()

    # 注目3件セクションをスキップするフラグ
    in_top_section = False
    current: dict | None = None

    for line in lines:
        # セクション見出し（## で始まる）
        if line.startswith("## "):
            section = line[3:].strip()
            in_top_section = section == "注目3件"
            continue

        if in_top_section:
            continue

        # 記事見出し（### N. Title）
        m = re.match(r"^###\s+\d+\.\s+(.+)", line)
        if m:
            if current and current.get("title"):
                articles.append(current)
            current = {"title": m.group(1).strip(), "date": date_str,
                        "summary_ja": "", "tags": [], "link": ""}
            continue

        if current is None:
            continue

        # フィールド抽出
        if line.startswith("- Summary: "):
            current["summary_ja"] = line[len("- Summary: "):].strip()
        elif line.startswith("- Tags: "):
            current["tags"] = [t.strip() for t in line[len("- Tags: "):].split(",")]
        elif line.startswith("- Link: "):
            # [url](url) 形式から URL を抽出
            link_m = re.search(r"\((https?://[^)]+)\)", line)
            if link_m:
                current["link"] = link_m.group(1)

    # 最後の記事を追加
    if current and current.get("title"):
        articles.append(current)

    return articles


def load_past_articles(lookback_days: int | None = None) -> list[dict]:
    """過去 N 日分の日報 Markdown から記事を読み込む。"""
    days = lookback_days if lookback_days is not None else LOOKBACK_DAYS
    today = datetime.now(timezone.utc)
    articles: list[dict] = []
    seen_links: set[str] = set()

    for i in range(1, days + 1):
        d = today - timedelta(days=i)
        date_str = d.strftime("%Y-%m-%d")
        year, month, _ = date_str.split("-")
        md_path = BASE_DIR / "news" / year / month / f"{date_str}.md"

        if not md_path.exists():
            continue

        try:
            md_text = md_path.read_text(encoding="utf-8")
            parsed = _parse_articles_from_markdown(md_text, date_str)
            # URL で重複排除（Top3 と地域セクションの重複を除去）
            for a in parsed:
                link = a.get("link", "")
                if link and link not in seen_links:
                    seen_links.add(link)
                    articles.append(a)
        except Exception as e:
            print(f"[warn] 過去記事の読み込みに失敗: {md_path}: {e}")

    return articles


def detect_cross_day_duplicates(
    articles: list[dict],
    past_articles: list[dict] | None = None,
    threshold: float | None = None,
) -> list[dict]:
    """
    新規記事と過去記事を比較し、類似する過去記事があれば
    cross_day_related フィールドに追加して返す。
    記事は排除せず、フラグ付与のみ行う。
    """
    threshold = threshold if threshold is not None else CROSS_DAY_THRESHOLD

    if past_articles is None:
        past_articles = load_past_articles()

    if not past_articles:
        return articles

    past_tokenized = [_tokenize_article(a) for a in past_articles]

    for article in articles:
        article_tokens = _tokenize_article(article)
        cross_day: list[dict] = []

        for j, past in enumerate(past_articles):
            # 同じ URL は URL 重複排除で処理済みなのでスキップ
            if article.get("link") and article["link"] == past.get("link"):
                continue

            sim = composite_similarity(
                article, past,
                article_tokens, past_tokenized[j],
            )
            if sim >= threshold:
                cross_day.append({
                    "title": past.get("title", ""),
                    "source": past.get("source", ""),
                    "link": past.get("link", ""),
                    "date": past.get("date", ""),
                    "similarity": round(sim, 3),
                })

        if cross_day:
            # 類似度の高い順にソートして最大3件
            cross_day.sort(key=lambda x: x["similarity"], reverse=True)
            article["cross_day_related"] = cross_day[:3]

    return articles
