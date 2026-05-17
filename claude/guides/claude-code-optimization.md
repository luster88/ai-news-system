---
title: Claude Code Optimization
category: guides
subcategory: claude-code-optimization
tags:
- claude-code
- cowork
- mcp
- opus
- performance
- prompt
- sonnet
date: '2026-03-31'
updated: '2026-05-17'
sources:
- url: https://qiita.com/nishiken1118/items/6b16557fcabf784c861e
  title: 過去の session をほしい時に参照する方針で claude-mem のトークン消費を激減させた話
  date: '2026-03-31'
- url: https://qiita.com/masakazuimai/items/4952437e1e5d8c7a8803
  title: Claude CodeのAgent toolでサブエージェントのモデルを切り替えてトークンコストを下げる
  date: '2026-04-11'
- url: https://zenn.dev/northernlearner/articles/49c220b84f91ac
  title: AI駆動開発のための CLAUDE.md 設計パターン — 実運用で磨いた5つの型
  date: '2026-04-24'
- url: https://qiita.com/kkaattoo/items/e92e137f96545e9211cb
  title: Claude Code 使用量を節約する5つの工夫【公式ドキュメントまとめ】
  date: '2026-05-10'
- url: https://qiita.com/Tadashi_Kudo/items/524ca5cc51e6e4f74305
  title: 海外5M viewバズ投稿「Claudeレート制限回避Tips」——全部すでに実装してた話：CLAUDE.md駆動開発のすすめ
  date: '2026-05-17'
---





# Claude Code Optimization

---

## 2026-05-17

### 海外5M viewバズ投稿「Claudeレート制限回避Tips」——全部すでに実装してた話：CLAUDE.md駆動開発のすすめ

海外でバズった「Claudeレート制限回避Tips」は、CLAUDE.md駆動開発を実践していれば自動的に守られるルールだという実践報告。CLAUDE.mdはClaude Codeがプロジェクト文脈を把握するための設定ファイルで、モデルの使い分け、タスク分割、キャッシュ活用などを明示的にルール化できる。[I]（絶対ルール）と[G]（推奨指針）を区別し、フィードバックループで育てることで、コスト最適化とレート制限対策が自動化される。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/524ca5cc51e6e4f74305)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 2026-05-10

### Claude Code 使用量を節約する5つの工夫【公式ドキュメントまとめ】

Claude Code の使用量を節約するための実践的な工夫を公式ドキュメントをもとにまとめた記事。会話履歴のリセット（/clear、/compact）、モデルの使い分け（Sonnet/Opus）、ファイル参照の最適化、CLAUDE.md の整理、事前計画による無駄な生成の削減など、5つの具体的な節約テクニックを解説している。

- **ソース**: [Qiita claude](https://qiita.com/kkaattoo/items/e92e137f96545e9211cb)
- **重要度**: 6/10
- **タグ**: claude-code, sonnet, opus

---

## 2026-04-24

### AI駆動開発のための CLAUDE.md 設計パターン — 実運用で磨いた5つの型

Claude Code での実運用を通じて洗練された、CLAUDE.md ファイルの設計パターン5つを紹介。AI の思考プロセスと出力品質を制御するため、「戦略判断前の仮説引き出し」「提案の弱点自己検証」「セッションログの自動 git 記録」「時刻情報の再取得強制」「意思決定ログの主観優先記録」といった具体的なルールを CLAUDE.md に組み込む手法を解説。単なるスタイル指定ではなく、意思決定の順序とタスクフローの設計に焦点を当てている。

- **ソース**: [Zenn claude](https://zenn.dev/northernlearner/articles/49c220b84f91ac)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-11

### Claude CodeのAgent toolでサブエージェントのモデルを切り替えてトークンコストを下げる

Claude CodeのAgent toolでサブエージェントのモデルを切り替える方法を解説。メインセッションはOpusのまま、定型的なコード生成だけSonnetに委譲することでトークンコストを削減できる。ただしサブエージェントはコンテキストを共有しないため、プロンプトは自己完結が必須。委譲に向くのは「明確・大量・定型」の3条件が揃ったタスクのみで、迷ったらOpusに倒すのが安全。

- **ソース**: [Qiita claudecode](https://qiita.com/masakazuimai/items/4952437e1e5d8c7a8803)
- **重要度**: 7/10
- **タグ**: claude-code, opus, sonnet

---

## 2026-03-31

### 過去の session をほしい時に参照する方針で claude-mem のトークン消費を激減させた話

Claude Code の永続メモリツール claude-mem のトークン消費を削減する設定方法を解説。セッション開始時の自動注入を最小限に抑え（CONTEXT_OBSERVATIONS=1、FULL_COUNT=0等）、必要な情報は search と get_observations で都度取得する方針に変更。Read/Glob/Grep などのルーティン操作をスキップすることでノイズを削減し、検索精度も向上。デフォルト設定と比較して大幅なトークン削減を実現しつつ、過去情報へのアクセスは維持。

- **ソース**: [Qiita claude](https://qiita.com/nishiken1118/items/6b16557fcabf784c861e)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-31 | 自動生成 |
