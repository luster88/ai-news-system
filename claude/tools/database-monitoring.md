---
title: Database Monitoring
category: tools
subcategory: database-monitoring
tags:
- claude-code
- mcp
- setup
date: '2026-10-17'
updated: '2026-10-17'
sources:
- url: https://ai-heartland.com/tool/pgbot
  title: pgbotとは｜Postgresを読み取り専用で診断するGo製CLIを、MCPとCIの終了コードまで実測
  date: '2026-10-17'
---

# Database Monitoring

---

## 2026-10-17

### pgbotとは｜Postgresを読み取り専用で診断するGo製CLIを、MCPとCIの終了コードまで実測

pgbotはPostgreSQLの統計ビューを読み取り専用で診断するGo製CLIツール。pg_monitorロールで接続し、インデックスの未使用やVACUUMの問題などを所見として出力する。終了コードでCI連携が可能で、--jsonオプションでAIエージェントへの受け渡しにも対応。MCPサーバーとして12のツールを提供し、任意のSQL実行はできない読み取り専用設計。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/pgbot)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-17 | 自動生成 |
