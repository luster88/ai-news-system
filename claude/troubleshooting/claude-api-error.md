---
title: Claude Api Error
category: troubleshooting
subcategory: claude-api-error
tags:
- bugfix
- claude-api
- cowork
date: '2026-05-11'
updated: '2026-05-11'
sources:
- url: https://zenn.dev/zoetaka38/articles/2328ea1c852dee
  title: AI consultation が突然 400 BadRequest ループに陥る原因と、3層防御で直した話
  date: '2026-05-11'
---

# Claude Api Error

---

## 2026-05-11

### AI consultation が突然 400 BadRequest ループに陥る原因と、3層防御で直した話

Claude API との会話履歴に空の assistant message が混入すると、以降すべてのリクエストが 400 BadRequest でループする障害が発生。原因は Claude API が稀に空 content を返す際、コード側でバリデーションせずに DB 保存していたこと。空文字列の事前チェック、DB 制約追加、履歴送信前フィルタの 3 層防御で解決した実例。

- **ソース**: [Zenn claude](https://zenn.dev/zoetaka38/articles/2328ea1c852dee)
- **重要度**: 6/10
- **タグ**: claude-api, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-11 | 自動生成 |
