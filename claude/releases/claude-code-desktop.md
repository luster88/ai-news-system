---
title: Claude Code Desktop
category: releases
subcategory: claude-code-desktop
tags:
- bugfix
- claude-code
- cowork
- release
- 新機能
date: '2026-04-14'
updated: '2026-06-18'
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
---







# Claude Code Desktop

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
