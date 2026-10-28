---
title: Browser Use Security
category: guides
subcategory: browser-use-security
tags:
- claude-api
- prompt
- 新機能
date: '2026-10-28'
updated: '2026-10-28'
sources:
- url: https://qiita.com/khronov/items/431c9e1b28673e2aadde
  title: Claude の browser use tool を Playwright の自作ドライバで試した：外部サイトへの移動と注文確定は止まるか
  date: '2026-10-28'
---

# Browser Use Security

---

## 2026-10-28

### Claude の browser use tool を Playwright の自作ドライバで試した：外部サイトへの移動と注文確定は止まるか

Claude の browser use tool を Playwright で実装し、プロンプトインジェクション攻撃と意図しない注文確定を防ぐ仕組みを検証。架空の書店サイトで、URL ポリシーによる外部サイトへの移動制限と confirm による操作確認機能を実装し、2 回のテストでは Claude がページ内の偽指示に従わず、制限機能も正常に動作した。実運用では各サイトで個別の検証が必要。

- **ソース**: [Qiita claude](https://qiita.com/khronov/items/431c9e1b28673e2aadde)
- **重要度**: 7/10
- **タグ**: claude-api, prompt, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-28 | 自動生成 |
