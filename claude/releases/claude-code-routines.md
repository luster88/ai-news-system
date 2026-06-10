---
title: Claude Code Routines
category: releases
subcategory: claude-code-routines
tags:
- bugfix
- claude-code
- mcp
- opus
- performance
- release
- windows
- 新機能
date: '2026-04-19'
updated: '2026-06-10'
sources:
- url: https://qiita.com/tai0921/items/a6323df5024b1d3a9b27
  title: Claude CodeのRoutines機能で「寝ている間にPRが自動レビューされる」時代へ
  date: '2026-04-19'
- url: https://qiita.com/moha0918_/items/d42ad8905e76c9b7a0c1
  title: Claude Code v2.1.153〜v2.1.154 リリース｜毎日Changelog解説
  date: '2026-05-28'
- url: https://qiita.com/moha0918_/items/1c20a1401487b278ecc9
  title: Claude Code v2.1.159〜v2.1.161 リリース｜毎日Changelog解説
  date: '2026-06-02'
- url: https://qiita.com/picnic/items/59b8378b59d036048cf7
  title: 'Claude Code v2.1.160: workflowキーワードがultracodeに変更・セキュリティ強化'
  date: '2026-06-02'
- url: https://qiita.com/moha0918_/items/c31d5e74c50848db7859
  title: Claude Code v2.1.162 リリース｜毎日Changelog解説
  date: '2026-06-03'
- url: https://ai-heartland.com/explain/claude-code-dynamic-workflows
  title: Claude Code Dynamic Workflows解説：1,000サブエージェント並列とOpus 4.8
  date: '2026-06-03'
- url: https://ai-heartland.com/explain/claude-code-v2-1-152-update
  title: Claude Code v2.1.152｜Skillを動的制御：disallowed-tools・/reload-skills・MessageDisplayフック
  date: '2026-06-03'
- url: https://qiita.com/picnic/items/49ff0025c97ab6ac1430
  title: 'Claude Code v2.1.162: 権限制御バグ修正とagents大幅改善まとめ'
  date: '2026-06-04'
- url: https://qiita.com/moha0918_/items/dab2d73fbb0ce6eea33d
  title: Claude Code v2.1.166〜v2.1.167 リリース｜毎日Changelog解説
  date: '2026-06-06'
- url: https://qiita.com/moha0918_/items/82494952b384c4e2c208
  title: Claude Code v2.1.168 リリース｜毎日Changelog解説
  date: '2026-06-07'
- url: https://qiita.com/moha0918_/items/90ccc7a4c0595a51c1cf
  title: Claude Code v2.1.172 リリース｜毎日Changelog解説
  date: '2026-06-10'
- url: https://zenn.dev/ty2/articles/tweet-bcherny-2060390853835726946
  title: Claude Codeのダイナミックワークフローで大規模移行が劇的に加速
  date: '2026-06-10'
---








# Claude Code Routines

---

## 2026-06-10

### Claude Code v2.1.172 リリース｜毎日Changelog解説

Claude Code v2.1.172 がリリースされ、サブエージェントが最大5階層まで再帰的にサブエージェントを起動できる機能が追加された。また、1Mコンテキストでクレジット不足時にセッションが固まる重大な不具合や、WebFetchのワイルドカードドメイン許可が機能していなかったセキュリティ関連のバグが修正された。その他、多数のバグフィックスとパフォーマンス改善が含まれる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/90ccc7a4c0595a51c1cf)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### Claude Codeのダイナミックワークフローで大規模移行が劇的に加速

Claude Codeに「ダイナミックワークフロー」機能が追加され、大規模タスクを並列処理可能に。Salesforceの導入事例では231日分の作業が13日で完了し、スピードと品質の両立を実現。プロンプトに「workflow」を含めるだけで起動でき、技術的負債の解消が劇的に加速する。

- **ソース**: [Zenn claude](https://zenn.dev/ty2/articles/tweet-bcherny-2060390853835726946)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, performance

---

### Claude Code v2.1.172 リリース｜毎日Changelog解説

Claude Code v2.1.172 では、サブエージェントが最大5階層まで再帰的にサブエージェントを起動できる機能が追加されました。また、WebFetchのワイルドカードドメイン許可が正常に機能するようになり、1Mコンテキスト使用時にセッションが固まる不具合が修正されました。その他、Bedrockのリージョン読み込み改善、プラグイン検索バー追加、長い会話時の負荷軽減などの改善が含まれています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/90ccc7a4c0595a51c1cf)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-06-07

### Claude Code v2.1.168 リリース｜毎日Changelog解説

Claude Code v2.1.168 がリリースされました。これは新機能を含まないメンテナンスリリースで、バグ修正と信頼性改善のみが含まれています。公式 Changelog には詳細な修正内容の記載はなく、v2.1.167 からの日常利用者は安心してアップデート可能です。挙動が変わる変更はなく、既存の不具合が解消されている可能性があるため、手元で確認することが推奨されています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/82494952b384c4e2c208)
- **重要度**: 4/10
- **タグ**: claude-code, release, bugfix

---

## 2026-06-06

### Claude Code v2.1.166〜v2.1.167 リリース｜毎日Changelog解説

Claude Code v2.1.166〜v2.1.167 のリリースノート解説。モデル過負荷時の対策として最大3つのフォールバックモデル指定が可能になり、対話セッション中でも自動切り替えが動作。deny ルールに glob パターン対応でホワイトリスト運用が容易に。クロスセッションメッセージの権限昇格問題を修正し、JetBrains IDE や各種ターミナルでの不具合も解消。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/dab2d73fbb0ce6eea33d)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.166〜v2.1.167 リリース｜毎日Changelog解説

Claude Code v2.1.166〜v2.1.167がリリースされ、モデル過負荷への対策が大幅強化された。fallbackModelを最大3つまで設定可能になり、対話セッション中でも自動切り替えが効くようになった。deny ルールでのglob対応によりホワイトリスト運用が容易になり、クロスセッション権限の脆弱性も修正された。その他、IDE連携やターミナル互換性、Windows/macOS固有のバグなど多数の修正が含まれる。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/dab2d73fbb0ce6eea33d)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-06-04

### Claude Code v2.1.162: 権限制御バグ修正とagents大幅改善まとめ

Claude Code v2.1.162 がリリースされ、WebFetch の権限ルール適用漏れ、Windows 環境でのパス照合不具合など、セキュリティ・権限制御に関わる重要なバグが修正されました。特に組み込みの事前承認ドメインへの明示的な deny/allow ルールが今まで無視されていた問題や、Windows でのバックスラッシュ・大文字小文字の違いによるルール不一致が解消されています。また claude agents コマンドの大規模な不具合修正、MCP タイムアウト設定の誤動作修正、起動表示の UX 改善も含まれています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/49ff0025c97ab6ac1430)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, windows

---

## 2026-06-03

### Claude Code v2.1.162 リリース｜毎日Changelog解説

Claude Code v2.1.162 がリリースされました。主な変更点は、スラッシュコマンドのクリック挙動の変更（即実行から入力欄への挿入に変更）、WebFetch の権限ルールがプリアプルーブドドメインより優先されるようになった点、MCP のタイムアウト処理の修正です。その他、claude agents の表示崩れや Windows の権限ルール、LSP ツールなど複数のバグが修正されています。新機能は少なく、既存機能の磨き込みと安定性向上に焦点を当てたリリースです。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/c31d5e74c50848db7859)
- **重要度**: 6/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.162 リリース｜毎日Changelog解説

Claude Code v2.1.162がリリース。主な変更点は、スラッシュコマンドのクリック挙動が即実行から挿入+Enter方式に変更、WebFetchの権限ルールがプリアプルーブドドメインより優先されるよう修正、MCPのタイムアウトが1000ms未満でも全ツールが停止しないバグ修正など。Windows環境での権限ルール処理やclaude agentsの表示崩れも修正された。新機能は控えめで、既存機能の磨き込みとバグ修正が中心のリリース。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/c31d5e74c50848db7859)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, mcp

---

### Claude Code Dynamic Workflows解説：1,000サブエージェント並列とOpus 4.8

AnthropicがClaude CodeにDynamic Workflowsを追加。JavaScriptスクリプトで最大1,000サブエージェントを並列オーケストレーションし、コンテキスト飽和を回避。同時にClaude Opus 4.8リリースとFast Mode価格を3分の1に値下げ。計画をコードに移すことで、大規模コードベースのマイグレーションやリサーチで従来より信頼性の高い結果を実現。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-dynamic-workflows)
- **重要度**: 9/10
- **タグ**: claude-code, 新機能, opus

---

### Claude Code v2.1.152｜Skillを動的制御：disallowed-tools・/reload-skills・MessageDisplayフック

Claude Code v2.1.152では、スキル実行中に特定ツールを無効化する「disallowed-tools」フロントマターが追加され、セッション再起動なしでスキルを再読み込みする「/reload-skills」コマンドが実装されました。SessionStartフックにreloadSkills機能が追加され、MessageDisplayフックでアシスタント出力を表示前に変換可能になり、スキルとツールの動的制御が大幅に強化されました。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-v2-1-152-update)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, release

---

## 2026-06-02

### Claude Code v2.1.159〜v2.1.161 リリース｜毎日Changelog解説

Claude Code v2.1.159〜v2.1.161の3バージョンをまとめた解説記事。主な変更点は、シェル起動ファイルやビルドツール設定への書き込み時に確認プロンプトを追加、並列ツール呼び出しの独立化、grepで開いたファイルをRead不要でEdit可能に、MCPコマンドのシークレット保護強化など。acceptEditsモードでもセキュリティ重視の設計に変更された。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/1c20a1401487b278ecc9)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.160: workflowキーワードがultracodeに変更・セキュリティ強化

Claude Code v2.1.160がリリースされ、動的ワークフローのトリガーキーワードが「workflow」から「ultracode」に変更される破壊的変更が含まれています。シェル起動ファイルやビルドツール設定への書き込み前に確認を求めるセキュリティ強化、バックグラウンドセッションの会話履歴喪失やWindows/WSL環境の不具合修正も実施されました。既存のワークフローやCLAUDE.mdファイルを使用している場合、キーワードの更新が必要です。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/59b8378b59d036048cf7)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.159〜v2.1.161 リリース｜毎日Changelog解説

Claude Code v2.1.159〜v2.1.161のリリース内容を解説。シェル起動ファイルやビルドツール設定への書き込み時に確認プロンプトを追加し、意図しないコード実行を防止。並列ツール呼び出しが独立動作するようになり、1つの失敗が他に影響しない改善。grepで確認したファイルはReadを挟まずEditできるようになった。MCPコマンドでシークレット情報を非表示化する機能も追加。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/1c20a1401487b278ecc9)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-05-28

### Claude Code v2.1.153〜v2.1.154 リリース｜毎日Changelog解説

Claude Code v2.1.153〜v2.1.154のリリース解説。新モデルOpus 4.8が登場し、既定でhigh effortに設定され、最難関タスク向けに/effort xhighが新設された。数百のエージェントをバックグラウンドで束ねるdynamic workflowsが実装され、大規模タスクの並行処理が可能に。Fast modeは標準の2倍料金で2.5倍速と大幅に安価になり、lean system promptが全モデルで既定化された。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/d42ad8905e76c9b7a0c1)
- **重要度**: 8/10
- **タグ**: claude-code, opus, 新機能

---

### Claude Code v2.1.153〜v2.1.154 リリース｜毎日Changelog解説

Claude Code v2.1.153〜v2.1.154のリリースノート解説。新モデルOpus 4.8が登場し、既定でhigh effort、最難関タスク向けに/effort xhighを新設。数百エージェントをバックグラウンドで束ねるdynamic workflowsが実装され、大規模タスクの並列処理が可能に。Fast modeが標準の2倍料金で2.5倍速に改善され、以前より大幅に安価になった。lean system promptが既定化され、/modelの選択がデフォルト保存されるなど、UI/UX改善と複数のバグ修正を実施。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/d42ad8905e76c9b7a0c1)
- **重要度**: 8/10
- **タグ**: claude-code, opus, 新機能

---

## 2026-04-19

### Claude CodeのRoutines機能で「寝ている間にPRが自動レビューされる」時代へ

2026年4月14日、AnthropicがClaude CodeにRoutines機能をリサーチプレビューとして追加。PCを閉じていてもクラウド上でAIが自律的にタスクを実行し続ける。定期実行・APIトリガー・GitHubイベント連動が可能で、PRの自動レビューや夜間のバグ修正PRの作成などが実現できる。ただし承認なしで動作するため、プロンプトインジェクションなどセキュリティリスクへの注意が必要。

- **ソース**: [Qiita claudecode](https://qiita.com/tai0921/items/a6323df5024b1d3a9b27)
- **重要度**: 9/10
- **タグ**: claude-code, 新機能, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-19 | 自動生成 |
