---
title: Performance Testing
category: guides
subcategory: performance-testing
tags:
- claude-code
- performance
- pricing
- sonnet
date: '2026-08-01'
updated: '2026-10-13'
sources:
- url: https://qiita.com/udonAir/items/3779c72e02e37d88b273
  title: 「Sonnet 5 にしたらトークン数が増える」は本当か、実測してみた
  date: '2026-08-01'
- url: https://qiita.com/kenji_harada/items/43f5348563728dea7e12
  title: Claude Sonnet 5.5 の性能を実測｜5 モデル計 90 回で時間は Opus 5 の 0.35 倍、成功数は差なし
  date: '2026-10-13'
---


# Performance Testing

---

## 2026-10-13

### Claude Sonnet 5.5 の性能を実測｜5 モデル計 90 回で時間は Opus 5 の 0.35 倍、成功数は差なし

Claude Sonnet 5.5を含む5モデルでNode.js課題90回の実測を実施。Opus 5比で時間0.35倍、費用0.28倍と「Sonnet 5より速く安い」という公式発表と一致。全モデルが18/18で成功し、易しい課題では性能差は見られなかったが、Sonnet 5.5が時間・費用ともに最小を記録。

- **ソース**: [Qiita claudecode](https://qiita.com/kenji_harada/items/43f5348563728dea7e12)
- **重要度**: 6/10
- **タグ**: sonnet, performance, claude-code

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
