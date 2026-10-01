---
title: Data Validation
category: guides
subcategory: data-validation
tags:
- claude-api
- cowork
- prompt
date: '2026-10-01'
updated: '2026-10-01'
sources:
- url: https://zenn.dev/liatris/articles/20261001-content-drift-check
  title: 公開ページと実データのずれをAIで自動検知する
  date: '2026-10-01'
---

# Data Validation

---

## 2026-10-01

### 公開ページと実データのずれをAIで自動検知する

公開ページと内部データの意味的な差異を Claude API で自動検知する仕組みの実装例。html.parser でページを構造化し、Claude に両者を渡して「意味として食い違っている項目」のみを JSON で抽出させる。表記ゆれは無視し、価格や機能の欠落など重要な差分だけを報告。CI 組み込みを想定し、差異があれば exit code 1 で終了する設計。unittest.mock で API キーなしでもテスト可能にしている。

- **ソース**: [Zenn claude](https://zenn.dev/liatris/articles/20261001-content-drift-check)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-01 | 自動生成 |
