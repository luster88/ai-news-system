---
title: Claude Code Model Switching
category: troubleshooting
subcategory: claude-code-model-switching
tags:
- claude-code
- performance
- pricing
- setup
- 新機能
date: '2026-08-25'
updated: '2026-09-03'
sources:
- url: https://qiita.com/y104autumn/items/9fe3baf9fe7b7d313006
  title: Claude Code のモデル切替設定、実は思ってた仕様と違った
  date: '2026-08-25'
- url: https://qiita.com/syun136_616/items/96ce74dc54cfb63a7089
  title: Claude Codeのモデル切り替えで書き直しが急増する理由
  date: '2026-09-03'
---


# Claude Code Model Switching

---

## 2026-09-03

### Claude Codeのモデル切り替えで書き直しが急増する理由

Claude Codeでセッション中に/modelコマンドでモデルを切り替えると、キャッシュがモデルごとに分離されているため切り替え直後のターンで入力トークンが全量再計算される。通常はキャッシュ読み取りで約1割の単価に抑えられているが、切り替え直後はフル単価となり、長時間セッションでは処理量が数倍から数百倍に跳ね上がる可能性がある。対策としてフェーズの節目での切り替えやサブエージェントの活用が有効。

- **ソース**: [Qiita claudecode](https://qiita.com/syun136_616/items/96ce74dc54cfb63a7089)
- **重要度**: 7/10
- **タグ**: claude-code, performance, pricing

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
