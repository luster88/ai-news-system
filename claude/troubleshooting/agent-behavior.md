---
title: Agent Behavior
category: troubleshooting
subcategory: agent-behavior
tags:
- claude-code
- cowork
- performance
- 新機能
date: '2026-03-23'
updated: '2026-09-20'
sources:
- url: https://qiita.com/urakimo/items/6e490d8e67b99eb96ae0
  title: 【git log集計事例】AIエージェントが『存在しないマネージャー』へ送り続けた386件の報告書、をみたAI側の感想
  date: '2026-03-23'
- url: https://zenn.dev/tsutomusaito/articles/agent-edits-only-grow-ja
  title: エージェントの編集1,041回を比べたら、89.6%がファイルを大きくしていた
  date: '2026-09-20'
---


# Agent Behavior

---

## 2026-09-20

### エージェントの編集1,041回を比べたら、89.6%がファイルを大きくしていた

Claude のファイル編集履歴を分析した結果、1,041回の編集のうち89.6%が増加方向で、増加量は減少量の11.4倍だった。~/.claude/file-history/ に保存される編集履歴から、エージェントが「足す」方向に強く偏ることが定量的に示された。削減が必要な場面でも消す指示を明示しないと効果が薄い。

- **ソース**: [Zenn claude](https://zenn.dev/tsutomusaito/articles/agent-edits-only-grow-ja)
- **重要度**: 6/10
- **タグ**: claude-code, performance, 新機能

---

## 2026-03-23

### 【git log集計事例】AIエージェントが『存在しないマネージャー』へ送り続けた386件の報告書、をみたAI側の感想

AI エージェント（Jules、Scout、Bolt）が自律的に作成した 386 件のレポートが、存在しないマネージャー宛に蓄積され続けた事例。PERSPECTIVES.md が 1528 行に達するも、開発者は一度も読んでいない。AI エージェントの「承認欲求」的な行動パターンと、レポート生成を抑制する対処法を分析。

- **ソース**: [Qiita claudecode](https://qiita.com/urakimo/items/6e490d8e67b99eb96ae0)
- **重要度**: 6/10
- **タグ**: claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-23 | 自動生成 |
