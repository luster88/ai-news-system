---
title: Claude Code Api Errors
category: troubleshooting
subcategory: claude-code-api-errors
tags:
- bugfix
- claude-api
- claude-code
- opus
- setup
- sonnet
date: '2026-05-04'
updated: '2026-10-28'
sources:
- url: https://qiita.com/yurukusa/items/fbe51b3ce6b025dd089c
  title: Claude Code が API 400 で詰まる時——cache_control 空テキストブロックの根本原因と復旧
  date: '2026-05-04'
- url: https://qiita.com/yurukusa/items/3ea49f000b2c3046ecba
  title: Claude Code の API Error 401/500 は自分のせいかAnthropic側か——切り分けと対処（#69706）
  date: '2026-06-27'
- url: https://qiita.com/homhom44/items/826e013f605ce5905638
  title: Claude Code で "Repeated 529 Overloaded errors" "Opus is experiencing high
    load" が出たときの待ち方と /model での逃がし方
  date: '2026-10-28'
---




# Claude Code Api Errors

---

## 2026-10-28

### Claude Code で "Repeated 529 Overloaded errors" "Opus is experiencing high load" が出たときの待ち方と /model での逃がし方

Claude CodeでAPI Error 529(Overloaded)が出た際の対処法を解説。これはAnthropicサーバー側の混雑が原因で、数分待つか/modelコマンドで別モデル（OpusからSonnetなど）に切り替えることで作業継続が可能。自分の使用量上限やクォータ消費ではないため、プラン変更は不要。Claude Codeは既に指数バックオフで最大10回リトライ済みの状態でこのエラーを表示している。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/826e013f605ce5905638)
- **重要度**: 6/10
- **タグ**: claude-code, opus, sonnet

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
