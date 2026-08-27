---
title: Vision Extraction
category: troubleshooting
subcategory: vision-extraction
tags:
- bugfix
- claude-api
- cowork
date: '2026-08-27'
updated: '2026-08-27'
sources:
- url: https://zenn.dev/tyuya/articles/handwritten-sheet-blank-trap
  title: 「読み取りはLLM・判定はJS」に分けても見逃した——手書き帳票の異常が通知から消える2つの経路
  date: '2026-08-27'
---

# Vision Extraction

---

## 2026-08-27

### 「読み取りはLLM・判定はJS」に分けても見逃した——手書き帳票の異常が通知から消える2つの経路

手書き帳票をClaude visionで読み取りLINE通知する個人開発システムで、異常データが通知から消える2つの経路を発見した事例。経路1は抽出成功後にルール未設定で判定対象外になった問題、経路2は未記入欄を印刷文字として誤抽出した問題。LLMには読み取りのみを担当させ判定はJSで行う設計思想だったが、ルール型の不足と網羅性チェックの欠如により「判定していないのに問題なしと報告する」という silent failure が発生していた。

- **ソース**: [Zenn claude](https://zenn.dev/tyuya/articles/handwritten-sheet-blank-trap)
- **重要度**: 6/10
- **タグ**: claude-api, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-27 | 自動生成 |
