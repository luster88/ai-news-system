---
title: Line Bot Timeout
category: troubleshooting
subcategory: line-bot-timeout
tags:
- bugfix
- claude-api
- setup
date: '2026-11-19'
updated: '2026-11-19'
sources:
- url: https://zenn.dev/liatris/articles/20261119-line-bot-reply-token-budget
  title: LINEボットの返信をreply tokenの期限内に収める
  date: '2026-11-19'
---

# Line Bot Timeout

---

## 2026-11-19

### LINEボットの返信をreply tokenの期限内に収める

LINEボットでLLMを使う際、reply tokenの有効期限（30秒前後～60秒）内に応答が間に合わず400エラーになる問題への対処法。受信からの経過時間を測定し、閾値未満ならreply、超過時やreply失敗時はpushにフォールバックする実装を紹介。webhook署名検証、重複排除、エラー種別による処理分岐をPython3で実装し、課金対象のpush使用を最小化しつつ確実な配信を実現する。

- **ソース**: [Zenn claude](https://zenn.dev/liatris/articles/20261119-line-bot-reply-token-budget)
- **重要度**: 5/10
- **タグ**: claude-api, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-19 | 自動生成 |
