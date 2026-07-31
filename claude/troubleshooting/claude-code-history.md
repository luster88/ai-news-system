---
title: Claude Code History
category: troubleshooting
subcategory: claude-code-history
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

# Claude Code History

---

## 2026-07-31

### 【あたりまえ体操】Claude Codeの対話履歴は別端末に引き継げない

Claude Code（VS Code拡張）の対話履歴は端末ローカルの~/.claude/配下に.jsonl形式で保存されており、別端末への引き継ぎはできない。履歴はリポジトリ外にあるためGit管理対象外で、さらにOS依存の絶対パスに紐づいているため単純なファイルコピーでも移行困難。対策として、重要な文脈はCLAUDE.mdやコメントとしてドキュメント化し、リポジトリに含めることが推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/san_bay3/items/44e4189b14c9f0e103d5)
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
