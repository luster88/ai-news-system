---
title: Claude Code Setup
category: guides
subcategory: claude-code-setup
tags:
- claude-code
- pricing
- prompt
- setup
- vscode
- windows
- 新機能
date: '2026-04-04'
updated: '2026-05-03'
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
- url: https://zenn.dev/linkedge/articles/27c38cdd9bedc6
  title: 【Claude Code】CLAUDE.md・skills・agents を整備して開発体験が劇的に変わった話
  date: '2026-04-29'
- url: https://qiita.com/manchan/items/63745b9198f1989c2a15
  title: Claude Codeを120%使いこなす設定3選【ECC・Memory.md・Obsidian連携】
  date: '2026-05-03'
- url: https://zenn.dev/yt8220/articles/f0465e79d0abd9
  title: Claude Codeの設定を育てた話 — permission・hooks・CLAUDE.md・subagentで「任せられる環境」を作る
  date: '2026-05-03'
---







# Claude Code Setup

---

## 2026-05-03

### Claude Codeを120%使いこなす設定3選【ECC・Memory.md・Obsidian連携】

Claude Codeを実務で活用するための3つの設定を解説。ECC（Everything Claude Code）で専門家エージェントを追加し、CLAUDE.md/Memory.mdでセッション間の文脈を保持し、Obsidian連携で調査内容を永続化する方法を、実際のコード例とともに紹介。フリーランスエンジニアがX投稿自動化・YouTube投稿パイプライン構築で実践した具体的なTipsを共有。

- **ソース**: [Qiita claude](https://qiita.com/manchan/items/63745b9198f1989c2a15)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

### Claude Codeの設定を育てた話 — permission・hooks・CLAUDE.md・subagentで「任せられる環境」を作る

Claude Codeの実運用で直面した課題（確認ダイアログ過多、テスト漏れ、コスト増）に対し、permission設計・hooks・CLAUDE.md・subagentの4つの仕組みを段階的に導入して解決した知見を紹介。安全性とスムーズな作業フローを両立させる設定育成の実践例。

- **ソース**: [Zenn claude](https://zenn.dev/yt8220/articles/f0465e79d0abd9)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-29

### 【Claude Code】CLAUDE.md・skills・agents を整備して開発体験が劇的に変わった話

Claude Code の開発体験を向上させるため、CLAUDE.md・skills・agents などのファイル・ディレクトリを整備した実践記事。プロジェクト環境や技術スタックを事前に定義することで、的外れな提案や毎回の説明が不要になり、開発効率が劇的に改善。新入社員のオンボーディングと同様、Claude Code にも「育成」が必要だという知見を共有している。

- **ソース**: [Zenn claude](https://zenn.dev/linkedge/articles/27c38cdd9bedc6)
- **重要度**: 7/10
- **タグ**: claude-code, setup, vscode

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
