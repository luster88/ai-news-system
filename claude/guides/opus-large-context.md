---
title: Opus Large Context
category: guides
subcategory: opus-large-context
tags:
- claude-code
- opus
- performance
date: '2026-05-25'
updated: '2026-05-25'
sources:
- url: https://qiita.com/kenimo49/items/59ace7346579dc9997a9
  title: Claude Opus 4.7の100万トークン、本当に使い切れるのか — モノレポ丸投げで実測した
  date: '2026-05-25'
---

# Opus Large Context

---

## 2026-05-25

### Claude Opus 4.7の100万トークン、本当に使い切れるのか — モノレポ丸投げで実測した

Claude Opus 4.7の100万トークンコンテキストを実測した記事。640kトークンの中規模モノレポを丸投げして4タスクを検証した結果、依存グラフ整理や横断的なリファクタリングで効果を発揮する一方、NIAH精度は1Mで76%、256kなら93%と低下することが判明。初回応答は約2.1分かかるが、prompt cachingで2回目以降は高速化できる。真の用途は単純なコード生成ではなく文脈横断タスクにある。

- **ソース**: [Qiita claude](https://qiita.com/kenimo49/items/59ace7346579dc9997a9)
- **重要度**: 7/10
- **タグ**: opus, performance, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-25 | 自動生成 |
