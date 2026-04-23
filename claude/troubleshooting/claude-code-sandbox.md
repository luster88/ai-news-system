---
title: Claude Code Sandbox
category: troubleshooting
subcategory: claude-code-sandbox
tags:
- bugfix
- claude-code
- setup
date: '2026-04-23'
updated: '2026-04-23'
sources:
- url: https://qiita.com/yurukusa/items/1a11ad1320dd3b98d783
  title: Claude Codeのsandbox設定、Writeツールには効いていません——denyWriteバイパス問題と回避策
  date: '2026-04-23'
---

# Claude Code Sandbox

---

## 2026-04-23

### Claude Codeのsandbox設定、Writeツールには効いていません——denyWriteバイパス問題と回避策

Claude Codeのsandbox.filesystem.denyWrite設定に重大なバグが存在。Bashツールのみがsandbox制限を受け、Write/Editツールは制限を素通りするため、意図しないファイル上書きが発生。2026年2月から複数回報告されているが未修正。PreToolUseフックでWrite/Editの書き込み先を検査する回避策が提示されている。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/1a11ad1320dd3b98d783)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-23 | 自動生成 |
