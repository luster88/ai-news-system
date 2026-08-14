---
title: Claude Code Routine Setup
category: troubleshooting
subcategory: claude-code-routine-setup
tags:
- bugfix
- claude-code
- setup
date: '2026-08-14'
updated: '2026-08-14'
sources:
- url: https://zenn.dev/devex12/articles/claude-code-routine-unattended-followup
  title: 「隔離環境の構築はこれから」の5日後、実際に選んだのはEC2ではなくRoutineだった
  date: '2026-08-14'
---

# Claude Code Routine Setup

---

## 2026-08-14

### 「隔離環境の構築はこれから」の5日後、実際に選んだのはEC2ではなくRoutineだった

Claude Code Remoteの夜間バッチ無人実行を検討していた著者が、当初想定していたEC2+tmux構成ではなく、Routineのスケジュール機能を採用した事例。allowed_toolsにBashがある以上、git pushやPR作成の制御はツール権限ではなくプロンプトの明示的禁止で担保する必要があること、cronがUTC入力必須でJST換算時に日付ズレが発生すること、外部APIアクセスが実行環境のネットワークポリシーでブロックされた実例などが記録されている。

- **ソース**: [Zenn claude](https://zenn.dev/devex12/articles/claude-code-routine-unattended-followup)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-14 | 自動生成 |
