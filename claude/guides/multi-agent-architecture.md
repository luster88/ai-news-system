---
title: Multi Agent Architecture
category: guides
subcategory: multi-agent-architecture
tags:
- claude-api
- cowork
- prompt
date: '2026-04-24'
updated: '2026-04-24'
sources:
- url: https://qiita.com/bit-tanghao/items/29708ac044a58e8e0844
  title: 【AIエージェントシリーズ 第7弾】マルチAgent基礎：Anthropic Harness論文に学ぶ専門家チームレビューの作り方
  date: '2026-04-24'
---

# Multi Agent Architecture

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
