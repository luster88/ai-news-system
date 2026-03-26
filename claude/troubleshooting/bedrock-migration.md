---
title: Bedrock Migration
category: troubleshooting
subcategory: bedrock-migration
tags:
- bugfix
- claude-api
- sonnet
date: '2026-03-26'
updated: '2026-03-26'
sources:
- url: https://qiita.com/enumura1/items/d0f53e82ed6b59668b67
  title: Bedrock (Claude 4.6) 環境における pre-fill 廃止と代替手段の整理
  date: '2026-03-26'
---

# Bedrock Migration

---

## 2026-03-26

### Bedrock (Claude 4.6) 環境における pre-fill 廃止と代替手段の整理

AWS Bedrock 経由で Claude Sonnet 4.6 を利用する際、pre-fill（アシスタントメッセージのプリフィル）が廃止され 400 エラーが発生する問題について解説。代替手段として Structured Outputs（JSON Schema 指定）やシステムプロンプトでの直接指示を紹介し、Lambda（Python）からの実装例を提示している。

- **ソース**: [Qiita claude](https://qiita.com/enumura1/items/d0f53e82ed6b59668b67)
- **重要度**: 7/10
- **タグ**: sonnet, claude-api, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-26 | 自動生成 |
