---
title: Mcp Servers
category: tools
subcategory: mcp-servers
tags:
- claude-code
- claude-console
- cowork
- mcp
- 新機能
date: '2026-04-21'
updated: '2026-05-16'
sources:
- url: https://zenn.dev/megaphone_tokyo/articles/9c0cffdf9e176b
  title: Claude Code / Desktop の記憶 OSS「KIOKU」に PDF / URL 取り込みを実装した
  date: '2026-04-21'
- url: https://ai-heartland.com/mcp/sv-excel-agent
  title: sv-excel-agent解説｜LLMがExcelを直接編集するMCPサーバ＋AIエージェント
  date: '2026-05-10'
- url: https://ai-heartland.com/agent/archify-claude-skill-architecture-diagram
  title: Archify徹底解説：Claude Skillで5種類の技術図を一発生成する自己完結HTML
  date: '2026-05-16'
---



# Mcp Servers

---

## 2026-05-16

### Archify徹底解説：Claude Skillで5種類の技術図を一発生成する自己完結HTML

ArchifyはClaude Skillとして配布される技術図生成ツールで、自然言語から5種類の図（アーキテクチャ、ワークフロー、シーケンス、データフロー、ライフサイクル）を単一HTMLで生成する。Cocoon-AIのarchitecture-diagram-generatorのfork rewriteバージョンで、深色/浅色テーマ切替、4倍解像度PNG出力、SVG自動配色対応などの拡張機能を持つ。Claude Skillの仕組みを活用し、ユーザーは図の構文を学ぶ必要なく自然言語で説明するだけでプロ品質の図を生成できる。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/archify-claude-skill-architecture-diagram)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-05-10

### sv-excel-agent解説｜LLMがExcelを直接編集するMCPサーバ＋AIエージェント

sv-excel-agentは、LLMがExcelファイルを直接編集できるMCPサーバとエージェントランナーのセット。約30のMCPツールでExcel操作をカバーし、fastmcpで実装されている。SpreadsheetBenchの検証50題でモデル別ベンチマーク結果を公開しており、Claude DesktopやCursorなど既存MCPクライアントから即座に接続可能。WebデモとSlackボット実装も含む4点セット構成。

- **ソース**: [AI Heartland](https://ai-heartland.com/mcp/sv-excel-agent)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, cowork

---

## 2026-04-21

### Claude Code / Desktop の記憶 OSS「KIOKU」に PDF / URL 取り込みを実装した

Claude Code/Desktop の記憶 OSS「KIOKU」に PDF と URL の取り込み機能を実装。kioku_ingest_pdf と kioku_ingest_url の 2 つの MCP ツールを追加し、会話の流れで「この PDF 読んで」「この URL の記事をまとめて」と自然に頼めるようになった。raw-sources パイプラインに乗せる設計により冪等性を担保し、既存の自動要約機能との統合を実現。

- **ソース**: [Zenn claude](https://zenn.dev/megaphone_tokyo/articles/9c0cffdf9e176b)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, claude-console

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-21 | 自動生成 |
