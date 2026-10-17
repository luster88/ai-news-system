---
title: Bedrock Prompt Cache
category: troubleshooting
subcategory: bedrock-prompt-cache
tags:
- claude-api
- performance
- pricing
date: '2026-10-17'
updated: '2026-10-17'
sources:
- url: https://qiita.com/ntaka329/items/9ddba124de03b15166c4
  title: スキーマを変えるとプロンプトキャッシュが共有されなかったので、Bedrock の構造化出力をやめた話（2026年版）
  date: '2026-10-17'
---

# Bedrock Prompt Cache

---

## 2026-10-17

### スキーマを変えるとプロンプトキャッシュが共有されなかったので、Bedrock の構造化出力をやめた話（2026年版）

Amazon BedrockのConverse APIで構造化出力を使うと、JSON Schemaがプロンプトの前方に挿入されキャッシュポイントより前に配置されるため、スキーマを変更するたびにキャッシュが無効化される。スキーマを本文に記述する方式に変更したところ、4回の呼び出しで費用が約28%、時間が約31%削減された。構造化出力では各スキーマが独立したキャッシュを生成し、本文記述方式の約2倍のトークンを消費する。

- **ソース**: [Qiita claude](https://qiita.com/ntaka329/items/9ddba124de03b15166c4)
- **重要度**: 7/10
- **タグ**: claude-api, performance, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-17 | 自動生成 |
