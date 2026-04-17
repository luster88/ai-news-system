---
title: Agent Development
category: guides
subcategory: agent-development
tags:
- claude-api
- cowork
- prompt
- setup
date: '2026-03-31'
updated: '2026-04-17'
sources:
- url: https://zenn.dev/dysksh/articles/27617be34cc336
  title: フレームワークを使わずにLLMエージェントを作る — Go + Claude API + AWSの設計と実装
  date: '2026-03-31'
- url: https://qiita.com/bit-tanghao/items/e9512d1b26fc7f1caf63
  title: 【AIエージェント 第一弾】ReActエージェント入門 ── フレームワーク不使用でコードレビュアー・エージェントを作る
  date: '2026-04-17'
---


# Agent Development

---

## 2026-04-17

### 【AIエージェント 第一弾】ReActエージェント入門 ── フレームワーク不使用でコードレビュアー・エージェントを作る

LangChainなどのフレームワークを使わず、Anthropic Python SDKだけでReActパターンのAIエージェントを実装する技術解説。read_code、think、commentの3ツールを持つコードレビューエージェントを構築し、バグ検出を実演。messagesの積み重ねによる状態管理とツール実行フローを詳細に解説している。

- **ソース**: [Qiita claude](https://qiita.com/bit-tanghao/items/e9512d1b26fc7f1caf63)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 2026-03-31

### フレームワークを使わずにLLMエージェントを作る — Go + Claude API + AWSの設計と実装

Discordから自然言語でタスクを投げるとClaudeがコードを生成してGitHub PRを作成するエージェント「Nemuri」の設計と実装解説。LangChain等のフレームワークを使わず、Go + Claude API + AWSサーバーレスで構築。2フェーズエージェントループ（情報収集→成果物生成）でトークンコストを最適化し、常時起動インフラなしで実現。

- **ソース**: [Zenn claude](https://zenn.dev/dysksh/articles/27617be34cc336)
- **重要度**: 7/10
- **タグ**: claude-api, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-31 | 自動生成 |
