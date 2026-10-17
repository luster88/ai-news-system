---
title: Multi Agent System
category: guides
subcategory: multi-agent-system
tags:
- claude-code
- cowork
- mcp
date: '2026-10-13'
updated: '2026-10-17'
sources:
- url: https://qiita.com/sescore/items/1d2743916da65a40d4e3
  title: OpenClawで9体のAIエージェント経営OSを作った話｜設定と権限設計を全公開
  date: '2026-10-13'
- url: https://qiita.com/sescore/items/cf57317fffda0ceb88af
  title: OpenClawで9体のAIエージェント経営OSを構築した実践記録｜設定とSES市場分析への活用法
  date: '2026-10-17'
---


# Multi Agent System

---

## 2026-10-17

### OpenClawで9体のAIエージェント経営OSを構築した実践記録｜設定とSES市場分析への活用法

Claude Codeのサブエージェント機能とcron/PM2を組み合わせ、9体のAIエージェントによる経営OS「OpenClaw」を構築した実践記録。市場データ分析、契約書レビュー、セキュリティ監視など役割ごとにエージェントを定義し、SES市場分析やフリーランス案件探索に活用。エージェントは.claude/agents/*.mdで1ファイル1責務として管理し、cronとPM2で常時稼働させる運用レイヤーを実装。

- **ソース**: [Qiita claude](https://qiita.com/sescore/items/cf57317fffda0ceb88af)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-10-13

### OpenClawで9体のAIエージェント経営OSを作った話｜設定と権限設計を全公開

SESエンジニアが Claude Code 上に9体のAIエージェントを構築し、経営の意思決定補助・財務管理・タスク管理などを自動化した実践事例。.claude/agents/*.md でサブエージェントを定義し、役職ごとに異なるモデルとツール権限を割り当てる設計を採用。セキュリティ面では最小権限の原則に基づき、各エージェントに必要最低限のツール（WebSearch、Bash、Edit等）のみを許可している。

- **ソース**: [Qiita claude](https://qiita.com/sescore/items/1d2743916da65a40d4e3)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-13 | 自動生成 |
