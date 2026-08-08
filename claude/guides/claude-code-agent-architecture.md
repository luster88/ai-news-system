---
title: Claude Code Agent Architecture
category: guides
subcategory: claude-code-agent-architecture
tags:
- claude-api
- claude-code
- cowork
- mcp
- performance
- prompt
- setup
- 新機能
date: '2026-04-15'
updated: '2026-08-08'
sources:
- url: https://zenn.dev/chiakidayo/articles/agent-teams-subagent-comparison
  title: 【Claude Code】Agent teamsとSubagent並列実行比較メモ
  date: '2026-04-15'
- url: https://qiita.com/bit-tanghao/items/bec927ebf9621d131d9e
  title: AIエージェントシリーズ 第5弾｜プランニングAgent——大きなPRを自動分解して実行する
  date: '2026-04-20'
- url: https://ai-heartland.com/explain/agent-provenance-commit-dag-knowledge-graph
  title: AIエージェントの出力に来歴を残す設計｜コミットDAGと知識グラフで根拠を追える状態にする
  date: '2026-07-27'
- url: https://qiita.com/kkaattoo/items/ed08671ba6374d8b8a75
  title: CLAUDE.md に書くこと・書かないことの判断基準
  date: '2026-08-02'
- url: https://zenn.dev/collabostyle/articles/1a8dfea6cee9ae
  title: Claude in Chrome 導入紹介
  date: '2026-08-02'
- url: https://qiita.com/syun136_616/items/d0030020308534fd896c
  title: Claude CodeとCodexを活用したタスク管理の方法
  date: '2026-08-05'
- url: https://zenn.dev/subagent_lab/articles/claude-code-slash-commands-current-spec
  title: Claude Codeのカスタムスラッシュコマンドは今どう書くのか ― v2.1.221で全部試した
  date: '2026-08-05'
- url: https://ai-heartland.com/explain/claude-code-cross-session-messaging
  title: Claude Code cross-session messaging解説｜別セッションに伝言を送る仕組みを実測
  date: '2026-08-08'
---






# Claude Code Agent Architecture

---

## 2026-08-08

### Claude Code cross-session messaging解説｜別セッションに伝言を送る仕組みを実測

Claude Codeの複数セッション間でメッセージをやり取りする機能「cross-session messaging」の詳細解説。別々のターミナルで動作する複数のClaude Codeセッション間で、Claudeが自動的に宛先を発見し、破壊的変更の通知や並行作業の同期を実現する。v2.1.224以降で利用可能。ツールはListAgentsとSendMessageだが、ユーザーが直接呼ぶ必要はなく、自然文で指示するだけで動作する。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-cross-session-messaging)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-08-05

### Claude CodeとCodexを活用したタスク管理の方法

Claude CodeとCodexを中～大規模開発のタスク管理に活用する方法を解説。タスクの明確化、細分化、優先順位付けの重要性を説明し、AIによる自動化で開発者の時間を節約しエラーを軽減できるとしている。実例として、テストケース自動生成により手動テスト時間を80％削減した事例を紹介。AIへの過度な依存によるスキル低下リスクなどデメリットにも言及している。

- **ソース**: [Qiita claude](https://qiita.com/syun136_616/items/d0030020308534fd896c)
- **重要度**: 4/10
- **タグ**: claude-code, cowork, 新機能

---

### Claude Codeのカスタムスラッシュコマンドは今どう書くのか ― v2.1.221で全部試した

Claude Code v2.1.221におけるカスタムスラッシュコマンドの実装仕様を全パターン検証した記事。.claude/commands/*.mdは現行版でも動作し移行不要だが、新規作成時はSkills形式が推奨される。引数展開($0が1番目)、動的コンテキスト(!`コマンド`)、allowed-tools、modelオプションなどを実測で確認し、公式ドキュメントに記載のない挙動の違いを明らかにしている。

- **ソース**: [Zenn claude](https://zenn.dev/subagent_lab/articles/claude-code-slash-commands-current-spec)
- **重要度**: 7/10
- **タグ**: claude-code

---

## 2026-08-02

### CLAUDE.md に書くこと・書かないことの判断基準

CLAUDE.mdはセッションごとに全文読み込まれるため、コンテキスト消費を抑える必要がある。判断基準は「削除するとClaudeがミスするか」であり、推測できる一般的なルールは不要。書くべきは独自の実装ルールやプロジェクト固有の方針のみ。.claude/rules/でトピック別に分割でき、pathsで条件付き読み込みも可能だが、同時に読み込まれれば行数削減にはならない。

- **ソース**: [Qiita claude](https://qiita.com/kkaattoo/items/ed08671ba6374d8b8a75)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

### Claude in Chrome 導入紹介

Claude Code から Chrome 拡張機能を経由してブラウザ操作が可能になる Claude in Chrome の機能を紹介。MCP 経由で Chrome を操作し、実装したコードの動作確認やブラウザテストを自動化できる。Google 検索を例に、タブ操作・検索・結果確認・記録保存までの一連の流れを Claude に任せる実例を解説。

- **ソース**: [Zenn claude](https://zenn.dev/collabostyle/articles/1a8dfea6cee9ae)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-07-27

### AIエージェントの出力に来歴を残す設計｜コミットDAGと知識グラフで根拠を追える状態にする

AIエージェントを並列化すると出力の根拠や来歴が追えなくなる問題を、コミットDAGと知識グラフを用いた4層の記憶設計で解決する手法を解説。会話ログ、成果物、コミットDAG、知識グラフの各層が答える質問の違いを明確にし、並列ワーカーの発見が要約でしか外に出られない情報の目詰まりを解消する。Anthropicの5つのワークフローパターンに対する永続層の役割も整理している。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/agent-provenance-commit-dag-knowledge-graph)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-20

### AIエージェントシリーズ 第5弾｜プランニングAgent——大きなPRを自動分解して実行する

大規模なPRレビューを効率化するため、Plan-and-Executeパターンを実装したAIエージェントの解説記事。ReActループの欠点（ファイル数に比例したステップ増加と一貫性の欠如）を克服し、事前計画フェーズと実行フェーズの分離により、全体を見渡した効率的なレビューを実現。静的解析（正規表現・AST）とLLMを組み合わせ、セキュリティやパフォーマンスの問題を自動検出・改善提案する実装を紹介。

- **ソース**: [Qiita claude](https://qiita.com/bit-tanghao/items/bec927ebf9621d131d9e)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 2026-04-15

### 【Claude Code】Agent teamsとSubagent並列実行比較メモ

Claude Codeの2つのマルチエージェント機能を比較した記事。Subagent並列実行は独立したタスクをMain Agent主導で効率的に処理し、トークン消費が少ない。一方Agent teamsは各Agentが独立したインスタンスを持ち、エージェント間で直接やり取りしながら複雑なタスクを協働処理できるが、トークン消費は多い。タスクの独立性と協働の必要性に応じて使い分けることが推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/chiakidayo/articles/agent-teams-subagent-comparison)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-15 | 自動生成 |
