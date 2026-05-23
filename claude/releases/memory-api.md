---
title: Memory Api
category: releases
subcategory: memory-api
tags:
- claude-api
- release
- 新機能
date: '2026-05-23'
updated: '2026-05-23'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/402879f0c01c2c746d13
  title: Anthropic Memory APIとは何か——Managed Agentsの「記憶」設計を読み解く
  date: '2026-05-23'
---

# Memory Api

---

## 2026-05-23

### Anthropic Memory APIとは何か——Managed Agentsの「記憶」設計を読み解く

Anthropicが2025年5月に公開したMemory APIは、Managed Agentsプラットフォーム上でエージェントがセッション間で記憶を保持する公式機能。ファイルシステム型のMemory Storeを採用し、Claudeが得意なBash操作で記憶を整理できる設計。Optimistic Concurrencyで並列書き込みを制御し、Permission Scopeで読み書き権限を管理。同時発表のDreamingは複数セッションを横断分析してパターンを自動抽出する。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/402879f0c01c2c746d13)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-23 | 自動生成 |
