---
title: Security Env Protection
category: troubleshooting
subcategory: security-env-protection
tags:
- bugfix
- claude-code
- setup
- 新機能
date: '2026-08-03'
updated: '2026-08-03'
sources:
- url: https://qiita.com/tomada/items/650546e8b9f5e33d5820
  title: 【実測あり】Claude Codeから.envを守る：permissions.deny vs PreToolUseフック
  date: '2026-08-03'
- url: https://qiita.com/tomada/items/650546e8b9f5e33d5820
  title: 【実測あり】Claude Codeから.envを守る：permissions.deny vs PreToolUseフック
  date: '2026-08-03'
---

# Security Env Protection

---

## 2026-08-03

### 【実測あり】Claude Codeから.envを守る：permissions.deny vs PreToolUseフック

Claude Codeが.envファイルを確認なしで読み取り、パスワードが履歴に残る問題を実測で検証。permissions.denyで4行追加する方法と、PreToolUseフック（Python約40行）による代替手段を比較し、Read/Edit/Write/Bashのcatまで全てブロック可能と確認。結論は両者の併用でガードと誘導メッセージを実現。

- **ソース**: [Qiita claude](https://qiita.com/tomada/items/650546e8b9f5e33d5820)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

### 【実測あり】Claude Codeから.envを守る：permissions.deny vs PreToolUseフック

Claude Codeが.envファイルを無断で読み取るリスクを検証し、permissions.denyとPreToolUseフックの2つの防御手法を実装・比較した記事。ガード無しの状態では秘密情報が応答とセッション履歴に平文で残ることを実測で確認。permissions.denyは4行の追加でRead/Edit/新規作成に加えてBashのcatコマンドまでブロック可能。結論として両手法の併用（denyを土台にフックで例外処理と誘導メッセージを追加）を推奨。

- **ソース**: [Qiita claudecode](https://qiita.com/tomada/items/650546e8b9f5e33d5820)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-03 | 自動生成 |
