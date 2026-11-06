---
title: Opus Migration
category: guides
subcategory: opus-migration
tags:
- claude-api
- claude-code
- opus
- performance
- 新機能
date: '2026-08-09'
updated: '2026-11-06'
sources:
- url: https://zenn.dev/horizon_it00/articles/claude-opus5-one-week
  title: Claude Opus 5を1週間使って分かったこと
  date: '2026-08-09'
- url: https://qiita.com/kai_kou/items/89ac7d29c7cc3f02ebd1
  title: Opus 5系のthinkingとeffort移行ガイド、4.8から5.5で変わる設定
  date: '2026-11-06'
---


# Opus Migration

---

## 2026-11-06

### Opus 5系のthinkingとeffort移行ガイド、4.8から5.5で変わる設定

Anthropic Opus 4.8、5、5.5における thinking と effort パラメータの世代間の違いを詳細に解説。Opus 4.8では thinking を指定しなければ無効だったが、Opus 5以降は adaptive thinking がデフォルトで有効になり、Opus 5.5では thinking の無効化自体が不可能に。また既定 effort も Opus 5の high から Opus 5.5では medium に変更され、SDK の型チェックでは検出できない破壊的変更が含まれている点を警告。

- **ソース**: [Qiita claude](https://qiita.com/kai_kou/items/89ac7d29c7cc3f02ebd1)
- **重要度**: 8/10
- **タグ**: opus, claude-api, 新機能

---

## 2026-08-09

### Claude Opus 5を1週間使って分かったこと

Claude Opus 5を1週間使用した実践レポート。5ファイルにまたがるリファクタリングがSonnet 5では3往復必要だったのに対し、Opus 5では1セッションで完了。複数ファイル作業での持続力とコンテキスト維持能力が大幅に向上した一方、Adaptive thinkingのデフォルト変更やmax_tokensの調整、システムプロンプトの見直しが必要という注意点も指摘。価格はOpus 4.8と同額でFable 5の半額。

- **ソース**: [Zenn claude](https://zenn.dev/horizon_it00/articles/claude-opus5-one-week)
- **重要度**: 8/10
- **タグ**: opus, claude-code, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-09 | 自動生成 |
