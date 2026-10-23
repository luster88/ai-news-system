---
title: Claude Code Tasks
category: troubleshooting
subcategory: claude-code-tasks
tags:
- bugfix
- claude-code
- setup
date: '2026-10-23'
updated: '2026-10-23'
sources:
- url: https://zenn.dev/vellum_office/articles/d212998fbfcd8a
  title: Claude Codeの定期タスクが2日半見送られた件：global_limitと承認待ちの実行
  date: '2026-10-23'
---

# Claude Code Tasks

---

## 2026-10-23

### Claude Codeの定期タスクが2日半見送られた件：global_limitと承認待ちの実行

Claude デスクトップアプリの Code タブにおける定期タスクの実行トラブル事例。2日半にわたり承認待ちの実行が枠を占有し続け、新規タスクが見送られていた。コマンドの書き方（$()、cd && など）が承認待ちの原因となり、エラー通知も来ないため発見が遅れた。解決策として監視処理を launchd に移行し、コマンド形式を変更した。

- **ソース**: [Zenn claude](https://zenn.dev/vellum_office/articles/d212998fbfcd8a)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-23 | 自動生成 |
