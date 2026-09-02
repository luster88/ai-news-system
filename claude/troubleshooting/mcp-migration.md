---
title: Mcp Migration
category: troubleshooting
subcategory: mcp-migration
tags:
- bugfix
- mcp
- setup
date: '2026-09-02'
updated: '2026-09-02'
sources:
- url: https://qiita.com/daisuke-nagata/items/58a30db7eddc8c587ea5
  title: 【2026年版】MCP SDK 2.0で壊れる5箇所まとめ。移行は3行
  date: '2026-09-02'
---

# Mcp Migration

---

## 2026-09-02

### 【2026年版】MCP SDK 2.0で壊れる5箇所まとめ。移行は3行

MCP SDK 2.0への移行で発生する破壊的変更について、実際に1.27.1と2.1.1を比較検証した記録。pyproject.tomlで上限指定なしの場合、pip installで2.1.1が入りimportエラーが発生する。移行自体は3行の修正で済むが、ctx.client_idが黙って変わる点が厄介。公式は1.xブランチでの保守を継続しており、急ぐ理由がなければmcp<2で上限指定するのが推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/daisuke-nagata/items/58a30db7eddc8c587ea5)
- **重要度**: 7/10
- **タグ**: mcp, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-02 | 自動生成 |
