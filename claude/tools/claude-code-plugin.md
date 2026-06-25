---
title: Claude Code Plugin
category: tools
subcategory: claude-code-plugin
tags:
- claude-code
- cowork
- mcp
- setup
- vscode
- 新機能
date: '2026-04-01'
updated: '2026-06-25'
sources:
- url: https://qiita.com/Andhy/items/371621273924d74e9917
  title: 自作のClaude Codeのプラグインの有効性を検証してみたところなかなか良い結果に
  date: '2026-04-01'
- url: https://ai-heartland.com/agent/understand-anything-knowledge-graph-plugin
  title: Understand Anything入門：コードベースをナレッジグラフ化するClaude Codeプラグイン
  date: '2026-04-26'
- url: https://www.reddit.com/r/ClaudeAI/comments/1t3osat/built_a_plugin_so_my_parallel_claude_code
  title: built a plugin so my parallel Claude Code sessions can message each other
    instead of me alt-tabbing
  date: '2026-05-04'
- url: https://ai-heartland.com/agent/tzachbon-smart-ralph-spec-driven-claude-code
  title: Smart Ralph｜Claude Code/Codexにspec-driven開発を持ち込む14コマンド・6エージェント基盤
  date: '2026-05-09'
- url: https://zenn.dev/qvtec/articles/b66911e2e9a829
  title: Claude Code の結果を喋ってくれるプラグインを作った
  date: '2026-06-16'
- url: https://qiita.com/bhryan1013/items/a0cf32aecd42fc64ae90
  title: Claude Codeの「考え中…」の待ち時間を、開発ニュースのフィードに変えるプラグインを作った
  date: '2026-06-25'
---






# Claude Code Plugin

---

## 2026-06-25

### Claude Codeの「考え中…」の待ち時間を、開発ニュースのフィードに変えるプラグインを作った

Claude Codeの待ち時間中にHacker NewsやGitHub Trendingなどの開発ニュースをステータスラインに表示するプラグイン「claudenews」が公開された。エージェントの動作をhookで検知し、バックグラウンドでニュースを取得・キャッシュする。ハイパーリンク対応ターミナルではクリック可能で、OSの言語設定に応じて自動翻訳される。コンテキストの喪失を防ぎながら待ち時間を有効活用できる。

- **ソース**: [Qiita claude](https://qiita.com/bhryan1013/items/a0cf32aecd42fc64ae90)
- **重要度**: 5/10
- **タグ**: claude-code, vscode, setup

---

## 2026-06-16

### Claude Code の結果を喋ってくれるプラグインを作った

Claude Code の実行完了や権限確認を音声で通知するプラグインの紹介。goal/auto mode 使用時に画面を見ていなくても結果を把握できるよう、OS標準のTTS機能で読み上げを実装。簡単なコマンドでインストール可能で、macOSとWSL2に対応。

- **ソース**: [Zenn claude](https://zenn.dev/qvtec/articles/b66911e2e9a829)
- **重要度**: 5/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-09

### Smart Ralph｜Claude Code/Codexにspec-driven開発を持ち込む14コマンド・6エージェント基盤

Smart Ralphは、Claude CodeとCodex CLIに対応したspec-driven開発プラグイン。曖昧な要件を研究→要件→設計→タスク→実装の5フェーズに分解し、6つの専門エージェントが処理する。タスクごとにコンテキストをリフレッシュすることでトークン消費を抑え、長時間の自律実行を実現。v3.0.0で外部依存を排除し、self-containedな実行ループへ移行した。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/tzachbon-smart-ralph-spec-driven-claude-code)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-05-04

### built a plugin so my parallel Claude Code sessions can message each other instead of me alt-tabbing

複数のClaude Codeセッション間で直接メッセージをやり取りできるプラグイン「Relay」が開発されました。フロントエンドとバックエンドなど異なるリポジトリで作業する際、ウィンドウ切り替えやコピー&ペーストなしで、Claude同士が直接通信できます。MCPサーバーのchannels機能を利用し、Unix socketを介してローカルマシン上で動作します。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1t3osat/built_a_plugin_so_my_parallel_claude_code)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-04-26

### Understand Anything入門：コードベースをナレッジグラフ化するClaude Codeプラグイン

Understand Anythingは、200,000行規模のコードベースをマルチエージェントパイプラインで解析し、ファイル・関数・依存関係を対話型ナレッジグラフとして可視化するClaude Codeプラグイン。Technical GraphとDomain Graphの2種類のビューを提供し、新規参画者が「コードを読む」ではなく「コードを探索する」アプローチを実現する。6種類の専門エージェントが協調動作し、インクリメンタル更新により大規模リポジトリでも分単位で解析完了する。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/understand-anything-knowledge-graph-plugin)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-04-01

### 自作のClaude Codeのプラグインの有効性を検証してみたところなかなか良い結果に

Claude Code用の自作プラグイン「Formal Agent Contracts」の有効性検証結果。AIにコードを書かせる前に仕様を形式言語（VDM-SL）で整理することで、ビジネスルールのカバー率が39%から82%に向上。特に複雑なシステム（オークションなど）で効果が顕著で、30回の試行で一貫した品質改善が確認された。

- **ソース**: [Qiita claude](https://qiita.com/Andhy/items/371621273924d74e9917)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-01 | 自動生成 |
