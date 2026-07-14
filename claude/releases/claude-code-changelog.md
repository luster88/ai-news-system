---
title: Claude Code Changelog
category: releases
subcategory: claude-code-changelog
tags:
- bugfix
- claude-code
- mcp
- performance
- release
- sonnet
- 新機能
date: '2026-06-29'
updated: '2026-07-14'
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
- url: https://qiita.com/picnic/items/333e17bf379a0e6a9952
  title: Claude Code v2.1.198：Claude in Chrome GAと自動PR作成のインパクト解説
  date: '2026-07-02'
- url: https://qiita.com/moha0918_/items/6fc5910d8bdf6343498b
  title: Claude Code v2.1.201｜Sonnet 5 が会話途中の system role をやめる｜毎日Changelog解説
  date: '2026-07-05'
- url: https://qiita.com/moha0918_/items/bcd8b890eb0f4c224365
  title: Claude Code v2.1.202〜v2.1.203｜バックグラウンドエージェント総ざらい修正｜毎日Changelog解説
  date: '2026-07-07'
- url: https://qiita.com/moha0918_/items/6b07151a020d40ff6657
  title: Claude Code v2.1.204〜v2.1.205｜自動モードの安全弁が増える｜毎日Changelog解説
  date: '2026-07-08'
- url: https://qiita.com/picnic/items/e6d330b7723ee647fdcd
  title: Claude Code v2.1.205まとめ：MCP名予約の破壊的変更と安全性強化
  date: '2026-07-09'
- url: https://qiita.com/moha0918_/items/719ee336cd64f9e78423
  title: Claude Code v2.1.206｜/doctor が CLAUDE.md を削れと言い出す｜毎日Changelog解説
  date: '2026-07-10'
- url: https://qiita.com/picnic/items/d1ac24b797423941d494
  title: Claude Code v2.1.207の破壊的変更まとめ：Auto mode既定化とプラグインのシェル対策
  date: '2026-07-11'
- url: https://qiita.com/moha0918_/items/7701fef6ec098243ba32
  title: Claude Code v2.1.208〜v2.1.209｜長時間セッションのメモリリーク一掃｜毎日Changelog解説
  date: '2026-07-14'
---












# Claude Code Changelog

---

## 2026-07-14

### Claude Code v2.1.208〜v2.1.209｜長時間セッションのメモリリーク一掃｜毎日Changelog解説

Claude Code v2.1.208では長時間セッションのメモリリークを修正し、ツール実行が最大7倍、transcriptサイズが最大79倍改善された。MCP stdeerの64MB制限、LSPドキュメントのLRU管理、file editキャッシュの16MB上限化など、複数のメモリ最適化が実施された。v2.1.209は背景セッションのダイアログ回帰を修正するhotfixリリース。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/7701fef6ec098243ba32)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, performance

---

### Claude Code v2.1.208〜v2.1.209｜長時間セッションのメモリリーク一掃｜毎日Changelog解説

Claude Code v2.1.208では長時間セッションで発生していた複数のメモリリークを修正し、ツール実行を最大7倍高速化、transcriptサイズを最大79倍削減しました。MCP stdioの stderr制限（64MB）、LSPドキュメントのLRU管理、file editキャッシュの制限など、メモリとパフォーマンスの最適化が中心です。v2.1.209は背景セッションでのダイアログ表示の回帰バグを修正するhotfixです。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/7701fef6ec098243ba32)
- **重要度**: 7/10
- **タグ**: claude-code, release, performance

---

## 2026-07-11

### Claude Code v2.1.207の破壊的変更まとめ：Auto mode既定化とプラグインのシェル対策

Claude Code v2.1.207では、Bedrock/Vertex/Foundry経由のデフォルトモデルがClaude Opus 4.8に変更され、Auto modeが既定で有効化されました。最も重要な破壊的変更として、プラグインのheadersHelperでシェル形式コマンド内での${user_config.*}展開がセキュリティ上の理由で禁止されました。また、.claude/settings.local.jsonとプロジェクトの.claude/settings.jsonの読み込み制限が強化され、既存の設定が無視される可能性があります。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/d1ac24b797423941d494)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-07-10

### Claude Code v2.1.206｜/doctor が CLAUDE.md を削れと言い出す｜毎日Changelog解説

Claude Code v2.1.206 では /doctor コマンドに CLAUDE.md の冗長な記述を削除する診断機能が追加されました。コードベースから読み取れる内容を自動検出し削除候補として提示します。また MCP のサーバーごとの request_timeout_ms 設定が正しく反映されるようになり、60秒で切れていた長時間処理が解消されました。/commit-push-pr は pushDefault リモートも自動許可し、EnterWorktree は管理外 worktree で確認を挟むようになりました。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/719ee336cd64f9e78423)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, bugfix

---

### Claude Code v2.1.206｜/doctor が CLAUDE.md を削れと言い出す｜毎日Changelog解説

Claude Code v2.1.206がリリースされ、/doctorコマンドにCLAUDE.mdの肥大化診断機能が追加されました。コードから読み取れる重複記述を削除候補として提案し、コンテキスト圧迫を防ぎます。またMCPのper-server request_timeout_ms設定が正しく反映されるようになり、60秒で打ち切られていた長時間ツール呼び出しが動作するようになりました。その他、/commit-push-prがpushDefaultリモートを自動許可、バックグラウンドエージェントの自己更新が即座に行われるなど、18件のバグ修正を含む改善が施されています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/719ee336cd64f9e78423)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, bugfix

---

## 2026-07-09

### Claude Code v2.1.205まとめ：MCP名予約の破壊的変更と安全性強化

Claude Code v2.1.205がリリースされ、MCPサーバー名「Claude Browser」「Claude Preview」の予約化という破壊的変更が実施されました。autoモードでのトランスクリプト改ざん防止や危険なコマンド実行前の確認など安全性が大幅に強化され、Windowsでのworktree削除時のデータ損失バグなど重大なバグが修正されました。自動更新のメモリ使用量も約400MB削減され、/doctorコマンドが診断だけでなく修復機能も持つように進化しています。

- **ソース**: [Qiita claudecode](https://qiita.com/picnic/items/e6d330b7723ee647fdcd)
- **重要度**: 8/10
- **タグ**: claude-code, mcp, bugfix

---

## 2026-07-08

### Claude Code v2.1.204〜v2.1.205｜自動モードの安全弁が増える｜毎日Changelog解説

Claude Code v2.1.205で自動モードの安全機能が強化されました。セッション記録の改ざん禁止、未解決変数へのrm -rf実行前確認、通知への「人間の承認なし」明記が追加され、バックグラウンドエージェントの安全性が向上。自動更新のメモリ使用量も約400MB削減され、/doctorコマンドが総合セットアップ点検機能に拡張されました。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/6b07151a020d40ff6657)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.204〜v2.1.205｜自動モードの安全弁が増える｜毎日Changelog解説

Claude Code v2.1.205で自動モード利用時の安全対策が大幅強化。セッション記録の改ざん禁止、未解決変数のrm -rf実行前確認、通知への「人間承認なし」明記が追加された。JSON Schema無効時の黙った挙動変更も修正され、--dangerously-skip-permissionsでの無人実行の安全性が向上。/doctorコマンドが総合セットアップ点検に進化し、自動更新のメモリ使用量も約400MB削減された。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/6b07151a020d40ff6657)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-07

### Claude Code v2.1.202〜v2.1.203｜バックグラウンドエージェント総ざらい修正｜毎日Changelog解説

Claude Code v2.1.202〜v2.1.203のリリース解説。バックグラウンドエージェントの安定性向上が中心で、ANTHROPIC_BASE_URL環境変数が無視されAPIキーが既定エンドポイントに送信される重大なバグを修正。macOSで起動・切替時に15〜20秒フリーズする問題（v2.1.196のリグレッション）も解消。サブエージェントの作業引き継ぎ、Dynamic workflow size設定の追加、スキル再読み込みの二重化修正など20件超の修正を実施。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/bcd8b890eb0f4c224365)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.202〜v2.1.203｜バックグラウンドエージェント総ざらい修正｜毎日Changelog解説

Claude Code v2.1.202〜v2.1.203のChangelog解説。バックグラウンドエージェント周りの安定化が中心で、ANTHROPIC_BASE_URLが無視されてAPIキーが既定エンドポイントに送信される重大なバグや、macOSで15〜20秒フリーズする問題（v2.1.196のリグレッション）が修正された。その他、サブエージェントの作業引き継ぎ、動的ワークフローサイズ設定の追加、スキル再読み込み時の二重化修正など20件超の改善を含む。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/bcd8b890eb0f4c224365)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, release

---

## 2026-07-05

### Claude Code v2.1.201｜Sonnet 5 が会話途中の system role をやめる｜毎日Changelog解説

Claude Code v2.1.201 で、Claude Sonnet 5 のセッションにおいて会話途中に system role で差し込んでいた harness reminder（TODO リスト、開いているファイル、ツール利用可否などのリマインダー）を通常のメッセージ列に変更。system role で渡すか user 側で渡すかでモデルの受け取り方が変わるため、Sonnet 5 向けにロール構成を調整した。対話利用では体感差はなく、セッションログを直接扱う開発者向けの変更。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/6fc5910d8bdf6343498b)
- **重要度**: 6/10
- **タグ**: claude-code, sonnet, release

---

## 2026-07-05

### Claude Code v2.1.201｜Sonnet 5 が会話途中の system role をやめる｜毎日Changelog解説

Claude Code v2.1.201 では、Claude Sonnet 5 のセッションにおいて、会話途中に system role で差し込んでいた harness reminder の挙動が変更された。リマインダー自体は残るが、system role ではなく通常のメッセージ列に載せる形に変更。対話利用では体感差はなく、セッションログを直接扱う開発者向けの調整となる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/6fc5910d8bdf6343498b)
- **重要度**: 6/10
- **タグ**: claude-code, sonnet, release

---

## 2026-07-02

### Claude Code v2.1.198：Claude in Chrome GAと自動PR作成のインパクト解説

Claude Code v2.1.198がリリースされ、Chrome拡張機能の一般提供開始とバックグラウンドエージェントの自律化が進みました。最も重要な変更は、エージェントが完了時に確認なしで自動的にcommit・push・ドラフトPR作成まで行うようになった点です。これはCI/CDやブランチ保護ルールを運用するチームに大きな影響を与える破壊的変更であり、/agentsウィザードの廃止と合わせて運用手順の見直しが必要です。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/333e17bf379a0e6a9952)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

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
