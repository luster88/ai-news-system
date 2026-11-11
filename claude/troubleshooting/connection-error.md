---
title: Connection Error
category: troubleshooting
subcategory: connection-error
tags:
- bugfix
- claude-code
- setup
date: '2026-11-11'
updated: '2026-11-11'
sources:
- url: https://qiita.com/homhom44/items/7bd1909c3d6d76d89676
  title: Claude Code で "Unable to connect to API (ECONNRESET)" / "The socket connection
    was closed unexpectedly" が出たときの切り分け（MTU・IPv6・VPN、Request timed out も）
  date: '2026-11-11'
---

# Connection Error

---

## 2026-11-11

### Claude Code で "Unable to connect to API (ECONNRESET)" / "The socket connection was closed unexpectedly" が出たときの切り分け（MTU・IPv6・VPN、Request timed out も）

Claude Codeで発生する接続エラー（ECONNRESET、socket connection closed）の切り分け方法を解説。公式対処法に加え、GitHubのissueで報告されているMTU設定変更、IPv6無効化、VPN切り替えなどの対処法を整理。PPPoE環境でのMTU問題、TLS 1.3ハンドシェイクでの耐量子鍵共有による切断など、技術的な原因も分析されている。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/7bd1909c3d6d76d89676)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-11 | 自動生成 |
