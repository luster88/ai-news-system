---
title: Breaking Changes
category: releases
subcategory: breaking-changes
tags:
- claude-api
- opus
- release
date: '2026-06-22'
updated: '2026-06-22'
sources:
- url: https://qiita.com/picnic/items/7f47405f515731b37f3f
  title: Claude Fable 5 & Opus 4.8 の破壊的変更と移行ガイド
  date: '2026-06-22'
---

# Breaking Changes

---

## 2026-06-22

### Claude Fable 5 & Opus 4.8 の破壊的変更と移行ガイド

Anthropic が Claude Fable 5・Mythos 5・Opus 4.8 で破壊的変更を実施。thinking モードが adaptive のみサポートとなり、disabled 指定や手動 budget 設定は 400 エラーに。Opus 4.8 では temperature・top_p・top_k の非デフォルト値が使用不可。Fable 5 は 30 日間データ保持が必須で ZDR 不可。Opus 4.6 Fast mode は 2026 年 7 月下旬に削除予定。移行時はステージング環境での全体テストが必須。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/7f47405f515731b37f3f)
- **重要度**: 9/10
- **タグ**: opus, release, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-22 | 自動生成 |
