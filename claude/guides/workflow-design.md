---
title: Workflow Design
category: guides
subcategory: workflow-design
tags:
- claude-code
- cowork
- opus
- prompt
date: '2026-05-01'
updated: '2026-10-23'
sources:
- url: https://zenn.dev/zoetaka38/articles/5beb5aad3e0e34
  title: PRD を「タスクグラフ」に落とすときに、どこを順序エッジにしてどこを並列に開くかという話
  date: '2026-05-01'
- url: https://zenn.dev/tmiyachi/articles/ai-video-edit-tacit-knowledge-design
  title: AIに動画編集を任せられるかは、暗黙知をどう渡すかで決まる ― 7つの法則を「入力・確かめ方・記憶・手入れ」で読む
  date: '2026-10-23'
---


# Workflow Design

---

## 2026-10-23

### AIに動画編集を任せられるかは、暗黙知をどう渡すかで決まる ― 7つの法則を「入力・確かめ方・記憶・手入れ」で読む

Claude Code（Opus 5.5）を使った動画編集の実践報告。編集の暗黙知（カットのタイミング、テロップの見せ方、間の取り方など）をAIに渡すため、完成動画・編集データ・レギュレーションシート・過去の修正履歴という3種の「跡」を入力し、サンプル動画での確認と理由付きフィードバックという確かめ方を設計。AIに「自分らしい編集」をさせるには、判断基準の言語化が不可欠という知見。

- **ソース**: [Zenn claude](https://zenn.dev/tmiyachi/articles/ai-video-edit-tacit-knowledge-design)
- **重要度**: 6/10
- **タグ**: claude-code, opus, prompt

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
