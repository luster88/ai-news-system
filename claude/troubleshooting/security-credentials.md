---
title: Security Credentials
category: troubleshooting
subcategory: security-credentials
tags:
- bugfix
- claude-code
- setup
date: '2026-04-01'
updated: '2026-04-01'
sources:
- url: https://zenn.dev/miz_1123/articles/claude-code-subprocess-env-scrub
  title: Claude Codeを使うなら今すぐ設定すべき、認証情報漏洩対策の環境変数
  date: '2026-04-01'
---

# Security Credentials

---

## 2026-04-01

### Claude Codeを使うなら今すぐ設定すべき、認証情報漏洩対策の環境変数

Claude Code v2.1.83で追加されたCLAUDE_CODE_SUBPROCESS_ENV_SCRUB環境変数について実際に検証。この設定を1に設定すると、AWS/Azure/GCP等の認証情報がサブプロセス環境から削除され、プロンプトインジェクション攻撃による情報漏洩リスクを軽減できる。AWSのシークレットキーやGCPのサービスアカウント情報など、主要クラウドプロバイダーの認証情報が対象だが、CloudflareやOpenAIのトークンは対象外であることを確認。

- **ソース**: [Zenn claude](https://zenn.dev/miz_1123/articles/claude-code-subprocess-env-scrub)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-01 | 自動生成 |
