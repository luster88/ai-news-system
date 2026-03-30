---
title: Mcp Memory Server
category: tools
subcategory: mcp-memory-server
tags:
- claude-api
- claude-code
- cowork
- mcp
date: '2026-03-30'
updated: '2026-03-30'
sources:
- url: https://zenn.dev/cloto/books/claude-memory-mcp-server
  title: Claudeは明日もあなたを忘れる — MCP Memory Server cpersona 設計と実践
  date: '2026-03-30'
- url: https://zenn.dev/cloto/articles/claude-memory-changed-dev-experience
  title: Claude CodeとClaude Desktopの記憶を共有して変わったこと
  date: '2026-03-30'
---

# Mcp Memory Server

---

## 2026-03-30

### Claudeは明日もあなたを忘れる — MCP Memory Server cpersona 設計と実践

MCP Memory Server「cpersona」の設計と実装に関する解説記事。AIエージェントの記憶管理において、3層ハイブリッドアーキテクチャ、記憶の確からしさを数値化するConfidence Score、エージェント間の記憶汚染を防ぐAnti-Contaminationなどの設計思想と実践方法を詳述している。Claude の文脈保持問題を解決するためのMCPサーバー実装例として有用。

- **ソース**: [Zenn claude](https://zenn.dev/cloto/books/claude-memory-mcp-server)
- **重要度**: 7/10
- **タグ**: mcp, claude-api, cowork

---

### Claude CodeとClaude Desktopの記憶を共有して変わったこと

Claude CodeとClaude Desktopで記憶が分断される問題を、MCP Memory Server「cpersona」で解決した事例。自宅PCをStreamable HTTPサーバーとして起動し、全デバイスから同一のSQLite記憶DBにアクセスすることで、セッション横断・デバイス横断での文脈維持を実現。無料のDDNSとCloudflare Tunnelを使い、ランニングコストゼロで運用可能。

- **ソース**: [Zenn claude](https://zenn.dev/cloto/articles/claude-memory-changed-dev-experience)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-30 | 自動生成 |
