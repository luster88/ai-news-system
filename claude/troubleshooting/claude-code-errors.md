---
title: Claude Code Errors
category: troubleshooting
subcategory: claude-code-errors
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

# Claude Code Errors

---

## 2026-06-05

### Claude Codeで「The model's tool call could not be parsed」エラーを回避する方法

Claude Code（特にOpus 4.8）で日本語環境使用時に発生する「tool call could not be parsed」エラーの回避方法を解説。CLAUDE.mdに「Think in English, interact with the user in Japanese」を追加することで、内部思考を英語化してマルチバイト文字密度を下げ、XMLタグ構造の崩壊を防ぐ。エラー発生時は「Restore conversation」で即座にロールバック可能。

- **ソース**: [Qiita claudecode](https://qiita.com/natume_nat/items/76fe608d570caebb4f4c)
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
