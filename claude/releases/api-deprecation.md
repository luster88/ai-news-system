---
title: Api Deprecation
category: releases
subcategory: api-deprecation
tags:
- bugfix
- claude-api
- claude-console
date: '2026-07-20'
updated: '2026-07-20'
sources:
- url: https://qiita.com/picnic/items/9b95bd4d0c80f3299f26
  title: Claude旧Workbench廃止＆実験的プロンプトAPI終了、8/17までの移行対応まとめ
  date: '2026-07-20'
---

# Api Deprecation

---

## 2026-07-20

### Claude旧Workbench廃止＆実験的プロンプトAPI終了、8/17までの移行対応まとめ

Anthropicが2026年8月17日に旧Workbench（platform.claude.com/workbench）と実験的プロンプトツールAPI 3種（generate_prompt/improve_prompt/templatize_prompt）を廃止すると発表。severity: criticalの破壊的変更で、廃止後はリクエストがエラーになる。移行猶予は約1ヶ月のため、保存済みプロンプト・変数・評価データのエクスポートとAPI利用箇所の洗い出し・代替実装への移行が急務。通常のMessages APIでの代替実装が推奨される。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/9b95bd4d0c80f3299f26)
- **重要度**: 9/10
- **タグ**: claude-console, claude-api, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-20 | 自動生成 |
