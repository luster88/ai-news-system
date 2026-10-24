---
title: Mcp Custom Server
category: tools
subcategory: mcp-custom-server
tags:
- claude-api
- cowork
- mcp
date: '2026-10-24'
updated: '2026-10-24'
sources:
- url: https://zenn.dev/kitchy/articles/890a8f821869de
  title: Google Drive の旅行動画を、自作 MCP で Claude に vlog へ編集させる
  date: '2026-10-24'
---

# Mcp Custom Server

---

## 2026-10-24

### Google Drive の旅行動画を、自作 MCP で Claude に vlog へ編集させる

Google Driveの旅行動画をClaudeに自動でvlog編集させる仕組みの実装例。自作MCPサーバーをCloud Runに配置し、claude.aiのカスタムコネクタから利用。ffmpeg操作、Google Drive連携、Veo/Lyria等の生成APIをMCP化し、Googleログイン認証で保護。動画はCloud Storageで管理し、Claudeは静止画抽出で内容を確認しながら編集手順を実行する。

- **ソース**: [Zenn claude](https://zenn.dev/kitchy/articles/890a8f821869de)
- **重要度**: 6/10
- **タグ**: mcp, claude-api, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-24 | 自動生成 |
