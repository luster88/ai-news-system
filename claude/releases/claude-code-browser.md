---
title: Claude Code Browser
category: releases
subcategory: claude-code-browser
tags:
- bugfix
- claude-code
- cowork
- pricing
- release
- setup
- 新機能
date: '2026-07-12'
updated: '2026-09-01'
sources:
- url: https://the-decoder.com/claude-code-now-has-a-built-in-browser-that-lets-the-ai-read-click-and-type-on-external-websites
  title: Claude Code now has a built-in browser that lets the AI read, click, and
    type on external websites
  date: '2026-07-12'
- url: https://qiita.com/moha0918_/items/5acf087c20983cff5f7c
  title: Claude Code v2.1.227〜v2.1.229｜Write の read 必須が新モデルで外れる｜毎日Changelog解説
  date: '2026-08-12'
- url: https://www.reddit.com/r/ClaudeAI/comments/1vndhg6/finally_claude_code_has_autocontinue_when_limits
  title: Finally, Claude Code has “Auto-continue when limits reset”
  date: '2026-08-13'
- url: https://qiita.com/picnic/items/ec718a60bd314c5d8c90
  title: Claude Code v2.1.232まとめ：PowerShell権限バイパス等の重大修正と新機能
  date: '2026-08-14'
- url: https://qiita.com/moha0918_/items/b604352231f9a8a76a38
  title: Claude Code v2.1.233｜TodoWrite が Fable 5 / Sonnet 5 で無効に｜毎日Changelog解説
  date: '2026-08-15'
- url: https://qiita.com/moha0918_/items/75f3681463180844e8ed
  title: Claude Code v2.1.234｜利用上限リセットで自動再開｜毎日Changelog解説
  date: '2026-08-17'
- url: https://qiita.com/moha0918_/items/ca1fa2fb4e355433cee3
  title: Claude Code v2.1.237〜v2.1.238｜長時間セッションのメモリリークが直る｜毎日Changelog解説
  date: '2026-08-20'
- url: https://qiita.com/picnic/items/e2b9a324815c7ef21782
  title: 'Claude Code v2.1.238: メモリ無限増大の修正とMCP認証まわりの破壊的変更'
  date: '2026-08-21'
- url: https://qiita.com/picnic/items/ff939c5e26e47d011a58
  title: 'Claude Code v2.1.239: Bedrock二重課金バグ修正とPython SDK移行コマンド追加'
  date: '2026-08-22'
- url: https://qiita.com/picnic/items/f6c4074a99d25f780122
  title: Claude Code v2.1.248まとめ：--restrictedモードとcacheTtlで安全性と速度が向上
  date: '2026-08-28'
- url: https://qiita.com/NaokiIshimura/items/7636068d678804fbda26
  title: Claude Codeのセッション同士が会話しはじめた — SendMessage / ListAgents 完全ガイド
  date: '2026-08-29'
- url: https://qiita.com/NaokiIshimura/items/0acc467e15b9c2b69288
  title: Claude Code v2.1.248 - v2.1.251 リリースノートまとめ
  date: '2026-08-29'
- url: https://qiita.com/moha0918_/items/08dfa2f03d89272498dc
  title: Claude Code v2.1.251｜権限チェック後の symlink 差し替えを塞ぐ｜毎日Changelog解説
  date: '2026-08-29'
- url: https://qiita.com/moha0918_/items/09b61fa44e12b8e9bd36
  title: Claude Code v2.1.252｜always allow が保存されない条件｜毎日Changelog解説
  date: '2026-09-01'
- url: https://qiita.com/moha0918_/items/74317aca2bd592a109a6
  title: Claude Code v2.1.257｜auto モードの自動承認が縮む｜毎日Changelog解説
  date: '2026-09-01'
- url: https://qiita.com/picnic/items/ba95f05d2b78799f238b
  title: 'Claude Code v2.1.257: Fable 5.1追加と権限すり抜け修正まとめ'
  date: '2026-09-01'
---














# Claude Code Browser

---

## 2026-09-01

### Claude Code v2.1.257｜auto モードの自動承認が縮む｜毎日Changelog解説

Claude Code v2.1.257 がリリースされました。auto モードでクラウドメタデータ認証情報取得や egress 回避が自動承認されなくなり、.claude/settings.json の bypassPermissions 指定も無視されるようになりました。新たに Fable 5.1 モデルが追加され、コンテキスト 1M トークン、料金は入力 $10/出力 $50 per Mtok、キャッシュ読み取り $0.25/Mtok で利用可能です。作業ディレクトリ外のファイル読み取りに確認プロセスが追加され、セキュリティが強化されています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/74317aca2bd592a109a6)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.257: Fable 5.1追加と権限すり抜け修正まとめ

Claude Code v2.1.257では新モデルFable 5.1が追加されたが、より重要なのは権限すり抜けに関する複数のセキュリティ修正。プロジェクト設定でのbypassPermissions指定が無視される破壊的変更、複合コマンドやsymlinkを悪用した権限回避の修正、autoモードへのContainment Escapeルール追加など、実質的にセキュリティパッチとしての性格が強い。Bedrock/Vertex/Foundryなどサードパーティプロバイダ利用時の認証ヘッダ混入も修正された。

- **ソース**: [Qiita claudecode](https://qiita.com/picnic/items/ba95f05d2b78799f238b)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-09-01

### Claude Code v2.1.252｜always allow が保存されない条件｜毎日Changelog解説

Claude Code v2.1.252 のバグ修正リリース。.claude/settings.local.json が存在しないプロジェクトで always allow が保存されない問題を修正。Mac環境でのBashコマンド失敗、Remote Control セッションでの応答遅延、巨大な失敗出力によるAPIリクエストサイズ超過も解決。新機能追加はなく、4件すべてがバグ修正。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/09b61fa44e12b8e9bd36)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, release

---

### Claude Code v2.1.252｜always allow が保存されない条件｜毎日Changelog解説

Claude Code v2.1.252 のバグ修正リリース。.claude/settings.local.json が存在しないプロジェクトで always allow が保存されない問題を修正。Mac 環境での Bash コマンドエラー、Remote Control セッションでの応答遅延、巨大な失敗出力による API リクエストサイズ超過の問題も解消。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/09b61fa44e12b8e9bd36)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-08-29

### Claude Code v2.1.251｜権限チェック後の symlink 差し替えを塞ぐ｜毎日Changelog解説

Claude Code v2.1.251 で複数のセキュリティ問題が修正されました。権限チェック後の symlink 差し替えによる承認範囲外へのアクセス、Grep/Glob の symlink 経由での deny ルール回避、プロジェクト設定からの環境変数設定の制限などが対応されました。また PreModelSwitch/PostModelSwitch フック、CLAUDE_CODE_SUBAGENT_MODEL の動作変更、プロンプトキャッシュ統計の追加など機能改善も含まれています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/08dfa2f03d89272498dc)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, release

---

## 2026-08-29

### Claude Codeのセッション同士が会話しはじめた — SendMessage / ListAgents 完全ガイド

Claude Code v2.1.224で、セッション間でメッセージをやり取りできるクロスセッションメッセージング機能が追加されました。ListAgentsでセッション一覧を取得し、SendMessageで相互に通信できますが、セキュリティ境界が厳格に設計されており、bypassPermissions動作中のセッション宛メッセージは自動配信されず承認待ちになります。プレーンテキストのみが送信され、会話履歴やファイルは共有されない仕様です。

- **ソース**: [Qiita claude](https://qiita.com/NaokiIshimura/items/7636068d678804fbda26)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, cowork

---

### Claude Code v2.1.248 - v2.1.251 リリースノートまとめ

Claude Code v2.1.248～v2.1.251の3リリースをまとめた記事。--restrictedフラグによるセキュリティモード、シンボリックリンク差し替えやパストラバーサルのセキュリティ修正、PreModelSwitch/PostModelSwitchフックの追加、プロンプトキャッシュの可視化など運用面の改善が中心。ネイティブバイナリの軽量化やサブエージェントのライブストリーミングも実装された。

- **ソース**: [Qiita claude](https://qiita.com/NaokiIshimura/items/0acc467e15b9c2b69288)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-08-28

### Claude Code v2.1.248まとめ：--restrictedモードとcacheTtlで安全性と速度が向上

Claude Code v2.1.248がリリースされ、CI/CD環境向けの--restrictedモード、プロンプトキャッシュTTL設定、Bedrock/Vertex/Foundryでのクロスセッション通信対応などが追加されました。長時間セッションでのキャッシュミス問題やセキュリティ関連の重要なバグ修正も含まれています。CI/CDでClaude Codeを使うチームやサブエージェント活用者は特に確認が必要な大型アップデートです。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/f6c4074a99d25f780122)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.248まとめ：--restrictedモードとcacheTtlで安全性と速度が向上

Claude Code v2.1.248は、--restrictedモードによるセキュリティ強化、エージェント単位のプロンプトキャッシュTTL設定、Bedrock/Vertex/Foundryでのクロスセッション通信対応を含む大型アップデートです。長時間セッションで発生していたプロンプトキャッシュミスの修正や、機密ファイルの誤アップロード問題も解消されました。CI/CDでの利用やサブエージェント活用においてキャッシュヒット率向上とコスト削減が期待できます。

- **ソース**: [Qiita claudecode](https://qiita.com/picnic/items/f6c4074a99d25f780122)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

## 2026-08-22

### Claude Code v2.1.239: Bedrock二重課金バグ修正とPython SDK移行コマンド追加

Claude Code v2.1.239では、Amazon Bedrock経由でプロキシ使用時にAPIコールが2倍課金されていた重大なバグが修正されました。また、Python SDK 0.xから1.xへの移行を支援する/claude-api upgradeコマンドが追加され、データレジデンシー対応ワークスペースのコスト見積もりロジックも修正されています。プロキシ環境のユーザーは過去の請求額を確認し、予算設定の見直しが推奨されます。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/ff939c5e26e47d011a58)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 2026-08-21

### Claude Code v2.1.238: メモリ無限増大の修正とMCP認証まわりの破壊的変更

Claude Code v2.1.238のリリース情報。長時間セッションでのメモリ無限増大の重大なバグが修正され、数時間以上の対話セッションの安定性が向上。MCP headersHelperにセキュリティ強化が入り、CI/自動化環境では信頼ダイアログの承認が必須となる破壊的変更を含む。プラグインマーケットプレイスにheadersHelper機能が追加され、プライベート配布での認証が容易に。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/e2b9a324815c7ef21782)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-08-20

### Claude Code v2.1.237〜v2.1.238｜長時間セッションのメモリリークが直る｜毎日Changelog解説

Claude Code v2.1.237〜v2.1.238では、長時間セッションでサブエージェントを繰り返し使用した際のメモリリーク問題が修正されました。ツール結果が表示ウィンドウから外れると適切に解放されるようになり、朝から晩まで同じセッションを開き続ける使い方での無制限なメモリ消費が解消されました。その他、Concise出力スタイルの追加、カスタム出力スタイルの維持バグ修正、プラグインマーケットプレイスへのheadersHelper追加、プロンプトキャッシュの修正などが含まれます。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/ca1fa2fb4e355433cee3)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.237〜v2.1.238｜長時間セッションのメモリリークが直る｜毎日Changelog解説

Claude Code v2.1.237〜v2.1.238 のリリースで、長時間セッションでサブエージェントを繰り返し使用した際のメモリリーク問題が修正されました。表示ウィンドウから外れたツール結果が適切に解放されるようになり、朝から晩まで同じセッションを開き続ける使い方で顕在化していたメモリ増加が止まります。また、Concise 出力スタイルの追加、カスタム出力スタイルの不具合修正、プラグインマーケットプレイスへの headersHelper 追加、プロンプトキャッシュの修正などが含まれています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/ca1fa2fb4e355433cee3)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, release

---

## 2026-08-17

### Claude Code v2.1.234｜利用上限リセットで自動再開｜毎日Changelog解説

Claude Code v2.1.234では、claude.aiの利用上限リセット後に自動的にセッションを再開する機能が追加されました。/goalの30分チェックイン機能、compaction後のauto modeバグ修正、サブエージェント権限回答の保存バグ修正など、ユーザーが不在時の挙動改善が行われています。Windows NTパス（\??\形式）はセキュリティ対策として拒否されるようになりました。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/75f3681463180844e8ed)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, bugfix

---

## 2026-08-15

### Claude Code v2.1.233｜TodoWrite が Fable 5 / Sonnet 5 で無効に｜毎日Changelog解説

Claude Code v2.1.233 で、Opus 4.8・Sonnet 5・Fable 5・Mythos 5 以降のモデルでは TodoWrite / TaskCreate などの Todo 系ツールがデフォルトで無効化されました。これにより PostToolUse hook や statusline で TodoWrite を参照している設定が動作しなくなります。CLAUDE_CODE_ENABLE_TODO_TOOLS=1 で有効化可能ですが、今後の維持は要検討です。Windows 版では v2.1.232 の Bash コマンド承認問題と NTLM 認証情報漏洩の脆弱性が修正され、GitLab マージリクエスト対応や MCP v2 の接続安定性向上も含まれます。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/b604352231f9a8a76a38)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-08-14

### Claude Code v2.1.232まとめ：PowerShell権限バイパス等の重大修正と新機能

Claude Code v2.1.232がリリースされ、PowerShellとWindows Git Bashにおける2件の重大な権限バイパス脆弱性（critical/high）が修正されました。サブエージェントのフォーク機能がデフォルト化され、セッション間メッセージング機能が追加されています。GitLabトークンの秘匿化強化やRemote Control機能の安定化も実施されており、Windows環境のユーザーは早急なアップデートが推奨されます。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/ec718a60bd314c5d8c90)
- **重要度**: 9/10
- **タグ**: claude-code, bugfix, 新機能

---

## 2026-08-13

### Finally, Claude Code has “Auto-continue when limits reset”

Claude Code に「使用制限がリセットされた際に自動継続」する新機能が追加されました。この機能により、使用制限に達した後、制限が解除されると自動的にセッションを再開できるようになり、長時間のコーディングセッションがより快適になります。ユーザーからは便利な改善として評価されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vndhg6/finally_claude_code_has_autocontinue_when_limits)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-08-12

### Claude Code v2.1.227〜v2.1.229｜Write の read 必須が新モデルで外れる｜毎日Changelog解説

Claude Code v2.1.227〜v2.1.229のChangelog解説。v2.1.228で新モデルに限りWriteツールの「同セッション内でReadしてから書く」制約が撤廃され、未読ファイルの上書きが可能に。一方で安全性が低下する側面もある。/commit-push-prの危険フラグ自動承認廃止、claude.ai同期スキルの挙動制限、セッション後始末のバグ修正なども含まれる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/5acf087c20983cff5f7c)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.227〜v2.1.229｜Write の read 必須が新モデルで外れる｜毎日Changelog解説

Claude Code v2.1.227〜v2.1.229のアップデートで、Writeツールの「Read必須」制約が新モデルでは撤廃され、未読ファイルの上書きが可能になった。一方、/commit-push-prコマンドの危険フラグ自動承認が廃止され、claude.ai同期スキルのローカルコマンド実行も制限された。これらは利便性と安全性のバランスを調整する重要な変更である。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/5acf087c20983cff5f7c)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-12

### Claude Code now has a built-in browser that lets the AI read, click, and type on external websites

Anthropic が Claude Code に統合ブラウザ機能を追加。AI が外部ウェブサイトを直接開き、読み取り、クリック、入力が可能に。ドキュメントサイトや課題トラッカーへのアクセスに対応し、タブベースで動作。書き込み操作には安全性チェックが適用され、購入・アカウント作成・CAPTCHA回避は同意なしでは実行されない。組織はアクセス制限やブラウザツールの無効化が可能で、ログインセッション内での操作には Chrome 拡張機能の使用を推奨。

- **ソース**: [The Decoder Claude](https://the-decoder.com/claude-code-now-has-a-built-in-browser-that-lets-the-ai-read-click-and-type-on-external-websites)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-12 | 自動生成 |
