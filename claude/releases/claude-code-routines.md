---
title: Claude Code Routines
category: releases
subcategory: claude-code-routines
tags:
- bugfix
- claude-code
- opus
- release
- 新機能
date: '2026-04-19'
updated: '2026-06-02'
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
---



# Claude Code Routines

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
