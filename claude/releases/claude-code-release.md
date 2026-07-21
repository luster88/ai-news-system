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
updated: '2026-07-21'
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
- url: https://qiita.com/moha0918_/items/9be8047b5f9980465623
  title: Claude Code v2.1.212｜暴走ループにセッション上限｜毎日Changelog解説
  date: '2026-07-17'
- url: https://zenn.dev/galirage/articles/code-with-claude-2026-london-summary
  title: Claudeの開発者イベント「Code with Claude 2026」総まとめ〜ロンドン編〜
  date: '2026-07-17'
- url: https://qiita.com/moha0918_/items/6c6646ec2759b63216c5
  title: Claude Code v2.1.214｜permission チェックの穴が一斉に塞がる｜毎日Changelog解説
  date: '2026-07-18'
- url: https://qiita.com/moha0918_/items/cec53cc700e513ac13d7
  title: Claude Code v2.1.215｜/verify・/code-review の自動実行が止まる｜毎日Changelog解説
  date: '2026-07-19'
- url: https://qiita.com/moha0918_/items/2ad6f36fd302017b9267
  title: Claude Code v2.1.216〜v2.1.217｜サブエージェントの無制限増殖に上限｜毎日Changelog解説
  date: '2026-07-21'
---







# Claude Code Release

---

## 2026-07-21

### Claude Code v2.1.216〜v2.1.217｜サブエージェントの無制限増殖に上限｜毎日Changelog解説

Claude Code v2.1.216〜v2.1.217 でサブエージェントの制御が強化されました。デフォルトで同時実行が20並列に制限され、ネストした生成も無効化。予算上限到達時にバックグラウンドエージェントも停止するようになり、長セッションでの応答遅延バグも修正されました。多段エージェント構成を使用している場合は環境変数の設定が必要です。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/2ad6f36fd302017b9267)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-07-19

### Claude Code v2.1.215｜/verify・/code-review の自動実行が止まる｜毎日Changelog解説

Claude Code v2.1.215 で /verify と /code-review の自動実行が廃止されました。これまで Claude が自動的に検証やレビューを起動していましたが、今後は明示的にコマンドを実行する必要があります。トークン消費が予測しやすくなる一方、自動検証に依存していたワークフローは手順の見直しが必要です。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/cec53cc700e513ac13d7)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.215｜/verify・/code-review の自動実行が止まる｜毎日Changelog解説

Claude Code v2.1.215 で /verify と /code-review コマンドが自動実行されなくなり、明示的な呼び出しが必要になりました。これまで Claude が自動で検証やレビューを開始していましたが、今後はユーザーが意図的にコマンドを実行する必要があります。トークン消費が予測しやすくなる一方、自動検証を前提としたワークフローは見直しが必要です。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/cec53cc700e513ac13d7)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-18

### Claude Code v2.1.214｜permission チェックの穴が一斉に塞がる｜毎日Changelog解説

Claude Code v2.1.214 では、permission チェックの重大なバグが修正されました。Edit(src/**) のような allow ルールがツリー内のどこにある src/ への書き込みも自動承認していた問題が解消され、<cwd>/src のみに限定されました。Bash の permission チェックも厳格化され、10,000 文字超のコマンドや FD リダイレクトなどが自動承認されなくなりました。また、悪質な利用や脱獄試行に対して Claude 側からセッションを終了できる EndConversation ツールが追加されました。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/6c6646ec2759b63216c5)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.214｜permission チェックの穴が一斉に塞がる｜毎日Changelog解説

Claude Code v2.1.214 では、permission チェックの複数の脆弱性が修正されました。Edit(src/**) のような allow ルールが意図せず深い階層の src/ ディレクトリまで自動承認していたバグが修正され、<cwd>/src のみに限定されました。Bash コマンドの permission チェックも厳格化され、10,000 文字超のコマンドや FD リダイレクト、zsh の特殊構文が自動承認されなくなりました。また、docker のデーモンリダイレクトフラグや悪質な利用に対する EndConversation ツールが追加され、セキュリティが大幅に強化されています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/6c6646ec2759b63216c5)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-07-17

### Claude Code v2.1.212｜暴走ループにセッション上限｜毎日Changelog解説

Claude Code v2.1.212で、WebSearchとサブエージェント生成にセッション上限（デフォルト200回）が追加され、暴走ループを防止する安全弁が実装されました。Plan modeが許可なしにファイルを書き換えていた重大なバグが修正され、/forkコマンドがバックグラウンドセッション化に変更されました。MCPツールは2分超で自動的にバックグラウンド実行され、worktreeのsymlink経由でリポジトリ外に書き込む脆弱性も修正されています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/9be8047b5f9980465623)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

### Claudeの開発者イベント「Code with Claude 2026」総まとめ〜ロンドン編〜

2026年5月19日にロンドンで開催されたAnthropicの開発者カンファレンス「Code with Claude 2026」の総まとめ記事。全24セッションから、Claude APIの利用量が前年比17倍に拡大したこと、Self-hosted sandboxes、MCP tunnels、Routines、CI Autofix、Claude Code Desktopなど6つの新機能が発表された。Spotify、Shopify、Mercado Libreなどの企業事例も紹介され、Auto ModeやAuto Memoryなどの機能アップデートが詳説されている。

- **ソース**: [Zenn claude](https://zenn.dev/galirage/articles/code-with-claude-2026-london-summary)
- **重要度**: 9/10
- **タグ**: claude-code, 新機能, release

---

### Claude Code v2.1.212｜暴走ループにセッション上限｜毎日Changelog解説

Claude Code v2.1.212 では、WebSearch とサブエージェント生成にセッション単位で 200 回の上限が導入され、無限ループによる暴走を防止。Plan mode が承認なしでファイル変更コマンドを実行していたバグと、worktree の symlink を悪用してリポジトリ外にファイルを書き込める脆弱性が修正された。また、/fork コマンドの挙動が変更され、新しいバックグラウンドセッションに会話を複製する方式に刷新された。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/9be8047b5f9980465623)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

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
