---
title: Multi Agent Patterns
category: guides
subcategory: multi-agent-patterns
tags:
- claude-code
- cowork
- haiku
- prompt
- sonnet
- 新機能
date: '2026-07-18'
updated: '2026-10-02'
sources:
- url: https://qiita.com/Koukyosyumei/items/d496148c5a68ae486de1
  title: '実装して理解するマルチエージェントのデザインパターン - ①: AgentCoder - コード実装とテスト設計の分離'
  date: '2026-07-18'
- url: https://zenn.dev/mskbhd/articles/lab-045-claude
  title: ClaudeにClaudeをレビューさせる連鎖は単発に勝つのか計測した
  date: '2026-10-02'
---


# Multi Agent Patterns

---

## 2026-10-02

### ClaudeにClaudeをレビューさせる連鎖は単発に勝つのか計測した

Claude Code開発者の「Claudeに別のClaudeをレビューさせる」手法を検証した実験記事。LeetCode hard級の5関数実装タスクで、単一プロンプトと3段階連鎖(coder→reviewer→fixer)を比較した結果、精度は同等だがコストは3.5倍に。同一モデルの自己批評は盲点を共有するため効果が薄く、「弱いモデル×連鎖」より「強いモデル×単発」が全軸で勝利した。

- **ソース**: [Zenn claude](https://zenn.dev/mskbhd/articles/lab-045-claude)
- **重要度**: 7/10
- **タグ**: sonnet, haiku, prompt

---

## 2026-07-18

### 実装して理解するマルチエージェントのデザインパターン - ①: AgentCoder - コード実装とテスト設計の分離

コロンビア大学の研究者が、Claude CodeとCodexを使用したマルチエージェントシステムの実装パターンを紹介。AgentCoderという手法では、コード実装担当のProgrammerエージェントとテスト設計担当のTest Designerエージェントを独立したサンドボックスで分離し、テスターが実装を見ないことで元のタスク要件に忠実なテストを作成する。h5i-python SDKを使用して、安全なエージェント間通信と監査可能なワークフローを実現している。

- **ソース**: [Qiita claudecode](https://qiita.com/Koukyosyumei/items/d496148c5a68ae486de1)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-18 | 自動生成 |
