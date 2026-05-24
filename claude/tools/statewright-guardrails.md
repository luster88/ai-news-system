---
title: Statewright Guardrails
category: tools
subcategory: statewright-guardrails
tags:
- claude-code
- mcp
- performance
date: '2026-05-24'
updated: '2026-05-24'
sources:
- url: https://ai-heartland.com/agent/statewright-state-machine-ai-guardrails
  title: Statewright完全解説｜Rust製状態機械ガードレールがSWE-bench 2→10/10に変えた理由
  date: '2026-05-24'
---

# Statewright Guardrails

---

## 2026-05-24

### Statewright完全解説｜Rust製状態機械ガードレールがSWE-bench 2→10/10に変えた理由

StatewrightはRust製のOSSで、AIエージェントに状態機械ガードレールを追加し、各フェーズで呼べるツールをMCPとフックでプロトコル層から制限する。Claude Codeなどに40以上のツールを与えると、モデルが同じファイルを繰り返し読んだりテスト前にデプロイしようとするが、Statewrightは「問題を小さくする」ことで、planning→implementing→testing→completedというフェーズ定義により各フェーズで5個以下のツールに絞り込む。SWE-benchの内部選定5タスクで2/10→10/10の改善を示し、「同じファイル読み込みループ死の阻止」と「ツール空間絞り込みによる推論改善」の2つの構造的効果を実現した。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/statewright-state-machine-ai-guardrails)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-24 | 自動生成 |
