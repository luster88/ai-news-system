---
title: Mcp Oauth Integration
category: guides
subcategory: mcp-oauth-integration
tags:
- mcp
- setup
date: '2026-09-15'
updated: '2026-09-15'
sources:
- url: https://qiita.com/hirajo/items/c7217b125f1135266e54
  title: 自分のSaaSのMCPを、ChatGPTとclaude.aiからログインだけで繋がるようにした｜OAuth対応で踏んだ落とし穴
  date: '2026-09-15'
---

# Mcp Oauth Integration

---

## 2026-09-15

### 自分のSaaSのMCPを、ChatGPTとclaude.aiからログインだけで繋がるようにした｜OAuth対応で踏んだ落とし穴

SaaSにMCPサーバーのOAuth対応を実装し、ChatGPTとclaude.aiのチャット画面から利用可能にした事例。従来のAPIトークン方式はClaude Codeのみ対応で、チャット画面には使えなかった。@modelcontextprotocol/sdk 1.29.0を使い、Express製アプリにOAuthフローを追加。Dynamic Client Registration、PKCE、refresh tokenなど標準的なOAuthフローを実装し、CDN経由でのレート制限対応も行った。

- **ソース**: [Qiita claude](https://qiita.com/hirajo/items/c7217b125f1135266e54)
- **重要度**: 7/10
- **タグ**: mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-15 | 自動生成 |
