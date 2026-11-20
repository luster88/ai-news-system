---
title: Claude Code Stdin Error
category: troubleshooting
subcategory: claude-code-stdin-error
tags:
- bugfix
- claude-code
- setup
date: '2026-11-20'
updated: '2026-11-20'
sources:
- url: https://qiita.com/homhom44/items/69c886d6a34b3346b82f
  title: Claude Code で "Raw mode is not supported on the current process.stdin" が出たときの直し方(パイプ・CI
    では claude -p)
  date: '2026-11-20'
---

# Claude Code Stdin Error

---

## 2026-11-20

### Claude Code で "Raw mode is not supported on the current process.stdin" が出たときの直し方(パイプ・CI では claude -p)

Claude Code をパイプ・CI環境で実行時に「Raw mode is not supported on the current process.stdin」エラーが出る問題の対処法を解説。対話モードは端末（TTY）が必要なため、スクリプトやCI環境では `-p`（print モード）を使用してプロンプトを引数または標準入力で渡す必要がある。v2.1.287以降はエラーメッセージが改善され、Windows/macOS/Linuxで挙動が異なる。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/69c886d6a34b3346b82f)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-20 | 自動生成 |
