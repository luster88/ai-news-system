---
title: Thinking Block Signature
category: troubleshooting
subcategory: thinking-block-signature
tags:
- bugfix
- claude-api
date: '2026-10-15'
updated: '2026-10-15'
sources:
- url: https://zenn.dev/persimmoq/articles/claude-fable-invalid-signature-thinking
  title: Claude の Invalid signature in thinking block を直す ― 履歴は追記のみに
  date: '2026-10-15'
---

# Thinking Block Signature

---

## 2026-10-15

### Claude の Invalid signature in thinking block を直す ― 履歴は追記のみに

Claude Fable 5.1以降のモデルで、履歴編集時に「Invalid signature in thinking block」エラーが発生する問題について解説。preserved thinking という仕様により、前の応答に含まれる思考ブロックを送り返す際、会話のプレフィックス（system, tools, 前のメッセージ）が変更されていると400エラーになる。対策は履歴を追記のみにし、先頭を削らないこと。単発のAPI呼び出しは影響を受けないが、エージェントループやチャットなど前のassistantターンを送り返すコードは注意が必要。

- **ソース**: [Zenn claude](https://zenn.dev/persimmoq/articles/claude-fable-invalid-signature-thinking)
- **重要度**: 8/10
- **タグ**: claude-api, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-15 | 自動生成 |
