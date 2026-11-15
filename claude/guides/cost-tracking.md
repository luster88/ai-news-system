---
title: Cost Tracking
category: guides
subcategory: cost-tracking
tags:
- claude-code
- performance
- pricing
date: '2026-11-15'
updated: '2026-11-15'
sources:
- url: https://qiita.com/joinclass/items/9b8f696841ad8e29d6d3
  title: 夜間のclaude -pジョブをモデル別に計測する — ログからトークン数・所要時間・失敗率を集計する方法
  date: '2026-11-15'
---

# Cost Tracking

---

## 2026-11-15

### 夜間のclaude -pジョブをモデル別に計測する — ログからトークン数・所要時間・失敗率を集計する方法

合同会社ジョインクラスでは30個以上のClaude CLIジョブを夜間・日中に運用しているが、コスト把握が不十分だった。`claude -p --output-format json`を共通ラッパー経由で呼び出し、トークン数・所要時間・失敗率をジョブ単位・モデル単位で集計する仕組みを構築。cache_creation_input_tokensが41,000トークンと大きく、固定オーバーヘッドが大半を占めることが判明し、呼び出し回数削減が最も効果的だとわかった。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/9b8f696841ad8e29d6d3)
- **重要度**: 6/10
- **タグ**: claude-code, performance, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-15 | 自動生成 |
