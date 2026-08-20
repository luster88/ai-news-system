---
title: Usage Analysis
category: tools
subcategory: usage-analysis
tags:
- claude-code
- performance
- pricing
date: '2026-08-20'
updated: '2026-08-20'
sources:
- url: https://zenn.dev/chiisanasoft/articles/88757cec318916
  title: Claude Code の利用ログを SQLite に取り込んで API 換算したら302万円だった
  date: '2026-08-20'
---

# Usage Analysis

---

## 2026-08-20

### Claude Code の利用ログを SQLite に取り込んで API 換算したら302万円だった

Claude Code のローカル利用ログを SQLite に取り込み API 単価で換算したところ、4ヶ月弱で302万円相当だった。重要な発見として、プロンプト短縮の節約効果は0.2%に過ぎず、金額の3分の2はキャッシュ読み出しが占める。また、集計ツールが新モデルを0円扱いしていたため、総額の33%を見落とす問題が発生。「0円」と「不明」を区別せず、フォールバック処理も痕跡を残さない設計の危険性を指摘している。

- **ソース**: [Zenn claude](https://zenn.dev/chiisanasoft/articles/88757cec318916)
- **重要度**: 6/10
- **タグ**: claude-code, pricing, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-20 | 自動生成 |
