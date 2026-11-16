---
title: Mcp Implementation
category: tools
subcategory: mcp-implementation
tags:
- claude-code
- mcp
date: '2026-11-16'
updated: '2026-11-16'
sources:
- url: https://zenn.dev/mappy55/articles/ckakeibo-mcp-server
  title: 自作の家計簿に MCP サーバーを載せたら、Claude がアプリの集計のずれを見つけた
  date: '2026-11-16'
---

# Mcp Implementation

---

## 2026-11-16

### 自作の家計簿に MCP サーバーを載せたら、Claude がアプリの集計のずれを見つけた

自作の家計簿アプリにMCPサーバーを実装し、Claude Desktopから家計診断を依頼したところ、Claude自身が集計ツール間のデータ不一致を発見。原因は旧ソフトからの移行時に「支出」の定義が画面によって異なっていたことで、口座払い支出の扱いに問題があった。MCPツールは既存関数を再利用して実装し、データ整合性テストを追加して修正した。

- **ソース**: [Zenn claude](https://zenn.dev/mappy55/articles/ckakeibo-mcp-server)
- **重要度**: 6/10
- **タグ**: mcp, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-16 | 自動生成 |
