---
title: Code Review Patterns
category: troubleshooting
subcategory: code-review-patterns
tags:
- bugfix
- claude-code
- cowork
date: '2026-06-05'
updated: '2026-06-05'
sources:
- url: https://zenn.dev/pikuto/articles/ai-code-correlated-blindspot
  title: AIが書いた15本の自動化スクリプト、全部同じ場所でバグっていた — 別のAIに監査させて分かったこと
  date: '2026-06-05'
---

# Code Review Patterns

---

## 2026-06-05

### AIが書いた15本の自動化スクリプト、全部同じ場所でバグっていた — 別のAIに監査させて分かったこと

Claude Codeで生成した15本の自動化スクリプトを別のAI（GPT、Gemini）に監査させたところ、全て同じ3パターンのバグ（並行処理の競合、破損データの誤処理、エラーハンドリングの不備）が見つかった。これはモデル固有の「書き癖」による系統的盲点であり、同じAIによるセルフレビューでは検出できない。別系統のモデルを使った相互監査が有効。

- **ソース**: [Zenn claude](https://zenn.dev/pikuto/articles/ai-code-correlated-blindspot)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-05 | 自動生成 |
