---
title: Claude Code Token Limit
category: troubleshooting
subcategory: claude-code-token-limit
tags:
- bugfix
- claude-code
- setup
date: '2026-11-09'
updated: '2026-11-09'
sources:
- url: https://qiita.com/homhom44/items/9d35b8c4aa0461043200
  title: Claude Code で "Claude's response exceeded the 32000 output token maximum"
    が出たときの直し方(CLAUDE_CODE_MAX_OUTPUT_TOKENS と分割指示)
  date: '2026-11-09'
---

# Claude Code Token Limit

---

## 2026-11-09

### Claude Code で "Claude's response exceeded the 32000 output token maximum" が出たときの直し方(CLAUDE_CODE_MAX_OUTPUT_TOKENS と分割指示)

Claude Codeで32000出力トークン上限エラーが発生した際の対処法を解説。continueコマンドで続きを出力させる方法、環境変数CLAUDE_CODE_MAX_OUTPUT_TOKENSで上限を引き上げる方法、根本的な解決として1ファイル・1節ずつ小さな単位に分割して出力を依頼する方法を紹介。思考トークンも出力トークンに含まれるため、長時間の思考と大量出力の組み合わせで上限に達しやすい点も説明している。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/9d35b8c4aa0461043200)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-09 | 自動生成 |
