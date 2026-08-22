---
title: Watermarking Tech
category: guides
subcategory: watermarking-tech
tags:
- claude-api
- performance
- 新機能
date: '2026-08-22'
updated: '2026-08-22'
sources:
- url: https://zenn.dev/rinrin_ds_17/articles/bc093cfa3bdbd1
  title: Claudeのテキスト透かし（ウォーターマーク）は何をしているのか ── サンプリングの仕組みから理解する
  date: '2026-08-22'
---

# Watermarking Tech

---

## 2026-08-22

### Claudeのテキスト透かし（ウォーターマーク）は何をしているのか ── サンプリングの仕組みから理解する

Anthropicが2026年8月にClaudeのテキスト透かし技術を発表。LLMの重みは変えず、サンプリング段階で秘密鍵と直前トークンから乱数シードを決定する仕組み。透かしは文章品質に影響せず、第三者には検出不可能だが、単語の書き換えで消える特性を持つ。GoogleのSynthID-Textベースのトーナメントサンプリングを採用。

- **ソース**: [Zenn claude](https://zenn.dev/rinrin_ds_17/articles/bc093cfa3bdbd1)
- **重要度**: 7/10
- **タグ**: claude-api, 新機能, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-22 | 自動生成 |
