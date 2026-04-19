---
title: Agent Memory
category: guides
subcategory: agent-memory
tags:
- claude-api
- mcp
- prompt
date: '2026-04-19'
updated: '2026-04-19'
sources:
- url: https://qiita.com/bit-tanghao/items/20e0366ce3f08f291ce5
  title: '# 【AIエージェントシリーズ 第4弾】メモリを持つAgent：プロジェクト文脈を覚えているレビュアーを作る'
  date: '2026-04-19'
---

# Agent Memory

---

## 2026-04-19

### # 【AIエージェントシリーズ 第4弾】メモリを持つAgent：プロジェクト文脈を覚えているレビュアーを作る

Claude Agentに短期メモリ（messages配列）と長期メモリ（JSON）の2層構造を実装し、プロジェクト文脈を記憶するコードレビューAgentを構築。remember_rule/recall_historyツールでAgent自身が記憶を管理し、2回目以降のレビューで過去履歴を参照して指摘内容を変化させる。ReActパターンとツール連携でセッションをまたいだ記憶の永続化を実現。

- **ソース**: [Qiita claude](https://qiita.com/bit-tanghao/items/20e0366ce3f08f291ce5)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-19 | 自動生成 |
