---
title: Prompt Caching Optimization
category: guides
subcategory: prompt-caching-optimization
tags:
- claude-code
- performance
- prompt
date: '2026-04-23'
updated: '2026-04-30'
sources:
- url: https://zenn.dev/ai_arai_ally/articles/20260422-1601-claude-code-prompt-caching-api
  title: Claude Code の Prompt Caching で API コスト 1/8 削減
  date: '2026-04-23'
- url: https://zenn.dev/snowflakejp/articles/4def632fe30a9b
  title: コーディングエージェントにおけるプロンプトキャッシュの仕組み — なぜ最初のターンはトークン使用量が多く見えるのか
  date: '2026-04-30'
---


# Prompt Caching Optimization

---

## 2026-04-30

### コーディングエージェントにおけるプロンプトキャッシュの仕組み — なぜ最初のターンはトークン使用量が多く見えるのか

コーディングエージェント（Claude Code、Cursor等）で短いプロンプトでも最初のターンで大量のトークンが消費される理由を解説。システムプロンプト、ツール定義、会話履歴などが毎回送信されるため、5単語の入力でも10,000トークン以上になる。Anthropic と OpenAI のプロンプトキャッシュの仕組みを説明し、2回目以降のターンでキャッシュヒットによりトークン消費が削減される原理を詳述。

- **ソース**: [Zenn claude](https://zenn.dev/snowflakejp/articles/4def632fe30a9b)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, performance

---

## 2026-04-23

### Claude Code の Prompt Caching で API コスト 1/8 削減

Claude Code の自律エージェント実装において、Prompt Caching を適切に活用することでAPIコストを1/8に削減し、レイテンシを4秒から0.6秒に短縮した実践記録。キャッシュが無効化される5つの落とし穴（タイムスタンプ、MCP ツール定義の順序揺れ、skill の動的差し込み、CLAUDE.md への動的変数注入、MCP 再接続）を解説し、cache hit 率を30%から90%に向上させた設計手法を紹介。キャッシュは「不動のものを前に積む」という設計規律が重要。

- **ソース**: [Zenn claude](https://zenn.dev/ai_arai_ally/articles/20260422-1601-claude-code-prompt-caching-api)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-23 | 自動生成 |
