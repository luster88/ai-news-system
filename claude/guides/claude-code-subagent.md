---
title: Claude Code Subagent
category: guides
subcategory: claude-code-subagent
tags:
- claude-code
- performance
- 新機能
date: '2026-06-14'
updated: '2026-06-14'
sources:
- url: https://zenn.dev/mdtechknowledge/articles/claude-code-subagent-readonly-switch
  title: Claude Code サブエージェントの歩き方 — Explore が read-only な理由と切替の仕組み
  date: '2026-06-14'
---

# Claude Code Subagent

---

## 2026-06-14

### Claude Code サブエージェントの歩き方 — Explore が read-only な理由と切替の仕組み

Claude Codeのサブエージェント（メインエージェントが委任する単一の作業者）の仕組みを解説。Explore/Plan/general-purposeなど複数タイプがあり、Explore/Planは意図的にread-only設計となっている。v2.1.172以降はサブエージェント自身がさらに下位のサブエージェントを最大5階層まで呼び出せるようになり、Dynamic Workflowsの並列数（最大1,000）と階層の深さ（最大5）の2軸で拡張可能になった。

- **ソース**: [Zenn claude](https://zenn.dev/mdtechknowledge/articles/claude-code-subagent-readonly-switch)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-14 | 自動生成 |
