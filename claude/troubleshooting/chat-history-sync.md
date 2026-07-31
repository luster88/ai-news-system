---
title: Chat History Sync
category: troubleshooting
subcategory: chat-history-sync
tags:
- claude-code
- setup
- vscode
date: '2026-07-31'
updated: '2026-07-31'
sources:
- url: https://qiita.com/san_bay3/items/44e4189b14c9f0e103d5
  title: 【あたりまえ体操】Claude Codeの対話履歴は別端末に引き継げない
  date: '2026-07-31'
---

# Chat History Sync

---

## 2026-07-31

### 【あたりまえ体操】Claude Codeの対話履歴は別端末に引き継げない

Claude Code（VS Code拡張）の対話履歴はローカルPC（~/.claude/配下）に保存されており、別端末への引き継ぎは不可能。履歴ファイルはGit管理外かつOS依存の絶対パスに紐づくため、WindowsとMac間での移行は困難。対策として、重要な文脈はCLAUDE.mdやコメントに明示的に記録し、必要に応じて再度読み込ませる方法が推奨される。

- **ソース**: [Qiita claude](https://qiita.com/san_bay3/items/44e4189b14c9f0e103d5)
- **重要度**: 6/10
- **タグ**: claude-code, vscode, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-31 | 自動生成 |
