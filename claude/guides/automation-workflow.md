---
title: Automation Workflow
category: guides
subcategory: automation-workflow
tags:
- claude-code
- cowork
- prompt
- setup
- 新機能
date: '2026-04-08'
updated: '2026-04-17'
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
---




# Automation Workflow

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
