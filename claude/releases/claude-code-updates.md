---
title: Claude Code アップデート履歴
category: releases
subcategory: claude-code
tags:
- changelog
- claude-code
- release
- 新機能
date: 2026-03-23
updated: '2026-03-25'
sources:
- url: https://github.com/anthropics/claude-code/releases
  title: Claude Code GitHub Releases
  date: 2026-03-23
- url: https://code.claude.com/docs/en/changelog
  title: Claude Code Changelog
  date: 2026-03-23
- url: https://www.reddit.com/r/ClaudeAI/comments/1s2ok85/claude_code_now_has_auto_mode
  title: Claude Code now has auto mode
  date: '2026-03-25'
---


# Claude Code アップデート履歴

Claude Code の主要なリリース・機能追加を時系列で記録する。

---

## 2026年3月

### v2.1.81（2026-03-20）

- `--bare` フラグ追加: スクリプトからの呼び出し用に余分な出力を抑制
- `--channels` パーミッションリレー機能
- OAuth・ボイスモード・並行セッション処理のバグ修正

### 主な機能追加（2026年3月）

**ボイスモード（/voice）**
- Push-to-talk 方式: スペースバー長押しで発話、離すと送信
- 対応言語が 20 言語に拡大（3月に 10 言語追加）
- 全ユーザーに段階的にロールアウト中

**リカーリングタスク（/loop）**
- 定期実行プロンプト機能: `/loop 5m check the deploy` のような構文
- インターバルを指定して繰り返しタスクを実行可能

**拡張コンテキストウィンドウ**
- 1M トークンウィンドウが Max / Team / Enterprise プランで利用可能
- Opus 4.6 がデフォルトモデルに変更

**出力トークン上限の引き上げ**
- Claude Opus 4.6 のデフォルト最大出力トークン: 64K
- Opus 4.6 / Sonnet 4.6 の上限: 128K トークン

**VS Code プラン機能の改善**
- プランプレビューが Claude の反復作業中に自動更新されるように改善
- プランがレビュー可能になった段階でのみコメント機能を有効化
- リジェクト時にプレビューを開いたまま維持（Claude が修正可能に）

---

## 関連リンク

- [セットアップガイド](../guides/setup.md)
- [ツール比較](../tools/comparison.md)

---

## 2026-03-25

### Claude Code now has auto mode

Claude Code に自動モード（auto mode）が追加されました。ファイル書き込みやbashコマンドの実行時に、毎回承認する代わりに、Claudeが安全性を判断して自動的に処理を進めます。破壊的な操作は分類器が事前にチェックしてブロックし、安全な操作のみ自動実行されます。現在Team プランでリサーチプレビューとして利用可能で、Enterprise および API アクセスは数日以内に展開予定です。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s2ok85/claude_code_now_has_auto_mode)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, release

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-23 | 初版作成（2026年3月分まで記録） |
