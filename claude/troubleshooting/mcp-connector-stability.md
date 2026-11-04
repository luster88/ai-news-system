---
title: Mcp Connector Stability
category: troubleshooting
subcategory: mcp-connector-stability
tags:
- claude-code
- cowork
- mcp
date: '2026-11-04'
updated: '2026-11-04'
sources:
- url: https://qiita.com/Hideki_Tamae/items/1791f7b58a7fe4e22018
  title: 2。16日前「即使える」と書いたコネクタ4個と、今日実際に使えた4個を比べたら、重なっていたのはこの数字だった
  date: '2026-11-04'
---

# Mcp Connector Stability

---

## 2026-11-04

### 2。16日前「即使える」と書いたコネクタ4個と、今日実際に使えた4個を比べたら、重なっていたのはこの数字だった

Claude Code の MCP コネクタ接続状態を16日間隔で2回観測した結果、「即使える」コネクタ数は4個で変わらなかったが、内訳は Gmail/Google Calendar が切断され、Notion/Supabase が接続済みに変わるなど入れ替わっていた。接続状態の合計数が同じでも中身が変動する可能性があり、自動化パイプラインでは定期的な接続確認が必要であることを実証した観測記録。

- **ソース**: [Qiita claudecode](https://qiita.com/Hideki_Tamae/items/1791f7b58a7fe4e22018)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-04 | 自動生成 |
