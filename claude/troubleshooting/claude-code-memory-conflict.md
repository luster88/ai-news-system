---
title: Claude Code Memory Conflict
category: troubleshooting
subcategory: claude-code-memory-conflict
tags:
- bugfix
- claude-code
date: '2026-11-08'
updated: '2026-11-08'
sources:
- url: https://zenn.dev/murooka_az/articles/claude-degraded-or-correction-unreachable
  title: 「指示どおりにやりました」と言うのに従っていないClaude。原因は、AI自身が指示ファイルやメモリに書き残していた昔の仕様
  date: '2026-11-08'
---

# Claude Code Memory Conflict

---

## 2026-11-08

### 「指示どおりにやりました」と言うのに従っていないClaude。原因は、AI自身が指示ファイルやメモリに書き残していた昔の仕様

Claude Code を長期間使用していると、廃止した機能を繰り返し使おうとしたり、指示に従わない挙動が発生することがある。原因は自動メモリや .claude/rules/ ファイルに古い仕様が残っていたため。メモリを整理しても rule ファイルに写しが残っていたケースや、一時的な例外が恒久方針としてメモリに記録されたケースが確認された。155回の再現実験では、新しい訂正が目に入れば Claude は訂正に従うことが判明した。

- **ソース**: [Zenn claude](https://zenn.dev/murooka_az/articles/claude-degraded-or-correction-unreachable)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-08 | 自動生成 |
