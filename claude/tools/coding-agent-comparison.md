---
title: Coding Agent Comparison
category: tools
subcategory: coding-agent-comparison
tags:
- claude-code
- copilot
- cowork
- cursor
- performance
- pricing
date: '2026-03-29'
updated: '2026-06-23'
sources:
- url: https://zenn.dev/sn0w_easy/articles/7c610896f4d08e
  title: 格安コーディングエージェントCodexのススメ
  date: '2026-03-29'
- url: https://ai-heartland.com/tool/codebuff-ai-coding-agent
  title: Codebuff徹底解説｜Claude Codeを61% vs 53%で上回る4エージェント型OSS
  date: '2026-05-16'
- url: https://zenn.dev/marvelousu/articles/sakana-fugu-vs-claude-codex
  title: Sakana Fugu と Claude Code/Codex を同じプロンプトで回して比べた — いま乗り換えないと判断した理由
  date: '2026-06-23'
---



# Coding Agent Comparison

---

## 2026-06-23

### Sakana Fugu と Claude Code/Codex を同じプロンプトで回して比べた — いま乗り換えないと判断した理由

Claude Code/Codex と Sakana Fugu を同一プロンプトで実測比較した結果、品質は横並びだがコストと速度で差がついた。Fugu Ultra はコストが約20倍、内部処理で約8,180トークンを消費し、速度も数倍遅い。既存ユーザーには急な乗り換えは不要で、速度・コストを重視するなら Claude/OpenAI を直接使うほうが無難と結論づけている。

- **ソース**: [Zenn claude](https://zenn.dev/marvelousu/articles/sakana-fugu-vs-claude-codex)
- **重要度**: 6/10
- **タグ**: claude-code, performance, pricing

---

## 2026-05-16

### Codebuff徹底解説｜Claude Codeを61% vs 53%で上回る4エージェント型OSS

Codebuffは4つの専門エージェント（File Picker、Planner、Editor、Reviewer）で役割分担するOSSのAIコーディングエージェント。独自評価でClaude Codeを61% vs 53%で上回ると主張。OpenRouter経由で任意のLLMを選択でき、エージェントごとに異なるモデルを割り当て可能。Apache-2.0ライセンスでスター5.3k、サブスク版CLI・SDK・広告版Freebuffの3形態で提供。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/codebuff-ai-coding-agent)
- **重要度**: 6/10
- **タグ**: claude-code, copilot, cowork

---

## 2026-03-29

### 格安コーディングエージェントCodexのススメ

Codex（OpenAI製コーディングエージェント）の紹介記事。Claude Codeは月額$100-200必要だが、Codexは同等性能を月額$20で利用可能と価格面で大きな優位性を持つ。CLI版の使い方、AGENTS.md（エージェント用README）の作成方法、Planモードでの実装計画立案、Agent Skills（再利用可能な専門知識ファイル）の活用方法を解説している。

- **ソース**: [Zenn claude](https://zenn.dev/sn0w_easy/articles/7c610896f4d08e)
- **重要度**: 6/10
- **タグ**: claude-code, cursor, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-29 | 自動生成 |
