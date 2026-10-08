---
title: Claude Code File Limits
category: troubleshooting
subcategory: claude-code-file-limits
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

# Claude Code File Limits

---

## 2026-10-08

### Claude Code の @ で渡したファイルは、英文110KB・日本語3万字で黙って外された。修正は256KB超だけだった

Claude Code 2.1.292 の検証により、@メンションでファイルを渡す際の実際の上限が判明。公式には256KB超で通知が出るとされているが、実際には英文110KB・日本語3万字程度で黙って除外される。境目はバイト数ではなくトークン数で決まっており、CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS 環境変数で調整可能。ツールが使えない場合、Haikuは存在しない内容を捏造する傾向がある。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/830108715f8dc017b97e)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, haiku

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-08 | 自動生成 |
