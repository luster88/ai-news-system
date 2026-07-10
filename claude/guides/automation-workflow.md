---
title: Automation Workflow
category: guides
subcategory: automation-workflow
tags:
- claude-api
- claude-code
- claude-console
- cowork
- haiku
- mcp
- prompt
- setup
- sonnet
- 新機能
date: '2026-04-08'
updated: '2026-07-10'
sources:
- url: https://zenn.dev/shelty/articles/20260408-budget-book-asset-management
  title: MoneyForwardの家計簿データで資産予測を自動化してみた＠Claude
  date: '2026-04-08'
- url: https://www.reddit.com/r/ClaudeAI/comments/1shngqm/i_automated_most_of_my_job
  title: I automated most of my job
  date: '2026-04-10'
- url: https://qiita.com/saitoko/items/e1c07bfd3e7416cdbe4f
  title: Claude Codeのスケジュール枠は3つだけ——ディスパッチャー方式で何タスクでも回す設計
  date: '2026-04-13'
- url: https://qiita.com/4q_sano/items/6d2bcfceb4fc2e728204
  title: 【もうSlackを読むのをやめた】Claude Codeを“AIパートナー化”して朝の情報整理を自動化した話
  date: '2026-04-17'
- url: https://zenn.dev/itsuya/articles/ai-content-pipeline-2026
  title: Claude CLIとPythonで“無料”の自律コンテンツ生成パイプラインを作る
  date: '2026-05-31'
- url: https://qiita.com/1280itsuya/items/d3f55afeba54cda1e361
  title: 【ガチ検証】Python＋Claude APIでアフィリ記事を半自動量産する個人開発パイプラインを作ったら、1記事の手間が90分→7分になった話
  date: '2026-06-04'
- url: https://qiita.com/drasenas/items/338537f2f7fea9014207
  title: Claude Code Routines で GWS ライセンス棚卸しを月次自動化する
  date: '2026-06-14'
- url: https://www.reddit.com/r/ClaudeAI/comments/1uszlay/how_claude_does_my_40_hour_a_week_job_by_itself
  title: How Claude does my 40 hour a week job by itself - for 15 Cents
  date: '2026-07-10'
---








# Automation Workflow

---

## 2026-07-10

### How Claude does my 40 hour a week job by itself - for 15 Cents

RedditユーザーがWebサイトから情報を抽出する契約業務を、Claudeに自動化スクリプトを書かせて完全自動化した事例。週40時間かかる作業をわずか15セントのトークンコストで処理でき、専門知識が必要な単純作業を効率化できることを実証。Claudeがスクリプトを生成し、ユーザーは開始指示と最終提出のみを行う。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uszlay/how_claude_does_my_40_hour_a_week_job_by_itself)
- **重要度**: 6/10
- **タグ**: claude-api, cowork, prompt

---

## 2026-06-14

### Claude Code Routines で GWS ライセンス棚卸しを月次自動化する

Anthropic が2026年4月に公開した Claude Code Routines を使い、Google Workspace のライセンス棚卸しを月次で自動化する実装パターンを解説。Admin SDK Directory API で未使用ライセンスを検出し、Slack MCP 経由でレポートを自動生成する手順と、GAS との比較判断基準を整理している。100名規模の環境で月1〜2時間かかる作業を自動化でき、プロンプトとリポジトリを組み合わせてスケジュール実行する方法を示している。

- **ソース**: [Qiita claudecode](https://qiita.com/drasenas/items/338537f2f7fea9014207)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-06-04

### 【ガチ検証】Python＋Claude APIでアフィリ記事を半自動量産する個人開発パイプラインを作ったら、1記事の手間が90分→7分になった話

Python と Claude API を用いたアフィリエイト記事の半自動生成パイプラインの実装事例。90分かかっていた記事作成を7分に短縮した一方、全自動化による3日でのスパム判定の失敗から「生成は自動・公開は人間」という設計思想に至った実践レポート。テーマ固定検証、アフィリリンク自動差し込み、7日間重複ロック、コスト最適化（Sonnet生成・Haiku採点で4割削減）などの具体的な実装手法を紹介。

- **ソース**: [Qiita claude](https://qiita.com/1280itsuya/items/d3f55afeba54cda1e361)
- **重要度**: 6/10
- **タグ**: claude-api, sonnet, haiku

---

## 2026-05-31

### Claude CLIとPythonで“無料”の自律コンテンツ生成パイプラインを作る

Claude の Max プラン（定額）と Claude CLI を活用し、従量課金ゼロでテキスト生成を行う自律コンテンツ生成パイプラインの構築方法を解説。API キーではなくログイン済み CLI をサブプロセスで呼び出し、stdin 経由でプロンプトを渡す実装の勘所や、生成コンテンツのドリフト防止策、JSON 抽出のテクニックを紹介。Qiita/Zenn/Dev.to など view 数が取得できるプラットフォームを活用し、反応を実測しながら改善するアプローチを提案している。

- **ソース**: [Zenn claude](https://zenn.dev/itsuya/articles/ai-content-pipeline-2026)
- **重要度**: 6/10
- **タグ**: claude-console, prompt, cowork

---

## 2026-04-17

### 【もうSlackを読むのをやめた】Claude Codeを“AIパートナー化”して朝の情報整理を自動化した話

Claude Codeを使ってSlackの未読メッセージを自動で要約・整理し、必要な情報だけをDMで受け取るワークフローを構築した事例。朝の情報収集作業を自動化し、AIに「自分に関係ある情報の選別」をさせることで業務効率を改善。

- **ソース**: [Qiita claudecode](https://qiita.com/4q_sano/items/6d2bcfceb4fc2e728204)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-04-13

### Claude Codeのスケジュール枠は3つだけ——ディスパッチャー方式で何タスクでも回す設計

Claude Codeのスケジュール実行機能には枠数制限（Max 5xプランで3枠）があるため、ディスパッチャー方式で複数タスクを1枠で管理する設計パターンを紹介。タスクリストとタスク定義ファイルを分離し、hourly/daily/adhocの3種類のスケジュールで運用する実践的な自動化手法を解説している。

- **ソース**: [Qiita claudecode](https://qiita.com/saitoko/items/e1c07bfd3e7416cdbe4f)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-10

### I automated most of my job

11年のキャリアを持つソフトウェアエンジニアが、Claude CLIと.NETアプリを組み合わせて業務の80%を自動化した事例。GitLab APIから課題を取得し、Claudeで分類・開発・PRレビュー対応まで自動化。15分ループで実行し、レビューとテストのみ2-3時間/日で対応する運用を1週間継続中。コード品質は手動開発時と同等を維持している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1shngqm/i_automated_most_of_my_job)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-04-08

### MoneyForwardの家計簿データで資産予測を自動化してみた＠Claude

MoneyForward MEの家計簿データをPythonで分析し、数十年先の資産予測を自動化するシステムを構築した事例。保有株式のCAGR計算による複利シミュレーション、生活費と事業経費の自動分離、GitLab CIによる週次・月次の自動更新機能を実装。コードはオープンソースで公開され、ClaudeやChatGPTを使って誰でも構築可能な仕組みとなっている。

- **ソース**: [Zenn claude](https://zenn.dev/shelty/articles/20260408-budget-book-asset-management)
- **重要度**: 5/10
- **タグ**: claude-code, cowork, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-08 | 自動生成 |
