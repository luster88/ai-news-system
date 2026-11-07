---
title: Sdk Migration
category: guides
subcategory: sdk-migration
tags:
- bugfix
- claude-api
- setup
date: '2026-11-07'
updated: '2026-11-07'
sources:
- url: https://qiita.com/khronov/items/4dd5155b0db7f482ea64
  title: Anthropic Python SDK 2.0 の移行ポイント 5 つを、v1 と同じコードを動かして確かめた
  date: '2026-11-07'
---

# Sdk Migration

---

## 2026-11-07

### Anthropic Python SDK 2.0 の移行ポイント 5 つを、v1 と同じコードを動かして確かめた

Anthropic Python SDK 2.0.0（2026-10-21リリース）への移行ポイントを実コードで検証した記事。APIバージョン2026-10-21では、APIキーの送り方がx-api-keyからAuthorization: Bearerに変更され、temperature等のサンプリングパラメータをextra_bodyで送ると400エラーになる点などを確認。v1.17.0とv2.5.0で同じコードを実行し、7つの書き方で動作の違いを比較している。

- **ソース**: [Qiita claude](https://qiita.com/khronov/items/4dd5155b0db7f482ea64)
- **重要度**: 7/10
- **タグ**: claude-api, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-07 | 自動生成 |
