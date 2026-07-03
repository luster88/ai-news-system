---
title: Model Comparison
category: guides
subcategory: model-comparison
tags:
- cowork
- opus
- performance
- sonnet
date: '2026-06-12'
updated: '2026-07-03'
sources:
- url: https://zenn.dev/znet/articles/2026-stronger-model-as-reviewer
  title: 高性能モデルの使いどころは『実装者』でなく『レビュアー』 — Fable 5 実機評価
  date: '2026-06-12'
- url: https://zenn.dev/yukurash/articles/aba0e5d2acf7cd
  title: 【Fable 5 vs Opus 4.8】PM として優れているのはどちらか検証した
  date: '2026-07-03'
---


# Model Comparison

---

## 2026-07-03

### 【Fable 5 vs Opus 4.8】PM として優れているのはどちらか検証した

Claude の Fable 5 と Opus 4.8 を PM（プロジェクトマネージャー）役に設定し、Sonnet エージェントを部下としたアプリ開発チームを構成して比較検証。完成時間は Fable 5 が早く、ゲームの見た目も優れていたが、トークン数はほぼ同等で大きな差は見られなかった。簡単なタスクでは両モデルの違いが現れにくく、Fable 5 の価値を最大化するには人間側の使い方も重要という結論に至った。

- **ソース**: [Zenn claude](https://zenn.dev/yukurash/articles/aba0e5d2acf7cd)
- **重要度**: 6/10
- **タグ**: opus, sonnet, performance

---

## 2026-06-12

### 高性能モデルの使いどころは『実装者』でなく『レビュアー』 — Fable 5 実機評価

Claude Fable 5（Opus 4.8の約2倍の単価）を実機評価した結果、中難度タスクでは速度面で優位だが価値差は小さく、真価を発揮するのは高難度タスクでのレビュアー役であることが判明。実装側モデルが創作した存在しないAPIフィールドを、Fable 5が公式仕様を自走取得して検出し、本番事故を未然に防いだ事例を紹介。採用方針は「実装は従来モデル×レビューはFable」の独立アドバーサリアル構成が本命。

- **ソース**: [Zenn claude](https://zenn.dev/znet/articles/2026-stronger-model-as-reviewer)
- **重要度**: 7/10
- **タグ**: opus, performance, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-12 | 自動生成 |
