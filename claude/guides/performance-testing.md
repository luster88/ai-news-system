---
title: Performance Testing
category: guides
subcategory: performance-testing
tags:
- performance
- pricing
- sonnet
date: '2026-08-01'
updated: '2026-08-01'
sources:
- url: https://qiita.com/udonAir/items/3779c72e02e37d88b273
  title: 「Sonnet 5 にしたらトークン数が増える」は本当か、実測してみた
  date: '2026-08-01'
---

# Performance Testing

---

## 2026-08-01

### 「Sonnet 5 にしたらトークン数が増える」は本当か、実測してみた

Sonnet 5 のトークナイザ変更による影響を実測した結果、日本語は1トークンも変わらず、英語は1.28〜1.46倍に増加することが判明。API の input_tokens には 120〜160 トークンの固定オーバーヘッドが含まれており、短い文章での測定では誤差が大きくなる。4.6 → 5 のコスト変動は日本語チャットで −7%〜+12% 程度と推定。

- **ソース**: [Qiita claude](https://qiita.com/udonAir/items/3779c72e02e37d88b273)
- **重要度**: 7/10
- **タグ**: sonnet, performance, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-01 | 自動生成 |
