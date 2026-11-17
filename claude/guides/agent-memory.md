---
title: Agent Memory
category: guides
subcategory: agent-memory
tags:
- claude-api
- claude-code
- mcp
- performance
- prompt
- sonnet
- 新機能
date: '2026-04-19'
updated: '2026-11-17'
sources:
- url: https://qiita.com/bit-tanghao/items/20e0366ce3f08f291ce5
  title: '# 【AIエージェントシリーズ 第4弾】メモリを持つAgent：プロジェクト文脈を覚えているレビュアーを作る'
  date: '2026-04-19'
- url: https://ai-heartland.com/explain/continual-arc-agent-memory
  title: Continual-ARCとは｜エージェントの「メモリ」は学習になっていたか、新ベンチと3つの教訓
  date: '2026-11-12'
- url: https://the-decoder.com/anthropic-says-the-key-to-agent-memory-is-knowing-what-to-forget-not-how-much-to-store
  title: Anthropic says the key to agent memory is knowing what to forget, not how
    much to store
  date: '2026-11-17'
---



# Agent Memory

---

## 2026-11-17

### Anthropic says the key to agent memory is knowing what to forget, not how much to store

Anthropic は、AI エージェントの記憶管理において「何を記憶するか」よりも「何を忘れるか」が重要であることを発表しました。ポケモン Red を用いた実験では、全ての情報を記録する手法よりも、戦略やルールを選択的に記録する方が効果的であることが判明しました。また、セッション後に「Dreaming」と呼ばれるプロセスで Claude が自身のメモリを見直し、誤りを修正する機能も紹介されています。この研究は、長期的なタスクにおける AI エージェントの記憶保持の課題に対する新しいアプローチを示しています。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-says-the-key-to-agent-memory-is-knowing-what-to-forget-not-how-much-to-store)
- **重要度**: 7/10
- **タグ**: 新機能, sonnet, performance

---

## 2026-11-12

### Continual-ARCとは｜エージェントの「メモリ」は学習になっていたか、新ベンチと3つの教訓

Continual-ARCは、AIエージェントのメモリ機能が本当に学習になっているかを測定する新ベンチマーク。ARC-AGIをベースに、記憶（既見タスク）と汎化（未見タスク）の2軸で評価した結果、ハーネスの記憶機能は明示的な指示がないと効果が薄く、未見タスクではモデルの重み学習のみが有効だった。エージェント設計における「保存しない・読まない・一般論ばかり」という失敗パターンが明らかになった。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/continual-arc-agent-memory)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, performance

---

## 2026-04-19

### # 【AIエージェントシリーズ 第4弾】メモリを持つAgent：プロジェクト文脈を覚えているレビュアーを作る

Claude Agentに短期メモリ（messages配列）と長期メモリ（JSON）の2層構造を実装し、プロジェクト文脈を記憶するコードレビューAgentを構築。remember_rule/recall_historyツールでAgent自身が記憶を管理し、2回目以降のレビューで過去履歴を参照して指摘内容を変化させる。ReActパターンとツール連携でセッションをまたいだ記憶の永続化を実現。

- **ソース**: [Qiita claude](https://qiita.com/bit-tanghao/items/20e0366ce3f08f291ce5)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-19 | 自動生成 |
