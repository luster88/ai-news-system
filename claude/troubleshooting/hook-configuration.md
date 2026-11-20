---
title: Hook Configuration
category: troubleshooting
subcategory: hook-configuration
tags:
- claude-code
- setup
- windows
date: '2026-11-20'
updated: '2026-11-20'
sources:
- url: https://zenn.dev/shogaku/articles/claude-code-hook-visibility
  title: Claude Code に作ってもらった hook の警告が、Claude に届いていなかった
  date: '2026-11-20'
---

# Hook Configuration

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
