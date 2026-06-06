---
title: Cost Management
category: troubleshooting
subcategory: cost-management
tags:
- claude-api
- claude-code
- opus
- performance
- pricing
date: '2026-05-01'
updated: '2026-06-06'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1t11mmy/i_accidentally_burned_6000_of_claude_usage
  title: I accidentally burned ~$6,000 of Claude usage overnight with one command.
  date: '2026-05-01'
- url: https://zenn.dev/acntechjp/articles/claude-code-cost-history-bloat
  title: ご利用は計画的に
  date: '2026-06-06'
---


# Cost Management

---

## 2026-06-06

### ご利用は計画的に

Claude Code使用時のトークン消費とキャッシュコストの可視化に関する記事。会話履歴がキャッシュとしてトークン計上される仕組みを解説し、~/.claude/projects/フォルダのログデータを分析。セッションごとの会話ターン数別に、input/output/cache_read/cache_writeの4種類のトークン使用量と概算コストを算出した結果を共有している。

- **ソース**: [Zenn claude](https://zenn.dev/acntechjp/articles/claude-code-cost-history-bloat)
- **重要度**: 6/10
- **タグ**: claude-code, pricing, performance

---

## 2026-05-01

### I accidentally burned ~$6,000 of Claude usage overnight with one command.

Redditユーザーが、30分ごとにPRをチェックする/loopコマンドを一晩放置し、約6,000ドルのClaude使用料を消費した事例。Claude APIは毎回会話履歴全体を送信するため、プロンプトキャッシュが5分で期限切れになると、巨大な会話履歴（最終的に80万トークン）を毎回再キャッシュする必要があり、コストが急増した。ダッシュボードの報告遅延により、問題に気づくのが遅れた。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1t11mmy/i_accidentally_burned_6000_of_claude_usage)
- **重要度**: 8/10
- **タグ**: claude-api, pricing, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-01 | 自動生成 |
