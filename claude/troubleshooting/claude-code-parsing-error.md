---
title: Claude Code Parsing Error
category: troubleshooting
subcategory: claude-code-parsing-error
tags:
- bugfix
- claude-code
- opus
date: '2026-06-05'
updated: '2026-06-05'
sources:
- url: https://qiita.com/natume_nat/items/76fe608d570caebb4f4c
  title: Claude Codeで「The model's tool call could not be parsed」エラーを回避する方法
  date: '2026-06-05'
---

# Claude Code Parsing Error

---

## 2026-06-05

### Claude Codeで「The model's tool call could not be parsed」エラーを回避する方法

Claude Code（特にOpus 4.8）で日本語使用時に発生する「The model's tool call could not be parsed」エラーの原因と対策を解説。マルチバイト文字の密度が高いとモデルの出力デコーダーがバグを起こしツール呼び出し用XMLタグが崩れる問題に対し、CLAUDE.mdに「thinkingは英語でしてください」と記載することで、内部思考を英語に固定しバイト密度を下げてエラーを回避できる。エラー発生時は「Restore conversation」で即座にロールバック可能。

- **ソース**: [Qiita claude](https://qiita.com/natume_nat/items/76fe608d570caebb4f4c)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-05 | 自動生成 |
