---
title: Opus 5 Migration
category: troubleshooting
subcategory: opus-5-migration
tags:
- claude-api
- opus
- sonnet
date: '2026-10-03'
updated: '2026-10-03'
sources:
- url: https://zenn.dev/persimmoq/articles/claude-opus-5-migration-400-errors
  title: Claude Opus 5 / Sonnet 5 に model だけ変えて移行すると壊れる 7 つの理由
  date: '2026-10-03'
---

# Opus 5 Migration

---

## 2026-10-03

### Claude Opus 5 / Sonnet 5 に model だけ変えて移行すると壊れる 7 つの理由

Claude Opus 5とSonnet 5への移行時に発生する7つの破壊的変更を解説した技術記事。temperatureやtop_k等のサンプリングパラメータが400エラーになる、adaptive thinkingがデフォルトで有効になる、安全分類器による拒否応答の仕様変更、トークナイザの変更によるトークン数1.3倍増など、2026年10月時点の公式移行ガイドに基づく具体的な問題と対処法を網羅。静的解析ツールも提供されている。

- **ソース**: [Zenn claude](https://zenn.dev/persimmoq/articles/claude-opus-5-migration-400-errors)
- **重要度**: 8/10
- **タグ**: opus, sonnet, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-03 | 自動生成 |
