---
title: Token Usage Analysis
category: troubleshooting
subcategory: token-usage-analysis
tags:
- claude-code
- claude-console
- performance
- pricing
- prompt
date: '2026-06-07'
updated: '2026-08-11'
sources:
- url: https://qiita.com/yurukusa/items/5d49ed7d798c9650fe16
  title: Claude Codeの週次の利用枠が「軽い作業」で1日で枯れる本当の理由——消費の99%はコードではなく文脈の再読み込みだった
  date: '2026-06-07'
- url: https://www.reddit.com/r/ClaudeAI/comments/1vgcf89/claude_overusing_my_tokens
  title: Claude overusing my tokens
  date: '2026-08-05'
- url: https://zenn.dev/honeymarron/articles/claude-code-context-diet
  title: 「おはよう」1回 = 5時間制限の7%！？ — 挨拶3トークンの裏で送られる数万トークンの話
  date: '2026-08-11'
---



# Token Usage Analysis

---

## 2026-08-11

### 「おはよう」1回 = 5時間制限の7%！？ — 挨拶3トークンの裏で送られる数万トークンの話

Claude Codeで「おはよう」と挨拶しただけで5時間枠の7%が消費される現象を解説。原因はCLAUDE.md、メモリ索引、skill/プラグイン説明など数万トークンのベースラインコンテキストが毎ターン送信されるため。特にキャッシュ切れ後の最初のリクエストは高コスト。対策として/contextコマンドでカテゴリ別消費を測定し、メモリ・CLAUDE.md・skill説明などの常時ロード分を削減する手順を紹介。見た目のファイルサイズと実際のトークン消費は一致せず、MCP遅延ロードなど測定が重要。

- **ソース**: [Zenn claude](https://zenn.dev/honeymarron/articles/claude-code-context-diet)
- **重要度**: 7/10
- **タグ**: claude-code, performance, prompt

---

## 2026-08-05

### Claude overusing my tokens

Claude が不必要に長い回答を生成し、トークンを過剰消費しているという報告。ユーザーは簡潔なテキスト回答のみを要求したにもかかわらず、Claude がリクエストを無視し、1通のメール作成だけでトークンを使い切ってしまうと不満を述べている。有料プランへの誘導を疑っており、対策として複数アカウントを使用している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vgcf89/claude_overusing_my_tokens)
- **重要度**: 4/10
- **タグ**: claude-console, pricing, prompt

---

## 2026-06-07

### Claude Codeの週次の利用枠が「軽い作業」で1日で枯れる本当の理由——消費の99%はコードではなく文脈の再読み込みだった

Claude Codeの週次利用枠が1日で枯渇する原因を、実際のログデータから分析した記事。ユーザーの99%のトークン消費が「コード生成」ではなく「文脈の再読み込み（cache_read）」によるものだと実データで示し、ログ解析スクリプトとブラウザベースの分析ツール（Token Drain Analyzer）を提供。対策として、/clearコマンドの活用、作業フォルダの絞り込み、巨大ファイルの除外などを提案している。

- **ソース**: [Qiita claude](https://qiita.com/yurukusa/items/5d49ed7d798c9650fe16)
- **重要度**: 7/10
- **タグ**: claude-code, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-07 | 自動生成 |
