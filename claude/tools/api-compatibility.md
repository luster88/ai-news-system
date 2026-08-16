---
title: Api Compatibility
category: tools
subcategory: api-compatibility
tags:
- claude-api
- cowork
- pricing
- 新機能
date: '2026-08-16'
updated: '2026-08-16'
sources:
- url: https://qiita.com/TaichiYamasaki/items/959378ebb76eda594807
  title: OpenAI/Anthropic 向けに書いたコードを、さくらのAI Engine に差し替えだけで載せてみた
  date: '2026-08-16'
- url: https://qiita.com/TaichiYamasaki/items/959378ebb76eda594807
  title: OpenAI/Anthropic 向けに書いたコードを、さくらのAI Engine に差し替えだけで載せてみた
  date: '2026-08-16'
---

# Api Compatibility

---

## 2026-08-16

### OpenAI/Anthropic 向けに書いたコードを、さくらのAI Engine に差し替えだけで載せてみた

さくらのAI EngineがOpenAI/Anthropic API互換であることを検証した記事。base_urlとAPIキーの差し替えのみで、function calling、JSON出力、streaming、Anthropic Messages APIが全て動作した。課金がトークン量ではなくリクエスト回数ベースのため、1リクエストにまとめる設計が有利になる点が特徴。同一トークンでOpenAI形式とAnthropic形式の両方を利用可能。

- **ソース**: [Qiita claude](https://qiita.com/TaichiYamasaki/items/959378ebb76eda594807)
- **重要度**: 6/10
- **タグ**: claude-api, cowork, 新機能

---

### OpenAI/Anthropic 向けに書いたコードを、さくらのAI Engine に差し替えだけで載せてみた

さくらのAI EngineがOpenAI/Anthropic互換APIを提供しており、既存コードのbase_urlとAPIキーを差し替えるだけで動作することを検証。function calling、JSON出力、streaming、両形式の同時利用が可能。課金がトークン量ではなくリクエスト回数ベースのため、1リクエストにまとめる設計が有利になる点が特徴的。

- **ソース**: [Qiita claudecode](https://qiita.com/TaichiYamasaki/items/959378ebb76eda594807)
- **重要度**: 6/10
- **タグ**: claude-api, cowork, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-16 | 自動生成 |
