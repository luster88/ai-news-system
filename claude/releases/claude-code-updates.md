---
title: Claude Code アップデート履歴
category: releases
subcategory: claude-code
tags:
- bugfix
- changelog
- claude-code
- cowork
- mac
- release
- 新機能
date: 2026-03-23
updated: '2026-04-26'
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
- url: https://www.reddit.com/r/ClaudeAI/comments/1s7wkky/computer_use_is_now_in_claude_code
  title: Computer use is now in Claude Code.
  date: '2026-03-30'
- url: https://zenn.dev/joemike/articles/claude-code-computer-use-20260403
  title: Claude CodeのComputer Useって何ができるの？CLIからPC操作を自動化する新機能を解説
  date: '2026-04-03'
- url: https://www.reddit.com/r/ClaudeAI/comments/1se1kpr/claude_code_v2192_introduces_ultraplan_draft
  title: Claude Code v2.1.92 introduces Ultraplan — draft plans in the cloud, review
    in your browser, execute anywhere
  date: '2026-04-06'
- url: https://qiita.com/moha0918_/items/1d5e804cd3bd172b398a
  title: 今日のClaude Code v2.1.94 リリース｜毎日Changelog解説
  date: '2026-04-07'
- url: https://qiita.com/moha0918_/items/112149866223f8b5f6a0
  title: 今日のClaude Code v2.1.97 リリース｜毎日Changelog解説
  date: '2026-04-08'
- url: https://qiita.com/moha0918_/items/2733a8fbd2c7c3861b47
  title: 今日のClaude Code v2.1.108 リリース｜毎日Changelog解説
  date: '2026-04-14'
- url: https://ai-heartland.com/explain/claude-code-2-1-108-guide
  title: Claude Code v2.1.108徹底解説｜/recap・Skill経由スラコマ・プロンプトキャッシュ1時間TTLで何が変わるか
  date: '2026-04-14'
- url: https://qiita.com/moha0918_/items/54918006b98ea36880cc
  title: Claude Code v2.1.120 リリース｜毎日Changelog解説
  date: '2026-04-26'
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

## 2026-04-26

### Claude Code v2.1.120 リリース｜毎日Changelog解説

Claude Code v2.1.120 がリリースされました。主な更新は /config 設定の永続化、GitLab/Bitbucket/GitHub Enterprise の PR レビュー対応、Hooks への duration_ms 追加によるツール実行時間の計測、Plugin の自動更新、MCP サーバー再構成の並列化など。業務運用における利便性と計測機能が大幅に向上しています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/54918006b98ea36880cc)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.120 リリース｜毎日Changelog解説

Claude Code v2.1.120がリリースされました。主な更新は/config設定の永続化（~/.claude/settings.jsonへの保存）、GitLab/Bitbucket/GitHub EnterpriseのPRレビュー対応、Hooksへのduration_ms追加によるツール実行時間の計測、Plugin自動更新の改善などです。業務運用を効率化する機能強化と、多数のバグ修正が含まれています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/54918006b98ea36880cc)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-04-14

### 今日のClaude Code v2.1.108 リリース｜毎日Changelog解説

Claude Code v2.1.108がリリースされました。セッション復帰時に作業内容を自動要約するRecap機能、プロンプトキャッシュTTLの環境変数制御、スラッシュコマンドのモデル自動発見などが追加されました。新機能2つ、改善5つ、バグ修正14件を含む、日常的な使い勝手向上に重点を置いたアップデートです。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/2733a8fbd2c7c3861b47)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.108徹底解説｜/recap・Skill経由スラコマ・プロンプトキャッシュ1時間TTLで何が変わるか

Claude Code v2.1.108では、/recapによるセッション復帰の自動化、Skill経由でのスラッシュコマンド自動呼び出し、プロンプトキャッシュ1時間TTLの3つの機能が追加された。長時間エージェント運用における「文脈の喪失」「ツール呼び出しの手間」「APIコスト」という課題に対処する実用的なアップデートだが、DISABLE_TELEMETRY環境下での制約や要約精度の限界など、導入時の注意点も存在する。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-2-1-108-guide)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-04-08

### 今日のClaude Code v2.1.97 リリース｜毎日Changelog解説

Claude Code v2.1.97では、--dangerously-skip-permissionsフラグのサイレントダウングレード問題を修正し、CI/CD環境での安定性が向上。NO_FLICKERモードにCtrl+Oでフォーカスビューへの切り替え機能を追加し、プロンプト・ツール要約・最終応答のみを表示可能に。APIレート制限時の429リトライが指数バックオフで適切に分散され、長時間タスクの安定性が改善。Bashツールのパーミッションチェックを強化し、環境変数プレフィックスやネットワークリダイレクト周りの誤プロンプト表示を削減。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/112149866223f8b5f6a0)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### 今日のClaude Code v2.1.97 リリース｜毎日Changelog解説

Claude Code v2.1.97 では、--dangerously-skip-permissions フラグのサイレントダウングレード問題を修正し、CI/CD 環境での一貫性が向上しました。NO_FLICKER モードに Ctrl+O でフォーカスビューに切り替える機能が追加され、プロンプト・ツール要約・最終応答のみを表示可能になりました。API レート制限時の 429 リトライロジックが改善され、指数バックオフが適切に適用されるようになり、長時間タスクの安定性が向上しました。Bash ツールのパーミッションチェックが強化され、環境変数やネットワークリダイレクト周りの誤プロンプト表示が削減されました。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/112149866223f8b5f6a0)
- **重要度**: 6/10
- **タグ**: claude-code, release, bugfix

---

## 2026-04-07

### 今日のClaude Code v2.1.94 リリース｜毎日Changelog解説

Claude Code v2.1.94では、API・Bedrock・Team・Enterpriseユーザーのデフォルトeffortレベルがhighに引き上げられ、設定変更なしで高品質な応答が得られるようになった。Amazon Bedrock Mantle対応が環境変数で可能になり、Slack MCPのUI改善やレートリミット時のフリーズ、macOSログイン失敗など多数のバグが修正された。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/1d5e804cd3bd172b398a)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### 今日のClaude Code v2.1.94 リリース｜毎日Changelog解説

Claude Code v2.1.94がリリースされ、API・Bedrock・Team・Enterpriseユーザーのデフォルトeffortレベルが「high」に格上げされました。これにより設定変更なしでより高品質な応答が得られます。Amazon Bedrock Mantle対応が追加され、環境変数一つで新基盤へ接続可能に。Slack MCPのチャンネルリンク表示改善や、レートリミット時のフリーズ、macOSログイン失敗など複数のバグが修正されました。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/1d5e804cd3bd172b398a)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-04-06

### Claude Code v2.1.92 introduces Ultraplan — draft plans in the cloud, review in your browser, execute anywhere

Claude Code v2.1.92 で Ultraplan（ベータ版）機能が追加されました。ターミナルで実行し、ブラウザでインラインコメント付きでプランをレビューし、リモート実行またはCLIに送り返すことができます。claude.ai/code で Claude Code Web も同時リリースされ、クラウドファーストのワークフローを推進しながら、ターミナルをパワーユーザー向けエントリーポイントとして維持しています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1se1kpr/claude_code_v2192_introduces_ultraplan_draft)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, release

---

## 2026-04-03

### Claude CodeのComputer Useって何ができるの？CLIからPC操作を自動化する新機能を解説

2026年3月24日、AnthropicがClaude CodeとClaude Coworkに「Computer Use」機能を追加。CLIセッションからPCのデスクトップを直接操作でき、スクリーンショット取得、マウス操作、GUIアプリ操作が可能に。E2Eテスト自動実行やデザイン微調整など開発ワークフローの連続性が向上。まだResearch Previewだが、X上で5.9万いいねを集める注目機能。

- **ソース**: [Zenn claude](https://zenn.dev/joemike/articles/claude-code-computer-use-20260403)
- **重要度**: 9/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-03-30

### Computer use is now in Claude Code.

Claude Code に Computer Use 機能が追加されました。Claude が macOS 上でアプリを開き、UI をクリックし、ビルドしたものをテストできるようになりました。SwiftUI アプリ、Electron ビルド、CLI のない GUI ツールなど、Mac で開けるあらゆるものに対応しています。Pro および Max プランで研究プレビューとして利用可能で、/mcp コマンドで有効化できます。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s7wkky/computer_use_is_now_in_claude_code)
- **重要度**: 9/10
- **タグ**: claude-code, 新機能, mac

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
