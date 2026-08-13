---
title: Mcp Oauth Redirect
category: troubleshooting
subcategory: mcp-oauth-redirect
tags:
- bugfix
- claude-code
- mcp
date: '2026-08-13'
updated: '2026-08-13'
sources:
- url: https://qiita.com/moha0918_/items/e0970dd96706c59e6b69
  title: Claude Code v2.1.231｜Slack の MCP OAuth が redirect URI で弾かれる問題を修正｜毎日Changelog解説
  date: '2026-08-13'
---

# Mcp Oauth Redirect

---

## 2026-08-13

### Claude Code v2.1.231｜Slack の MCP OAuth が redirect URI で弾かれる問題を修正｜毎日Changelog解説

Claude Code v2.1.231 では、事前登録済み OAuth クライアントを使う MCP サーバー（Slack など）でサインイン時に redirect URI の不一致で弾かれていた問題が修正されました。リダイレクトポートが毎回変わることで認証が失敗していましたが、--callback-port オプションでポートを固定できるようになり、事前登録した redirect URI との一致が保証されるようになりました。HTTP/SSE トランスポート専用の機能で、古い認証情報がある場合は claude mcp logout で削除してから再ログインする必要があります。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/e0970dd96706c59e6b69)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-13 | 自動生成 |
