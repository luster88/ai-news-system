---
title: Mcp Filesystem Failure
category: troubleshooting
subcategory: mcp-filesystem-failure
tags:
- bugfix
- claude-code
- mcp
date: '2026-07-25'
updated: '2026-07-25'
sources:
- url: https://zenn.dev/shin_endo/articles/57dfcec6de783e
  title: Claudeのツールが動かなくなった日 ── MCP不具合の記録と、各ツールがどう使えなかったか
  date: '2026-07-25'
---

# Mcp Filesystem Failure

---

## 2026-07-25

### Claudeのツールが動かなくなった日 ── MCP不具合の記録と、各ツールがどう使えなかったか

2026年7月23日、Claude DesktopのfilesystemMCPサーバーが突然動作不能になり、list_allowed_directories、list_directory、get_file_infoなど全ツールがTool execution failedを返した。設定画面では正常表示されるが呼び出しのみ失敗する状態が2日半続き、7月25日のアップデートで復旧。各ツールの本来の用途と今回の不具合での挙動を詳細に記録した障害レポート。

- **ソース**: [Zenn claude](https://zenn.dev/shin_endo/articles/57dfcec6de783e)
- **重要度**: 6/10
- **タグ**: mcp, bugfix, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-25 | 自動生成 |
