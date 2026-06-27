---
title: Claude Code Api Errors
category: troubleshooting
subcategory: claude-code-api-errors
tags:
- bugfix
- claude-api
- claude-code
- setup
date: '2026-05-04'
updated: '2026-06-27'
sources:
- url: https://qiita.com/yurukusa/items/fbe51b3ce6b025dd089c
  title: Claude Code が API 400 で詰まる時——cache_control 空テキストブロックの根本原因と復旧
  date: '2026-05-04'
- url: https://qiita.com/yurukusa/items/3ea49f000b2c3046ecba
  title: Claude Code の API Error 401/500 は自分のせいかAnthropic側か——切り分けと対処（#69706）
  date: '2026-06-27'
---



# Claude Code Api Errors

---

## 2026-06-27

### Claude Code の API Error 401/500 は自分のせいかAnthropic側か——切り分けと対処（#69706）

Claude Code で発生する API Error 401/500 の切り分け方法を解説。500系エラーはサーバ側の問題で設定変更は無効。401エラーには「資格情報が空・古い」クライアント側の問題と「アカウント・オンボーディング側」の問題の2種類があり、それぞれ対処法が異なる。環境変数 ANTHROPIC_API_KEY の設定ミスや ~/.claude/.credentials.json の refreshToken 欠損が原因となるケースが多い。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/3ea49f000b2c3046ecba)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

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
