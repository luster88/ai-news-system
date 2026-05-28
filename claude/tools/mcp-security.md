---
title: Mcp Security
category: tools
subcategory: mcp-security
tags:
- claude-code
- mcp
- setup
- 新機能
date: '2026-05-28'
updated: '2026-05-28'
sources:
- url: https://zenn.dev/masuda_masuo/articles/2026-05-28-mcp-launcher
  title: MCPのクレデンシャルをconfigから追い出す：OSキーストアで一元管理するmcp-launcher
  date: '2026-05-28'
- url: https://qiita.com/Ju571nK/items/5b6a3f05e7e7de20e3ee
  title: AIコーディングエージェントを見張るOSSを、Claudeから『危険な設定どれ?』と聞けるようにした（MCP対応）
  date: '2026-05-28'
---

# Mcp Security

---

## 2026-05-28

### MCPのクレデンシャルをconfigから追い出す：OSキーストアで一元管理するmcp-launcher

MCPサーバーのクレデンシャル（PAT等）をconfigファイルから分離し、OSキーストア（macOS Keychain、Windows Credential Manager等）で一元管理するツール「mcp-launcher」の紹介。平文保存のリスク、設定の分散、更新コスト、config編集ミスといった課題を、既存のOS機能を活用して解決する実装が示されている。

- **ソース**: [Zenn claude](https://zenn.dev/masuda_masuo/articles/2026-05-28-mcp-launcher)
- **重要度**: 7/10
- **タグ**: mcp, setup, 新機能

---

### AIコーディングエージェントを見張るOSSを、Claudeから『危険な設定どれ?』と聞けるようにした（MCP対応）

AIコーディングエージェントの設定ファイルを監視するOSS「Sigil」にMCP対応機能が追加されました。v0.2.0では、sigil-mcpサーバーがフリート全体のセキュリティ状態を読み取り専用APIとして公開し、ClaudeからMCP経由で「どの設定が危険か」を日本語で問い合わせできるようになりました。AIを監視するツールをAIから問い合わせるという独特な構成で、ブロックはせず採点・記録に徹する設計です。

- **ソース**: [Qiita claudecode](https://qiita.com/Ju571nK/items/5b6a3f05e7e7de20e3ee)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-28 | 自動生成 |
