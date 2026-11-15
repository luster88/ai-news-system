---
title: Cowork Code Memory
category: troubleshooting
subcategory: cowork-code-memory
tags:
- claude-code
- cowork
- setup
date: '2026-11-15'
updated: '2026-11-15'
sources:
- url: https://qiita.com/takamins/items/d643ddd20da86ca9c0b9
  title: Cowork と Claude Code の memory の食い違いを防ぐ
  date: '2026-11-15'
---

# Cowork Code Memory

---

## 2026-11-15

### Cowork と Claude Code の memory の食い違いを防ぐ

Claude CodeとCoworkを併用する際のmemory管理の違いを解説。Claude Codeのmemoryは~/.claude/projects/<project>/memory/に保存され、Coworkとは別実体。Claude CodeからCoworkのmemoryは読めるが逆は不可。設定画面の指示はClaude Codeには届かず、CLAUDE.mdの記述が有効。併用時は相手側の索引を先に読み、書き込みは自分側のみに行うことで食い違いを防ぐ運用を推奨。

- **ソース**: [Qiita claude](https://qiita.com/takamins/items/d643ddd20da86ca9c0b9)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-15 | 自動生成 |
