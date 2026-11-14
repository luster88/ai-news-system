---
title: Chrome Extension Integration
category: tools
subcategory: chrome-extension-integration
tags:
- claude-api
- claude-console
- cowork
date: '2026-09-01'
updated: '2026-11-14'
sources:
- url: https://qiita.com/ynakayama/items/9584df2bd348e0c7ec11
  title: さくらの AI Engine 対応 Chrome 拡張 web-digest に OpenAI・Claude と日本語要約を追加した
  date: '2026-09-01'
- url: https://zenn.dev/recalm/articles/31c3b16f29aeb4
  title: Claudeの長い会話に目次を付けた話 — ThreadNavi v0.1.7、ジャンプ14秒→1〜3秒にした検証記録
  date: '2026-11-14'
---


# Chrome Extension Integration

---

## 2026-11-14

### Claudeの長い会話に目次を付けた話 — ThreadNavi v0.1.7、ジャンプ14秒→1〜3秒にした検証記録

Claude.aiの長い会話に目次機能を追加するChrome拡張「ThreadNavi」のv0.1.7リリース。先頭へのジャンプ速度を14秒から1〜3秒に短縮し、ジャンプアルゴリズムを「targeted化」して最適化。アウトライン表示、自動全件読み込み、会話内検索機能を実装し、データは全てローカル保存される。

- **ソース**: [Zenn claude](https://zenn.dev/recalm/articles/31c3b16f29aeb4)
- **重要度**: 5/10
- **タグ**: claude-console

---

## 2026-09-01

### さくらの AI Engine 対応 Chrome 拡張 web-digest に OpenAI・Claude と日本語要約を追加した

Chrome拡張機能web-digestのv1.1.0がリリースされ、さくらのAI Engineに加えてOpenAIとClaudeの要約APIに対応しました。provider-neutralな内部設計により、3社のネイティブAPIをadapterパターンで分離し、BYOKで利用者が認証情報を管理します。アプリケーション層では統一されたrequest/resultを使い、API固有の差異をadapter内に閉じ込める設計を採用しています。

- **ソース**: [Qiita claude](https://qiita.com/ynakayama/items/9584df2bd348e0c7ec11)
- **重要度**: 4/10
- **タグ**: claude-api, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-01 | 自動生成 |
