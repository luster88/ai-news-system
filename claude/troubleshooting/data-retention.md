---
title: Data Retention
category: troubleshooting
subcategory: data-retention
tags:
- bugfix
- claude-code
- setup
date: '2026-08-17'
updated: '2026-08-17'
sources:
- url: https://zenn.dev/kentaro_tak/articles/claude-code-logs-vanish-30-days
  title: Claude Codeの会話ログは既定30日で消える。私の6月は5セッションしか残っていなかった
  date: '2026-08-17'
---

# Data Retention

---

## 2026-08-17

### Claude Codeの会話ログは既定30日で消える。私の6月は5セッションしか残っていなかった

Claude Codeの会話ログは既定で30日後に自動削除される仕様により、ユーザーが6月の作業記録のほとんどを失った事例。cleanupPeriodDaysの設定変更と、生ログのミラーリング＋軽量インデックス化による対策を実施。assistant側の応答を統計量に畳み、user promptのみ全文保存することで、データサイズを0.5%（200分の1）に圧縮する手法を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/kentaro_tak/articles/claude-code-logs-vanish-30-days)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-17 | 自動生成 |
