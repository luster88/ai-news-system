---
title: Hallucination Limits
category: troubleshooting
subcategory: hallucination-limits
tags:
- claude-api
- performance
- prompt
date: '2026-04-17'
updated: '2026-04-17'
sources:
- url: https://qiita.com/himajisan/items/12dc52b7170570f2abb4
  title: claudeは知識にないことを聞くとアホである
  date: '2026-04-17'
---

# Hallucination Limits

---

## 2026-04-17

### claudeは知識にないことを聞くとアホである

Mini-ZのNRスポンジタイヤ自作でClaudeに接着寸法の最適化を依頼したところ、学習データに存在しない実験領域では破綻することを確認。ホイール径とスポンジ外径の周長計算を繰り返し、物理的直感を欠いた誤答を自信満々に返した。実測データ（ヤング率測定値）を与えると正確に動作したことから、AIは既存知識の範囲内でのみ有効であり、未知領域では「答えを出す圧力」により誤った方向へ進む構造的限界があると結論付けた。ChatGPTも同様の誤答を示した。

- **ソース**: [Qiita claude](https://qiita.com/himajisan/items/12dc52b7170570f2abb4)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-17 | 自動生成 |
