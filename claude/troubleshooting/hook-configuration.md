---
title: Hook Configuration
category: troubleshooting
subcategory: hook-configuration
tags:
- bugfix
- claude-code
- mcp
- setup
- windows
date: '2026-11-20'
updated: '2026-11-22'
sources:
- url: https://zenn.dev/shogaku/articles/claude-code-hook-visibility
  title: Claude Code に作ってもらった hook の警告が、Claude に届いていなかった
  date: '2026-11-20'
- url: https://zenn.dev/ojisan_ai_lab/articles/claude-code-hook-onfailure-block-20261121
  title: Claude Codeのフックが壊れたら操作は止まる？ 14通り中11通りで通り、"block" の1行でそのうち10通りが止まりました
  date: '2026-11-22'
---


# Hook Configuration

---

## 2026-11-22

### Claude Codeのフックが壊れたら操作は止まる？ 14通り中11通りで通り、"block" の1行でそのうち10通りが止まりました

Claude Codeのフック機能において、スクリプトが壊れた場合の挙動を検証。onFailure指定なしでは14通り中11通りが処理を通過、"onFailure": "block"を追加すると10通りが停止した。v2.1.328でmcp_toolフックにもblock機能が追加され、バージョンにより挙動が異なることを確認。

- **ソース**: [Zenn claude](https://zenn.dev/ojisan_ai_lab/articles/claude-code-hook-onfailure-block-20261121)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, bugfix

---

## 2026-11-20

### Claude Code に作ってもらった hook の警告が、Claude に届いていなかった

Claude Codeのhook機能で、exit 0のstderr出力がClaudeに届いていなかった問題を発見。公式ドキュメントを確認し、Claudeに届く出力方法（exit 2のstderr、JSON形式、拒否理由など）を整理して86本のhookを見直した記録。タイムアウトによる「hook error」も多数発見され、チェック自体が機能していなかったケースも判明。

- **ソース**: [Zenn claude](https://zenn.dev/shogaku/articles/claude-code-hook-visibility)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-20 | 自動生成 |
