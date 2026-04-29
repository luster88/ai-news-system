---
title: Workflow Engine Design
category: guides
subcategory: workflow-engine-design
tags:
- claude-code
- cowork
- 新機能
date: '2026-04-29'
updated: '2026-04-29'
sources:
- url: https://zenn.dev/zoetaka38/articles/b3fff02d511b73
  title: AI エージェントに「次の行動」を決めさせるとオペレーションが詰むので、ワークフローエンジンで step を固定した話
  date: '2026-04-29'
---

# Workflow Engine Design

---

## 2026-04-29

### AI エージェントに「次の行動」を決めさせるとオペレーションが詰むので、ワークフローエンジンで step を固定した話

AIエージェントに次の行動を決めさせるとオペレーションが不安定になる問題に対し、ワークフローをJSON定義の決定論的なステップマシンとして固定し、AIには各ステップの実行のみを担当させる設計を採用。VPS上でClaude Code CLIを実行し、状態管理はPostgresで厳密に制御、SSEでリアルタイム監視と途中介入が可能な仕組みを実装した事例。

- **ソース**: [Zenn claude](https://zenn.dev/zoetaka38/articles/b3fff02d511b73)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-29 | 自動生成 |
