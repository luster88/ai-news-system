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
date: '2026-04-26'
updated: '2026-05-23'
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
---



# Workflow Automation

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
