---
title: Mcp Aws Security
category: guides
subcategory: mcp-aws-security
tags:
- mcp
- setup
date: '2026-06-07'
updated: '2026-06-07'
sources:
- url: https://zenn.dev/masuda_masuo/articles/2026-06-07-aws-mcp-selection
  title: 便利だからといって、AWS API MCPを使っていないか？用途別サーバーの選び方と権限設計
  date: '2026-06-07'
---

# Mcp Aws Security

---

## 2026-06-07

### 便利だからといって、AWS API MCPを使っていないか？用途別サーバーの選び方と権限設計

AWS MCPサーバーの選択と権限設計について、セキュリティベストプラクティスの観点から解説。aws-api-mcp-serverは便利だが広範な権限が必要になりがちで、用途別サーバー（cloudwatch-mcp-server、aws-serverless-mcp-serverなど）を組み合わせる方が最小権限の原則に適合する。READ_OPERATIONS_ONLYモードやIAM Role制限、ワークディレクトリ設定などの実装例も紹介。

- **ソース**: [Zenn claude](https://zenn.dev/masuda_masuo/articles/2026-06-07-aws-mcp-selection)
- **重要度**: 7/10
- **タグ**: mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-07 | 自動生成 |
