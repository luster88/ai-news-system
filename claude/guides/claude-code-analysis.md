---
title: Claude Code Analysis
category: guides
subcategory: claude-code-analysis
tags:
- claude-code
- setup
- 新機能
date: '2026-08-24'
updated: '2026-10-07'
sources:
- url: https://zenn.dev/chiisanasoft/articles/08f0341f5565ff
  title: Claude Code のログでブランチ運用を数えたら、git_branch の "HEAD" が2つの意味を持っていた
  date: '2026-08-24'
- url: https://zenn.dev/tanashun/articles/claude-code-transcript-jsonl
  title: Claude Code の会話ログ（jsonl）を読んで「Claude が読んだファイル」を一覧にする
  date: '2026-10-07'
---


# Claude Code Analysis

---

## 2026-10-07

### Claude Code の会話ログ（jsonl）を読んで「Claude が読んだファイル」を一覧にする

Claude Code の会話ログ（jsonl形式）を解析し、Claudeが読み書きしたファイルを一覧化する方法を解説。jqコマンドを使った抽出方法、ログの構造（type、tool_use、結果の格納場所）、サブエージェントや圧縮による状態変化の扱い方を詳述。実際のログ追跡アプリ「tanacode」の実装例も紹介。

- **ソース**: [Zenn claude](https://zenn.dev/tanashun/articles/claude-code-transcript-jsonl)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-08-24

### Claude Code のログでブランチ運用を数えたら、git_branch の "HEAD" が2つの意味を持っていた

Claude Code の4か月分436セッションのログを分析し、名前付きブランチでの作業は12セッション（2.8%）のみだった。git_branch の "HEAD" は detached HEAD とリポジトリ外の2つの意味を持ち、198件のうち66件が detached HEAD、132件はリポジトリ外だった。集計には sessions とターン数の不一致、.git の判定方法、ログの自動削除など3つの注意点がある。

- **ソース**: [Zenn claude](https://zenn.dev/chiisanasoft/articles/08f0341f5565ff)
- **重要度**: 5/10
- **タグ**: claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-24 | 自動生成 |
