---
title: Claude Code Agent Architecture
category: guides
subcategory: claude-code-agent-architecture
tags:
- claude-api
- claude-code
- cowork
- performance
- prompt
- 新機能
date: '2026-04-15'
updated: '2026-07-27'
sources:
- url: https://zenn.dev/chiakidayo/articles/agent-teams-subagent-comparison
  title: 【Claude Code】Agent teamsとSubagent並列実行比較メモ
  date: '2026-04-15'
- url: https://qiita.com/bit-tanghao/items/bec927ebf9621d131d9e
  title: AIエージェントシリーズ 第5弾｜プランニングAgent——大きなPRを自動分解して実行する
  date: '2026-04-20'
- url: https://ai-heartland.com/explain/agent-provenance-commit-dag-knowledge-graph
  title: AIエージェントの出力に来歴を残す設計｜コミットDAGと知識グラフで根拠を追える状態にする
  date: '2026-07-27'
---



# Claude Code Agent Architecture

---

## 2026-07-27

### AIエージェントの出力に来歴を残す設計｜コミットDAGと知識グラフで根拠を追える状態にする

AIエージェントを並列化すると出力の根拠や来歴が追えなくなる問題を、コミットDAGと知識グラフを用いた4層の記憶設計で解決する手法を解説。会話ログ、成果物、コミットDAG、知識グラフの各層が答える質問の違いを明確にし、並列ワーカーの発見が要約でしか外に出られない情報の目詰まりを解消する。Anthropicの5つのワークフローパターンに対する永続層の役割も整理している。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/agent-provenance-commit-dag-knowledge-graph)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-20

### AIエージェントシリーズ 第5弾｜プランニングAgent——大きなPRを自動分解して実行する

大規模なPRレビューを効率化するため、Plan-and-Executeパターンを実装したAIエージェントの解説記事。ReActループの欠点（ファイル数に比例したステップ増加と一貫性の欠如）を克服し、事前計画フェーズと実行フェーズの分離により、全体を見渡した効率的なレビューを実現。静的解析（正規表現・AST）とLLMを組み合わせ、セキュリティやパフォーマンスの問題を自動検出・改善提案する実装を紹介。

- **ソース**: [Qiita claude](https://qiita.com/bit-tanghao/items/bec927ebf9621d131d9e)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 2026-04-15

### 【Claude Code】Agent teamsとSubagent並列実行比較メモ

Claude Codeの2つのマルチエージェント機能を比較した記事。Subagent並列実行は独立したタスクをMain Agent主導で効率的に処理し、トークン消費が少ない。一方Agent teamsは各Agentが独立したインスタンスを持ち、エージェント間で直接やり取りしながら複雑なタスクを協働処理できるが、トークン消費は多い。タスクの独立性と協働の必要性に応じて使い分けることが推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/chiakidayo/articles/agent-teams-subagent-comparison)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-15 | 自動生成 |
