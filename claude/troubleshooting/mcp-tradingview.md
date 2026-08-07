---
title: Mcp Tradingview
category: troubleshooting
subcategory: mcp-tradingview
tags:
- bugfix
- mcp
date: '2026-08-07'
updated: '2026-08-07'
sources:
- url: https://zenn.dev/kairos_systems/articles/bf4b2c01a212ad
  title: TradingView MCPの落とし穴 — エラーを出さずに間違った値を返す6つの挙動
  date: '2026-08-07'
---

# Mcp Tradingview

---

## 2026-08-07

### TradingView MCPの落とし穴 — エラーを出さずに間違った値を返す6つの挙動

TradingView MCPの実運用で発見された6つの重大な問題点を報告。data_get_study_valuesが小数を整数に丸める、銘柄指定が無視される、最大500本制限など、エラーを出さずに間違った値を返す挙動を3ヶ月の運用で確認。各ツールの信頼性を個別検証する必要があり、精度が必要な場合は別経路でのデータ取得を推奨。

- **ソース**: [Zenn claude](https://zenn.dev/kairos_systems/articles/bf4b2c01a212ad)
- **重要度**: 7/10
- **タグ**: mcp, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-07 | 自動生成 |
