---
title: Claude Code Quality Issue
category: troubleshooting
subcategory: claude-code-quality-issue
tags:
- bugfix
- claude-code
- performance
date: '2026-04-28'
updated: '2026-04-28'
sources:
- url: https://qiita.com/daisuke-nagata/items/437f92a3210fbfa99e62
  title: Claude Code 品質劣化 postmortem 解説——3バグから学んだプロンプト1行の重み
  date: '2026-04-28'
---

# Claude Code Quality Issue

---

## 2026-04-28

### Claude Code 品質劣化 postmortem 解説——3バグから学んだプロンプト1行の重み

Claude Codeが2026年3-4月に品質劣化した原因を公式postmortemから解説。①推論努力レベル(effort)がhighからmediumに変更、②thinkingブロックの過剰削除バグ、③プロンプト1行の追加で3%性能低下、という3つのバグが時系列で重なっていた。特に「テキストは25語以下」という冗長性削減プロンプトが評価で3%の性能低下を引き起こした点が衝撃的。影響はSonnet 4.6とOpus 4.6で、v2.1.116以降で修正済み。

- **ソース**: [Qiita claudecode](https://qiita.com/daisuke-nagata/items/437f92a3210fbfa99e62)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-28 | 自動生成 |
