---
title: Claude Code Desktop
category: releases
subcategory: claude-code-desktop
tags:
- bugfix
- claude-code
- cowork
- mcp
- release
- 新機能
date: '2026-04-14'
updated: '2026-06-22'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1slictc/claude_code_on_desktop_redesigned_for_parallel
  title: Claude Code on desktop, redesigned for parallel agentic work.
  date: '2026-04-14'
- url: https://qiita.com/picnic/items/45af77de8f8f26a1d26c
  title: Claude Code v2.1.172 サブエージェント5階層化と重要バグ修正まとめ
  date: '2026-06-11'
- url: https://qiita.com/moha0918_/items/397036a48b61dd257ef9
  title: Claude Code v2.1.173〜v2.1.176 リリース｜毎日Changelog解説
  date: '2026-06-12'
- url: https://qiita.com/picnic/items/f8974940833ddc6bef5a
  title: 'Claude Code v2.1.176: モデル制御の抜け穴修正とバグ修正まとめ'
  date: '2026-06-13'
- url: https://qiita.com/picnic/items/152a5a72dce27fb1e0d0
  title: 'Claude Code v2.1.178: Tool(param:value)権限構文とセキュリティ改善'
  date: '2026-06-16'
- url: https://ai-heartland.com/news/claude-code-june-2026-update
  title: Claude Code 6月版アップデートまとめ｜v2.1.153〜v2.1.178の新機能を一覧で読む
  date: '2026-06-17'
- url: https://qiita.com/picnic/items/5dbedcdd25053ee70eb5
  title: Claude Code v2.1.181 の新機能・バグ修正まとめ ─ /config 構文と重大バグ修正
  date: '2026-06-18'
- url: https://the-decoder.com/anthropic-brings-artifacts-to-claude-code-letting-teams-share-live-pages-from-coding-sessions
  title: Anthropic brings Artifacts to Claude Code, letting teams share live pages
    from coding sessions
  date: '2026-06-18'
- url: https://qiita.com/moha0918_/items/74e97e0f8be8174d312e
  title: Claude Code v2.1.181〜v2.1.183｜auto modeが破壊的コマンドを止める｜毎日Changelog解説
  date: '2026-06-19'
- url: https://ai-heartland.com/news/claude-code-artifacts
  title: Claude CodeにArtifacts登場｜セッションを社内共有リンクの生ページに
  date: '2026-06-19'
- url: https://qiita.com/moha0918_/items/9cafe58f1e98d3af2599
  title: Claude Code v2.1.185｜ストール表示が10秒→20秒に｜毎日Changelog解説
  date: '2026-06-20'
- url: https://qiita.com/moha0918_/items/c8e4090853e599e25b4a
  title: Claude Code v2.1.186｜bashコマンド出力にClaudeが自動応答｜毎日Changelog解説
  date: '2026-06-22'
---










# Claude Code Desktop

---

## 2026-06-22

### Claude Code v2.1.186｜bashコマンド出力にClaudeが自動応答｜毎日Changelog解説

Claude Code v2.1.186では、bashコマンドの出力にClaudeが自動応答する挙動がデフォルトに変更されました。従来は出力を文脈に追加するだけでしたが、Claudeが結果を読んで次のアクションを提案します。MCP認証のCLIコマンド追加、サブエージェントの権限制限バグ修正も含まれます。従来の挙動に戻すにはrespondToBashCommands: falseの設定が必要です。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/c8e4090853e599e25b4a)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.186｜bashコマンド出力にClaudeが自動応答｜毎日Changelog解説

Claude Code v2.1.186で、インラインbashコマンドの実行結果にClaudeが自動応答する仕様に変更。従来の「出力を文脈に追加するだけ」の動作は respondToBashCommands: false で維持可能。MCP サーバーの CLI 認証（claude mcp login/logout）が追加され、SSH環境でもブラウザなしで認証可能に。named サブエージェントの権限制限が正しく適用されていなかったバグを修正。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/c8e4090853e599e25b4a)
- **重要度**: 7/10
- **タグ**: claude-code, release, mcp

---

## 2026-06-20

### Claude Code v2.1.185｜ストール表示が10秒→20秒に｜毎日Changelog解説

Claude Code v2.1.185では、API応答待ちのストール表示が改善されました。表示が出るまでの時間が10秒から20秒に延長され、文言も「No response from API」から「Waiting for API response」に変更されました。これにより、長いプロンプトや大きなコンテキスト処理中の誤発火が減少し、ユーザーが正常な待機とエラーを区別しやすくなりました。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/9cafe58f1e98d3af2599)
- **重要度**: 4/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.185｜ストール表示が10秒→20秒に｜毎日Changelog解説

Claude Code v2.1.185では、API応答待機時のストール表示が改善された。表示が出るまでの時間が10秒から20秒に延長され、文言も「No response from API」から「Waiting for API response」に変更。大きなコンテキスト処理時の誤発火を減らし、ユーザー体験を向上させる改善。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/9cafe58f1e98d3af2599)
- **重要度**: 4/10
- **タグ**: claude-code, release, bugfix

---

## 2026-06-19

### Claude Code v2.1.181〜v2.1.183｜auto modeが破壊的コマンドを止める｜毎日Changelog解説

Claude Code v2.1.181〜v2.1.183のリリースで、auto modeが破壊的コマンド（git reset --hard、terraform destroyなど）を自動的にブロックする機能が追加されました。プロンプトから/config key=value構文で設定を直接変更できるようになり、カスタムBASE_URLとFoundryでのprompt cachingの不具合も修正されました。これにより、auto modeでの安全性が大幅に向上し、より安心して自動化を任せられるようになりました。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/74e97e0f8be8174d312e)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.181〜v2.1.183｜auto modeが破壊的コマンドを止める｜毎日Changelog解説

Claude Code v2.1.181〜v2.1.183では、auto modeが破壊的コマンド（git reset --hard、terraform destroyなど）を自動ブロックする機能が追加されました。ユーザーが明示的に指示していない限り、ローカルの変更を破棄する操作やインフラ破棄コマンドは実行前に停止されます。また、/config key=value構文によるプロンプトからの設定変更、カスタムBASE_URLでのprompt caching修正、非推奨モデルの警告機能も追加されています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/74e97e0f8be8174d312e)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude CodeにArtifacts登場｜セッションを社内共有リンクの生ページに

2026年6月18日、AnthropicがClaude CodeにArtifacts機能を発表。ターミナルでの作業セッションを共有可能なインタラクティブWebページに変換し、チーム内でリンク1本で共有できる。セッションの進行に合わせてページが更新され、diff表示やチャート、複数案の比較などをビジュアル化。TeamおよびEnterpriseプランでベータ提供開始。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/claude-code-artifacts)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-06-18

### Claude Code v2.1.181 の新機能・バグ修正まとめ ─ /config 構文と重大バグ修正

Claude Code v2.1.181 がリリースされ、プロンプトから直接設定変更できる /config 構文が追加されました。ネットワークドライブや OneDrive 環境でファイルが破損する重大バグ、起動時のハング・クラッシュ、プロンプトキャッシュ未読み込み問題など複数の重大バグが修正されました。カスタム ANTHROPIC_BASE_URL や AWS Bedrock 利用者、クラウド同期フォルダでの作業者にとって重要なアップデートです。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/5dbedcdd25053ee70eb5)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

### Anthropic brings Artifacts to Claude Code, letting teams share live pages from coding sessions

Anthropic が Claude Code に Artifacts 機能を追加しました。コーディングセッションの結果を対話的なWebページに変換し、チームで共有できます。ページはコード、接続されたツール、チャット履歴から自動生成され、変更があると同じURLで自動更新されます。PRウォークスルー、インシデントタイムライン、ライセンス監査などの用途に対応し、Claude Team/Enterprise顧客向けにベータ版として提供されています。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-brings-artifacts-to-claude-code-letting-teams-share-live-pages-from-coding-sessions)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-06-17

### Claude Code 6月版アップデートまとめ｜v2.1.153〜v2.1.178の新機能を一覧で読む

Claude Code の2026年6月版アップデート（v2.1.153～v2.1.178）をまとめた記事。主な新機能として、プロンプトキャッシュを維持したままディレクトリを移動できる /cd コマンド、サブエージェントが子を起動できる入れ子構造、トラブルシューティング用の --safe-mode、障害時に自動で切り替わる fallbackModel、ツールのパラメータ値まで制御できる権限構文などが追加された。モデル面では Opus 4.8 と Claude Fable 5 が登場。全体として新機能よりも長時間運用と堅牢性向上に重点が置かれたアップデートとなっている。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/claude-code-june-2026-update)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-06-16

### Claude Code v2.1.178: Tool(param:value)権限構文とセキュリティ改善

Claude Code v2.1.178では、ツールの引数レベルで権限を制御できるTool(param:value)構文が追加され、セキュリティが大幅に強化されました。autoモードでサブエージェント起動前の評価が実装され、カスタムAPIゲートウェイ使用時の401認証エラーやOOMクラッシュなど実運用に影響する複数のバグが修正されました。モノレポ環境では、作業ディレクトリに応じた.claude/skillsの自動ロード機能も追加されています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/152a5a72dce27fb1e0d0)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

## 2026-06-13

### Claude Code v2.1.176: モデル制御の抜け穴修正とバグ修正まとめ

Claude Code v2.1.176では、availableModelsの強制を回避できる重大なセキュリティの抜け穴が修正されました。環境変数経由でのブロック済みモデルへのリダイレクトや/fastコマンドによる許可リスト外モデルへの切替えが遮断されます。その他、Bedrock認証情報キャッシュの改善、Remote Controlの複数不具合修正、バックグラウンドセッションのサンドボックス起動問題など、開発者にとって重要な修正が多数含まれています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/f8974940833ddc6bef5a)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-06-12

### Claude Code v2.1.173〜v2.1.176 リリース｜毎日Changelog解説

Claude Code v2.1.173〜v2.1.176の4つのバージョンをまとめたChangelog解説記事。会話言語に合わせたセッションタイトル生成、availableModelsの厳格な統制機能（enforceAvailableModels）、/usageコマンドでのトークン消費内訳表示が主な新機能。Remote ControlやバックグラウンドまわりのバグFix、モデルピッカーの改善など細かい修正も多数含まれる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/397036a48b61dd257ef9)
- **重要度**: 6/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.173〜v2.1.176 リリース｜毎日Changelog解説

Claude Code v2.1.173〜v2.1.176の4つのバージョンをまとめたリリースノート。主な変更点は、会話言語に応じたセッションタイトル生成、availableModelsの厳格な統制機能（enforceAvailableModels）、/usageコマンドでのトークン利用内訳表示、Remote ControlやバックグラウンドまわりのバグFix。特に組織でモデル制限を運用している管理者向けの機能強化が目立つ。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/397036a48b61dd257ef9)
- **重要度**: 6/10
- **タグ**: claude-code, release, 新機能

---

## 2026-06-11

### Claude Code v2.1.172 サブエージェント5階層化と重要バグ修正まとめ

Claude Code v2.1.172/v2.1.173 がリリース。サブエージェントの最大5階層ネスト対応という大型機能追加に加え、availableModels 制約の適用漏れ、Amazon Bedrock のリージョン解決失敗、1M コンテキスト利用時のフリーズ問題など、複数の重要バグを修正。v2.1.173 では Fable 5 モデル名正規化と Windows 起動警告を修正。マルチエージェントシステム構築者や Bedrock ユーザーに影響。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/45af77de8f8f26a1d26c)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-04-14

### Claude Code on desktop, redesigned for parallel agentic work.

Claude Code デスクトップアプリが大幅刷新され、並列エージェント作業に対応。新しいサイドバーで複数セッションを同時実行可能になり、ドラッグ&ドロップレイアウト、統合ターミナル、ファイル編集機能、HTML/PDFプレビュー、改善された差分ビューアーを搭載。Mac向けSSH対応、キーボードショートカット、CLIプラグイン機能も追加され、サイドチャットによる分岐やPRマージ時の自動アーカイブにも対応。現在利用可能。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1slictc/claude_code_on_desktop_redesigned_for_parallel)
- **重要度**: 9/10
- **タグ**: claude-code, 新機能, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-14 | 自動生成 |
