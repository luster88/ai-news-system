---
title: Login Oauth Errors
category: troubleshooting
subcategory: login-oauth-errors
tags:
- bugfix
- claude-code
- setup
date: '2026-11-12'
updated: '2026-11-12'
sources:
- url: https://qiita.com/homhom44/items/b86ef3361bbcd67ca9a0
  title: 'Claude Code で "OAuth error: timeout of 15000ms exceeded" と "Invalid code"
    が出てログインできないときの対処（SSH・WSL でコードを貼る場合も）'
  date: '2026-11-12'
---

# Login Oauth Errors

---

## 2026-11-12

### Claude Code で "OAuth error: timeout of 15000ms exceeded" と "Invalid code" が出てログインできないときの対処（SSH・WSL でコードを貼る場合も）

Claude Codeのログイン時に「OAuth error: timeout of 15000ms exceeded」や「Invalid code」エラーが発生する問題の対処法を解説。前者はplatform.claude.comへのトークン交換通信が15秒以内に完了しないことが原因で、DNS設定変更や旧バージョンでの再試行が有効。後者はコードの期限切れや貼り付けミスが原因で、特にSSH・WSL環境で発生しやすい。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/b86ef3361bbcd67ca9a0)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-12 | 自動生成 |
