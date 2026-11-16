---
title: Email Automation
category: guides
subcategory: email-automation
tags:
- claude-api
- cowork
- setup
date: '2026-11-16'
updated: '2026-11-16'
sources:
- url: https://zenn.dev/newsletterready/articles/deff1fbb8e7e34
  title: メルマガへの返信を AI に仕分けさせる：SES 受信から返信の下書きまで
  date: '2026-11-16'
---

# Email Automation

---

## 2026-11-16

### メルマガへの返信を AI に仕分けさせる：SES 受信から返信の下書きまで

メルマガ返信を自動仕分けするシステムの実装例。SESでメール受信→S3保存→SNS通知→Claudeで用件分類・返信下書き生成という流れ。引用除去や自動返信フィルタで前処理し、スキーマで出力を固定。配信停止は即座に処理するが、それ以外は人間の確認を経て送信。Next.jsのafter()で非同期処理し、キャッシュで効率化。

- **ソース**: [Zenn claude](https://zenn.dev/newsletterready/articles/deff1fbb8e7e34)
- **重要度**: 6/10
- **タグ**: claude-api, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-16 | 自動生成 |
