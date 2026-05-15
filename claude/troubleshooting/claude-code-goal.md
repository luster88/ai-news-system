---
title: Claude Code Goal
category: troubleshooting
subcategory: claude-code-goal
tags:
- bugfix
- claude-code
- 新機能
date: '2026-05-15'
updated: '2026-05-15'
sources:
- url: https://zenn.dev/zaico/articles/e0678bd81d198c
  title: goal 機能の挙動確認実験記録
  date: '2026-05-15'
---

# Claude Code Goal

---

## 2026-05-15

### goal 機能の挙動確認実験記録

Claude Code v2.1.139で追加された/goalコマンドの詳細な挙動検証記事。公式ドキュメントに記載されていない重要な仕様として、「or stop after N turns」はevaluator（Haiku）によるソフトキャップであり、条件文を文字列として解釈して判定していることが判明。またClaude本体とevaluatorは独立して判定を行うため、ターン数のカウント精度に差異が生じる可能性があることも実験で確認された。

- **ソース**: [Zenn claude](https://zenn.dev/zaico/articles/e0678bd81d198c)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-15 | 自動生成 |
