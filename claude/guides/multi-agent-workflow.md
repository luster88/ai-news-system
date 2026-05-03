---
title: Multi Agent Workflow
category: guides
subcategory: multi-agent-workflow
tags:
- claude-code
- cowork
- cursor
- prompt
- 新機能
date: '2026-03-29'
updated: '2026-05-03'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s6jouf/anthropic_shares_how_to_make_claude_code_better
  title: Anthropic shares how to make Claude code better with a harness
  date: '2026-03-29'
- url: https://qiita.com/Tadashi_Kudo/items/ce29e76f94d3a0b64dac
  title: Claude / Codex / Cursor を「中立層」で束ねる：AI-AGENT.md 設計と adapter pattern
  date: '2026-04-29'
- url: https://zenn.dev/taroh_7/articles/2026-04-18-ai-career-strategy-multiagent
  title: Claude Codeでキャリア戦略レポートの作り方を自動化した話
  date: '2026-05-03'
---



# Multi Agent Workflow

---

## 2026-05-03

### Claude Codeでキャリア戦略レポートの作り方を自動化した話

Claude Codeで複数のエージェントを並列動作させ、個人向けキャリア戦略レポートを自動生成した事例。調査エージェントと批判専用の検証エージェントを分離し、楽観バイアスを補正する設計が特徴。市場分析、スキルギャップ、キャリアシナリオ（楽観・現実・保守）、学習ロードマップ、リスク分析を含む長文レポートを出力し、意思決定に使える実用的な成果物を作成した。

- **ソース**: [Zenn claude](https://zenn.dev/taroh_7/articles/2026-04-18-ai-career-strategy-multiagent)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-29

### Claude / Codex / Cursor を「中立層」で束ねる：AI-AGENT.md 設計と adapter pattern

複数のAIコーディングエージェント（Claude Code、Codex CLI、Cursor）を併用する際に、共通ルールの重複管理問題をAdapter Patternで解決する設計手法を解説。中立層のAI-AGENT.mdを正本とし、各ランタイム固有の差分だけを個別ファイルに記述することで、DRY原則を保ちながらルールの一元管理を実現。Hexagonal Architectureの発想をAIエージェント運用に適用した実践的アプローチ。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/ce29e76f94d3a0b64dac)
- **重要度**: 7/10
- **タグ**: claude-code, cursor, cowork

---

## 2026-03-29

### Anthropic shares how to make Claude code better with a harness

Anthropic が Claude のコード生成品質を向上させる「ハーネス設計」手法を公式ブログで公開。長時間作業時の「コンテキスト不安」と「自己評価バイアス」を解決するため、GAN にヒントを得た複数エージェント構成（Generator・Evaluator・Planner）を提案。フロントエンド開発では4つの評価基準で5-15回の改訂を行い、フルスタック開発では3エージェント構成を採用することで、単独実行時と比較して大幅に高品質で美しいコードが生成される。将来的により強力なモデル（Opus 4.6など）では不要なハーネス要素を削減すべきとも示唆。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s6jouf/anthropic_shares_how_to_make_claude_code_better)
- **重要度**: 8/10
- **タグ**: claude-code, prompt, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-29 | 自動生成 |
