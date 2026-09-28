---
title: Simulation Validation
category: troubleshooting
subcategory: simulation-validation
tags:
- bugfix
- claude-code
- performance
date: '2026-09-28'
updated: '2026-09-28'
sources:
- url: https://zenn.dev/canaiclimbspire/articles/001_sim_lost_to_average
  title: 自作の「ラン全体シミュレーター」が、ただの平均値に負けた話
  date: '2026-09-28'
---

# Simulation Validation

---

## 2026-09-28

### 自作の「ラン全体シミュレーター」が、ただの平均値に負けた話

Claude を使った Slay the Spire の AI プレイヤー開発で、「ラン全体シミュレーター」を自作したが検証の結果、精度が「常に勝つと予測する単純な基準」にすら負けた失敗談。デッキの強さを1つの数字で表現する簡易モデルから、カード実装ベースの戦闘エンジンへ作り直したが、実装バグで効果を過大評価していた。戦闘シミュレーターの精度88.7%も、実際の勝率94.1%を下回る結果に。機械学習における評価指標の落とし穴と、シミュレーション開発の難しさを示す実例。

- **ソース**: [Zenn claude](https://zenn.dev/canaiclimbspire/articles/001_sim_lost_to_average)
- **重要度**: 4/10
- **タグ**: claude-code, performance, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-28 | 自動生成 |
