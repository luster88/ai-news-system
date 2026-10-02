---
title: Output Validation
category: guides
subcategory: output-validation
tags:
- bugfix
- claude-api
- prompt
date: '2026-10-02'
updated: '2026-10-02'
sources:
- url: https://zenn.dev/horibe/articles/verify-llm-output-mechanically
  title: LLMの答えを機械で検算する — 「間違って書くより、書かない」を3か所で実装した話
  date: '2026-10-02'
---

# Output Validation

---

## 2026-10-02

### LLMの答えを機械で検算する — 「間違って書くより、書かない」を3か所で実装した話

TOEIC学習アプリに Claude Vision と構文解析を組み込む際、LLM の出力を機械的に検証する仕組みを3箇所で実装した事例。SVOC解析では元文との一致確認、文型判定では区切り情報との突き合わせ、正解選択肢では英語以外の混入チェックを行い、「間違って書くより書かない」方針を徹底。多数決の罠や上書き制御、データ構造の設計など実装上の注意点も詳述。

- **ソース**: [Zenn claude](https://zenn.dev/horibe/articles/verify-llm-output-mechanically)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-02 | 自動生成 |
