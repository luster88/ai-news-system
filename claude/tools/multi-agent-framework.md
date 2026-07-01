---
title: Multi Agent Framework
category: tools
subcategory: multi-agent-framework
tags:
- claude-code
- copilot
- cowork
- cursor
- mcp
- prompt
- 新機能
date: '2026-04-04'
updated: '2026-07-01'
sources:
- url: https://ai-heartland.com/explain/claude-code-open-multi-agent
  title: Claude Codeのソースコード漏洩から生まれた軽量マルチエージェントOSS「open-multi-agent」
  date: '2026-04-04'
- url: https://ai-heartland.com/tool/addyosmani-agent-skills-framework
  title: Addy Osmani agent-skills徹底解剖｜AIエージェントの言い訳を封じる20スキル7コマンド
  date: '2026-05-09'
- url: https://ai-heartland.com/agent/agent-native-framework
  title: Agent-Native徹底解説：AIエージェントを一級ユーザーにするBuilder.ioのアプリ基盤
  date: '2026-07-01'
---



# Multi Agent Framework

---

## 2026-07-01

### Agent-Native徹底解説：AIエージェントを一級ユーザーにするBuilder.ioのアプリ基盤

Builder.ioが公開したAgent-Nativeフレームワークは、AIエージェントを後付けチャットではなく一級のユーザーとして扱うオープンソースのアプリケーション基盤です。1つのActionを定義するだけでUI・API・MCP・CLIなど全インターフェースから同じ処理を呼べ、UIとAIの状態二重管理の問題を解決します。TypeScript製・MITライセンスで、エージェントと人間ユーザーを対等に扱う設計思想が特徴です。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/agent-native-framework)
- **重要度**: 6/10
- **タグ**: mcp, cowork, 新機能

---

## 2026-05-09

### Addy Osmani agent-skills徹底解剖｜AIエージェントの言い訳を封じる20スキル7コマンド

GoogleのChrome DX責任者Addy Osmani氏が開発した「agent-skills」は、AIコーディングエージェントが最短ルートを優先して重要な工程を省略する問題を解決するフレームワークです。20のスキル、7つのスラッシュコマンド、反論テーブルで構成され、Claude Code、Cursor、Copilot等の主要ツールに対応しています。GitHub Starは35,000超を達成し、シニアエンジニアの暗黙知を明文化してエージェントに強制する仕組みを提供します。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/addyosmani-agent-skills-framework)
- **重要度**: 7/10
- **タグ**: claude-code, cursor, copilot

---

## 2026-04-04

### Claude Codeのソースコード漏洩から生まれた軽量マルチエージェントOSS「open-multi-agent」

2026年3月のClaude Codeソースコード漏洩事件を契機に、元Anthropicプロダクトマネージャーが独自設計したTypeScript製マルチエージェントフレームワーク「open-multi-agent」が公開された。公式SDKとは異なり完全インプロセス実行でサーバーレス対応し、DAGベースのタスクスケジューラでエージェント間の依存関係を自動解決する。Claude、GPT、Copilot、Ollamaなどあらゆるモデルに対応し、型安全なJSON出力とトレーシング機能を標準搭載している。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-open-multi-agent)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-04 | 自動生成 |
