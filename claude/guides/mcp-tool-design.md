---
title: Mcp Tool Design
category: guides
subcategory: mcp-tool-design
tags:
- mcp
- performance
- prompt
date: '2026-08-18'
updated: '2026-08-18'
sources:
- url: https://zenn.dev/ma2no4413/articles/mcp-tool-design-csv-argument
  title: サンプル 8 行では完璧だった — MCP ツールに CSV を引数で渡す設計をやめた話
  date: '2026-08-18'
---

# Mcp Tool Design

---

## 2026-08-18

### サンプル 8 行では完璧だった — MCP ツールに CSV を引数で渡す設計をやめた話

MCP ツールで CSV データを引数として渡す設計の問題点を解説。1MB の CSV では 26 万トークンを消費し、モデルのコンテキストを無駄に圧迫する。データの置き場所を指定する方式に変更し、describe_dataset でメタデータを返す設計に改善。エラーメッセージにはモデルが自己修正できる情報を含め、集計処理は D1（SQL）に押し出すことで Cloudflare Workers の CPU 時間制約を回避する実装パターンを紹介。

- **ソース**: [Zenn claude](https://zenn.dev/ma2no4413/articles/mcp-tool-design-csv-argument)
- **重要度**: 7/10
- **タグ**: mcp, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-18 | 自動生成 |
