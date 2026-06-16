---
title: Claude Code Startup
category: troubleshooting
subcategory: claude-code-startup
tags:
- bugfix
- claude-code
- setup
date: '2026-06-16'
updated: '2026-06-16'
sources:
- url: https://qiita.com/yurukusa/items/3205bde64f3a691a6599
  title: Claude Codeが突然起動しなくなった——設定ファイルが原因の「締め出し」を切り分けて復旧する
  date: '2026-06-16'
---

# Claude Code Startup

---

## 2026-06-16

### Claude Codeが突然起動しなくなった——設定ファイルが原因の「締め出し」を切り分けて復旧する

Claude Codeが設定ファイル（~/.claude/settings.local.json）内の存在しないディレクトリパスによって起動不能になる問題と、その復旧手順を解説。additionalDirectoriesに削除済みフォルダの参照が残ると起動が完全に失敗する。層ごとに設定を切り分け、存在しないパスのみを削除するスクリプトと、JSON構文チェックによる診断方法を提供。定期的な設定クリーニングと削除前の確認を推奨。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/3205bde64f3a691a6599)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-16 | 自動生成 |
