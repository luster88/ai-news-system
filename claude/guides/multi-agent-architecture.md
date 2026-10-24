---
title: Multi Agent Architecture
category: guides
subcategory: multi-agent-architecture
tags:
- claude-api
- cowork
- mcp
- performance
- prompt
- 新機能
date: '2026-04-24'
updated: '2026-10-24'
sources:
- url: https://qiita.com/bit-tanghao/items/29708ac044a58e8e0844
  title: 【AIエージェントシリーズ 第7弾】マルチAgent基礎：Anthropic Harness論文に学ぶ専門家チームレビューの作り方
  date: '2026-04-24'
- url: https://qiita.com/portalmatsuki/items/0d5fe7892b813f29a58a
  title: brain と hands を切り離す — エージェントの「手」はどこまで抽象化できるか
  date: '2026-09-18'
- url: https://qiita.com/hathibei7/items/b3b6aa8874aab70717ff
  title: サブエージェントはメインループに「畳む」べきか？Anthropicの記事をモックECサポートで実測してみた
  date: '2026-10-24'
---



# Multi Agent Architecture

---

## 2026-10-24

### サブエージェントはメインループに「畳む」べきか？Anthropicの記事をモックECサポートで実測してみた

Anthropic公式記事の「サブエージェントをメインループに統合すべきか」という主張を、モックECサポート環境で実測検証。組織図どおりに分けたサブエージェント構成(A)とシングルループ+スキル構成(B)を比較した結果、Bは平均2.1倍高速で1.7〜2.6倍低コストだった。品質面では明確な差は見られなかったが、ベンチマークが易しすぎて天井効果の可能性がある。Anthropicの推奨する段階的開示アプローチの有効性を実データで裏付けた。

- **ソース**: [Qiita claude](https://qiita.com/hathibei7/items/b3b6aa8874aab70717ff)
- **重要度**: 7/10
- **タグ**: claude-api, performance, 新機能

---

## 2026-09-18

### brain と hands を切り離す — エージェントの「手」はどこまで抽象化できるか

Anthropic が公開した「Scaling Managed Agents」の解説記事。エージェントアーキテクチャを brain（判断）と hands（実行）に分離し、セッション情報を外部化することで、応答時間を p50 で約60%、p95 で90%以上短縮。ハーネスを「ペット」から「家畜」（stateless で交換可能）に変え、MCP を含む任意のツールを統一インターフェースで接続可能にした設計思想を紹介。

- **ソース**: [Qiita claude](https://qiita.com/portalmatsuki/items/0d5fe7892b813f29a58a)
- **重要度**: 7/10
- **タグ**: mcp, claude-api, performance

---

## 2026-04-24

### 【AIエージェントシリーズ 第7弾】マルチAgent基礎：Anthropic Harness論文に学ぶ専門家チームレビューの作り方

Anthropic Harness論文に基づき、コードレビューAgentをマルチAgent構造に改良した実装解説。Self-evaluation Bias（自己評価バイアス）を回避するため、Security/Performance/Styleの3つの専門Agentに分離し、それぞれが担当観点のみを指摘する設計を採用。結果の重複排除とseverity順ソートを実装し、専門性の向上による多角的レビューの実現を確認。

- **ソース**: [Qiita claude](https://qiita.com/bit-tanghao/items/29708ac044a58e8e0844)
- **重要度**: 7/10
- **タグ**: claude-api, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-24 | 自動生成 |
