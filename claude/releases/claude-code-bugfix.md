---
title: Claude Code Bugfix
category: releases
subcategory: claude-code-bugfix
tags:
- bugfix
- claude-code
- cowork
- mac
- mcp
- opus
- pricing
- release
- 新機能
date: '2026-07-16'
updated: '2026-09-02'
sources:
- url: https://qiita.com/moha0918_/items/c8b144e3ba36744b964b
  title: Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説
  date: '2026-07-16'
- url: https://qiita.com/moha0918_/items/e534c1c6270347af0a5c
  title: Claude Code v2.1.219｜Opus 5 が新デフォルトに｜毎日Changelog解説
  date: '2026-07-24'
- url: https://qiita.com/picnic/items/fd81f1614b95cafdc830
  title: 'Claude Code v2.1.219: Opus 5追加とサブエージェント3階層化を解説'
  date: '2026-07-24'
- url: https://qiita.com/moha0918_/items/4a520c01ae3e04f211e4
  title: Claude Code v2.1.221｜zsh の [[ ]] で権限チェックが素通りしていた｜毎日Changelog解説
  date: '2026-08-04'
- url: https://qiita.com/moha0918_/items/e124c85649184c8a6922
  title: Claude Code v2.1.222｜worktree 隔離の穴が塞がる｜毎日Changelog解説
  date: '2026-08-05'
- url: https://qiita.com/moha0918_/items/8d9bb54bff914f7017cd
  title: Claude Code v2.1.224｜セッション間 SendMessage が解禁｜毎日Changelog解説
  date: '2026-08-07'
- url: https://www.reddit.com/r/ClaudeAI/comments/1vj4aqt/claude_code_now_lets_sessions_talk_to_each_other
  title: Claude Code now lets sessions talk to each other on macOS
  date: '2026-08-08'
- url: https://qiita.com/zhao-xy/items/463b310c8a9401a4f2e1
  title: Claude Codeが「セッション同士で会話」できるように。並列開発を変えるCross-session messagingとは？
  date: '2026-08-08'
- url: https://qiita.com/moha0918_/items/e0970dd96706c59e6b69
  title: Claude Code v2.1.231｜Slack の MCP OAuth が redirect URI で弾かれる問題を修正｜毎日Changelog解説
  date: '2026-08-13'
- url: https://qiita.com/moha0918_/items/9cdc566dadb9a8e30e1a
  title: Claude Code v2.1.258｜macOS 12 で起動できない退行が直る｜毎日Changelog解説
  date: '2026-09-02'
---








# Claude Code Bugfix

---

## 2026-09-02

### Claude Code v2.1.258｜macOS 12 で起動できない退行が直る｜毎日Changelog解説

Claude Code v2.1.258 がリリースされ、macOS 12 (Monterey) で起動できなかった退行バグが修正されました。v2.1.255 から発生していた起動失敗の問題が解消され、リモート/スケジュールセッションが権限承認の再送で落ちるバグも修正されています。新機能の追加はなく、バグフィックスのみのリリースです。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/9cdc566dadb9a8e30e1a)
- **重要度**: 4/10
- **タグ**: claude-code, bugfix, mac

---

## 2026-08-13

### Claude Code v2.1.231｜Slack の MCP OAuth が redirect URI で弾かれる問題を修正｜毎日Changelog解説

Claude Code v2.1.231 で、Slack など事前登録型 OAuth を使う MCP サーバーへのログインが redirect URI 不一致で失敗していた問題が修正されました。コールバックポートが毎回変わることが原因で、--callback-port オプションで固定ポートを指定可能になりました。古い認証情報が残っている場合は claude mcp logout で削除してから再ログインが必要です。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/e0970dd96706c59e6b69)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, bugfix

---

## 2026-08-08

### Claude Code now lets sessions talk to each other on macOS

Claude Code が macOS で複数のセッション間通信機能を追加しました。この機能により、異なるセッションが相互にやり取りできるようになりましたが、既存のサブエージェント機能との重複が指摘されています。コミュニティでは、この新機能の実用性や既存機能との関係性について議論が行われています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vj4aqt/claude_code_now_lets_sessions_talk_to_each_other)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, mac

---

### Claude Codeが「セッション同士で会話」できるように。並列開発を変えるCross-session messagingとは？

Claude Codeに複数セッション間で直接メッセージを送受信できる「Cross-session messaging」機能が追加された。従来は人間が各セッション間の情報伝達を担う必要があったが、SendMessageとListAgentsによりClaude同士が必要な情報のみを共有可能に。コンテキスト全体ではなく必要な情報だけを送信することでトークン消費を抑制し、並列開発の管理コストを削減できる。

- **ソース**: [Qiita claude](https://qiita.com/zhao-xy/items/463b310c8a9401a4f2e1)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-08-07

### Claude Code v2.1.224｜セッション間 SendMessage が解禁｜毎日Changelog解説

Claude Code v2.1.224で、別マシンで動作する複数セッション間でのSendMessageによる直接通信が可能になりました。ListAgentsで相手を探索し、crossSessionInboundで受信側の承認ルールを設定できます。また、sandboxのdeny設定の脆弱性修正、構造化環境変数の抽出機能、セルフホスト実行環境のサポートなど、多数の機能追加とバグ修正が含まれています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/8d9bb54bff914f7017cd)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.224｜セッション間 SendMessage が解禁｜毎日Changelog解説

Claude Code v2.1.224で、別マシンで動作するセッション間でのメッセージング機能（SendMessage/ListAgents）が追加されました。セルフホストランナー、zipからのプラグイン導入、sandboxのdeny抜け穴の修正、フィードバック共有時のsystem prompt含有など、複数の重要な機能追加とセキュリティ修正が含まれています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/8d9bb54bff914f7017cd)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-08-05

### Claude Code v2.1.222｜worktree 隔離の穴が塞がる｜毎日Changelog解説

Claude Code v2.1.222では、worktree隔離の重大な脆弱性が修正されました。これまで隔離セッションからメインのチェックアウトに破壊的なgitコマンドが実行できていましたが、隔離がファイル編集とBashの両方に適用されるようになりました。また、PreToolUseフックのツール制限迂回、SendMessageの権限分類器スルー、Remote Control自動起動の権限など、複数の権限境界の穴が同時に塞がれています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/e124c85649184c8a6922)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

### Claude Code v2.1.222｜worktree 隔離の穴が塞がる｜毎日Changelog解説

Claude Code v2.1.222で、worktree隔離セッションがメインチェックアウトに破壊的gitコマンドを実行できていた脆弱性が修正されました。PreToolUseフックの自動許可がツール制限を回避していた問題、SendMessageが権限分類器を通らなかった問題も同時に解決され、権限境界が3箇所で強化されています。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/e124c85649184c8a6922)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, release

---

## 2026-08-04

### Claude Code v2.1.221｜zsh の [[ ]] で権限チェックが素通りしていた｜毎日Changelog解説

Claude Code v2.1.221では、zshの[[]]構文を悪用したBashツールの権限チェック回避の脆弱性が修正されました。これまで承認なしで実行できていたコマンドが許可プロンプトの対象となり、特にallowルールで自動実行している環境では挙動が変わります。同時にMCPサーバーの初回ターン接続問題、サンドボックスの認証情報マスクモード追加、VSCodeのFocus view機能なども実装されました。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/4a520c01ae3e04f211e4)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, release

---

## 2026-07-24

### Claude Code v2.1.219｜Opus 5 が新デフォルトに｜毎日Changelog解説

Claude Code v2.1.219では、Opus 5が新しいデフォルトモデルとなり、1M contextとfast modeに対応しました。fast modeの対象モデルがOpus 4.7からOpus 5とOpus 4.8に変更され、サブエージェントのネスト深さがデフォルトで3階層まで可能になりました。Dynamic workflowの既定サイズがmedium（15エージェント未満）に変更され、sandboxのネットワーク制限機能も追加されています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/e534c1c6270347af0a5c)
- **重要度**: 8/10
- **タグ**: claude-code, opus, release

---

### Claude Code v2.1.219: Opus 5追加とサブエージェント3階層化を解説

Claude Code v2.1.219がリリースされ、新モデルClaude Opus 5（1Mトークンコンテキスト対応、fast mode料金は入力$10/出力$50 per Mtok）が追加されOpus選択時のデフォルトに。サブエージェントのネスト生成が深さ3まで拡大され、多段オーケストレーションの自律性が向上。managed MCPの許可/拒否リストにおける変数解決ロジックが変更され、環境変数とmanaged-settingsのenvのみから解決されるようBreaking Changeが導入された。Opus 4.7はfast mode対象外となり、利用チームは移行が必要。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/fd81f1614b95cafdc830)
- **重要度**: 8/10
- **タグ**: claude-code, opus, release

---

### Claude Code v2.1.219｜Opus 5 が新デフォルトに｜毎日Changelog解説

Claude Code v2.1.219 では Opus 5 が新しいデフォルトの Opus モデルとなり、1M context と fast mode に対応しました。/fast の対象モデルが Opus 5 と Opus 4.8 に変更され、Opus 4.7 が外れました。サブエージェントのネスト深さがデフォルトで 3 階層まで可能になり、Dynamic workflow の既定サイズが medium（15エージェント未満）に変更されました。sandbox.network.strictAllowlist の追加により、許可リスト外のホストへの通信を即座に拒否できるようになりました。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/e534c1c6270347af0a5c)
- **重要度**: 8/10
- **タグ**: claude-code, opus, release

---

### Claude Code v2.1.219: Opus 5追加とサブエージェント3階層化を解説

Claude Code v2.1.219がリリースされ、新モデルClaude Opus 5（1Mトークン対応、fast mode料金$10/$50）が追加されOpus選択時のデフォルトに。サブエージェントのネスト生成が深さ3まで拡大され、多段オーケストレーションが可能に。managed MCPの許可リストで環境変数解決ロジックが変更され、既存の構成に影響する可能性あり。Opus 4.7はfast mode対象外となり移行が必要。

- **ソース**: [Qiita claudecode](https://qiita.com/picnic/items/fd81f1614b95cafdc830)
- **重要度**: 8/10
- **タグ**: claude-code, opus, 新機能

---

## 2026-07-16

### Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説

Claude Code v2.1.211がリリースされ、Bedrock/Vertex/Mantle/Foundryでプロンプトキャッシュが機能せず、システムコンテキストの末尾が毎回新規トークンとして課金されていた重大なバグが修正されました。この不具合により、ゲートウェイ経由での会話が重なるほど無駄な入力トークン課金が積み上がっていました。新機能は--forward-subagent-textフラグの追加のみで、その他は権限とキャッシュ周りの挙動修正が中心となっています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/c8b144e3ba36744b964b)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-16 | 自動生成 |
