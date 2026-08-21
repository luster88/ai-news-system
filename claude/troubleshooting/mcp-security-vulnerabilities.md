---
title: Mcp Security Vulnerabilities
category: troubleshooting
subcategory: mcp-security-vulnerabilities
tags:
- bugfix
- claude-code
- cursor
- mcp
- performance
- prompt
date: '2026-04-06'
updated: '2026-08-21'
sources:
- url: https://qiita.com/emi_ndk/items/c3b99612ec044e5d612e
  title: 【緊急警告】MCPサーバーが60日で30件のCVE！Azure脆弱性は「認証ゼロ」でCVSS 9.1
  date: '2026-04-06'
- url: https://qiita.com/kix/items/3bb2bdc5830cc1bd0a58
  title: WebSearch MCPのセキュリティリスクと対策 — allowlist/denylistによるドメイン制御
  date: '2026-04-27'
- url: https://zenn.dev/ju571n/articles/ai-agent-config-attack-surface
  title: AIコーディングエージェントの本当の攻撃面は設定ファイルだった
  date: '2026-05-23'
- url: https://ai-heartland.com/security/nginx-ui-mcp-rce-vulnerability-chain
  title: nginx-ui 脆弱性 CVE-2026-33032｜MCP機能起点の認証バイパスから半年で25件超のRCE連鎖
  date: '2026-08-16'
- url: https://qiita.com/shinji_bank/items/d374470edf72431d986a
  title: 自作MCPサーバで「Tool Poisoning」を試す（Claude Codeを騙してみた）
  date: '2026-08-21'
---





# Mcp Security Vulnerabilities

---

## 2026-08-21

### 自作MCPサーバで「Tool Poisoning」を試す（Claude Codeを騙してみた）

MCPサーバの説明文（description）を実装と異なる内容に偽装し、Claude Codeがどう反応するか検証した記事。delete_memoの説明文だけ変更した場合は矛盾を検知したが、関数名もview_memo_detailに偽装すると実行されてしまい、Tool Poisoning攻撃が成立することを実証。MCPのセキュリティリスクを具体的に示した実験報告。

- **ソース**: [Qiita claudecode](https://qiita.com/shinji_bank/items/d374470edf72431d986a)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, bugfix

---

## 2026-08-16

### nginx-ui 脆弱性 CVE-2026-33032｜MCP機能起点の認証バイパスから半年で25件超のRCE連鎖

nginx-ui の MCP 機能に起因する脆弱性 CVE-2026-33032（CVSS 9.8）が発見され、半年間で25件超のセキュリティアドバイザリが連鎖的に公開された。MCP インターフェースの認証バイパス・検証漏れが主因で、AI エージェント連携機能の実装不備がサーバー全体のセキュリティリスクとなった事例。最新版への更新だけでは対処できないケースもあり、手動でのシークレットローテーションが必要な環境が存在する。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/nginx-ui-mcp-rce-vulnerability-chain)
- **重要度**: 8/10
- **タグ**: mcp, bugfix, performance

---

## 2026-05-23

### AIコーディングエージェントの本当の攻撃面は設定ファイルだった

AIコーディングエージェントの最大のセキュリティリスクはモデルの暴走ではなく設定ファイルの脆弱性。TrustFall や AWS Kiro の事例では、悪意ある設定ファイルやプロンプトインジェクションによる設定書き換えでRCEが成立。対策として設定ファイル監視ツール Sigil（AI-SPM エージェント）を開発し、危険な設定変更を検知・記録する。

- **ソース**: [Zenn claude](https://zenn.dev/ju571n/articles/ai-agent-config-attack-surface)
- **重要度**: 8/10
- **タグ**: claude-code, cursor, mcp

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
