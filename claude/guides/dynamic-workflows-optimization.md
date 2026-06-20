---
title: Dynamic Workflows Optimization
category: guides
subcategory: dynamic-workflows-optimization
tags:
- claude-code
- performance
- 新機能
date: '2026-06-20'
updated: '2026-06-20'
sources:
- url: https://zenn.dev/mdtechknowledge/articles/dynamic-workflows-token-cache-analysis
  title: Dynamic Workflows のトークン実測分析 — キャッシュ読込比率とコスト削減率は『並列度』とともに上がる（15実行）
  date: '2026-06-20'
---

# Dynamic Workflows Optimization

---

## 2026-06-20

### Dynamic Workflows のトークン実測分析 — キャッシュ読込比率とコスト削減率は『並列度』とともに上がる（15実行）

Claude Code の Dynamic Workflows を15回実行した実測データ分析。キャッシュ読込比率は44〜90%、コスト削減率は23〜77%に分布し、両者は強く連動。最大の傾向は「並列度（サブエージェント数）が高いほどキャッシュ効率が上がる」点で、31〜52体規模では削減率65〜77%に達する。共有プレフィックス（システムプロンプト・ツール定義等）を多数のサブエージェントが再利用するため、大規模ファンアウトは費用効率的。1エージェント当たりコストは規模を上げても膨らまない。

- **ソース**: [Zenn claude](https://zenn.dev/mdtechknowledge/articles/dynamic-workflows-token-cache-analysis)
- **重要度**: 7/10
- **タグ**: claude-code, performance, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-20 | 自動生成 |
