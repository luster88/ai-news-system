---
title: Mcp Architecture
category: guides
subcategory: mcp-architecture
tags:
- mcp
- prompt
- setup
date: '2026-05-31'
updated: '2026-10-16'
sources:
- url: https://qiita.com/jjking/items/4c0825aad6fdd1a84a80
  title: MCP Appsの基本構造：Resources・Prompts・Toolsの役割分担からマルチエージェント、Smitheryへの展望
  date: '2026-05-31'
- url: https://zenn.dev/jpopendata/articles/665d94c946cb5d
  title: MCPの本質と5つの役割分担：1,016万件の公的データをAIに直結して見えた最大のブルーオーシャン
  date: '2026-10-16'
---


# Mcp Architecture

---

## 2026-10-16

### MCPの本質と5つの役割分担：1,016万件の公的データをAIに直結して見えた最大のブルーオーシャン

MCPの本質を「AIに外部ツールやデータを接続する共通規格」として解説し、155種類・1,016万件の公的データを統合したMCPサーバー開発事例を紹介。AI実装を5つの役割（脳・台帳・道具・マニュアル・窓口）に分離する設計思想と、データ提供型・状態記録型・アクション型の3つのMCPパターンを提示し、個人開発におけるMCPの可能性を示す。

- **ソース**: [Zenn claude](https://zenn.dev/jpopendata/articles/665d94c946cb5d)
- **重要度**: 7/10
- **タグ**: mcp, setup

---

## 2026-05-31

### MCP Appsの基本構造：Resources・Prompts・Toolsの役割分担からマルチエージェント、Smitheryへの展望

Anthropic社が提唱したMCP（Model Context Protocol）の基本構造と設計思想を解説。Resources（読み取り専用データ）、Prompts（指示テンプレート）、Tools（副作用を伴う関数）の3つの抽象概念による関心の分離を詳述し、FastMCPを用いた実装例を提示。さらにマルチエージェント連携の展望とパッケージ管理ツールSmitheryの重要性に言及。

- **ソース**: [Qiita claude](https://qiita.com/jjking/items/4c0825aad6fdd1a84a80)
- **重要度**: 7/10
- **タグ**: mcp, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-31 | 自動生成 |
