---
title: Mcp Security Vulnerabilities
category: troubleshooting
subcategory: mcp-security-vulnerabilities
tags:
- bugfix
- claude-code
- mcp
- prompt
date: '2026-04-06'
updated: '2026-04-27'
sources:
- url: https://qiita.com/emi_ndk/items/c3b99612ec044e5d612e
  title: 【緊急警告】MCPサーバーが60日で30件のCVE！Azure脆弱性は「認証ゼロ」でCVSS 9.1
  date: '2026-04-06'
- url: https://qiita.com/kix/items/3bb2bdc5830cc1bd0a58
  title: WebSearch MCPのセキュリティリスクと対策 — allowlist/denylistによるドメイン制御
  date: '2026-04-27'
---


# Mcp Security Vulnerabilities

---

## 2026-04-27

### WebSearch MCPのセキュリティリスクと対策 — allowlist/denylistによるドメイン制御

WebSearch MCPは外部Webコンテンツを取得してLLMに渡すため、間接プロンプトインジェクションのリスクがある。Claude CodeのWebSearchツールはallowed_domains/blocked_domainsでドメイン制御が可能（同時指定不可）。Perplexity MCPはsearch_domain_filterで最大20ドメインを制御でき、mcp-filterプロキシを使えばツールレベルの制御も追加できる。allowlistによる「デフォルト全拒否、必要なものだけ許可」が最も安全な運用方法だが、コンテンツレベルの攻撃は完全には防げないため注意が必要。

- **ソース**: [Qiita claude](https://qiita.com/kix/items/3bb2bdc5830cc1bd0a58)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, prompt

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
