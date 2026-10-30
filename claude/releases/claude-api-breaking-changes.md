---
title: Claude Api Breaking Changes
category: releases
subcategory: claude-api-breaking-changes
tags:
- bugfix
- claude-api
- release
date: '2026-10-30'
updated: '2026-10-30'
sources:
- url: https://qiita.com/sakutto-panda/items/12e39ac7596f9da3fa59
  title: Claude API 2026-10-21の破壊的変更を自作ツールで検証——SDK 2.0でtemperatureが消えた
  date: '2026-10-30'
---

# Claude Api Breaking Changes

---

## 2026-10-30

### Claude API 2026-10-21の破壊的変更を自作ツールで検証——SDK 2.0でtemperatureが消えた

2026年10月21日にClaude APIの新バージョン2026-10-21がリリースされ、temperature/top_p/top_kパラメータが既定値以外では400エラーとなる破壊的変更が導入された。新しいSDK（Python 2.0.0、TypeScript 1.0.0等）は既定で新APIバージョンを使用し、認証方式もAuthorization: Bearerに変更された。筆者は自作の投資分析ツールRakuScanで旧SDK 0.97.0と新SDK 2.3.0をモックHTTPトランスポートで比較検証し、実際の変更点を確認した。temperatureパラメータはSDK側で引数エラーとなり、MessageParamの型定義も変更されている。

- **ソース**: [Qiita claude](https://qiita.com/sakutto-panda/items/12e39ac7596f9da3fa59)
- **重要度**: 8/10
- **タグ**: claude-api, release, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-30 | 自動生成 |
