---
title: Mcp Debugging
category: tools
subcategory: mcp-debugging
tags:
- claude-code
- mcp
- setup
date: '2026-07-13'
updated: '2026-07-13'
sources:
- url: https://ai-heartland.com/explain/mcpsnoop-mcp-wireshark
  title: MCPデバッグの通信を可視化するmcpsnoop｜MCP版Wiresharkでtool callを覗く
  date: '2026-07-13'
---

# Mcp Debugging

---

## 2026-07-13

### MCPデバッグの通信を可視化するmcpsnoop｜MCP版Wiresharkでtool callを覗く

mcpsnoopは、MCPサーバーとクライアント間のJSON-RPC通信を可視化するデバッグツール。通常は見えないtool callの実行内容、引数、レスポンス、所要時間をターミナルでリアルタイム表示する。Go製のシングルバイナリで、透過プロキシとして実運用中の通信をそのまま捕捉できる点が特徴。公式Inspectorがテスト呼び出しを発行するのに対し、mcpsnoopは実際の通信を観測する「MCP版Wireshark」として機能する。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/mcpsnoop-mcp-wireshark)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-13 | 自動生成 |
