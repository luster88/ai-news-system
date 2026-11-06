---
title: Ssl Proxy Certificate
category: troubleshooting
subcategory: ssl-proxy-certificate
tags:
- bugfix
- claude-code
- setup
date: '2026-11-06'
updated: '2026-11-06'
sources:
- url: https://qiita.com/homhom44/items/922d0458086bf4df7d0d
  title: Claude Code で "Self-signed certificate detected" / "SSL certificate verification
    failed" が出たときの直し方（社内プロキシと NODE_EXTRA_CA_CERTS）
  date: '2026-11-06'
---

# Ssl Proxy Certificate

---

## 2026-11-06

### Claude Code で "Self-signed certificate detected" / "SSL certificate verification failed" が出たときの直し方（社内プロキシと NODE_EXTRA_CA_CERTS）

Claude Code で「Self-signed certificate detected」や「SSL certificate verification failed」エラーが出る問題の解決方法を解説。社内プロキシがTLS検査で自己証明書を差し替えている場合、NODE_EXTRA_CA_CERTS環境変数に社内CAの証明書パスを指定することで解決できる。NODE_TLS_REJECT_UNAUTHORIZED=0による検証無効化は公式非推奨。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/922d0458086bf4df7d0d)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-06 | 自動生成 |
