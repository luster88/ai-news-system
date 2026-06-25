---
title: Performance Analysis
category: guides
subcategory: performance-analysis
tags:
- claude-code
- performance
- prompt
date: '2026-06-25'
updated: '2026-06-25'
sources:
- url: https://qiita.com/leomarokun/items/1e299daebd089b26786d
  title: Claude Code のトークン消費を実測したら、ほとんどは本当にキャッシュだった
  date: '2026-06-25'
---

# Performance Analysis

---

## 2026-06-25

### Claude Code のトークン消費を実測したら、ほとんどは本当にキャッシュだった

Claude Code の実際のトークン消費を JSONL から集計した結果、入力の 95% がキャッシュから読み込まれており、プロンプトキャッシュが無い場合と比較して約 77% のコスト削減効果があることが判明。長期セッションでは ReAct 型の履歴積み上げによりコンテキストが線形増加するが、キャッシュ再利用により実質的な課金を大幅に抑制できている。Don't Break the Cache 論文の主張を裏付ける実測データ。

- **ソース**: [Qiita claude](https://qiita.com/leomarokun/items/1e299daebd089b26786d)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-25 | 自動生成 |
