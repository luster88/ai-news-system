---
title: Mcp Security Scan
category: troubleshooting
subcategory: mcp-security-scan
tags:
- bugfix
- mcp
- setup
date: '2026-07-15'
updated: '2026-07-15'
sources:
- url: https://ai-heartland.com/security/mcp-server-scan-ai-credentials
  title: 公開 MCP サーバが標的に｜AI 開発者を狙い撃つ走査を SANS ISC が観測
  date: '2026-07-15'
---

# Mcp Security Scan

---

## 2026-07-15

### 公開 MCP サーバが標的に｜AI 開発者を狙い撃つ走査を SANS ISC が観測

SANS ISCが2026年7月13日、公開されたMCPサーバとAI開発者の認証情報を狙う体系的な攻撃走査を14日間のログから検出。攻撃者は正規のJSON-RPC 2.0ハンドシェイクでMCPプロトコルを試行し、Claude・Cursor・VSCodeの設定ファイル（.claude/mcp.json等）を名指しで探索。未認証のLLMエンドポイントやクラウドメタデータSSRFも標的となり、MCP HTTPトランスポートを外部公開している開発者は早急な対策（認証必須化、IP制限、レート制限）が必要。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/mcp-server-scan-ai-credentials)
- **重要度**: 8/10
- **タグ**: mcp, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
