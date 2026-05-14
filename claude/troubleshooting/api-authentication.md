---
title: Api Authentication
category: troubleshooting
subcategory: api-authentication
tags:
- claude-api
- claude-code
- pricing
date: '2026-05-14'
updated: '2026-05-14'
sources:
- url: https://zenn.dev/joemike/articles/claude-max-api-key-required-2026
  title: Claude MaxサブスクAnthropicのMessages APIは叩けない：別途APIキー必須、5分で解決
  date: '2026-05-14'
---

# Api Authentication

---

## 2026-05-14

### Claude MaxサブスクAnthropicのMessages APIは叩けない：別途APIキー必須、5分で解決

Claude MaxやProのサブスクリプションではAnthropicのMessages APIを直接叩けず、別途APIキーが必要。Claude CodeはOAuthトークンを内部利用しているが、anthropic.messages.create()を使う場合はANTHROPIC_API_KEYの設定が必須。2026年4月以降、OAuth経由の第三者ツールも公式ブロック。解決策として5ドルチャージしてAPIキーを.env.localに設定すれば利用可能。

- **ソース**: [Zenn claude](https://zenn.dev/joemike/articles/claude-max-api-key-required-2026)
- **重要度**: 7/10
- **タグ**: claude-api, claude-code, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-14 | 自動生成 |
