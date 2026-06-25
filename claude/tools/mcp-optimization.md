---
title: Mcp Optimization
category: tools
subcategory: mcp-optimization
tags:
- claude-code
- mcp
- performance
date: '2026-06-25'
updated: '2026-06-25'
sources:
- url: https://zenn.dev/taka4/articles/fb3809bc7e4a82
  title: 56本 → 5本、88%削減 — TiDB FTS+Vectorで作るAbility Discovery Layer
  date: '2026-06-25'
---

# Mcp Optimization

---

## 2026-06-25

### 56本 → 5本、88%削減 — TiDB FTS+Vectorで作るAbility Discovery Layer

MCP サーバーやスキルが50本以上になると毎回1万トークン以上消費する問題に対し、TiDB CloudのFTS+ベクター検索を使った「Ability Discovery Layer」を実装。ユーザーの問い合わせに応じて必要なツールだけを動的に選択することで、平均88%のトークン削減を達成した事例。日本語クエリの精度向上のためLLMでクエリ拡張を行い、FTS（全文検索）とベクター検索のハイブリッド方式で実用的な精度を実現。

- **ソース**: [Zenn claude](https://zenn.dev/taka4/articles/fb3809bc7e4a82)
- **重要度**: 6/10
- **タグ**: mcp, performance, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-25 | 自動生成 |
