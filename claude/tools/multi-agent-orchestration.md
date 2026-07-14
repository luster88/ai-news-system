---
title: Multi Agent Orchestration
category: tools
subcategory: multi-agent-orchestration
tags:
- claude-code
- cowork
- cursor
- mcp
- prompt
- setup
- 新機能
date: '2026-04-02'
updated: '2026-07-14'
sources:
- url: https://ai-heartland.com/ai/gemini/oh-my-gemini
  title: oh-my-gemini：Gemini CLIのマルチエージェント並列実行ツール
  date: '2026-04-02'
- url: https://zenn.dev/interpark/articles/59108508d7dec0
  title: AIは役割だけでどこまで本気の議論ができるのか：ツール開発で得た学びと、会議そのものへの気づき
  date: '2026-04-20'
- url: https://ai-heartland.com/agent/ruflo-multi-agent-swarm-claude-code
  title: ruflo｜Claude Code/Codexにネイティブ統合する100エージェント・スウォーム基盤
  date: '2026-05-04'
- url: https://ai-heartland.com/agent/paseo-guide
  title: Paseo徹底解説｜複数AIコーディングエージェントを束ねるOSSオーケストレーター【AGPL】
  date: '2026-06-24'
- url: https://qiita.com/Koukyosyumei/items/9ff3ddef9c11a44bcb30
  title: Claude Code・Codexのマルチエージェント構成をコードで定義する技術 ― プログラマブル・オーケストレーション入門
  date: '2026-07-14'
---





# Multi Agent Orchestration

---

## 2026-07-14

### Claude Code・Codexのマルチエージェント構成をコードで定義する技術 ― プログラマブル・オーケストレーション入門

Claude CodeやCodexなどの複数のコーディングエージェントを組み合わせたマルチエージェントワークフローを、通常のPython/Rustコードとして記述・実行できるフレームワーク「h5i-orchestra」と「h5i-python」の解説記事。エージェント間の並行実行、相互レビュー、条件分岐、テスト検証、成果物選択などの複雑なオーケストレーションを、特別なDSLではなく自然なPythonコードで表現可能。各エージェントは独立したサンドボックスとGit worktree内で作業し、再現可能なワークフローとして管理できる。

- **ソース**: [Qiita claude](https://qiita.com/Koukyosyumei/items/9ff3ddef9c11a44bcb30)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, 新機能

---

### Claude Code・Codexのマルチエージェント構成をコードで定義する技術 ― プログラマブル・オーケストレーション入門

Claude CodeやCodexなど複数のコーディングエージェントを組み合わせたマルチエージェントワークフローを、通常のPython/Rustコードで記述・実行できるフレームワーク「h5i-orchestra」と「h5i-python」の紹介記事。並列実行、相互レビュー、条件分岐を含む複雑な開発プロセスを再現可能な形でプログラム化でき、各エージェントは独立したサンドボックスとGit worktree内で作業するため環境を汚染しない。Conductorクラスを中心に、エージェントの雇用、作業依頼、レビュー、成果物の検証・選択・適用までを一貫して管理できる。

- **ソース**: [Qiita claudecode](https://qiita.com/Koukyosyumei/items/9ff3ddef9c11a44bcb30)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, 新機能

---

## 2026-06-24

### Paseo徹底解説｜複数AIコーディングエージェントを束ねるOSSオーケストレーター【AGPL】

Paseoは、Claude Code・Codex・Copilot・OpenCode・Piなど複数のAIコーディングエージェントを1つのインターフェースで統合管理できるOSSオーケストレーター（AGPL-3.0、9.1k★）です。セルフホストで並列実行が可能で、音声操作やiOS/Android/Web/CLIのマルチデバイス対応、プライバシー重視（テレメトリなし）が特徴。複数エージェントを併用する際のターミナルやUI管理の煩雑さを解消します。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/paseo-guide)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 2026-05-04

### ruflo｜Claude Code/Codexにネイティブ統合する100エージェント・スウォーム基盤

rufloは、Claude Code/Codexにネイティブ統合する100エージェント・スウォーム基盤のOSSです。Anthropic公式のClaude Code SDKを土台に、複数の専門エージェントを協調させるオーケストレーション機能を提供し、SWE-benchスコア84.8%、APIコスト75%削減を実現しています。プラグイン形式で1コマンド導入でき、ユーザー側のCLIコマンドを変えずにスウォーム機能を透過的に注入できる点が特徴です。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/ruflo-multi-agent-swarm-claude-code)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-04-20

### AIは役割だけでどこまで本気の議論ができるのか：ツール開発で得た学びと、会議そのものへの気づき

複数AIが多角的に議論するWebUIツールの開発記録。Next.js + MCP構成で、CLAUDE.mdの指示書によるファシリテーター機能を実装。サブエージェント方式（claude -p --agents）を採用し、ベクトル検索導入によるコスト変動（35%悪化→49.5%削減）の実測データを公開。会議の質向上を目指した個人用ツールとして、AIファシリテーターが会議プロセスに与える影響を考察。

- **ソース**: [Zenn claude](https://zenn.dev/interpark/articles/59108508d7dec0)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, prompt

---

## 2026-04-02

### oh-my-gemini：Gemini CLIのマルチエージェント並列実行ツール

oh-my-geminiは、Gemini CLIのマルチエージェントオーケストレーションツールで、複数のGemini CLIワーカーを並列実行・調整する。Team Modeによりタスクを分散処理し、結果を統合することで大規模なAI支援ワークフローを効率化する。Claude向けのoh-my-claudecode（OMC）やCodex向けのoh-my-codex（OMX）が姉妹プロジェクトとして提供されている。

- **ソース**: [AI Heartland](https://ai-heartland.com/ai/gemini/oh-my-gemini)
- **重要度**: 4/10
- **タグ**: cowork, claude-code, cursor

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
