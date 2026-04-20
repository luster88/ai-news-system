---
title: Claude Code Hooks
category: guides
subcategory: claude-code-hooks
tags:
- claude-code
- mac
- setup
- 新機能
date: '2026-03-23'
updated: '2026-04-20'
sources:
- url: https://qiita.com/pro-tein/items/49e5dbec705c3497dd51
  title: 【Claude Code】Hooks機能でデスクトップ通知を設定してみた
  date: '2026-03-23'
- url: https://qiita.com/Tadashi_Kudo/items/20cc213470c6a7576e44
  title: Claude Code のライフサイクルフック入門 — セッションの「前後」を自動化する
  date: '2026-04-20'
---


# Claude Code Hooks

---

## 2026-04-20

### Claude Code のライフサイクルフック入門 — セッションの「前後」を自動化する

Claude Code のライフサイクルフック機能を解説。セッション開始・ツール実行前後・コンパクト前後などのイベントに対してシェルコマンドやプロンプトを自動実行できる。危険コマンドのブロック、コンテキスト自動ロード、自動コミット、ユーザー入力の検証など実践的なユースケースを紹介。設定は ~/.claude/settings.json に記述し、matcher で対象ツールを絞り込める。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/20cc213470c6a7576e44)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-03-23

### 【Claude Code】Hooks機能でデスクトップ通知を設定してみた

Claude Code の Hooks 機能を使ってデスクトップ通知を設定する方法を解説。処理が止まった際の通知を自動化でき、PreToolUse/PostToolUse/Notification/Stop などのイベントタイプを活用できる。macOS環境で osascript や OSC 9 制御シーケンスを使った実装例を紹介し、Ghostty ターミナルからのネイティブ通知設定手順も含まれる。

- **ソース**: [Qiita claude](https://qiita.com/pro-tein/items/49e5dbec705c3497dd51)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-23 | 自動生成 |
