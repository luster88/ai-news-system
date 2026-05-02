---
title: Claude Code Intro
category: guides
subcategory: claude-code-intro
tags:
- claude-code
- performance
- pricing
- prompt
- setup
- 新機能
date: '2026-03-27'
updated: '2026-05-02'
sources:
- url: https://zenn.dev/beeeegle/articles/a50b1cdbe4973c
  title: 【初心者向】Claude CodeってAIじゃないみたいよ
  date: '2026-03-27'
- url: https://qiita.com/hty1123445_a/items/514d864ec0484f323ea9
  title: Claude Code の設定はどう作る？：最小構成から始める改善ループ設計
  date: '2026-03-29'
- url: https://qiita.com/kevinsmith/items/7d4b5f48a2fd020615e8
  title: Claude Codeのよく使うコマンド
  date: '2026-03-30'
- url: https://qiita.com/yurukusa/items/d1ae79a0a6d6939a6666
  title: Anthropic公式「Claude Codeベストプラクティス」を700時間使った非エンジニアが読んで気づいた7つのこと
  date: '2026-04-01'
- url: https://qiita.com/moha0918_/items/c24338fd8eb19a8bcb2f
  title: 知らないと損する Claude Code のモデル設定 — 5つの実践的な設定テクニック
  date: '2026-04-05'
- url: https://qiita.com/kamome_susume/items/9cba600d9849c0bb4dd3
  title: 今からでも間に合う？Claude Codeの機能・用途・活用例をまとめて解説
  date: '2026-05-02'
---






# Claude Code Intro

---

## 2026-05-02

### 今からでも間に合う？Claude Codeの機能・用途・活用例をまとめて解説

Claude Codeは2025年2月リリースの自律型AIコーディングツールで、コード生成だけでなくファイル編集・デバッグ・テスト作成を自動実行できる。エージェント型アーキテクチャにより目標を伝えるだけで完了まで自律的に作業し、.clinerules設定ファイルやサブエージェント機能で開発効率を大幅に向上させる。Proプラン契約者は追加費用なしで利用可能。

- **ソース**: [Qiita claude](https://qiita.com/kamome_susume/items/9cba600d9849c0bb4dd3)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-04-05

### 知らないと損する Claude Code のモデル設定 — 5つの実践的な設定テクニック

Claude Code のモデル設定に関する実践的な5つのテクニックを解説。opusplan による自動モデル切り替え、effortLevel での思考深度調整、1M トークンコンテキストの有効化、チーム向けモデル固定設定、カスタムモデルオプションによる社内ゲートウェイ連携など、効率とコストを最適化する設定方法を紹介。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/c24338fd8eb19a8bcb2f)
- **重要度**: 7/10
- **タグ**: claude-code, setup, performance

---

### 知らないと損する Claude Code のモデル設定 — 5つの実践的な設定テクニック

Claude Code のモデル設定に関する5つの実践的なテクニックを紹介。opusplan による自動モデル切り替え、effortLevel での思考深度調整、1M トークンコンテキストの有効化、チームでのモデル完全固定方法、社内 LLM ゲートウェイのピッカー追加など、作業効率とコスト最適化のための設定方法を解説している。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/c24338fd8eb19a8bcb2f)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-01

### Anthropic公式「Claude Codeベストプラクティス」を700時間使った非エンジニアが読んで気づいた7つのこと

非エンジニアが700時間以上Claude Codeを使用した実体験をもとに、Anthropic公式ベストプラクティスを解説。コンテキストウィンドウの制約、テストの重要性、CLAUDE.mdの簡潔性、フックとCLAUDE.mdの使い分け、計画モードの活用など7つのポイントを実例とともに紹介している。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/d1ae79a0a6d6939a6666)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-03-30

### Claude Codeのよく使うコマンド

Claude Codeの基本的な起動パラメータ（--resume、--dangerously-skip-permissions等）と、対話中の/コマンド（/clear、/model、/btw、/fork等）を網羅的に解説。特に2026年3月追加の/btwコマンドはToken節約に有効で、メインタスクを中断せずサイド質問ができる。Shift+Tabによる隠れモード（Planモード、思考モード）も紹介。

- **ソース**: [Qiita claude](https://qiita.com/kevinsmith/items/7d4b5f48a2fd020615e8)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 2026-03-29

### Claude Code の設定はどう作る？：最小構成から始める改善ループ設計

Claude Code の設定は最初から作り込まず、実際の利用で発生した「摩擦」を観測しながら段階的に拡張する手法を解説。「観測 → 改善 → 反映」のループを回すことで、設定を自分の作業スタイルに適応させる。hooks を使った改善候補の抽出方法や、CLAUDE.md/skills の最小構成から始める設計思想を提示。

- **ソース**: [Qiita claude](https://qiita.com/hty1123445_a/items/514d864ec0484f323ea9)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-03-27

### 【初心者向】Claude CodeってAIじゃないみたいよ

Claude Codeは単なるLLMではなく、開発作業を支援するツールである点を初心者向けに解説。Claude 3.7 SonnetというLLMを搭載し、ファイル操作やコード生成を自動化できる。有料プラン（サブスク・API従量課金）とFreeプランがあり、有料版はCLIでローカルファイルにアクセス可能。無料版はブラウザベースでChatGPTに近い使用感。実質無料で効率化する方法として「Claude Code Router」の存在も言及されている。

- **ソース**: [Zenn claude](https://zenn.dev/beeeegle/articles/a50b1cdbe4973c)
- **重要度**: 5/10
- **タグ**: claude-code, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-27 | 自動生成 |
