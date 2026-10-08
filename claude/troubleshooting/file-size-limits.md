---
title: File Size Limits
category: troubleshooting
subcategory: file-size-limits
tags:
- bugfix
- claude-code
- haiku
date: '2026-10-08'
updated: '2026-10-08'
sources:
- url: https://qiita.com/suwa_nobu/items/830108715f8dc017b97e
  title: Claude Code の @ で渡したファイルは、英文110KB・日本語3万字で黙って外された。修正は256KB超だけだった
  date: '2026-10-08'
---

# File Size Limits

---

## 2026-10-08

### Claude Code の @ で渡したファイルは、英文110KB・日本語3万字で黙って外された。修正は256KB超だけだった

Claude Code 2.1.292では@メンション付きファイルが256KB超で通知されるようになったが、実際には英文110KB・日本語3万字程度から既に黙って除外されていた。62回の検証で、除外の境界はバイト数ではなくトークン数で決まることが判明。ツールなしの場合、Haikuは存在しない内容を作り話として回答する傾向があった。環境変数CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENSで上限を変更可能だが、256KBの絶対上限は変わらない。

- **ソース**: [Qiita claudecode](https://qiita.com/suwa_nobu/items/830108715f8dc017b97e)
- **重要度**: 7/10
- **タグ**: claude-code, haiku, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-08 | 自動生成 |
