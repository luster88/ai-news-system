---
title: Mcp Server Setup
category: guides
subcategory: mcp-server-setup
tags:
- claude-code
- linux
- mcp
- prompt
- setup
date: '2026-04-30'
updated: '2026-06-23'
sources:
- url: https://zenn.dev/syyama/articles/a6d92f250f5793
  title: 【AlmaLinux】MCP Server を構築してみた
  date: '2026-04-30'
- url: https://qiita.com/asahide/items/860979ed23305aa4003b
  title: OCI DB Tools MCP の3タイプをカスタムロールで権限分離してみた
  date: '2026-05-29'
- url: https://zenn.dev/ray000/articles/momonga-search-mcp-setup
  title: 【初心者向け】Momonga Search MCP を Claude / Codex で使えるようにしよう！
  date: '2026-06-23'
---



# Mcp Server Setup

---

## 2026-06-23

### 【初心者向け】Momonga Search MCP を Claude / Codex で使えるようにしよう！

Momonga Search MCP サーバーを Claude Desktop / Claude Code / Codex で使うための初心者向けセットアップガイド。uv のインストールからリポジトリ取得、API キー設定までを順に解説。企業資料・経済ニュースを効率的に検索・取得し、必要な箇所だけを切り出してエージェントに渡すことで、コンテキストの無駄遣いを防ぎ性能向上を図る設計が特徴。stdio / ローカル実行スタイルで動作する。

- **ソース**: [Zenn claude](https://zenn.dev/ray000/articles/momonga-search-mcp-setup)
- **重要度**: 6/10
- **タグ**: mcp, setup, claude-code

---

## 2026-05-29

### OCI DB Tools MCP の3タイプをカスタムロールで権限分離してみた

OCI Database Tools MCPにおいて、カスタムアプリケーションロール（MCP_Analyst）を作成し、3種類のツールセット（組込みSQL/Custom SQL Tool/Reporting Tool）のうちReporting Toolのみを業務ユーザーに公開する権限分離を実機検証。ツールを絞ることでClaudeの選択挙動が改善し、試行錯誤が減少して正直な応答が得られた。ただし、ツール側とSQLレポート本体側の2層でロール許可が必要な点が落とし穴として指摘されている。

- **ソース**: [Qiita claude](https://qiita.com/asahide/items/860979ed23305aa4003b)
- **重要度**: 6/10
- **タグ**: mcp, setup, prompt

---

## 2026-04-30

### 【AlmaLinux】MCP Server を構築してみた

Windows上のClaude DesktopからVirtualBox内のAlmaLinuxサーバにMCP（Model Context Protocol）サーバを構築する手順を解説。Python 3.11のインストール、OpenWeatherMap APIを使った天気情報取得サーバの実装、Claude Desktop側の設定方法までを網羅。ネットワーク設定はブリッジアダプターを推奨し、claude_desktop_config.jsonでリモートMCPサーバを登録する具体的な手順を提示している。

- **ソース**: [Zenn claude](https://zenn.dev/syyama/articles/a6d92f250f5793)
- **重要度**: 6/10
- **タグ**: mcp, setup, linux

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-30 | 自動生成 |
