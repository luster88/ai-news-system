---
title: Claude Code Release
category: releases
subcategory: claude-code-release
tags:
- bugfix
- claude-code
- pricing
- release
- 新機能
date: '2026-06-05'
updated: '2026-07-16'
sources:
- url: https://qiita.com/picnic/items/0e8844c6590cb7dd838a
  title: Claude Code v2.1.163 新機能とバグ修正：バージョン強制機能が追加
  date: '2026-06-05'
- url: https://qiita.com/moha0918_/items/2b9faf5b4ab771d4496a
  title: Claude Code v2.1.210｜Write(path) 権限ルールに起動時警告｜毎日Changelog解説
  date: '2026-07-15'
- url: https://qiita.com/picnic/items/2623cb5a5f81928b4477
  title: Claude Code v2.1.210で強化された間接プロンプトインジェクション対策とworktree分離の修正
  date: '2026-07-15'
- url: https://qiita.com/moha0918_/items/c8b144e3ba36744b964b
  title: Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説
  date: '2026-07-16'
---



# Claude Code Release

---

## 2026-07-16

### Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説

Claude Code v2.1.211のリリース。Bedrock/Vertex/Mantle/Foundryでプロンプトキャッシュが効かず、システムコンテキスト末尾が毎リクエスト新規トークンとして課金されていた重大なバグが修正された。長いシステムプロンプトを使用していた場合、無駄な入力トークン課金が積み上がっていた。新機能として--forward-subagent-textフラグが追加され、サブエージェントの本文とthinkingをstream-jsonに出力可能に。PreToolUse hookのask判定がauto modeに上書きされない修正も実施。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/c8b144e3ba36744b964b)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 2026-07-15

### Claude Code v2.1.210｜Write(path) 権限ルールに起動時警告｜毎日Changelog解説

Claude Code v2.1.210では、settings.jsonのWrite(path)、NotebookEdit(path)、Glob(path)形式の権限ルールに起動時警告が追加され、Edit(path)とRead(path)への移行が推奨されている。worktree分離のサブエージェントがメインリポジトリを操作できていたバグや、ultracodeがwebhook経由で意図せず発火していた問題が修正された。権限設定を細かく記述しているユーザーや自動化環境を使用しているユーザーに影響がある。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/2b9faf5b4ab771d4496a)
- **重要度**: 6/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.210で強化された間接プロンプトインジェクション対策とworktree分離の修正

Claude Code v2.1.210のリリース情報。マルチエージェント運用時のセキュリティ強化が中心で、間接プロンプトインジェクション対策の強化、worktree分離の不具合修正、ultracodeキーワードの誤発火防止が実装された。settings.jsonの権限ルール（Write/NotebookEdit/Glob）に起動時警告が追加され、将来的な非推奨化に備えた移行が推奨される。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/2623cb5a5f81928b4477)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.210｜Write(path) 権限ルールに起動時警告｜毎日Changelog解説

Claude Code v2.1.210で、settings.jsonのWrite(path)系権限ルールに起動時警告が追加されました。Edit(path)とRead(path)への書き換えが推奨されます。また、worktreeの分離機能でサブエージェントがメインリポジトリを操作できていた問題や、ultracodeがwebhook経由でも発火していたセキュリティ問題が修正されました。チームで設定を共有している場合は早めの対応が必要です。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/2b9faf5b4ab771d4496a)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, release

---

## 2026-06-05

### Claude Code v2.1.163 新機能とバグ修正：バージョン強制機能が追加

Anthropic が Claude Code v2.1.163/v2.1.165 をリリース。組織向けバージョン強制機能（requiredMinimumVersion/requiredMaximumVersion）が追加され、古いバージョンの使用をブロック可能に。/plugin list コマンド追加、Stop/SubagentStop フックの改善に加え、claude -p ハング問題や Bedrock/Vertex/Foundry 利用時の API キーエラーなど複数のバグが修正された。CI/CD 環境やマネージドサービス利用者は早期アップデートが推奨される。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/0e8844c6590cb7dd838a)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-05 | 自動生成 |
