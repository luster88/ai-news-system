---
title: Claude Code Runaway
category: troubleshooting
subcategory: claude-code-runaway
tags:
- bugfix
- claude-code
- mcp
date: '2026-06-14'
updated: '2026-06-14'
sources:
- url: https://qiita.com/yurukusa/items/386a6d1e13cbece3d409
  title: Claude Codeのサブエージェントが暴走して枠を焼き尽くす事故——止める1つのhookと、消えた成果の復旧
  date: '2026-06-14'
---

# Claude Code Runaway

---

## 2026-06-14

### Claude Codeのサブエージェントが暴走して枠を焼き尽くす事故——止める1つのhookと、消えた成果の復旧

Claude Codeのサブエージェントが再帰的に子エージェントを生成し続け、30分で120万トークン以上を消費する事故が報告された。CLAUDE_CODE_FORK_SUBAGENT=0が無視される不具合があり、PreToolUseのhookを使った起動制限と、Console支出上限設定による対策が必要。暴走時も各サブエージェントの成果はディスクに記録されており、復旧可能。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/386a6d1e13cbece3d409)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-14 | 自動生成 |
