---
title: Claude Code Scheduled Tasks
category: troubleshooting
subcategory: claude-code-scheduled-tasks
tags:
- bugfix
- claude-code
- setup
date: '2026-07-28'
updated: '2026-07-28'
sources:
- url: https://zenn.dev/toyo_lab/articles/claude-code-scheduled-task-auto-setup
  title: Claude Code Desktopの定時タスクが承認待ちで止まる — 解決はsettingsではなく、タスク側の「権限モード」1つ
  date: '2026-07-28'
---

# Claude Code Scheduled Tasks

---

## 2026-07-28

### Claude Code Desktopの定時タスクが承認待ちで止まる — 解決はsettingsではなく、タスク側の「権限モード」1つ

Claude Code Desktopのスケジュールタスクが承認待ちで停止する問題について、settings.jsonではなくタスク編集フォームの「権限モード」を「自動」に設定することで解決できることを実測データとともに解説。手動モードでは96.8分停止していたタスクが、自動モードでは6.6〜9.4分で無人完走することを確認。権限モードピッカーは現在のモード名がラベル表示されるため見つけにくく、指示入力欄の左下に配置されている点が注意点。

- **ソース**: [Zenn claude](https://zenn.dev/toyo_lab/articles/claude-code-scheduled-task-auto-setup)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-28 | 自動生成 |
