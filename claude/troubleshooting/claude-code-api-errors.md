---
title: Claude Code Api Errors
category: troubleshooting
subcategory: claude-code-api-errors
tags:
- bugfix
- claude-api
- claude-code
date: '2026-05-04'
updated: '2026-05-04'
sources:
- url: https://qiita.com/yurukusa/items/fbe51b3ce6b025dd089c
  title: Claude Code が API 400 で詰まる時——cache_control 空テキストブロックの根本原因と復旧
  date: '2026-05-04'
---


# Claude Code Api Errors

---

## 2026-05-04

### Claude Code が API 400 で詰まる時——cache_control 空テキストブロックの根本原因と復旧

Claude Codeの自動運用で発生するAPI 400エラーの原因と復旧方法を解説。cache_controlが空テキストブロックに付く不具合が根本原因で、GitHub Issueに12件以上の報告あり。JSONLファイルから壊れたブロックを除去するPythonスクリプトと予防策5つを提示。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/fbe51b3ce6b025dd089c)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, claude-api

---

## 2026-05-04

### Claude Code が API 400 で詰まる時——cache_control 空テキストブロックの根本原因と復旧

Claude Code で API 400 エラーが頻発する問題について、cache_control が付いた空テキストブロックが原因であることを特定。GitHub Issue で12本以上の報告があり、セッションファイル（JSONL）から壊れたブロックを除去する復旧手順と予防策を解説。公式通知がないため利用者側での対処が必要。

- **ソース**: [Qiita claude](https://qiita.com/yurukusa/items/fbe51b3ce6b025dd089c)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-04 | 自動生成 |
