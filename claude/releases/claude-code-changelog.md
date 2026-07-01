---
title: Claude Code Changelog
category: releases
subcategory: claude-code-changelog
tags:
- claude-code
- release
- sonnet
- 新機能
date: '2026-06-29'
updated: '2026-07-01'
sources:
- url: https://qiita.com/moha0918_/items/8bd90fc2c1391c4769a1
  title: Claude Code v0.2.21〜v2.1.195｜CLIからマルチエージェント基盤への全履歴｜毎日Changelog解説
  date: '2026-06-29'
- url: https://qiita.com/moha0918_/items/8bd90fc2c1391c4769a1
  title: Claude Code v0.2.21〜v2.1.195｜CLIからマルチエージェント基盤への全履歴｜毎日Changelog解説
  date: '2026-06-29'
- url: https://qiita.com/moha0918_/items/6fac5264ef4c4497d188
  title: Claude Code v2.1.196〜v2.1.197｜Sonnet 5 がデフォルトに｜毎日Changelog解説
  date: '2026-06-30'
- url: https://qiita.com/moha0918_/items/181b45d5e97df7012263
  title: Claude Code v2.1.198｜背景エージェントがdraft PRまで自走｜毎日Changelog解説
  date: '2026-07-01'
---



# Claude Code Changelog

---

## 2026-07-01

### Claude Code v2.1.198｜背景エージェントがdraft PRまで自走｜毎日Changelog解説

Claude Code v2.1.198では、背景エージェントがworktree作業完了後に確認待ちで止まらず、commit・push・draft PR作成まで自動実行するようになった。agent_needs_input/agent_completedの通知フックが追加され、離席中の作業完了を検知可能に。ExploreエージェントがHaiku固定を廃止しメインセッションのモデルを継承、サブエージェントとコンパクションがextended thinking設定を引き継ぐようになり、出力品質が向上した。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/181b45d5e97df7012263)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, release

---

### Claude Code v2.1.198｜背景エージェントがdraft PRまで自走｜毎日Changelog解説

Claude Code v2.1.198で背景エージェントがworktreeでの作業完了後、commit・push・draft PR作成まで自動実行するようになった。agent_needs_input/agent_completedの通知フック追加により、離席中のエージェント状態を把握可能に。Exploreエージェントがメインセッションのモデルを継承し、サブエージェントとコンパクションがextended thinking設定を引き継ぐよう改善された。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/181b45d5e97df7012263)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

## 2026-06-30

### Claude Code v2.1.196〜v2.1.197｜Sonnet 5 がデフォルトに｜毎日Changelog解説

Claude Code v2.1.197でデフォルトモデルがClaude Sonnet 5に変更され、1Mトークンのコンテキスト窓と8/31までの$2/$10 per Mtokプロモ価格が利用可能に。v2.1.196では、コミット済み設定でのMCP自己承認の脆弱性修正、バックグラウンドジョブ復帰時の会話消失バグ修正、ストリーム監視のデフォルト有効化など、セキュリティと安定性の大幅な改善が実施された。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/6fac5264ef4c4497d188)
- **重要度**: 8/10
- **タグ**: claude-code, sonnet, release

---

## 2026-06-29

### Claude Code v0.2.21〜v2.1.195｜CLIからマルチエージェント基盤への全履歴｜毎日Changelog解説

Claude Codeの初期バージョンv0.2.21から最新v2.1.195までの全変更履歴を解説。単純なCLIツールからマルチエージェント基盤への進化を追跡し、Fable 5の一般公開、サブエージェントの5階層spawn、動的ワークフロー（数百エージェント編成）、プラグイン機構とSkills、Hooksなどの主要機能を網羅。PermissionルールやSandboxの修正履歴も詳述し、サブエージェントやバックグラウンド実行を業務活用する開発者向けに包括的な変遷をまとめている。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/8bd90fc2c1391c4769a1)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v0.2.21〜v2.1.195｜CLIからマルチエージェント基盤への全履歴｜毎日Changelog解説

Claude Codeの最初の公開v0.2.21から最新v2.1.195までの全履歴を振り返る記事。単純なCLI補助ツールから、サブエージェントの多階層spawn・バックグラウンド実行・数百エージェントの動的ワークフローを扱うマルチエージェント基盤へと進化した経緯を解説。Fable 5の一般公開(v2.1.170)が大きな節目となり、/rewindによるコード巻き戻し、/usageによるプラン消費確認、プラグイン機構、Hooks、permission修正など多岐にわたる機能追加が紹介されている。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/8bd90fc2c1391c4769a1)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-29 | 自動生成 |
