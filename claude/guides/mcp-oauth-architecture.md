---
title: Mcp Oauth Architecture
category: guides
subcategory: mcp-oauth-architecture
tags:
- claude-api
- mcp
- setup
date: '2026-09-07'
updated: '2026-09-07'
sources:
- url: https://zenn.dev/butanokakuni/articles/2935140061b696
  title: 自宅ObsidianをClaude.aiから安全に読み書きする認証アーキテクチャを設計した話
  date: '2026-09-07'
---

# Mcp Oauth Architecture

---

## 2026-09-07

### 自宅ObsidianをClaude.aiから安全に読み書きする認証アーキテクチャを設計した話

自宅サーバー上のObsidian VaultにClaude.aiから安全にアクセスするため、OAuth 2.1 + PKCEとDCRを満たす認証アーキテクチャを設計。Cloudflare AccessやKeycloak/Zitadelを検討し、http-oauth-mcp-serverをゲートウェイとして既存mcpvaultと組み合わせる方式を計画したが、モバイルアプリでtools/callが送信されない既知バグにより実装を断念した経緯をまとめた記事。

- **ソース**: [Zenn claude](https://zenn.dev/butanokakuni/articles/2935140061b696)
- **重要度**: 6/10
- **タグ**: mcp, setup, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-07 | 自動生成 |
