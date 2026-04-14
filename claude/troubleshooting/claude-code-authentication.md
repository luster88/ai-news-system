---
title: Claude Code Authentication
category: troubleshooting
subcategory: claude-code-authentication
tags:
- claude-code
- linux
- setup
date: '2026-04-14'
updated: '2026-04-14'
sources:
- url: https://zenn.dev/kazs1000/articles/1b3ad9ef68cfc9
  title: コンテナでClaudeCodeの認証が上手くいかない対処法
  date: '2026-04-14'
---

# Claude Code Authentication

---

## 2026-04-14

### コンテナでClaudeCodeの認証が上手くいかない対処法

Devcontainer 環境で Claude Code の認証が毎回必要になる問題の対処法。認証ファイルが2箇所に分散しており ~/.claude.json がマウントできていないことが原因。暫定対処として環境変数 CLAUDE_API_KEY にトークンを直接設定する方法を紹介。トークンの有効期限は約1年。

- **ソース**: [Zenn claude](https://zenn.dev/kazs1000/articles/1b3ad9ef68cfc9)
- **重要度**: 6/10
- **タグ**: claude-code, setup, linux

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-14 | 自動生成 |
