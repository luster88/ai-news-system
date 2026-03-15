import re
from collections import defaultdict


def normalize_text(text: str) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[^a-z0-9ぁ-んァ-ン一-龠 ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_title(title: str) -> set[str]:
    text = normalize_text(title)
    tokens = set(text.split())

    stopwords = {
        "the", "a", "an", "and", "or", "to", "of", "for", "in", "on", "with",
        "from", "by", "at", "is", "are", "be", "this", "that",
        "ai", "news", "announcement", "announcements",
    }

    return {t for t in tokens if len(t) >= 2 and t not in stopwords}


def jaccard_similarity(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def cluster_articles(articles: list[dict], threshold: float = 0.45) -> list[dict]:
    """
    類似タイトルの記事をざっくり束ねて、importanceが高いものを代表として残す。
    """
    clusters = []
    used = set()

    tokenized = [tokenize_title(a.get("title", "")) for a in articles]

    for i, article in enumerate(articles):
        if i in used:
            continue

        cluster = [article]
        used.add(i)

        for j in range(i + 1, len(articles)):
            if j in used:
                continue

            sim = jaccard_similarity(tokenized[i], tokenized[j])
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