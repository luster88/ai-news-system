---
title: Subagent Design
category: guides
subcategory: subagent-design
tags:
- claude-code
- setup
- 新機能
date: '2026-06-13'
updated: '2026-06-13'
sources:
- url: https://qiita.com/kai_kou/items/618da2497af1c1bf0f91
  title: Claude Codeのネスト型サブエージェント入門 — 最大5階層の設計とトークン設計の勘所
  date: '2026-06-13'
---

# Subagent Design

---

## 2026-06-13

### Claude Codeのネスト型サブエージェント入門 — 最大5階層の設計とトークン設計の勘所

Claude Code v2.1.172で追加されたネスト型サブエージェント機能について、最大5階層まで再帰的に処理を委譲できる仕組みを解説。サブエージェントの定義方法（.claude/agents/配下にMarkdownファイルを配置し、YAMLフロントマターでname/description/tools/modelを宣言）と、階層が深くなるほどモデルを軽くするなどトークン設計の勘所を整理。木構造や再帰的探索タスクに適しており、/usageコマンドでコスト内訳を確認できる。

- **ソース**: [Qiita claudecode](https://qiita.com/kai_kou/items/618da2497af1c1bf0f91)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-13 | 自動生成 |
