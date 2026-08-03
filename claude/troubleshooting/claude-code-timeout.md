---
title: Claude Code Timeout
category: troubleshooting
subcategory: claude-code-timeout
tags:
- bugfix
- claude-code
- performance
- setup
date: '2026-07-14'
updated: '2026-08-03'
sources:
- url: https://qiita.com/ou-mori/items/cd7b2cf089496215acbc
  title: 'Claude CodeでAPI Error: Response stalled mid-stream. The response above may
    be incomplete.が出る'
  date: '2026-07-14'
- url: https://zenn.dev/ebijun1007/articles/795a0fc9d3e60a
  title: Claude Code が間欠的に10分ハングする問題を、デバッグログから原因特定して緩和する
  date: '2026-08-03'
---


# Claude Code Timeout

---

## 2026-08-03

### Claude Code が間欠的に10分ハングする問題を、デバッグログから原因特定して緩和する

Claude Code で間欠的に10分ハングする問題の原因を特定した記事。デバッグログ解析により、api.anthropic.com への特定コネクションが「リクエスト送信済み・応答なし」の状態で API_TIMEOUT_MS（600秒）まで待機することが判明。macOS の TCP keepalive 既定値（2時間）が原因で、API_FORCE_IDLE_TIMEOUT=1 設定により待ち時間を約10分から約4分に短縮可能。根本的な first-byte タイムアウトは未実装。

- **ソース**: [Zenn claude](https://zenn.dev/ebijun1007/articles/795a0fc9d3e60a)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, performance

---

## 2026-07-14

### Claude CodeでAPI Error: Response stalled mid-stream. The response above may be incomplete.が出る

Claude Codeで「API Error: Response stalled mid-stream」エラーが発生する問題について、5分5秒でタイムアウトすることが判明。~/.claude/settings.jsonにタイムアウト時間延長の設定を追加し、/resumeやcontinueで再開することで一時的に解決できた事例を報告。

- **ソース**: [Qiita claude](https://qiita.com/ou-mori/items/cd7b2cf089496215acbc)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-14 | 自動生成 |
