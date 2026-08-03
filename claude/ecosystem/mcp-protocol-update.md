---
title: Mcp Protocol Update
category: ecosystem
subcategory: mcp-protocol-update
tags:
- mcp
- performance
- 新機能
date: '2026-07-30'
updated: '2026-08-03'
sources:
- url: https://zenn.dev/wack205/articles/1325e311a7e707
  title: MCPの新仕様は、デザイナーの道具箱をどう変えるか
  date: '2026-07-30'
- url: https://qiita.com/vcmacky/items/0ff1fd7e7990305677a3
  title: MCPが「ステートレス」になった日 — 2026-07-28仕様を、金融系フルスタックエンジニアの視点で読み解く
  date: '2026-08-03'
---


# Mcp Protocol Update

---

## 2026-08-03

### MCPが「ステートレス」になった日 — 2026-07-28仕様を、金融系フルスタックエンジニアの視点で読み解く

MCP（Model Context Protocol）の新仕様 2026-07-28 により、プロトコルが双方向ステートフルからリクエスト/レスポンスのステートレスへ大きく変更された。initialize/initializedハンドシェイクとMcp-Session-Idヘッダが廃止され、各リクエストが_metaフィールドで必要な情報を携行する形に。金融系エンジニアの視点から、この変更がロードバランシング、スケーラビリティ、サーバーレス対応にもたらす実務上の影響を詳細に解説。

- **ソース**: [Qiita claude](https://qiita.com/vcmacky/items/0ff1fd7e7990305677a3)
- **重要度**: 8/10
- **タグ**: mcp, 新機能, performance

---

## 2026-07-30

### MCPの新仕様は、デザイナーの道具箱をどう変えるか

2026年7月のModel Context Protocol新仕様リビジョンにより、デザインワークフローに大きな影響が発生。HTTP+SSEトランスポートが非推奨化され、セッション管理が廃止されステートレスモデルへ移行。FigmaのローカルMCPサーバーでは接続エラーが構造的に解消される一方、コードからのデザイン生成など長時間処理はTasks APIへの移行が必要となる。

- **ソース**: [Zenn claude](https://zenn.dev/wack205/articles/1325e311a7e707)
- **重要度**: 8/10
- **タグ**: mcp, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-30 | 自動生成 |
