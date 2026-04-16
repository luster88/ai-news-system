---
title: Claude Code Setup
category: guides
subcategory: claude-code-setup
tags:
- claude-code
- pricing
- prompt
- setup
- windows
- 新機能
date: '2026-04-04'
updated: '2026-04-16'
sources:
- url: https://qiita.com/taiki_i/items/2d75a882e0f3187f6bb8
  title: あなたの CLAUDE.md、ちゃんと機能してますか？作り方から公式プラグインで採点するまでの道のり
  date: '2026-04-04'
- url: https://qiita.com/naokami/items/47b73c5d39bd5650d2b0
  title: AIエージェント向け指示書（CLAUDE.md / AGENTS.md）の書き方 — 「毎回読まれるファイル」だからこそ削るべきもの
  date: '2026-04-04'
- url: https://qiita.com/taiki_i/items/2d75a882e0f3187f6bb8
  title: あなたの CLAUDE.md、ちゃんと機能してますか？作り方から公式プラグインで採点するまでの道のり
  date: '2026-04-04'
- url: https://zenn.dev/miyan/articles/ai-driven-dev-claude-md-context
  title: AI駆動開発の実践（1）CLAUDE.mdとコンテキスト戦略 — AIに「現場」を伝える技術
  date: '2026-04-05'
- url: https://qiita.com/Geek-3340/items/974b02ac3b606a0569ed
  title: '【Claude Code 学習記録 #１】Claude Codeを使ってみた！'
  date: '2026-04-11'
- url: https://qiita.com/moha0918_/items/72d4d32fce1b585ddbad
  title: CLAUDE.mdを「とりあえず」で済ませてる人に知ってほしい、指示精度が上がる7つの書き方
  date: '2026-04-14'
- url: https://ai-heartland.com/explain/what-is-claude-code-2026
  title: Claude Codeとは？Anthropic公式AIツールの使い方・インストール・料金を完全解説【2026年版】
  date: '2026-04-16'
---





# Claude Code Setup

---

## 2026-04-16

### Claude Codeとは？Anthropic公式AIツールの使い方・インストール・料金を完全解説【2026年版】

Claude Codeは、Anthropic公式のターミナルベースAIコーディングツールで、自然言語でコード生成・編集・Git操作・テスト実行を一気通貫で実行できる。従来の補完ツールと異なり「AIとペアプログラミング」するアプローチを採用し、パーミッションシステムで安全性を確保。インストールはnpmで1コマンド、Claude Pro（$20/月）から利用可能で、CLAUDE.md・Hooks・Skillsなどの主要機能を備える。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/what-is-claude-code-2026)
- **重要度**: 6/10
- **タグ**: claude-code, setup, pricing

---

## 2026-04-14

### CLAUDE.mdを「とりあえず」で済ませてる人に知ってほしい、指示精度が上がる7つの書き方

Claude CodeのCLAUDE.mdファイルの効果的な書き方を7つ紹介。/initコマンドによる自動生成、@importによる外部ファイル取り込み、.claude/rules/ディレクトリでのパス指定ルール、CLAUDE.local.mdによる個人設定の分離など、コンテキスト管理とトークン効率化のベストプラクティスを解説。長すぎるCLAUDE.mdは指示遵守率を下げるため、ファイル分割が重要。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/72d4d32fce1b585ddbad)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 2026-04-11

### 【Claude Code 学習記録 #１】Claude Codeを使ってみた！

Claude Codeの概要、始め方、セットアップ手順を解説した初心者向けガイド。ターミナル上で動作するAIコーディングエージェントとして、コマンド実行やファイル操作を自然言語で指示できる点が特徴。有料プラン（Pro $20/月〜）が必要で、WSL上のCursorターミナルでのインストール手順を詳しく紹介している。

- **ソース**: [Qiita claudecode](https://qiita.com/Geek-3340/items/974b02ac3b606a0569ed)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 2026-04-05

### AI駆動開発の実践（1）CLAUDE.mdとコンテキスト戦略 — AIに「現場」を伝える技術

CLAUDE.mdの効果的な設計手法を解説。肥大化を避け、階層構造（グローバル/プロジェクト/ディレクトリ）を活用し、現場の暗黙知を必要最小限に言語化する方法を提示。200Kトークンのコンテキストウィンドウの2-3%に収め、@import機能やYAMLフロントマターでスコープを限定する実践的戦略を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/miyan/articles/ai-driven-dev-claude-md-context)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 2026-04-04

### あなたの CLAUDE.md、ちゃんと機能してますか？作り方から公式プラグインで採点するまでの道のり

Claude Code の CLAUDE.md ファイルの作成方法と活用法を解説。CLAUDE.md はプロジェクト固有のルールやコーディング規約を Claude に伝える説明書で、/init コマンドで自動生成できる。100行以内に抑えることが推奨され、公式プラグイン claude-md-improver を使って品質を採点・改善できる。

- **ソース**: [Qiita claude](https://qiita.com/taiki_i/items/2d75a882e0f3187f6bb8)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

### AIエージェント向け指示書（CLAUDE.md / AGENTS.md）の書き方 — 「毎回読まれるファイル」だからこそ削るべきもの

AIコーディングエージェント向けの指示書ファイル（AGENTS.md / CLAUDE.md）の書き方を解説。毎セッション読まれるため、コンテキスト消費を抑える「引き算思考」が重要。Anthropic推奨は60〜200行で、350行を超えるとパフォーマンス悪化。ビルドコマンド、コードから読み取れない制約（DLL競合など）、プロジェクト概要のみに絞り、設定ファイルで読める内容は除外すべき。

- **ソース**: [Qiita claudecode](https://qiita.com/naokami/items/47b73c5d39bd5650d2b0)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

### あなたの CLAUDE.md、ちゃんと機能してますか？作り方から公式プラグインで採点するまでの道のり

Claude Code における CLAUDE.md ファイルの作成方法と活用法を解説。CLAUDE.md はプロジェクトごとのルールや規約を Claude に伝える説明書で、/init コマンドで自動生成可能。100行以内に抑えることが推奨され、公式プラグイン claude-md-improver で品質を採点・改善できる。

- **ソース**: [Qiita claudecode](https://qiita.com/taiki_i/items/2d75a882e0f3187f6bb8)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-04 | 自動生成 |
