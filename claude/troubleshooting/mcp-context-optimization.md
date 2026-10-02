---
title: Mcp Context Optimization
category: troubleshooting
subcategory: mcp-context-optimization
tags:
- mcp
- performance
- prompt
date: '2026-10-02'
updated: '2026-10-02'
sources:
- url: https://qiita.com/shioccii/items/e2496c98c2671c48804b
  title: MCPサーバーでコンテキスト消費が爆発する問題と、CLI/REST APIとの賢い使い分け
  date: '2026-10-02'
---

# Mcp Context Optimization

---

## 2026-10-02

### MCPサーバーでコンテキスト消費が爆発する問題と、CLI/REST APIとの賢い使い分け

MCP サーバーを複数接続すると、ツール定義の JSON Schema が毎ターン自動注入されることで、質問前から数万トークンが消費される構造的な問題が報告されている。GitHub MCP サーバー単体で 8,000-12,000 トークン、ブラウザツールの生レスポンスで数十万トークンが消費され、Prompt Caching でも注意散漫やコンテキスト圧迫は解決しない。対策として Unix CLI 経由でパイプライン処理を活用し、ツール定義を極小化する設計が再評価されている。

- **ソース**: [Qiita claude](https://qiita.com/shioccii/items/e2496c98c2671c48804b)
- **重要度**: 8/10
- **タグ**: mcp, performance, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-02 | 自動生成 |
