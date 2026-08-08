---
title: Permission Management
category: troubleshooting
subcategory: permission-management
tags:
- bugfix
- claude-code
- setup
date: '2026-08-08'
updated: '2026-08-08'
sources:
- url: https://zenn.dev/devex12/articles/claude-code-unattended-permission-mode-gap
  title: 「信頼済みコマンド」を設定しても夜間オート実行はできなかった - claude --helpで分かった見落とし
  date: '2026-08-08'
---

# Permission Management

---

## 2026-08-08

### 「信頼済みコマンド」を設定しても夜間オート実行はできなかった - claude --helpで分かった見落とし

Claude Codeの「信頼済みコマンド」設定では夜間の完全無人実行ができないことが判明。許可リスト（permissions.allow）は読み取り専用コマンドの承認を自動化するレイヤーで、git pushなど書き込み系コマンドは対象外。完全自動化には--dangerously-skip-permissionsが必要だが、プロンプトインジェクションのリスクがあるため、普段使いのマシンでは危険。AWS EC2+tmuxなど隔離環境での実行が推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/devex12/articles/claude-code-unattended-permission-mode-gap)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-08 | 自動生成 |
