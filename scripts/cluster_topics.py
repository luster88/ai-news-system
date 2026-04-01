import re
from collections import defaultdict

from scripts.config import get as cfg

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


def tokenize(text: str) -> set[str]:
    normalized = normalize_text(text)
    tokens = set(normalized.split())
    return {t for t in tokens if len(t) >= 2 and t not in STOPWORDS}


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
    """タイトル + 要約 + タグの加重スコアで複合類似度を計算する。"""
    title_sim = jaccard_similarity(tokens_a["title"], tokens_b["title"])
    summary_sim = jaccard_similarity(tokens_a["summary"], tokens_b["summary"])
    tags_sim = tag_similarity(
        article_a.get("tags", []),
        article_b.get("tags", []),
    )

    return (
        WEIGHT_TITLE * title_sim
        + WEIGHT_SUMMARY * summary_sim
        + WEIGHT_TAGS * tags_sim
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
