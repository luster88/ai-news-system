---
title: Claude Skills Comparison
category: guides
subcategory: claude-skills-comparison
tags:
- claude-code
- cowork
- 新機能
date: '2026-10-06'
updated: '2026-10-06'
sources:
- url: https://ai-heartland.com/agent/claude-skills-ui-polish
  title: Claude Skills UI磨き込み2本を突き合わせた｜指定値が食い違う3箇所をブラウザで検証
  date: '2026-10-06'
---

# Claude Skills Comparison

---

## 2026-10-06

### Claude Skills UI磨き込み2本を突き合わせた｜指定値が食い違う3箇所をブラウザで検証

Claude Skills（エージェント用の知識ファイル）のUI磨き込み系スキル2本（emil-design-engとbetter-ui）を比較検証。押下時の縮小率（0.97 vs 0.96）、stagger間隔（30-80ms vs 100ms）、ease-out曲線など3箇所で指定値が食い違うことを発見。ブラウザで実行して技術的主張を検証し、構成の違い（674行の一枚岩 vs 112行の索引＋分割ファイル）により読み込み量が3.8倍異なることを計測。複数のスキルを同時導入した際の挙動と設計思想の違いを実測データで明らかにした記事。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/claude-skills-ui-polish)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-06 | 自動生成 |
