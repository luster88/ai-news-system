---
title: Prompt Injection Security
category: troubleshooting
subcategory: prompt-injection-security
tags:
- bugfix
- claude-code
- prompt
date: '2026-08-05'
updated: '2026-08-05'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1vgif8w/the_cutting_room_floor_served_claude_code_a
  title: The Cutting Room Floor served Claude Code a payload telling it to wipe the
    working directory
  date: '2026-08-05'
---

# Prompt Injection Security

---

## 2026-08-05

### The Cutting Room Floor served Claude Code a payload telling it to wipe the working directory

Claude Code が The Cutting Room Floor（tcrf.net）からプロンプトインジェクション攻撃を検知し、作業ディレクトリを削除する悪意のあるペイロードをブロックした事例。サイト側はAIエージェントのDDoS攻撃に対抗するため、特定のUser-Agentに対して攻撃的なプロンプトを返していた。Claude Codeは自動的に攻撃を認識し、ユーザーに警告を表示してドメインを信頼しないと判断した。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vgif8w/the_cutting_room_floor_served_claude_code_a)
- **重要度**: 8/10
- **タグ**: claude-code, prompt, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-05 | 自動生成 |
