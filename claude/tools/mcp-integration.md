---
title: Mcp Integration
category: tools
subcategory: mcp-integration
tags:
- claude-code
- cowork
- cursor
- mcp
- 新機能
date: '2026-04-02'
updated: '2026-05-05'
sources:
- url: https://ai-heartland.com/news/cursor-firecrawl-mcp-aiagent
  title: Cursor × Firecrawl MCPで任意ウェブサイト複製が可能に。AIAgent強化
  date: '2026-04-02'
- url: https://qiita.com/trailfusion_ai/items/c8604bc73aac4b12d5c4
  title: AIに「回路設計して」と言うだけで動く電子回路ができる時代がきた — LTSpice × Claude Code を MCP で繋ぐ
  date: '2026-04-30'
- url: https://qiita.com/YushiYamamoto/items/7227a4be0a3a90cd3029
  title: n8n公式MCPが「実行」から「構築」へ：Claude/Codexからワークフローを直接作る時代が来た
  date: '2026-05-05'
---



# Mcp Integration

---

## 2026-05-05

### n8n公式MCPが「実行」から「構築」へ：Claude/Codexからワークフローを直接作る時代が来た

n8nの公式MCPサーバーが大幅アップデート。これまでの「実行」中心から、Claude/Codex等のAIクライアントからワークフローを直接作成・編集できる「構築」機能へ進化。TypeScript SDKベースでノード定義を参照しながら検証・修正を繰り返せるため、従来のJSON推測より実用的。2.18.4以上推奨でPublic Preview段階。Instance-level MCP serverとMCP Server Trigger nodeは別機能なので注意。

- **ソース**: [Qiita claudecode](https://qiita.com/YushiYamamoto/items/7227a4be0a3a90cd3029)
- **重要度**: 7/10
- **タグ**: mcp, claude-code

---

## 2026-04-30

### AIに「回路設計して」と言うだけで動く電子回路ができる時代がきた — LTSpice × Claude Code を MCP で繋ぐ

MCP（Model Context Protocol）を使って、LTSpiceとClaude Codeを連携させ、AI指示だけで電子回路の設計・シミュレーション・検証を自動実行できる実装事例。Claude Code、Codex CLI、GitHub Copilot、Cursorなど複数クライアントで同じMCPサーバーを使い回せる。従来のLLMが公式を返すだけだったのに対し、実際にツールを動かして検証済み数値を返す点が革新的。

- **ソース**: [Qiita claude](https://qiita.com/trailfusion_ai/items/c8604bc73aac4b12d5c4)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, cowork

---

## 2026-04-02

### Cursor × Firecrawl MCPで任意ウェブサイト複製が可能に。AIAgent強化

CursorがFirecrawl MCPサーバーを統合し、任意のウェブサイトからデータを抽出してAIが完全に理解できるようになった。JavaScriptレンダリングや複雑なレイアウトにも対応し、参考サイトを指定するだけでAIエージェントが自動的にコード生成から実装まで完結させる革新的なワークフローが実現。MCPプロトコルによるシームレスな連携により、Web開発の民主化とAI開発ツール市場の標準化が加速する見込み。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/cursor-firecrawl-mcp-aiagent)
- **重要度**: 7/10
- **タグ**: mcp, cursor, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
