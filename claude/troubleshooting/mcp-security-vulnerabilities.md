---
title: Mcp Security Vulnerabilities
category: troubleshooting
subcategory: mcp-security-vulnerabilities
tags:
- bugfix
- mcp
date: '2026-04-06'
updated: '2026-04-06'
sources:
- url: https://qiita.com/emi_ndk/items/c3b99612ec044e5d612e
  title: 【緊急警告】MCPサーバーが60日で30件のCVE！Azure脆弱性は「認証ゼロ」でCVSS 9.1
  date: '2026-04-06'
---

# Mcp Security Vulnerabilities

---

## 2026-04-06

### 【緊急警告】MCPサーバーが60日で30件のCVE！Azure脆弱性は「認証ゼロ」でCVSS 9.1

MCP（Model Context Protocol）に深刻なセキュリティ問題が大量発生。2026年1-2月の60日間で30件以上のCVEが報告され、Azure MCP ServerにはCVSS 9.1の認証なし脆弱性（CVE-2026-32211）が発見された。公式サーバーの4割近くが認証未実装で、APIキーや認証トークンの漏洩リスクがある。無料スキャンツール（npx mcp-scan）での即時確認が必要。

- **ソース**: [Qiita claude](https://qiita.com/emi_ndk/items/c3b99612ec044e5d612e)
- **重要度**: 9/10
- **タグ**: mcp, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-06 | 自動生成 |
