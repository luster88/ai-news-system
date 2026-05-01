---
title: Workflow Design
category: guides
subcategory: workflow-design
tags:
- claude-code
- cowork
- prompt
date: '2026-05-01'
updated: '2026-05-01'
sources:
- url: https://zenn.dev/zoetaka38/articles/5beb5aad3e0e34
  title: PRD を「タスクグラフ」に落とすときに、どこを順序エッジにしてどこを並列に開くかという話
  date: '2026-05-01'
---

# Workflow Design

---

## 2026-05-01

### PRD を「タスクグラフ」に落とすときに、どこを順序エッジにしてどこを並列に開くかという話

AI ワークフローでタスクを並列実行すると時間効率は良いが、1つの失敗で後続が全てやり直しになりコストが増大する問題を解説。PRD をタスクグラフに分解する際、データ依存・副作用の排他性・実行時検証の必要性・ドメイン知識の依存という4つの基準で順序エッジか並列実行かを判定する設計手法を、Purple Codens の実装コードを用いて詳述。

- **ソース**: [Zenn claude](https://zenn.dev/zoetaka38/articles/5beb5aad3e0e34)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-01 | 自動生成 |
