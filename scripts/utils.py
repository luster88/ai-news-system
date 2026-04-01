"""
utils.py — 複数モジュールで共有するユーティリティ関数
"""


def extract_text_from_message(msg) -> str:
    """Claude API レスポンスからテキスト部分を抽出する。"""
    return "".join(
        block.text for block in msg.content
        if getattr(block, "type", "") == "text"
    ).strip()


def clean_json_text(text: str) -> str:
    """Claude API レスポンスから JSON 文字列を抽出する。
    コードブロック（```json ... ```）のマーカーを除去する。"""
    text = text.strip()
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    elif text.startswith("```"):
        text = text[len("```"):].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text
