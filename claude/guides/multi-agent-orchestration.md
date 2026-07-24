---
title: Multi Agent Orchestration
category: guides
subcategory: multi-agent-orchestration
tags:
- claude-code
- cowork
- haiku
- opus
- prompt
- sonnet
date: '2026-04-12'
updated: '2026-07-24'
sources:
- url: https://qiita.com/saitoko/items/648124fec66afe2cd8df
  title: Claude Codeで8体AIエージェント組織を作った6日間 — 人間とAIはどんな対話をしたか
  date: '2026-04-12'
- url: https://www.reddit.com/r/ClaudeAI/comments/1ur2ml9/anthropic_just_benchmarked_fable_5_orchestrates
  title: 'Anthropic just benchmarked "Fable 5 orchestrates, cheap models execute":
    96% of the performance at 46% of the cost. You can run this pattern in Claude
    Code today'
  date: '2026-07-08'
- url: https://zenn.dev/canly/articles/7dd489193c41e4
  title: Claude Codeのスキルでお問い合わせ調査を半自動化し、チームで育てている話
  date: '2026-07-24'
---



# Multi Agent Orchestration

---

## 2026-07-24

### Claude Codeのスキルでお問い合わせ調査を半自動化し、チームで育てている話

カンリー店舗集客のチームが、Claude Codeのスキル機能を使ってお問い合わせ調査を半自動化した事例。DB・ログ・コードの3つを調査対象とし、メインエージェントと3つのサブエージェントによるマルチエージェント設計（Orchestrator-Workerパターン）を採用。各サブエージェントが要点のみを返すことでコンテキスト消費を抑え、メインエージェントが結果を統合して回答文案と調査レポートを作成する仕組みを構築した。

- **ソース**: [Zenn claude](https://zenn.dev/canly/articles/7dd489193c41e4)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-07-08

### Anthropic just benchmarked "Fable 5 orchestrates, cheap models execute": 96% of the performance at 46% of the cost. You can run this pattern in Claude Code today

Anthropic が公式ベンチマークで「Opus が指示、安価なモデルが実行」パターンを検証し、全 Opus 構成の 96% の性能を 46% のコストで達成できることを実証。Claude Code では subagent の model フロントマター、effort 設定、CLAUDE.md ポリシーの 3 機能を組み合わせて同じパターンを実装可能。pilotfish という 6 役割構成のパッケージが公開され、Haiku スカウト、Sonnet 実行、Opus 判断といった役割分担でコスト最適化を実現。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ur2ml9/anthropic_just_benchmarked_fable_5_orchestrates)
- **重要度**: 8/10
- **タグ**: opus, sonnet, haiku

---

## 2026-04-12

### Claude Codeで8体AIエージェント組織を作った6日間 — 人間とAIはどんな対話をしたか

SE歴26年の筆者が、Claude Codeを使い6日間でコードを1行も書かずに8体のAIエージェント組織を構築した実践記録。CLAUDE.mdを17行から育て、resarcherの調査提案を基に優先度判断を行い、CEOによるレビューサイクルを通じて組織を成長させた。重要なのは「人間が何をやらないかを決め、AIが提案を尽くす」という役割分担。

- **ソース**: [Qiita claudecode](https://qiita.com/saitoko/items/648124fec66afe2cd8df)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-12 | 自動生成 |
