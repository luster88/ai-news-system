---
title: Mcp Setup
category: guides
subcategory: mcp-setup
tags:
- claude-code
- mcp
- setup
date: '2026-04-07'
updated: '2026-06-24'
sources:
- url: https://qiita.com/76Hata/items/6ce2cde9826f5c3a1de2
  title: MCP（Model Context Protocol）入門 — AIエージェントと外部ツールをつなぐ標準規格
  date: '2026-04-07'
- url: https://qiita.com/Bulgent/items/b8e62b11f4789e62f144
  title: Claude CodeでAsanaを使うためのMCP設定手順
  date: '2026-04-21'
- url: https://qiita.com/DevMasatoman/items/caa0def95815085466a4
  title: claude mcp add で MCP を実運用した記録 — 設定・一覧・削除の全コマンドと詰まりどころ
  date: '2026-06-24'
---



# Mcp Setup

---

## 2026-06-24

### claude mcp add で MCP を実運用した記録 — 設定・一覧・削除の全コマンドと詰まりどころ

Claude Code の MCP 追加コマンド（claude mcp add）の実運用における詳細な手順と注意点を解説。起動コマンドの指定方法、追加後の確認（claude mcp list）、削除（claude mcp remove）の全コマンドを網羅。特に <command> 引数の書き方で詰まりやすく、各 MCP サーバーの公式 README を参照することが重要。認証情報を含む場合はローカルスコープ化と .gitignore 追加を推奨。設定変更後は必ず Claude Code の再起動が必要。

- **ソース**: [Qiita claudecode](https://qiita.com/DevMasatoman/items/caa0def95815085466a4)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 2026-04-21

### Claude CodeでAsanaを使うためのMCP設定手順

Claude CodeでAsanaを使用するためのMCP設定手順を解説。Asanaアプリの作成、OAuthリダイレクトURL設定、コマンドライン実行、認証プロセスを順を追って説明している。Claude Code再起動後にMCP接続を確認する必要がある。

- **ソース**: [Qiita claudecode](https://qiita.com/Bulgent/items/b8e62b11f4789e62f144)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 2026-04-07

### MCP（Model Context Protocol）入門 — AIエージェントと外部ツールをつなぐ標準規格

Anthropicが開発したMCP（Model Context Protocol）は、AIエージェントと外部サービス（Slack、Google Drive、PostgreSQLなど）を接続するためのオープン標準規格です。USB-Cのように統一されたプロトコルで、ツール・リソース・プロンプトの3種類の機能を提供し、Claude Codeなど対応クライアントから簡単に利用できます。ツールスキーマがコンテキストに含まれるためトークン消費に注意が必要で、認証やPrompt Injection対策などのセキュリティ考慮も重要です。

- **ソース**: [Qiita claude](https://qiita.com/76Hata/items/6ce2cde9826f5c3a1de2)
- **重要度**: 8/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-07 | 自動生成 |
