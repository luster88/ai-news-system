---
title: Multi Model Optimization
category: guides
subcategory: multi-model-optimization
tags:
- claude-api
- cowork
- performance
date: '2026-05-15'
updated: '2026-05-15'
sources:
- url: https://zenn.dev/zoetaka38/articles/084af47ccc3162
  title: Claude は 3 回、Qwen は 6 回：model ごとに fix_verify の retry cap を変える設計
  date: '2026-05-15'
---

# Multi Model Optimization

---

## 2026-05-15

### Claude は 3 回、Qwen は 6 回：model ごとに fix_verify の retry cap を変える設計

Codens Purpleのfix_verifyループで、モデル別にリトライ上限を設定した設計について解説。Claudeは3回、Qwenは6回とし、モデルごとのコスト構造と成功率の違いに基づいて最適化。Anthropic APIとself-hosted Qwenを組み合わせたマルチモデル本番環境の構築経緯と、API課金モデルの選択理由も説明している。

- **ソース**: [Zenn claude](https://zenn.dev/zoetaka38/articles/084af47ccc3162)
- **重要度**: 6/10
- **タグ**: claude-api, performance, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-15 | 自動生成 |
