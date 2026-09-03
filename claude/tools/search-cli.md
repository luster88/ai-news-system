---
title: Search Cli
category: tools
subcategory: search-cli
tags:
- mcp
- performance
- setup
date: '2026-09-03'
updated: '2026-09-03'
sources:
- url: https://ai-heartland.com/tool/zvec-grep
  title: zvec-grepとは｜ripgrep・BM25・ベクトル検索を1つにまとめるローカル検索CLIを実測
  date: '2026-09-03'
---

# Search Cli

---

## 2026-09-03

### zvec-grepとは｜ripgrep・BM25・ベクトル検索を1つにまとめるローカル検索CLIを実測

zvec-grepは、ripgrep（正規表現）・BM25（全文検索）・ベクトル検索を1つの索引で統合するローカル検索CLIツール。日本語Markdown 120本の実測では索引作成に20分50秒かかるが、検索自体は1秒前後で完了。ローカル完結設計のため展開後568MBと大きく、Node.js 22以上が必要。検索結果には使用した経路（fts/vector）が明示され、AIエージェントへの文脈供給に適した設計となっている。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/zvec-grep)
- **重要度**: 6/10
- **タグ**: mcp, performance, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-03 | 自動生成 |
