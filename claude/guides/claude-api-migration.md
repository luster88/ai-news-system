---
title: Claude Api Migration
category: guides
subcategory: claude-api-migration
tags:
- claude-api
- claude-code
- prompt
date: '2026-09-25'
updated: '2026-09-25'
sources:
- url: https://qiita.com/sakutto-panda/items/957b92456a7ebce1f394
  title: '`claude -p`からAnthropic APIへ — 個人開発の自動化をClaude Codeサブスクから切り離した話'
  date: '2026-09-25'
---

# Claude Api Migration

---

## 2026-09-25

### `claude -p`からAnthropic APIへ — 個人開発の自動化をClaude Codeサブスクから切り離した話

個人開発の日本株スクリーニングツール「RakuScan」において、Claude Code CLI（`claude -p`）からAnthropic API（anthropic SDK）への移行事例。Oracle Cloud無料枠VMへの移行時に、CLIがサブスク紐付きで無人運用に不向きという制約に直面し、API直接利用へ切り替えた。移行時にPrompt Caching（`cache_control: ephemeral`）、用途別モデル切り替え（日次Haiku/対話Sonnet）、明示的なエラーハンドリングを導入し、コスト最適化と運用の自律性を両立させた実装例。

- **ソース**: [Qiita claude](https://qiita.com/sakutto-panda/items/957b92456a7ebce1f394)
- **重要度**: 6/10
- **タグ**: claude-api, claude-code, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-25 | 自動生成 |
