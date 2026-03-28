---
title: Rate Limits
category: troubleshooting
subcategory: rate-limits
tags:
- claude-code
- claude-console
- opus
- performance
- pricing
date: '2026-03-25'
updated: '2026-03-28'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s3bcit/your_claude_code_limits_didnt_shrink_i_think_the
  title: Your Claude Code Limits Didn't Shrink — I Think the 1M Context Window Is
    Eating Them Alive
  date: '2026-03-25'
- url: https://www.reddit.com/r/ClaudeAI/comments/1s5r0hj/on_the_200_max_plan_and_never_been_rate_limited
  title: On the $200 Max plan and never been rate limited once. Ran the numbers to
    find out why everyone else is.
  date: '2026-03-28'
---


# Rate Limits

---

## 2026-03-28

### On the $200 Max plan and never been rate limited once. Ran the numbers to find out why everyone else is.

Reddit ユーザーが Claude Max プラン ($200) でレート制限に遭遇しない理由を分析。Anthropic の非公式情報として、平日の 5am-11am PT (8am-2pm ET) がピーク時間帯でトークン制限が厳しくなることが判明。西海岸の通常業務時間帯ユーザーが最も影響を受けやすく、夜間や早朝の利用でレート制限を回避できる可能性がある。コンテキスト管理もプラン階層より重要。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s5r0hj/on_the_200_max_plan_and_never_been_rate_limited)
- **重要度**: 7/10
- **タグ**: claude-console, pricing, performance

---

## 2026-03-25

### Your Claude Code Limits Didn't Shrink — I Think the 1M Context Window Is Eating Them Alive

Claude Code で最近レート制限やサービス停止が頻発している理由について、Reddit ユーザーが仮説を提示。Opus 4.6 の 100万トークンコンテキストウィンドウ導入後、Claude Code のコンテキスト圧縮が不十分なため、各リクエストで不必要に大量のトークンを消費し、サーバーに過負荷をかけている可能性を指摘。その結果、Anthropic が使用制限を引き下げて対処しているのではないかと分析。旧モデルに切り替えることで安定性が改善したと報告している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s3bcit/your_claude_code_limits_didnt_shrink_i_think_the)
- **重要度**: 7/10
- **タグ**: claude-code, opus, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-25 | 自動生成 |
