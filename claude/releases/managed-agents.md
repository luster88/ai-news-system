---
title: Managed Agents
category: releases
subcategory: managed-agents
tags:
- claude-api
- claude-console
- cowork
- mcp
- performance
- pricing
- release
- 新機能
date: '2026-04-08'
updated: '2026-05-19'
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
- url: https://www.reddit.com/r/ClaudeAI/comments/1t5j84j/new_in_claude_managed_agents_dreaming_outcomes
  title: 'New in Claude Managed Agents: dreaming, outcomes, multiagent orchestration,
    and webhooks.'
  date: '2026-05-06'
- url: https://zenn.dev/evolink/articles/6385a3cd937518
  title: '# AIエージェントが「夢を見る」時代が来た — Anthropic Dreaming の技術的意味'
  date: '2026-05-07'
- url: https://qiita.com/xiji2646/items/17395d355f0fbfe28860
  title: Claude Managed Agents の Dreaming 機能：セッション間で自己改善するエージェントの仕組み
  date: '2026-05-07'
- url: https://ai-heartland.com/news/claude-managed-agents-dreaming-outcomes
  title: Claude Managed Agents深掘り｜Dreaming・Outcomes・Multi-Agent Orchestrationを完全解説
  date: '2026-05-07'
- url: https://zenn.dev/kai_kou/articles/215-claude-managed-agents-guide
  title: Claude Managed Agents入門 — インフラ不要でAIエージェントを本番運用する
  date: '2026-05-18'
- url: https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents
  title: Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents
  date: '2026-05-19'
---








# Managed Agents

---

## 2026-05-19

### Anthropic adds self-hosted sandboxes and MCP tunnels to Claude Managed Agents

Anthropic が Claude Managed Agents に self-hosted sandboxes と MCP tunnels を追加。企業は AI エージェントのツール実行を自社インフラで行えるようになり、MCP tunnels により内部データベースや API への暗号化接続が可能に。ただしエージェントのオーケストレーション自体は Anthropic のサーバー上に残る。両機能とも初期テスト段階。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents)
- **重要度**: 8/10
- **タグ**: 新機能, mcp, claude-api

---

## 2026-05-18

### Claude Managed Agents入門 — インフラ不要でAIエージェントを本番運用する

Anthropicが2026年4月8日にClaude Managed Agentsをパブリックベータとして公開。エージェントループ、サンドボックス、ツール実行レイヤーを自前実装する必要がなくなり、Anthropicのマネージドインフラ上でAIエージェントを動かせる。Agent/Environment/Session/Eventsの4つのコアコンセプトで構成され、bash、ファイル操作、Web検索など8種の組み込みツールを提供。料金は$0.08/セッション時間＋通常APIトークン料金。

- **ソース**: [Zenn claude](https://zenn.dev/kai_kou/articles/215-claude-managed-agents-guide)
- **重要度**: 9/10
- **タグ**: 新機能, claude-api, release

---

## 2026-05-07

### # AIエージェントが「夢を見る」時代が来た — Anthropic Dreaming の技術的意味

Anthropic が5月6日に発表した Managed Agents の新機能「Dreaming」は、エージェントがセッション間でバックグラウンドで過去の会話を分析し、自律的にメモリを更新する仕組み。従来の受動的なメモリから能動的な学習へのシフトを示す。Outcomes（自動評価）やマルチエージェントオーケストレーション（パブリックベータ）と組み合わせることで、エージェントは稼働履歴を競争優位に変える「蓄積するシステム」へと進化。Automatic/Human Review の2モードを提供し、料金は $0.08/アクティブセッション時間 + トークンコスト。

- **ソース**: [Zenn claude](https://zenn.dev/evolink/articles/6385a3cd937518)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, release

---

### Claude Managed Agents の Dreaming 機能：セッション間で自己改善するエージェントの仕組み

Anthropic が2025年5月6日にリリースした Claude Managed Agents の Dreaming 機能は、エージェントがセッション間で自律的に過去の会話を振り返り、パターンを抽出してメモリに書き込む仕組み。Outcomes と組み合わせることで人間の介入なしにフィードバックループが閉じ、オーケストレーション機能により最大20のサブエージェントへの並列委譲が可能。Harvey で完了率が約6倍、Wisedocs でレビュー速度が50%改善など実績がある一方、現在はベータ版で Claude モデルのみ対応という制約がある。

- **ソース**: [Qiita claudecode](https://qiita.com/xiji2646/items/17395d355f0fbfe28860)
- **重要度**: 9/10
- **タグ**: 新機能, claude-api, release

---

### Claude Managed Agents深掘り｜Dreaming・Outcomes・Multi-Agent Orchestrationを完全解説

Anthropic の Code with Claude 2026 カンファレンスで、Claude Managed Agents に 3 つの大型機能（Dreaming・Outcomes・Multi-Agent Orchestration）と Memory の正式β昇格が発表された。特に注目は Dreaming 機能で、エージェントが夜間に過去の作業を振り返り Memory を整理して自己改善する仕組み。楽天が本番投入し 97% のエラー削減・27% のコスト削減・34% のレイテンシ削減を達成。Dreaming は過去のセッション履歴から重複・矛盾・古いエントリを整理し、新しい Memory ストアを生成する非同期ジョブとして実装されている。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/claude-managed-agents-dreaming-outcomes)
- **重要度**: 9/10
- **タグ**: 新機能, claude-api, release

---

## 2026-05-06

### New in Claude Managed Agents: dreaming, outcomes, multiagent orchestration, and webhooks.

Claude Managed Agents に4つの新機能が追加されました。「Dreaming」は過去のセッションからパターンを抽出しエージェントを改善する機能で、Harvey社ではタスク完了率が約6倍向上しました。「Outcomes」は品質基準を設定し自動評価・反復改善を行う機能、「Multiagent orchestration」は複数の専門エージェントを並行稼働させる機能、「Webhooks」は完了通知機能です。Dreaming はリサーチプレビュー、その他3機能はパブリックベータで提供開始されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1t5j84j/new_in_claude_managed_agents_dreaming_outcomes)
- **重要度**: 9/10
- **タグ**: 新機能, claude-api, release

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
