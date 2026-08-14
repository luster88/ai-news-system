---
title: Security Sandbox
category: troubleshooting
subcategory: security-sandbox
tags:
- bugfix
- claude-code
- setup
date: '2026-08-14'
updated: '2026-08-14'
sources:
- url: https://ai-heartland.com/security/claude-code-security-guide
  title: Claude Code セキュリティ｜サンドボックスの守備範囲と公開アドバイザリで見る攻撃面・確認コマンド
  date: '2026-08-14'
---

# Security Sandbox

---

## 2026-08-14

### Claude Code セキュリティ｜サンドボックスの守備範囲と公開アドバイザリで見る攻撃面・確認コマンド

Claude Codeのセキュリティについて、公開された30件のGitHub Security Advisoryを分析した技術記事。サンドボックスの実際の守備範囲は「Bashツールのみ」で、Read/Write/EditやMCPサーバーは対象外。既定値はfail-open（起動失敗時は警告を出して非サンドボックスで実行）であり、脆弱性の多くは「サンドボックス脱出」ではなく「承認・信頼境界の回避」に集中している。権限・信頼・サンドボックスの3層防御は直列構造であり、上流が破られれば下流も無効化される点を指摘。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/claude-code-security-guide)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-14 | 自動生成 |
