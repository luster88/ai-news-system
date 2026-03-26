---
title: Vscode Shortcuts
category: troubleshooting
subcategory: vscode-shortcuts
tags:
- bugfix
- claude-code
- vscode
date: '2026-03-26'
updated: '2026-03-26'
sources:
- url: https://qiita.com/k_bobchin/items/4dee07aaaab49c5a8599
  title: 【Claude Code】VS Codeでcmd+Nが新規会話にならなくなった原因と対処法
  date: '2026-03-26'
---

# Vscode Shortcuts

---

## 2026-03-26

### 【Claude Code】VS Codeでcmd+Nが新規会話にならなくなった原因と対処法

Claude Code拡張のアップデート後、VS CodeでCmd+Nによる新規会話ショートカットが動作しなくなる問題が発生。原因は`claudeCode.enableNewConversationShortcut`のデフォルト値がサイレントにtrueからfalseへ変更されたため。settings.jsonに明示的に`true`を設定することで解決可能。変更履歴に記載がなく、when句の条件により気づきにくい問題。

- **ソース**: [Qiita claude](https://qiita.com/k_bobchin/items/4dee07aaaab49c5a8599)
- **重要度**: 6/10
- **タグ**: claude-code, vscode, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-26 | 自動生成 |
