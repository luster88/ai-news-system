---
title: Workflow Automation
category: guides
subcategory: workflow-automation
tags:
- claude-api
- claude-code
- cowork
- haiku
- mcp
- prompt
- setup
date: '2026-04-26'
updated: '2026-07-03'
sources:
- url: https://zenn.dev/saytooy_arch/articles/14-zenn-auto-publish-pipeline
  title: Zenn自動公開パイプラインをclaude -pで構築した話
  date: '2026-04-26'
- url: https://zenn.dev/aiflowlab/articles/n8n-claude-haiku-inquiry-workflow
  title: Claude Haiku 4.5 + n8n で問い合わせ対応ワークフローを作ったら、100% 精度・1 件 0.5 円で運用できた
  date: '2026-05-08'
- url: https://zenn.dev/rkpg/articles/claude-code-content-factory
  title: Claude Codeを「コンテンツ工場」にした話。スラッシュコマンド60個 + Agent Teamsで個人メディアを半自動化する
  date: '2026-05-23'
- url: https://zenn.dev/sonicgarden/articles/402096a0f7b0c2
  title: 親方エージェントと毎日ふりかえりをするワークフロー
  date: '2026-05-24'
- url: https://qiita.com/10yama_k/items/845b08ad280ce1c832a6
  title: Googlecolabで無料で文字おこし
  date: '2026-07-03'
---





# Workflow Automation

---

## 2026-07-03

### Googlecolabで無料で文字おこし

Google Colabの無料枠とWhisperを使って音声ファイルを日本語で文字起こしする方法の備忘録。Claude Codeを秘書役として使い、夜の思いつきをボイスメモ→文字起こし→保存する個人的なワークフローが紹介されている。複数ファイルの一括処理にも対応。

- **ソース**: [Qiita claude](https://qiita.com/10yama_k/items/845b08ad280ce1c832a6)
- **重要度**: 4/10
- **タグ**: claude-code, cowork, setup

---

## 2026-05-24

### 親方エージェントと毎日ふりかえりをするワークフロー

ソニックガーデンのエンジニアが、Claude Codeを使って毎日の振り返りと週次KPTの準備を自動化するワークフローを構築。会社の文化や親方の実際のコミュニケーションスタイルを学習させたカスタムエージェント「oyakata」を作成し、日報レビューとKPT準備を自動化。コードを一切書かず、Markdownファイルとカスタムスキル・サブエージェント機能のみで実装し、振り返りの質が大幅に向上した事例。

- **ソース**: [Zenn claude](https://zenn.dev/sonicgarden/articles/402096a0f7b0c2)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-05-23

### Claude Codeを「コンテンツ工場」にした話。スラッシュコマンド60個 + Agent Teamsで個人メディアを半自動化する

個人メディア運営者がClaude Codeを「コンテンツ工場」として設計した実践事例。60個のカスタムスラッシュコマンドと複数のエージェントロールを組み合わせ、ブログ記事生成を7段階のパイプラインで半自動化。エージェント間のデータ受け渡しをファイルベースにすることで、長尺タスクでもコンテキスト切れに強い設計を実現。並列実行（Agent Teams）と逐次実行（Task tool）の使い分け、承認フロー、AI臭検査など、実運用で得た知見を詳述。

- **ソース**: [Zenn claude](https://zenn.dev/rkpg/articles/claude-code-content-factory)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-05-08

### Claude Haiku 4.5 + n8n で問い合わせ対応ワークフローを作ったら、100% 精度・1 件 0.5 円で運用できた

Claude Haiku 4.5とn8nを組み合わせた問い合わせ対応自動化ワークフローの実装事例。4軸分類（カテゴリ・緊急度・感情・推奨回答期限）で100%の精度を達成し、1件あたり約0.5円で運用可能。緊急度別に3つのドラフト生成ルートを分離し、Slack通知まで自動化している。分類とドラフト生成を分離する設計により、各タスクの精度を維持しながらコスト効率を実現。

- **ソース**: [Zenn claude](https://zenn.dev/aiflowlab/articles/n8n-claude-haiku-inquiry-workflow)
- **重要度**: 7/10
- **タグ**: haiku, claude-api

---

## 2026-04-26

### Zenn自動公開パイプラインをclaude -pで構築した話

Zennの投稿制限に対処するため、claude -pで全記事を一括俯瞰レビューし、1日1件自動公開するcronパイプラインを構築。個別レビューではなく全記事を俯瞰することで、重複テーマの統合や記事分割などの全体最適を実現。制約を手動対処ではなく恒久的な仕組みで解決した事例。

- **ソース**: [Zenn claude](https://zenn.dev/saytooy_arch/articles/14-zenn-auto-publish-pipeline)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-26 | 自動生成 |
