---
title: Claude Code Authentication
category: troubleshooting
subcategory: claude-code-authentication
tags:
- bugfix
- claude-code
- linux
- setup
date: '2026-04-14'
updated: '2026-10-24'
sources:
- url: https://zenn.dev/kazs1000/articles/1b3ad9ef68cfc9
  title: コンテナでClaudeCodeの認証が上手くいかない対処法
  date: '2026-04-14'
- url: https://qiita.com/homhom44/items/9a50e8fc034637d1a3e3
  title: Max/Pro 契約なのに Claude Code で『Credit balance is too low』が出るのは、環境に残った ANTHROPIC_API_KEY
    のせい
  date: '2026-10-24'
---


# Claude Code Authentication

---

## 2026-10-24

### Max/Pro 契約なのに Claude Code で『Credit balance is too low』が出るのは、環境に残った ANTHROPIC_API_KEY のせい

Claude Max/Pro契約者がClaude Codeで「Credit balance is too low」エラーが出る問題を解説。環境変数ANTHROPIC_API_KEYが残っていると、サブスクより優先されてAPI課金モードになることが原因。認証優先順位の仕組みと、設定ファイルからキーを削除する対処法を説明している。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/9a50e8fc034637d1a3e3)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

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
