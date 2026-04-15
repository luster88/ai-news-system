---
title: Claude Code Agent Architecture
category: guides
subcategory: claude-code-agent-architecture
tags:
- claude-code
- performance
- 新機能
date: '2026-04-15'
updated: '2026-04-15'
sources:
- url: https://zenn.dev/chiakidayo/articles/agent-teams-subagent-comparison
  title: 【Claude Code】Agent teamsとSubagent並列実行比較メモ
  date: '2026-04-15'
---

# Claude Code Agent Architecture

---

## 2026-04-15

### 【Claude Code】Agent teamsとSubagent並列実行比較メモ

Claude Codeの2つのマルチエージェント機能を比較した記事。Subagent並列実行は独立したタスクをMain Agent主導で効率的に処理し、トークン消費が少ない。一方Agent teamsは各Agentが独立したインスタンスを持ち、エージェント間で直接やり取りしながら複雑なタスクを協働処理できるが、トークン消費は多い。タスクの独立性と協働の必要性に応じて使い分けることが推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/chiakidayo/articles/agent-teams-subagent-comparison)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-15 | 自動生成 |
