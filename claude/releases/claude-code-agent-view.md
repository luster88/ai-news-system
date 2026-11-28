---
title: Claude Code Agent View
category: releases
subcategory: claude-code-agent-view
tags:
- bugfix
- claude-code
- mcp
- release
- 新機能
date: '2026-05-12'
updated: '2026-11-28'
sources:
- url: https://ai-heartland.com/news/claude-code-agent-view-research-preview
  title: Claude Code agent view発表｜全セッション一覧で並列エージェントを統治する新UI
  date: '2026-05-12'
- url: https://qiita.com/picnic/items/97faa0dd4bf19819958a
  title: Claude Code v2.1.304 変更点まとめ：/auto-mode-setup・Code Review・mod仕様変更
  date: '2026-10-20'
- url: https://qiita.com/NaokiIshimura/items/9d75f973a26bdb4f1965
  title: Claude Code 開発者が注目している5つのアップデート（v2.1.331 - v2.1.332）
  date: '2026-11-28'
---



# Claude Code Agent View

---

## 2026-11-28

### Claude Code 開発者が注目している5つのアップデート（v2.1.331 - v2.1.332）

Claude Code v2.1.331-v2.1.332の主要アップデートを解説。MCPサーバー経由でのスキル配布とセキュリティフック、Bedrock/Agent Platform/FoundryでのSonnet 5.5への移行と環境変数変更、サードパーティプロバイダーでのCode Mode対応拡大と安定性改善が含まれる。特にMCPスキルのシェルコマンド実行リスクへの対処、リージョン設定の変更による意図しないデータ送信の防止、長時間スクリプトやリスト処理の不具合修正が実務上重要。

- **ソース**: [Qiita claudecode](https://qiita.com/NaokiIshimura/items/9d75f973a26bdb4f1965)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, release

---

## 2026-10-20

### Claude Code v2.1.304 変更点まとめ：/auto-mode-setup・Code Review・mod仕様変更

Claude Code v2.1.304 がリリースされ、/auto-mode-setup コマンドの追加、Code Review のレビューレベル選択機能、mod の settings.read フック仕様変更（Breaking Change）などが実装されました。特に mod 開発者や LLM ゲートウェイ利用者は、settings.read の入力形式変更への対応が必要です。また、claude --worktree でのコミット消失問題や、スキルのフック数上限設定など、安全性・安定性に関する重要な修正が含まれています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/97faa0dd4bf19819958a)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-05-12

### Claude Code agent view発表｜全セッション一覧で並列エージェントを統治する新UI

Anthropicが2026年5月11日に発表したClaude Code agent viewは、全セッションを一覧表示する新UIで、claude agentsコマンドで起動できる。これまで「ターミナル1枚=セッション1つ」だった前提を覆し、複数の並列エージェントを1画面で管理可能に。状態ごとにグルーピングされ、「ピーク」機能でトランスクリプトを開かずに進捗確認・返信ができる。Anthropicが進める「エージェント並列実行の足場」整備の一環。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/claude-code-agent-view-research-preview)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-12 | 自動生成 |
