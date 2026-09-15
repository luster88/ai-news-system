---
title: Claude Code Naming
category: troubleshooting
subcategory: claude-code-naming
tags:
- claude-code
- cowork
- prompt
date: '2026-09-15'
updated: '2026-09-15'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1wghjmn/claude_keeps_naming_things_after_the_mistakes_i
  title: Claude keeps naming things after the mistakes I told it not to make. So I
    built a hook for it.
  date: '2026-09-15'
---

# Claude Code Naming

---

## 2026-09-15

### Claude keeps naming things after the mistakes I told it not to make. So I built a hook for it.

Claudeが過去の修正内容をファイル名やコミットメッセージに含めてしまう問題（例: grilled_cheese_no_ketchup.md）に対し、ユーザーが「チャット相手ではなくファイルの読者に向けて書く」というルールを実装したツール「ship-the-result」を開発。SKILL.md、スキャナースクリプト、PreToolUseフックの3要素で構成され、コミットメッセージやコメントから会話の痕跡を自動検出・除去する。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wghjmn/claude_keeps_naming_things_after_the_mistakes_i)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-15 | 自動生成 |
