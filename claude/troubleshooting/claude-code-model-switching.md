---
title: Claude Code Model Switching
category: troubleshooting
subcategory: claude-code-model-switching
tags:
- claude-code
- setup
- 新機能
date: '2026-08-25'
updated: '2026-08-25'
sources:
- url: https://qiita.com/y104autumn/items/9fe3baf9fe7b7d313006
  title: Claude Code のモデル切替設定、実は思ってた仕様と違った
  date: '2026-08-25'
---

# Claude Code Model Switching

---

## 2026-08-25

### Claude Code のモデル切替設定、実は思ってた仕様と違った

Claude Code の fallbackModel 設定は、サーバー混雑時だけでなく、安全分類器がセキュリティやバイオロジー関連コンテンツを検知した際にも自動的にモデルを切り替える。この切り替えはセッション開始時にリポジトリの内容や CLAUDE.md だけで発動する可能性があり、ユーザーが意図しない状況でも起こり得る。自動切り替えを停止するには switchModelsOnFlag 設定を明示的にオフにする必要がある。

- **ソース**: [Qiita claudecode](https://qiita.com/y104autumn/items/9fe3baf9fe7b7d313006)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-25 | 自動生成 |
