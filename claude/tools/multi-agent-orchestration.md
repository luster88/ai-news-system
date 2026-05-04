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
- 新機能
date: '2026-04-02'
updated: '2026-05-04'
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
---



# Multi Agent Orchestration

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
