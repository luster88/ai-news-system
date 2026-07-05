"""
utils.py — 複数モジュールで共有するユーティリティ関数
"""

import time


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


def run_message_batch(
    client,
    batch_requests: list[dict],
    poll_interval: int = 15,
    timeout: int = 1200,
) -> dict | None:
    """
    Message Batches API でリクエストを一括実行する（通常のAPI呼び出しの50%のコスト）。

    引数:
        client: Anthropic クライアント
        batch_requests: [{"custom_id": ..., "params": {...}}, ...]
        poll_interval: 完了ポーリング間隔（秒）
        timeout: 完了待ちの上限（秒）

    戻り値:
        {custom_id: Message} の dict（succeeded のエントリのみ）。
        タイムアウト・送信失敗時は None（呼び出し側で逐次実行にフォールバックする）。
    """
    try:
        batch = client.messages.batches.create(requests=batch_requests)
        print(f"[info] batch submitted: {batch.id} ({len(batch_requests)} requests)")

        deadline = time.monotonic() + timeout
        while batch.processing_status != "ended":
            if time.monotonic() > deadline:
                print(f"[warn] batch {batch.id} timed out after {timeout}s, cancelling")
                try:
                    client.messages.batches.cancel(batch.id)
                except Exception:
                    pass
                return None
            time.sleep(poll_interval)
            batch = client.messages.batches.retrieve(batch.id)

        results = {}
        for entry in client.messages.batches.results(batch.id):
            if entry.result.type == "succeeded":
                results[entry.custom_id] = entry.result.message
            else:
                print(f"[warn] batch entry {entry.custom_id}: {entry.result.type}")

        print(f"[info] batch complete: {len(results)}/{len(batch_requests)} succeeded")
        return results

    except Exception as e:
        print(f"[warn] batch execution failed: {e}")
        return None
