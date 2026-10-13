---
title: Security Configuration
category: guides
subcategory: security-configuration
tags:
- claude-code
- setup
- 新機能
date: '2026-10-13'
updated: '2026-10-13'
sources:
- url: https://zenn.dev/okzaq/articles/claude-code-env-guard-hook
  title: Claude Code が .env を開く前に止める。deny ルールと PreToolUse フックの最小構成
  date: '2026-10-13'
---

# Security Configuration

---

## 2026-10-13

### Claude Code が .env を開く前に止める。deny ルールと PreToolUse フックの最小構成

Claude Codeが.envファイルを開いてAPI キーやパスワードを会話ログに残すのを防ぐ方法を解説。permissions.denyによる組み込みツールとcatコマンドの拒否ルール設定と、PreToolUseフック（Python 1ファイル）による2段構えの防御構成を提示。拒否ルールだけではすり抜けられるsh -c経由のコマンドもフックで確実にブロックできる。

- **ソース**: [Zenn claude](https://zenn.dev/okzaq/articles/claude-code-env-guard-hook)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-13 | 自動生成 |
