---
title: Code Quality Monitoring
category: tools
subcategory: code-quality-monitoring
tags:
- claude-code
- cursor
- mcp
date: '2026-06-26'
updated: '2026-06-26'
sources:
- url: https://zenn.dev/k0chi/articles/76a4d1d72d2bdb
  title: AI が書いたコードの設計劣化を検知する sentrux をまとめてみる
  date: '2026-06-26'
---

# Code Quality Monitoring

---

## 2026-06-26

### AI が書いたコードの設計劣化を検知する sentrux をまとめてみる

AI コーディングエージェント（Claude Code、Cursor など）を使用する際のコードベース設計劣化を検知するOSSツール「sentrux」の紹介記事。quality_signal という0-10000のスコアで、依存関係、ファイルサイズの偏り、循環依存などからコードベース全体の健康状態を数値化する。MCP連携により、AIエージェント自身がsentruxを呼び出して変更前後の品質差分を確認できる。テストや型チェックの代替ではなく、コードベースが持続的に変更可能な形を保っているかを見るためのツール。

- **ソース**: [Zenn claude](https://zenn.dev/k0chi/articles/76a4d1d72d2bdb)
- **重要度**: 6/10
- **タグ**: claude-code, cursor, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-26 | 自動生成 |
