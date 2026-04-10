---
title: Claude Md Rules
category: troubleshooting
subcategory: claude-md-rules
tags:
- bugfix
- claude-code
- mcp
date: '2026-04-10'
updated: '2026-04-10'
sources:
- url: https://qiita.com/yurukusa/items/f0f1ffd024a1b9394df4
  title: CLAUDE.mdのルールを5回書き直しても無視された——GitHub 30件超の報告に共通する原因とhookで止めた方法
  date: '2026-04-10'
---

# Claude Md Rules

---

## 2026-04-10

### CLAUDE.mdのルールを5回書き直しても無視された——GitHub 30件超の報告に共通する原因とhookで止めた方法

CLAUDE.mdに何度ルールを記載してもClaudeが無視する問題について、GitHubで30件以上の報告があることを指摘。これはバグではなくLLMの構造的限界であり、コンテキストが長くなるとルールの影響力が低下する。解決策としてPreToolUseフックを使い、ツール実行前に物理的にブロックする方法を提案。「メモリはお願い、フックは壁」という区別が重要。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/f0f1ffd024a1b9394df4)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-10 | 自動生成 |
