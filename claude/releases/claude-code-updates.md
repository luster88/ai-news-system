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
- mcp
- release
- setup
- sonnet
- 新機能
date: 2026-03-23
updated: '2026-07-21'
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
- url: https://qiita.com/moha0918_/items/fbf4e1c6ed0629c2c248
  title: Claude Code v2.1.121 リリース｜毎日Changelog解説
  date: '2026-04-28'
- url: https://qiita.com/moha0918_/items/ca528c5eaee11b779dbf
  title: Claude Code v2.1.129〜v2.1.131 リリース｜毎日Changelog解説
  date: '2026-05-06'
- url: https://qiita.com/yurukusa/items/571471fd2962f29d46c7
  title: Anthropic 5/6 発表 24 時間後、 5 つの触媒の状態を翌朝の起票で読んだ
  date: '2026-05-06'
- url: https://qiita.com/kai_kou/items/ba88f403caf78fe5242b
  title: Code with Claude 2026 完全解説 — SpaceX提携とClaude Codeレート制限2倍
  date: '2026-05-07'
- url: https://www.reddit.com/r/ClaudeAI/comments/1tag1i9/new_in_claude_code_agent_view
  title: 'New in Claude Code: agent view.'
  date: '2026-05-11'
- url: https://qiita.com/moha0918_/items/9a85125fe731e2fc306a
  title: Claude Code v2.1.137〜v2.1.139 リリース｜毎日Changelog解説
  date: '2026-05-11'
- url: https://qiita.com/moha0918_/items/991c2556a7f9fe035d06
  title: Claude Code v2.1.141 リリース｜毎日Changelog解説
  date: '2026-05-14'
- url: https://qiita.com/moha0918_/items/82494952b384c4e2c208
  title: Claude Code v2.1.168 リリース｜毎日Changelog解説
  date: '2026-06-07'
- url: https://www.reddit.com/r/ClaudeAI/comments/1u9hp5y/new_claude_code_update_is_crazy
  title: New Claude code update is crazy
  date: '2026-06-18'
- url: https://qiita.com/picnic/items/4ce73f6d760a8850de39
  title: Claude Code v2.1.186の重要変更点：bash自動応答とセキュリティ修正
  date: '2026-06-22'
- url: https://qiita.com/moha0918_/items/6fac5264ef4c4497d188
  title: Claude Code v2.1.196〜v2.1.197｜Sonnet 5 がデフォルトに｜毎日Changelog解説
  date: '2026-06-30'
- url: https://qiita.com/picnic/items/e6d330b7723ee647fdcd
  title: Claude Code v2.1.205まとめ：MCP名予約の破壊的変更と安全性強化
  date: '2026-07-09'
- url: https://qiita.com/moha0918_/items/0b47d4c62a52b65ea7c0
  title: Claude Code v2.1.207｜Auto mode がクラウド3社で opt-in 不要に｜毎日Changelog解説
  date: '2026-07-11'
- url: https://qiita.com/moha0918_/items/2ad6f36fd302017b9267
  title: Claude Code v2.1.216〜v2.1.217｜サブエージェントの無制限増殖に上限｜毎日Changelog解説
  date: '2026-07-21'
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

## 2026-07-21

### Claude Code v2.1.216〜v2.1.217｜サブエージェントの無制限増殖に上限｜毎日Changelog解説

Claude Code v2.1.216〜v2.1.217でサブエージェントの制御が大幅に強化されました。デフォルトで並列実行が20に制限され、ネストした生成も無効化。予算上限による停止機能も改善され、バックグラウンドエージェントも確実に停止するようになりました。また、長時間セッションでの応答遅延問題（メッセージ正規化の2乗コスト）が修正され、サンドボックスのファイルシステム分離のみを無効化できる新オプションも追加されています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/2ad6f36fd302017b9267)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-11

### Claude Code v2.1.207｜Auto mode がクラウド3社で opt-in 不要に｜毎日Changelog解説

Claude Code v2.1.207では、Bedrock・Vertex AI・Foundryの3クラウドプロバイダでAuto modeがopt-in不要になりました。CLAUDE_CODE_ENABLE_AUTO_MODEの環境変数が不要になる一方、設定ファイルの読み込み先が.claude/settings.local.jsonから~/.claude/settings.jsonへ変更されています。また、デフォルトモデルがOpus 4.8に変更され、非対話実行での同意ダイアログ素通りバグの修正、シェルインジェクション対策の強化などが含まれます。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/0b47d4c62a52b65ea7c0)
- **重要度**: 7/10
- **タグ**: claude-code, release, setup

---

## 2026-07-11

### Claude Code v2.1.207｜Auto mode がクラウド3社で opt-in 不要に｜毎日Changelog解説

Claude Code v2.1.207では、Bedrock・Vertex AI・Foundryの3クラウドプロバイダでAuto modeがopt-in不要となり、環境変数CLAUDE_CODE_ENABLE_AUTO_MODEが不要になりました。設定ファイルの読み込み先が.claude/settings.local.jsonから~/.claude/settings.jsonに変更され、デフォルトモデルがOpus 4.8に更新されました。また、非対話実行時の同意ダイアログスキップの不具合修正、シェルインジェクション対策、プラグイン設定の読み込み経路変更などのセキュリティ修正が含まれています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/0b47d4c62a52b65ea7c0)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-09

### Claude Code v2.1.205まとめ：MCP名予約の破壊的変更と安全性強化

Claude Code v2.1.205がリリースされ、MCPサーバー名「Claude Browser」と「Claude Preview」が予約語化される破壊的変更が導入されました。autoモードの安全性強化（トランスクリプト改ざん防止、危険なコマンド実行前確認）、Windows環境でのworktree削除時のデータ損失バグ修正、/doctorコマンドの修復機能追加など、安全性とバグ修正に重点を置いた重要なアップデートです。独自MCPサーバーを運用している開発者は、アップデート前に名前の衝突確認が必須となります。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/e6d330b7723ee647fdcd)
- **重要度**: 8/10
- **タグ**: claude-code, mcp, bugfix

---

## 2026-06-30

### Claude Code v2.1.196〜v2.1.197｜Sonnet 5 がデフォルトに｜毎日Changelog解説

Claude Code v2.1.197でデフォルトモデルがClaude Sonnet 5に変更され、1Mトークンのコンテキスト窓と8/31までの$2/$10 per Mtokプロモ価格が利用可能に。v2.1.196では組織デフォルトモデル対応、MCP自己承認の封鎖、バックグラウンドジョブでの会話消失バグ修正など、安定性とセキュリティの改善が実施された。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/6fac5264ef4c4497d188)
- **重要度**: 8/10
- **タグ**: claude-code, sonnet, release

---

## 2026-06-22

### Claude Code v2.1.186の重要変更点：bash自動応答とセキュリティ修正

Claude Code v2.1.186がリリースされ、bash コマンド出力への Claude 自動応答がデフォルト化される Breaking Change が含まれます。CLAUDE_CODE_MAX_RETRIES の上限が15に制限され、MCP サーバーの CLI 認証コマンド（login/logout）が追加されました。サブエージェントの deny ルール未適用とツールゲートすり抜けのセキュリティ修正も実施されています。既存ワークフローへの影響が大きいため、アップデート後の動作確認が推奨されます。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/4ce73f6d760a8850de39)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-06-18

### New Claude code update is crazy

Reddit の ClaudeAI コミュニティで、Claude Code の新しいアップデートに関する投稿が話題になっています。ユーザーが画像を共有し、アップデートの内容について議論しています。具体的な機能追加や変更点の詳細は本文からは不明ですが、コミュニティの反応から注目度の高いアップデートであることが伺えます。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1u9hp5y/new_claude_code_update_is_crazy)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, release

---

## 2026-06-07

### Claude Code v2.1.168 リリース｜毎日Changelog解説

Claude Code v2.1.168がリリースされました。新機能は含まれず、バグ修正と信頼性改善のみのメンテナンスリリースです。公式Changelogには具体的な修正内容の記載はなく、既存ユーザーは安心してアップデート可能です。挙動の変更はなく、日常使用しているユーザーは更新して様子を見るだけで十分とされています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/82494952b384c4e2c208)
- **重要度**: 4/10
- **タグ**: claude-code, release, bugfix

---

## 2026-05-14

### Claude Code v2.1.141 リリース｜毎日Changelog解説

Claude Code v2.1.141 がリリースされ、hook の terminalSequence によるデスクトップ通知対応、Rewind の「Summarize up to here」機能、/feedback での過去セッション同梱機能が追加されました。40件超のバグ修正も含まれ、controlling terminal がない環境でも通知が出せるようになり、長いセッションのコンテキスト管理と不具合報告の利便性が向上しています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/991c2556a7f9fe035d06)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.141 リリース｜毎日Changelog解説

Claude Code v2.1.141がリリースされ、hook機能にterminalSequenceが追加されcontrolling terminalなしでも通知が可能に。Rewindメニューに「Summarize up to here」が追加され、手動で過去を要約しつつ直近のターンを保持できる。/feedbackコマンドが過去24時間または7日分のセッションを同梱可能になり、複数セッションに跨る不具合報告が容易になった。その他、40件超のバグ修正とHTTPS clone対応などの改善が含まれる。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/991c2556a7f9fe035d06)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-05-11

### Claude Code v2.1.137〜v2.1.139 リリース｜毎日Changelog解説

Claude Code v2.1.137〜v2.1.139の新機能解説。v2.1.139で複数セッションを一覧管理できるagent view、達成条件を指定して自動作業させる/goalコマンド、hookのargs配列によるシェル回避機能、continueOnBlock設定によるツール拒否時のターン継続など、ワークフロー改善の機能が多数追加された。その他、デッドロック問題やメモリリーク、hot-reload問題など複数のバグ修正も実施。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/9a85125fe731e2fc306a)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-05-11

### New in Claude Code: agent view.

Claude Code に新機能「agent view」が追加されました。複数のセッションを同時に管理できる機能で、`claude agents` コマンドで起動します。各セッションはターミナルタブを占有せずにバックグラウンドで実行され、実行中・ブロック中・完了したタスクを一目で確認できます。有料プラン全てで利用可能で、Research Preview として提供されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1tag1i9/new_in_claude_code_agent_view)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, cowork

---

### Claude Code v2.1.137〜v2.1.139 リリース｜毎日Changelog解説

Claude Code v2.1.137〜v2.1.139の3バージョンをまとめて解説。v2.1.139で複数の新機能が追加され、特に「claude agents」で並走セッションを一画面に集約する機能、「/goal」コマンドで達成条件を満たすまで自動作業を継続する機能、hooksのargs配列によるシェル経由なしのプロセス起動が実装された。その他、continueOnBlock設定やMCP stdio環境変数の追加、API key設定時の機能制限など複数の改善が含まれる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/9a85125fe731e2fc306a)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-05-07

### Code with Claude 2026 完全解説 — SpaceX提携とClaude Codeレート制限2倍

2026年5月6日、AnthropicはCode with Claude 2026イベントでSpaceX Colossus 1データセンター（22万台超GPU）との提携を発表。Claude Codeの5時間レート制限が全プランで2倍に緩和され、ピーク時間制限も撤廃された。Opus APIのレート制限も増量され、Code Review機能やCLIアップデート、金融サービス向けテンプレートも公開された。

- **ソース**: [Qiita claude](https://qiita.com/kai_kou/items/ba88f403caf78fe5242b)
- **重要度**: 9/10
- **タグ**: claude-code, release, 新機能

---

## 2026-05-06

### Anthropic 5/6 発表 24 時間後、 5 つの触媒の状態を翌朝の起票で読んだ

Anthropic が 5/6 に利用枠の倍化と peak time 減算撤廃、cache TTL 修正を発表。過去 6 週間で確認された 5 つの問題（cache TTL 短縮、利用枠構造の不透明性、子エージェント境界の不在、利用枠燃焼の透明性欠如、停止合図への応答失敗）のうち、cache TTL のみが v2.1.129 で解消。その他 4 点は未解決のまま。コミュニティの起票（#55663, #55488, #56297, #55909 等）で継続的に問題が報告されている。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/571471fd2962f29d46c7)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-05-06

### Claude Code v2.1.129〜v2.1.131 リリース｜毎日Changelog解説

Claude Code v2.1.129〜v2.1.131のリリースノート。--plugin-urlオプションによるURLからの直接プラグインロード機能追加、prompt cacheのTTLが5分に縮んでいた重大なバグ修正、Homebrew/WinGet自動アップデート対応、Ctrl+R履歴検索の全プロジェクト横断検索への復帰、VS Code拡張のWindows起動失敗修正など、新機能と重要なバグ修正が含まれる。特にprompt cache TTLのバグはトークンコストに大きく影響していた。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/ca528c5eaee11b779dbf)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, 新機能

---

### Claude Code v2.1.129〜v2.1.131 リリース｜毎日Changelog解説

Claude Code v2.1.129〜v2.1.131のリリース情報。--plugin-url フラグによるURL経由のプラグイン直接ロードが追加され、1時間のprompt cache TTLが実際は5分で揮発していた重大なバグが修正された。Ctrl+R履歴検索の全プロジェクト横断対応、Homebrew/WinGet自動アップデート機能、VS Code拡張のWindows起動失敗修正なども含まれる。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/ca528c5eaee11b779dbf)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, 新機能

---

## 2026-04-28

### Claude Code v2.1.121 リリース｜毎日Changelog解説

Claude Code v2.1.121のリリースノート解説記事。MCP周りの強化として、alwaysLoad設定による全ツール常時ロード機能と、PostToolUseフックの全ツール対応が追加された。また、長時間セッションを破綻させていた画像処理やメモリ周りの重大なメモリリーク3件が修正され、安定性が大幅に向上。その他、プラグイン管理コマンド追加やUI改善も含まれる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/fbf4e1c6ed0629c2c248)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, release

---

### Claude Code v2.1.121 リリース｜毎日Changelog解説

Claude Code v2.1.121がリリースされ、MCPサーバ単位での全ツール常時ロード機能（alwaysLoad）、PostToolUseフックの全ツール対応、長時間セッションで発生していた3件のメモリリーク修正が実装されました。その他、孤立プラグイン依存を削除するclaude plugin pruneコマンド追加、フルスクリーンモードのスクロール挙動改善、/skillsの検索ボックス追加などの機能強化が行われています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/fbf4e1c6ed0629c2c248)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, bugfix

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
