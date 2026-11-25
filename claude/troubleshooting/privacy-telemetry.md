---
title: Privacy Telemetry
category: troubleshooting
subcategory: privacy-telemetry
tags:
- setup
- 新機能
date: '2026-11-25'
updated: '2026-11-25'
sources:
- url: https://ai-heartland.com/tool/gemini-cli-telemetry
  title: Gemini CLI のテレメトリーとは｜送られる中身とメールアドレスの扱い、止め方を実測で確かめる
  date: '2026-11-25'
---

# Privacy Telemetry

---

## 2026-11-25

### Gemini CLI のテレメトリーとは｜送られる中身とメールアドレスの扱い、止め方を実測で確かめる

Google の Gemini CLI は初期設定で利用統計を Google に送信する。Google アカウントでログインしている場合はメールアドレスがそのまま送信されるが、API キー認証では端末ごとの UUID が使われる。プロンプト本文は送信されず、文字数やモデル名、OS 情報などのメタデータのみが送られる。テレメトリーの停止は ~/.gemini/settings.json で privacy.usageStatisticsEnabled を false に設定する必要があり、環境変数では制御できない。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/gemini-cli-telemetry)
- **重要度**: 4/10
- **タグ**: setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-25 | 自動生成 |
