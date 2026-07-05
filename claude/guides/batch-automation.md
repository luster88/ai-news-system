---
title: Batch Automation
category: guides
subcategory: batch-automation
tags:
- claude-api
- cowork
date: '2026-07-05'
updated: '2026-07-05'
sources:
- url: https://zenn.dev/yamachan_gogo/articles/07385c4ea7d9f8
  title: AWS Batch × Claude Code] YouTube動画 as Code
  date: '2026-07-05'
---

# Batch Automation

---

## 2026-07-05

### AWS Batch × Claude Code] YouTube動画 as Code

AWS BatchとClaude Codeを活用し、YouTubeの動画を完全自動生成するパイプラインの構築事例。毎週日曜にバッチ起動し、RSSからAWSアップデートを取得、Claude Code（claude-p）で台本生成、Remotionでレンダリング、音声合成・口パク合成まで全自動化。LLMの非決定性に対し、構造バリデーション・別モデルによるファクトチェック・自動修正ループの3段構えで品質を担保。Lambda制限回避のためBatchで16vCPU/32GB環境を利用し、定額サブスクで追加費用なしで運用。

- **ソース**: [Zenn claude](https://zenn.dev/yamachan_gogo/articles/07385c4ea7d9f8)
- **重要度**: 7/10
- **タグ**: claude-api, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-05 | 自動生成 |
