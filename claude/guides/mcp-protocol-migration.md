---
title: Mcp Protocol Migration
category: guides
subcategory: mcp-protocol-migration
tags:
- mcp
- setup
- 新機能
date: '2026-07-31'
updated: '2026-07-31'
sources:
- url: https://zenn.dev/hisa_tech_2973/articles/66aada00d0e727
  title: MCP新仕様(2026-07-28)のステートレス化を試してみました
  date: '2026-07-31'
---

# Mcp Protocol Migration

---

## 2026-07-31

### MCP新仕様(2026-07-28)のステートレス化を試してみました

MCPプロトコルの2026-07-28仕様で導入されたステートレス化を、Go + Dockerで実際に検証した記事。従来のハンドシェイク方式（initialize → notifications/initialized）が廃止され、接続の概念そのものが手放されたことを確認。Go SDK v1.6.1とv1.7.0を別モジュールとして並行稼働させ、旧仕様・新仕様の両方でJSON-RPCリクエストを直接送信して動作を比較。Claude Code自身はまだ旧仕様のハンドシェイクで接続してくることも確認し、クライアント・サーバー双方の対応が揃って初めてプロトコル変化が意味を持つことを実証した。

- **ソース**: [Zenn claude](https://zenn.dev/hisa_tech_2973/articles/66aada00d0e727)
- **重要度**: 7/10
- **タグ**: mcp, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-31 | 自動生成 |
