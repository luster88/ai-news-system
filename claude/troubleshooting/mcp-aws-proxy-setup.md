---
title: Mcp Aws Proxy Setup
category: troubleshooting
subcategory: mcp-aws-proxy-setup
tags:
- claude-code
- mcp
- setup
date: '2026-05-29'
updated: '2026-05-29'
sources:
- url: https://zenn.dev/jins/articles/93791476756f87
  title: MFA と企業プロキシ環境で「No MCP servers configured / failed」を踏み抜いた話
  date: '2026-05-29'
---

# Mcp Aws Proxy Setup

---

## 2026-05-29

### MFA と企業プロキシ環境で「No MCP servers configured / failed」を踏み抜いた話

Claude Code 2.x で AWS MCP Server を企業プロキシ環境（SSL インスペクション、MFA 必須の AssumeRole 構成）で動作させる際のトラブルシューティング記事。「No MCP servers configured」エラーや「failed」状態の原因を --debug ログで特定し、.mcp.json と --mcp-config の組み合わせ、uvx のフルパス指定、source_profile の認証情報不足などを解決した実践的な手順をまとめている。

- **ソース**: [Zenn claude](https://zenn.dev/jins/articles/93791476756f87)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-29 | 自動生成 |
