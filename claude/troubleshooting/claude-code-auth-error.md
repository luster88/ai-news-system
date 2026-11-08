---
title: Claude Code Auth Error
category: troubleshooting
subcategory: claude-code-auth-error
tags:
- bugfix
- claude-code
- setup
date: '2026-11-08'
updated: '2026-11-08'
sources:
- url: https://qiita.com/homhom44/items/e8d89b70cba590ac0cd4
  title: Claude Code で "Invalid API key · Fix external API key" "Invalid auth token"
    が出たときの直し方（キーが正しいのに出る場合は改行やゼロ幅スペースの混入）
  date: '2026-11-08'
---

# Claude Code Auth Error

---

## 2026-11-08

### Claude Code で "Invalid API key · Fix external API key" "Invalid auth token" が出たときの直し方（キーが正しいのに出る場合は改行やゼロ幅スペースの混入）

Claude Codeで「Invalid API key」や「Invalid auth token」エラーが出る場合の対処法を解説。主な原因は、キーの失効・間違い、環境変数の古いキー、コピペ時の改行やゼロ幅スペースの混入。エラーメッセージに「line break at character N」などの詳細が含まれる場合は、キーに不正な文字が混入している証拠。環境変数の確認や/loginコマンドでの再設定が推奨される。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/e8d89b70cba590ac0cd4)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-08 | 自動生成 |
