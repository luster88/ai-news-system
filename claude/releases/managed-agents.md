---
title: Managed Agents
category: releases
subcategory: managed-agents
tags:
- claude-api
- claude-console
- cowork
- performance
- pricing
- release
- 新機能
date: '2026-04-08'
updated: '2026-05-03'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1sfz7a5/introducing_claude_managed_agents_now_in_public
  title: Introducing Claude Managed Agents, now in public beta.
  date: '2026-04-08'
- url: https://qiita.com/ny7760/items/07af9d3facaf4af3d9f2
  title: Claude Managed Agents を触ってみる
  date: '2026-04-09'
- url: https://ai-heartland.com/news/claude-managed-agents
  title: Claude Managed Agents発表：エージェントの構築からデプロイまでをAnthropicがホスティング、パブリックベータ開始
  date: '2026-04-09'
- url: https://qiita.com/o0-sheeefk-0o/items/6a4d718f092187bf6652
  title: Claude がマネージドになった！他社サービスと何が違うのか調べてみた
  date: '2026-04-10'
- url: https://qiita.com/t_mando_/items/933ed7fa7b2d52b641f9
  title: Claude Managed Agentsって何？GeminiAPIと何が違うの？Claudeに聞きながら理解した
  date: '2026-04-10'
- url: https://qiita.com/tai0921/items/b542aafa29d363e50510
  title: Claude Managed Agentsとは？従来の自前実装との違い
  date: '2026-05-03'
---




# Managed Agents

---

## 2026-05-03

### Claude Managed Agentsとは？従来の自前実装との違い

Anthropic が発表した Claude Managed Agents は、エージェント開発におけるツール接続・メモリ管理・エラーハンドリングなどの複雑な実装を API レベルで引き受けるサービス。開発者はタスク定義に集中できる一方、従量課金への移行・ベンダーロックイン・既存基盤からの移行コストに注意が必要。2026年4月からサードパーティハーネス経由の利用がサブスクリプション対象外となり、API課金体系に統一される。

- **ソース**: [Qiita claude](https://qiita.com/tai0921/items/b542aafa29d363e50510)
- **重要度**: 8/10
- **タグ**: claude-api, 新機能, pricing

---

### Claude Managed Agentsとは？従来の自前実装との違い

AnthropicがClaude Managed Agentsを発表。従来の自前実装で必要だったツール接続、メモリ管理、エラーハンドリング、マルチステップ制御をAPIレベルで引き受け、開発者はタスク定義に集中できる。2026年4月からサードパーティハーネス経由のClaude利用はサブスクリプション対象外となり従量課金に移行。既存の自社エージェント基盤を持つチームは移行コストとベンダーロックインのリスクを慎重に評価する必要がある。

- **ソース**: [Qiita claudecode](https://qiita.com/tai0921/items/b542aafa29d363e50510)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, pricing

---

## 2026-04-10

### Claude がマネージドになった！他社サービスと何が違うのか調べてみた

Anthropic が Claude Managed Agents を発表。モデルベンダーが実行インフラまで提供する新しいアプローチで、AWS/Azure/Google のクラウドサービスとは異なり、Claude API キーのみで始められるフルマネージド実行環境。Session・Harness・Sandbox の3層アーキテクチャにより、障害復旧とスケーリングを自動化し、Time-to-First-Token を大幅削減。クラウドロックインを避けたいエージェント開発に適している。

- **ソース**: [Qiita claude](https://qiita.com/o0-sheeefk-0o/items/6a4d718f092187bf6652)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, performance

---

### Claude Managed Agentsって何？GeminiAPIと何が違うの？Claudeに聞きながら理解した

AnthropicがClaude Managed Agentsをパブリックベータとしてリリース。これは単なるAPIではなく、エージェント実行インフラを含む新サービスで、Web検索・状態管理・リトライなどをAnthropicが提供する。GeminiAPIがモデル呼び出しのみなのに対し、Managed Agentsは複数ステップのタスクをクラウドで自動実行できる点が特徴。料金はAPIトークン料金に加え$0.08/セッション時間が追加される。

- **ソース**: [Qiita claude](https://qiita.com/t_mando_/items/933ed7fa7b2d52b641f9)
- **重要度**: 8/10
- **タグ**: claude-api, 新機能, cowork

---

## 2026-04-09

### Claude Managed Agents を触ってみる

Anthropic が Claude Managed Agents のパブリックβ版を公開。Claude Console から数クリックでエージェントを起動できるマネージド実行環境サービス。Deep researcher などのテンプレートを選択でき、Web アクセスや思考プロセスのトレースが可能。従量課金制（0.08ドル/時間）で、セッション管理が必要。ハーネスをモデル進化に応じて差し替えられる設計が特徴。

- **ソース**: [Qiita claude](https://qiita.com/ny7760/items/07af9d3facaf4af3d9f2)
- **重要度**: 8/10
- **タグ**: 新機能, claude-console, release

---

### Claude Managed Agents発表：エージェントの構築からデプロイまでをAnthropicがホスティング、パブリックベータ開始

AnthropicがClaude Managed Agentsのパブリックベータを発表。エージェントの構築からデプロイまでをフルマネージドで提供し、Brain/Hands/Sessionの3層分離アーキテクチャを採用。TTFTを最大90%削減し、セッションの永続化と自動復旧を実現。プロトタイプから本番運用まで数日で移行可能になる。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/claude-managed-agents)
- **重要度**: 10/10
- **タグ**: 新機能, claude-api, release

---

## 2026-04-08

### Introducing Claude Managed Agents, now in public beta.

Anthropic が Claude Managed Agents のパブリックベータを発表。エージェントの構築とデプロイに必要なインフラ、状態管理、権限管理を提供し、数ヶ月かかっていた本番環境への展開を数日で実現可能に。Notion、Sentry、Rakuten、Asana、Vibecodeなどの企業が既に利用開始。タスク、ツール、ガードレールを定義するだけで、Anthropicのインフラ上でエージェントを実行できる。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1sfz7a5/introducing_claude_managed_agents_now_in_public)
- **重要度**: 9/10
- **タグ**: 新機能, claude-api, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-08 | 自動生成 |
