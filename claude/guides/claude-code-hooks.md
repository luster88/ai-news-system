---
title: Claude Code Hooks
category: guides
subcategory: claude-code-hooks
tags:
- claude-code
- mac
- prompt
- setup
- 新機能
date: '2026-03-23'
updated: '2026-06-04'
sources:
- url: https://qiita.com/pro-tein/items/49e5dbec705c3497dd51
  title: 【Claude Code】Hooks機能でデスクトップ通知を設定してみた
  date: '2026-03-23'
- url: https://qiita.com/Tadashi_Kudo/items/20cc213470c6a7576e44
  title: Claude Code のライフサイクルフック入門 — セッションの「前後」を自動化する
  date: '2026-04-20'
- url: https://qiita.com/Tadashi_Kudo/items/b4dae51eee76198cc509
  title: Claude Code ハーネスを「月次スキャン＋spec.md」で自己改善させる——type:"prompt" Hook の誤検知を GPT-5.4
    が発見した話
  date: '2026-05-16'
- url: https://qiita.com/satoshi_061/items/c3a20d437a55e59068c4
  title: Claude Code hooks 活用まとめ — 安全性・ログ・作業時間を全自動化する
  date: '2026-06-04'
---




# Claude Code Hooks

---

## 2026-06-04

### Claude Code hooks 活用まとめ — 安全性・ログ・作業時間を全自動化する

Claude Code の hooks 機能を活用した実用的な設定例を紹介。PreToolUse フックで rm -rf などの危険コマンドを自動ブロック、全ツール実行のログ記録、タスク完了時の作業時間自動計測を実装。hooks はトークンをほぼ消費せず、非同期実行なら完全にゼロコストで安全性とログ管理を自動化できる。

- **ソース**: [Qiita claude](https://qiita.com/satoshi_061/items/c3a20d437a55e59068c4)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-16

### Claude Code ハーネスを「月次スキャン＋spec.md」で自己改善させる——type:"prompt" Hook の誤検知を GPT-5.4 が発見した話

Claude Code の hooks 機能で type:"prompt" フックが誤検知する問題を、月次スキャンと spec.md による自己改善フローで解決した事例。deploy という単語を含む無関係なプロンプトにも反応する問題を GPT-5.4 のコードレビューで発見し、matcher を具体的なコマンド名に分割することで改善。フックと並行して変更意図を spec.md で管理し、30日ごとに設定ファイルと仕様書の乖離を検出する継続的改善の仕組みを紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/b4dae51eee76198cc509)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

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
