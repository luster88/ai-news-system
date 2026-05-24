---
title: Cutoff Date Limitation
category: troubleshooting
subcategory: cutoff-date-limitation
tags:
- claude-api
- performance
date: '2026-05-24'
updated: '2026-05-24'
sources:
- url: https://qiita.com/yosikawa-techwell/items/f8d952b0778fa3e30dcd
  title: 4大AIに同じ日本語の暦を4週連続で聞き続けたら、cutoff date による構造的不在が見えた — canonical API hub という解
  date: '2026-05-24'
---

# Cutoff Date Limitation

---

## 2026-05-24

### 4大AIに同じ日本語の暦を4週連続で聞き続けたら、cutoff date による構造的不在が見えた — canonical API hub という解

4大AI（ChatGPT、Claude、Perplexity、Gemini）に同じ日本語の暦を4週連続で質問した結果、Claudeのみが4週連続でhallucination を起こし、Geminiは唯一正確な回答を返した。Claudeは2026年1月のカットオフ日付により、5月リリースのShirabe Address APIを構造的に認識できないことが判明。SEOや記事などの訓練時経路がClaudeに届かない一方、Geminiは訓練データに反映済みだが自発的なランキング露出には課題があることが明らかになった。

- **ソース**: [Qiita claude](https://qiita.com/yosikawa-techwell/items/f8d952b0778fa3e30dcd)
- **重要度**: 6/10
- **タグ**: claude-api, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-24 | 自動生成 |
