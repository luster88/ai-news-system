import json
import os
import re
from collections import Counter

from anthropic import Anthropic
from dotenv import load_dotenv

from scripts.config import get as cfg

load_dotenv()

MODEL = cfg("model", "claude-sonnet-4-5")
MAX_ARTICLES_TO_SUMMARIZE = cfg("max_articles_to_summarize", 25)
MAX_PER_SOURCE = cfg("max_per_source", 3)

# タグ候補（プロンプトで提示して選択を安定させる）
TAG_CANDIDATES = [
    "LLM", "Agent", "画像生成", "音声AI", "コーディング支援",
    "規制・政策", "研究・論文", "産業応用", "ハードウェア", "セキュリティ",
]


def _extract_text_from_message(msg) -> str:
    return "".join(
        block.text for block in msg.content
        if getattr(block, "type", "") == "text"
    ).strip()


def _clean_json_text(text: str) -> str:
    text = text.strip()

    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    elif text.startswith("```"):
        text = text[len("```"):].strip()

    if text.endswith("```"):
        text = text[:-3].strip()

    return text


def _safe_parse_summary_json(text: str) -> dict:
    cleaned = _clean_json_text(text)

    try:
        parsed = json.loads(cleaned)
        # tags は候補リスト内の文字列のみ受け付ける
        raw_tags = parsed.get("tags", [])
        if isinstance(raw_tags, list):
            tags = [t for t in raw_tags if isinstance(t, str) and t in TAG_CANDIDATES][:3]
        else:
            tags = []
        # topic_id の正規化（kebab-case, 英数字とハイフンのみ）
        raw_topic_id = str(parsed.get("topic_id", "")).strip().lower()
        topic_id = re.sub(r"[^a-z0-9\-]", "-", raw_topic_id)
        topic_id = re.sub(r"-+", "-", topic_id).strip("-")
        return {
            "summary": str(parsed.get("summary", "")).strip(),
            "why_it_matters": str(parsed.get("why_it_matters", "")).strip(),
            "importance_score": int(parsed.get("importance_score", 1)),
            "tags": tags,
            "topic_id": topic_id,
        }
    except Exception:
        return {
            "summary": f"[解析失敗] {cleaned[:200]}",
            "why_it_matters": "",
            "importance_score": 1,
            "tags": [],
            "topic_id": "",
        }


def _is_low_value_article(article: dict) -> bool:
    title = (article.get("title", "") or "").lower()
    source = (article.get("source", "") or "").lower()

    weak_titles = [
        "morgen",
        "motion software",
    ]

    if title in weak_titles:
        return True

    # Product Hunt はAIキーワードが薄いものを弱めに落とす
    if "product hunt" in source:
        strong_keywords = [
            "ai", "agent", "llm", "gpt", "claude", "openclaw",
            "memory", "security", "automation", "voice",
        ]
        if not any(k in title for k in strong_keywords):
            return True

    return False


def _select_articles_for_summary(articles: list) -> list:
    articles = [a for a in articles if not _is_low_value_article(a)]

    selected = []
    source_counts = Counter()

    # 地域バランスを少し取りつつ、各ソース最大件数を制限
    region_order = ["us", "cn", "jp", "techblog", "research"]
    grouped = {r: [] for r in region_order}

    for article in articles:
        grouped.setdefault(article.get("region", "other"), []).append(article)

    # まず各地域から順番に拾う
    made_progress = True
    while made_progress and len(selected) < MAX_ARTICLES_TO_SUMMARIZE:
        made_progress = False

        for region in region_order:
            for article in grouped.get(region, []):
                source = article.get("source", "unknown")
                if article in selected:
                    continue
                if source_counts[source] >= MAX_PER_SOURCE:
                    continue

                selected.append(article)
                source_counts[source] += 1
                made_progress = True
                break

            if len(selected) >= MAX_ARTICLES_TO_SUMMARIZE:
                break

    # まだ足りなければ残りから追加
    if len(selected) < MAX_ARTICLES_TO_SUMMARIZE:
        for article in articles:
            source = article.get("source", "unknown")
            if article in selected:
                continue
            if source_counts[source] >= MAX_PER_SOURCE:
                continue

            selected.append(article)
            source_counts[source] += 1

            if len(selected) >= MAX_ARTICLES_TO_SUMMARIZE:
                break

    return selected


def _summarize_one_article(client: Anthropic, article: dict, model: str = "") -> dict:
    known_summary = article.get("summary", "").strip()
    body = article.get("body", "").strip()

    # 本文が取得できなかった場合、RSS summary をフォールバック本文として使用
    if known_summary and not body:
        body = known_summary
        known_summary = ""

    # 本文があれば [暫定] マークは不要
    has_body = bool(body)

    body_section = f"記事本文（抜粋）:\n{body[:2000]}" if body else "記事本文: 取得できませんでした"

    tag_list = "、".join(TAG_CANDIDATES)

    prompt = f"""
次の記事情報を日本語で要約してください。

タイトル: {article['title']}
URL: {article['link']}
既知の要約: {known_summary if known_summary else "なし"}
{body_section}

注意:
- 記事本文が十分でない場合は、推測を避ける
- 情報不足なら「タイトルベースの暫定要約」であることが分かる表現にする
- 断定しすぎない

タグは以下の候補から最大3つ選んでください:
{tag_list}

必ずJSONのみ返してください。
{{
    "summary": "3〜5行の要約",
    "why_it_matters": "重要性を1〜2行",
    "importance_score": 1,
    "tags": ["タグ1", "タグ2"],
    "topic_id": "英語のkebab-case短縮トピック名"
}}

topic_id はこの記事の主題を表す英語のkebab-case識別子です（例: "openai-sora-shutdown", "wikipedia-bans-ai-articles", "claude-code-source-leak"）。
同じニュースの別ソース報道には同じ topic_id を付けてください。固有名詞+動作で簡潔に。

importance_score は 1〜10 の整数で、以下の基準に従って返してください:
- 9〜10: 業界全体に影響する重大発表（主要モデルの新規リリース、大型買収、重要な規制変更）
- 7〜8: 特定分野で注目度が高いニュース（新機能発表、重要な研究成果、大手企業の戦略変更）
- 5〜6: 業界関係者にとって有用な情報（ツール更新、事例紹介、中規模な提携）
- 3〜4: 限定的な関心にとどまるニュース（マイナーアップデート、地域限定の話題）
- 1〜2: 情報価値が低い、または情報不足で判断困難な記事
"""

    msg = client.messages.create(
        model=model or MODEL,
        max_tokens=600,
        temperature=0.2,
        system="あなたはAIニュース要約の専門家です。指示に従い、必ず有効なJSONのみを返してください。JSONの前後に説明文やMarkdownコードブロックを付けないでください。",
        messages=[{"role": "user", "content": prompt}],
    )

    parsed = _safe_parse_summary_json(_extract_text_from_message(msg))

    article["summary_ja"] = parsed["summary"]
    article["why_it_matters"] = parsed["why_it_matters"]
    article["importance_score"] = max(1, min(10, parsed["importance_score"]))
    article["tags"] = parsed["tags"]
    article["topic_id"] = parsed.get("topic_id", "")

    # 本文も既知の要約もない場合のみ [暫定] を付ける
    if not has_body and not article.get("summary", "").strip():
        article["summary_ja"] = f"[暫定] {article['summary_ja']}"

    return article


def _generate_overall_summary(client: Anthropic, articles: list, model: str = "") -> list[str]:
    if not articles:
        return ["今日は有効な記事を取得できませんでした。"]

    top_articles = sorted(
        articles,
        key=lambda x: x.get("importance_score", 1),
        reverse=True
    )[:10]

    compact_lines = []
    for i, a in enumerate(top_articles, start=1):
        tags_str = ", ".join(a.get("tags", []))
        compact_lines.append(
            f"{i}. [{a.get('region', '').upper()}] {a['title']} "
            f"(importance={a.get('importance_score', 1)}, source={a.get('source', '')}, tags={tags_str}) "
            f"要約: {a.get('summary_ja', '')}"
        )

    joined = "\n".join(compact_lines)

    prompt = f"""
以下のAIニュース要約一覧をもとに、
Markdownの冒頭に置く「今日の総括」を日本語で3〜5行の箇条書きで作成してください。

条件:
- 箇条書きのみ
- 各行は簡潔に
- 全体の流れ、注目領域、地域バランスにも触れる
- 先頭に「- 」を付ける

記事一覧:
{joined}
"""

    msg = client.messages.create(
        model=model or MODEL,
        max_tokens=500,
        temperature=0.2,
        system="あなたはAIニュース要約の専門家です。指示されたフォーマットに正確に従って回答してください。",
        messages=[{"role": "user", "content": prompt}],
    )

    text = _extract_text_from_message(msg)
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    bullet_lines = []
    for line in lines:
        normalized = line.lstrip("- ").strip()

        # 見出し行を除外
        if normalized in {"今日の総括", "# 今日の総括", "## 今日の総括"}:
            continue

        if normalized.startswith("#"):
            continue

        if not normalized:
            continue

        bullet_lines.append(f"- {normalized}")

    return bullet_lines[:5] if bullet_lines else ["- 主要トピックの総括生成に失敗しました。"]


def summarize_articles(articles: list, model_override: str | None = None):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    use_model = model_override or MODEL
    if model_override:
        print(f"[info] model override: {use_model}")

    client = Anthropic(api_key=api_key, timeout=120.0)

    selected_articles = _select_articles_for_summary(articles)
    summarized = []

    print(f"[info] selected {len(selected_articles)} articles for summarization")

    for idx, article in enumerate(selected_articles, start=1):
        print(f"[info] summarizing {idx}/{len(selected_articles)}: {article['title']}")
        summarized.append(_summarize_one_article(client, article, model=use_model))

    # importance順に並べ替え
    summarized.sort(key=lambda x: x.get("importance_score", 1), reverse=True)

    overall_summary = _generate_overall_summary(client, summarized, model=use_model)

    api_calls = len(selected_articles) + 1  # 記事ごと + overall_summary
    print(f"[info] summarize complete: {api_calls} API calls ({len(selected_articles)} articles + 1 overall)")

    return {
        "articles": summarized,
        "overall_summary": overall_summary,
    }
