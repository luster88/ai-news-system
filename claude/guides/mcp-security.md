---
title: Mcp Security
category: guides
subcategory: mcp-security
tags:
- claude-code
- mcp
- setup
date: '2026-06-10'
updated: '2026-06-27'
sources:
- url: https://qiita.com/hisashiyamaguchi/items/47607c6657028700fe57
  title: Claude DesktopとEPSS, NVD, KEV, Anomaliで脆弱性対策を検討してみた
  date: '2026-06-10'
- url: https://zenn.dev/kta1kri/books/owasp-mcp-top10
  title: OWASP MCP Top 10 実装・検知・隔離ガイド ― SOCアナリストが書くMCPセキュリティ
  date: '2026-06-27'
---


# Mcp Security

---

## 2026-06-27

### OWASP MCP Top 10 実装・検知・隔離ガイド ― SOCアナリストが書くMCPセキュリティ

現役SOCアナリストによるMCP（Model Context Protocol）のセキュリティガイド。OWASP Top 10形式でスコープ肥大による権限昇格、コマンドインジェクション、認証・認可の不備、シャドーMCPサーバーなど10項目の脅威を実装・検知・隔離の観点から解説。AIエージェントを防御する側の実践的なセキュリティ知見を提供。

- **ソース**: [Zenn claude](https://zenn.dev/kta1kri/books/owasp-mcp-top10)
- **重要度**: 8/10
- **タグ**: mcp

---

## 2026-06-10

### Claude DesktopとEPSS, NVD, KEV, Anomaliで脆弱性対策を検討してみた

Claude DesktopとMCP連携を活用した脆弱性対策手順を紹介。EPSS、NVD、KEVなどの公開脆弱性データベースとAnomali脅威インテリジェンスを組み合わせて利用。MCP Bundlesを使ったセットアップ手順と、Chatモード利用時の注意点（Coworkではインターネット検索になる問題）を解説。脆弱性対策は自組織の資産とソフトウェア環境の把握が重要と強調。

- **ソース**: [Qiita claude](https://qiita.com/hisashiyamaguchi/items/47607c6657028700fe57)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-10 | 自動生成 |
