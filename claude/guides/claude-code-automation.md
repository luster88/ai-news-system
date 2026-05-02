---
title: Claude Code Automation
category: guides
subcategory: claude-code-automation
tags:
- claude-code
- cowork
- mcp
- prompt
- setup
- 新機能
date: '2026-03-28'
updated: '2026-05-02'
sources:
- url: https://qiita.com/kenji_harada/items/58b8dbb395199bbe9f1e
  title: Claude Codeで「AI同士の会話」によるブログ自動生成システムを作ってみた
  date: '2026-03-28'
- url: https://qiita.com/kenji_harada/items/ce01ef8185b48da92013
  title: 【やってみた】Claude Codeで作るSEO自動分析システム - GSC×GA4データを毎朝Slackに通知
  date: '2026-04-05'
- url: https://qiita.com/Kosei0412/items/d259982604a0186a7d8b
  title: GPTに切られたカウンセラーがClaudeCodeで自動化ラインを作った話
  date: '2026-04-05'
- url: https://qiita.com/kanta13jp1/items/38f0383e0ea01b787900
  title: 【実践】Claude Code Schedule でサポート対応を自動化する具体的な手順
  date: '2026-04-10'
- url: https://qiita.com/saitoko/items/e1c07bfd3e7416cdbe4f
  title: Claude Codeのスケジュール枠は3つだけ——ディスパッチャー方式で何タスクでも回す設計
  date: '2026-04-13'
- url: https://zenn.dev/gao0111/articles/5fe1dcedc8c112
  title: Claudeと2日でAIニュース自動収集サービスを作って公開した話
  date: '2026-04-14'
- url: https://qiita.com/okikusan-public/items/02d3c7b8a78836ca1b09
  title: Claude Code Skills × 投資分析 Vol.4 — ゼロから再設計。マルチAIエージェントが自律的に動く投資アシスタントに生まれ変わった
  date: '2026-04-19'
- url: https://qiita.com/apoloffice/items/0901269b7ea7e9ef4b66
  title: Claude Codeに開発を丸投げする方法―PCの前から離れられる環境構築の完全ガイド
  date: '2026-04-20'
- url: https://qiita.com/Northern_learner/items/8474a40482c72dd09c68
  title: AI駆動開発のための CLAUDE.md 設計パターン — 実運用で磨いた5つの型
  date: '2026-04-24'
- url: https://qiita.com/kotaro_ai_lab/items/119901d60f34e07da801
  title: SwiftData × Claude Code で永続化層を設計する — @Model設計からマイグレーションまで実務で詰まらないための完全ガイド
  date: '2026-04-25'
- url: https://qiita.com/JUMP_IN/items/ad519ebd526a633af70d
  title: AI アシスタントの設定ファイルに最初に書いておく 5 行 — CLAUDE.md 最小テンプレ
  date: '2026-04-28'
- url: https://qiita.com/Tadashi_Kudo/items/74737ca70a10cb4e57fa
  title: AIにとっての「記録階層」設計：feedback / ADR / working-memory / project_*.md の使い分け
  date: '2026-04-30'
- url: https://www.reddit.com/r/ClaudeAI/comments/1t1wrfs/i_used_claude_as_my_pair_programmer_to_build_a
  title: I used Claude as my pair programmer to build a safe for kids generative coloring
    book app for my daughter!
  date: '2026-05-02'
---












# Claude Code Automation

---

## 2026-05-02

### I used Claude as my pair programmer to build a safe for kids generative coloring book app for my daughter!

開発者が娘のために、Claudeをペアプログラマーとして活用し、子供向けの安全な生成AIぬり絵アプリをSwiftUIで構築。既存アプリの広告過多や複雑さを解決するため、シンプルで安全な設計を重視。ローカルデータ保存、保護者ロック機能を実装し、AIの責任ある活用を目指した実例。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1t1wrfs/i_used_claude_as_my_pair_programmer_to_build_a)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, 新機能

---

## 2026-04-30

### AIにとっての「記録階層」設計：feedback / ADR / working-memory / project_*.md の使い分け

AI コーディングエージェントの長期運用において、記録を4層（feedback、ADR、working-memory、project_*.md）に分離する設計手法を解説。CLAUDE.md に全てを詰め込むと破綻するため、更新サイクル別に分類し、feedback で禁止事項、ADR で設計判断の根拠、working-memory で一時メモ、project ファイルで PJ 状態を管理する。この構造化により、AI の挙動が同僚レベルに向上し、再調査時間が 15 分から 2 分に短縮された実例を紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/74737ca70a10cb4e57fa)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-28

### AI アシスタントの設定ファイルに最初に書いておく 5 行 — CLAUDE.md 最小テンプレ

Claude Code など AI アシスタントの設定ファイル (CLAUDE.md) に記載すべき最小限の 5 つのルールをテンプレート化した記事。「実装前に必ず計画」「曖昧な指示は確認」「設計提案時は反論もセット」「計測方法を示す」「仕様と実走の区別」の 5 項目を定義することで、毎セッション同じ前提を説明し直す手間を省き、AI の暴走や誤解を防ぐ。ChatGPT や Gemini にも移植可能。

- **ソース**: [Qiita claudecode](https://qiita.com/JUMP_IN/items/ad519ebd526a633af70d)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 2026-04-25

### SwiftData × Claude Code で永続化層を設計する — @Model設計からマイグレーションまで実務で詰まらないための完全ガイド

SwiftDataを使った永続化層の実務的な設計ガイド。Claude Codeを活用し、@Modelのデフォルト値設定、リレーションシップのdeleteRule指定、VersionedSchemaによるマイグレーション対応など、実務で詰まりやすいポイントを網羅的に解説。CLAUDE.mdによる設計規約の事前共有と、具体的なプロンプト例も提示している。

- **ソース**: [Qiita claudecode](https://qiita.com/kotaro_ai_lab/items/119901d60f34e07da801)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-24

### AI駆動開発のための CLAUDE.md 設計パターン — 実運用で磨いた5つの型

Claude Code で使う CLAUDE.md の実運用設計パターンを5つ紹介。一般論への収斂を防ぐための「ユーザー仮説優先ルール」、自己批判による品質向上、セッションログの git 管理による意思決定の再現性確保、時刻情報の自動取得による判断ミス防止、主観を残す記録フォーマットなど、AIの思考プロセスそのものを制御する設計手法を解説。

- **ソース**: [Qiita claude](https://qiita.com/Northern_learner/items/8474a40482c72dd09c68)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-20

### Claude Codeに開発を丸投げする方法―PCの前から離れられる環境構築の完全ガイド

Claude Codeを自律的に長時間稼働させる環境構築ガイド。settings.jsonのallowlistによる権限管理、Makefileによるコマンド一元管理、MCP活用によるE2Eテスト自動化など、エージェントが1〜2時間人間の介入なしで実装からPR作成まで完遂できる環境の実現方法を解説。プロンプトでの制約ではなく環境側での安全担保が鍵。

- **ソース**: [Qiita claudecode](https://qiita.com/apoloffice/items/0901269b7ea7e9ef4b66)
- **重要度**: 7/10
- **タグ**: claude-code, setup, mcp

---

## 2026-04-19

### Claude Code Skills × 投資分析 Vol.4 — ゼロから再設計。マルチAIエージェントが自律的に動く投資アシスタントに生まれ変わった

Claude Code を使った投資分析システムの進化を記録したシリーズ第4弾。従来のスクリプトベースの自動化から、6つのAIエージェントが役割分担して自律的に動くマルチエージェントオーケストレーションへとゼロから再設計。Agentic AI PatternとAgentic Engineeringを適用し、ルーティング・連鎖実行・自律修正ループを実装。ユーザーの意図に応じてエージェントが自動選択され、直列・並列で連鎖実行することで、複合的な投資判断を人間の介入なしに実現。

- **ソース**: [Qiita claudecode](https://qiita.com/okikusan-public/items/02d3c7b8a78836ca1b09)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-04-14

### Claudeと2日でAIニュース自動収集サービスを作って公開した話

個人開発者がClaude Maxプランを活用し、2日間でAIニュース自動収集サービス「AIフロントライン」を構築・公開。Anthropic、OpenAI、Google等15の公式ソースからRSS/GitHub Releasesを3時間ごとに収集し、Claudeが日本語要約・解説・重要度スコアを自動生成。レビュワー機能で低品質記事をフィルタリングし、VPS+systemdタイマーで月700円運用。実装のほぼ全てをClaudeに指示して完成させ、インフラ設定やDNSトラブルシューティングもClaude Code CLIで解決した実践例。

- **ソース**: [Zenn claude](https://zenn.dev/gao0111/articles/5fe1dcedc8c112)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-13

### Claude Codeのスケジュール枠は3つだけ——ディスパッチャー方式で何タスクでも回す設計

Claude Codeのスケジュール実行機能は登録枠が3つまでという制約があるため、ディスパッチャー方式で複数タスクを1枠で管理する設計パターンを紹介。タスクリストとタスク定義ファイルを分離し、hourly/daily/adhocの3種類のスケジュールでタスクを自動実行する仕組みを実装している。

- **ソース**: [Qiita claude](https://qiita.com/saitoko/items/e1c07bfd3e7416cdbe4f)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-04-10

### 【実践】Claude Code Schedule でサポート対応を自動化する具体的な手順

Claude Code の Schedule 機能を活用して、Flutter Web + Supabase アプリのサポート対応を自動化する実践的な手順を解説。Supabase Edge Function の作成、schedule_task_runs テーブルでの実行記録、Flutter 管理ダッシュボードでの確認方法など、具体的な実装例を含む。実際に稼働中のサービスと GitHub リポジトリも公開されている。

- **ソース**: [Qiita claudecode](https://qiita.com/kanta13jp1/items/38f0383e0ea01b787900)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-04-05

### 【やってみた】Claude Codeで作るSEO自動分析システム - GSC×GA4データを毎朝Slackに通知

Claude Codeを使ってGSC（Google Search Console）とGA4のデータを自動取得し、全記事をAIがスコアリングして改善すべき記事をSlackに毎朝通知するSEO自動分析システムの構築事例。月間4,000表示でCTR 0.02%という手動では見落としていたボトルネックを検出し、21件の改善機会を発見。googleapis とGoogle Analytics Data APIを使用し、OAuth2認証とサービスアカウント設定で実装。

- **ソース**: [Qiita claude](https://qiita.com/kenji_harada/items/ce01ef8185b48da92013)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

### GPTに切られたカウンセラーがClaudeCodeで自動化ラインを作った話

メンタルヘルス領域でGPTの利用制限を受けたカウンセラーが、ClaudeCodeを中心に5重監査・Slack承認・証跡保存を備えた業務自動化システムを再構築。「AIを信用しない」「止めるべきものは構造で止める」をコンセプトに、全工程に人間承認を必須とし、GPT・Claude・Geminiを直列配置した多層チェック機構を実装。福祉現場の事務作業効率化を、安全性を担保しながら実現した事例。

- **ソース**: [Qiita claudecode](https://qiita.com/Kosei0412/items/d259982604a0186a7d8b)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, setup

---

## 2026-03-28

### Claude Codeで「AI同士の会話」によるブログ自動生成システムを作ってみた

Claude Code Channelsを活用し、2つのAIエージェント（ライター役と編集者役）がDiscord上で会話しながらブログ記事を自動生成・改善するシステムの実装例。従来の「AIに一発で完璧な記事を書かせる」アプローチではなく、段階的な批評・推敲プロセスを導入することで読みやすさが大幅に向上。ローカル実行のためAPI料金がかからず、Brave SearchやSupabaseとMCP連携してトレンド調査からSNS展開まで自動化。

- **ソース**: [Qiita claude](https://qiita.com/kenji_harada/items/58b8dbb395199bbe9f1e)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-28 | 自動生成 |
