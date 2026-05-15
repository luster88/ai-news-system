---
title: Performance Optimization
category: troubleshooting
subcategory: performance-optimization
tags:
- claude-code
- performance
- setup
date: '2026-05-15'
updated: '2026-05-15'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/60adfc41690c45d59f15
  title: ハーネスを育てすぎたClaude Codeが素のClaude Codeに負ける「naked codex現象」——自己診断と対処法
  date: '2026-05-15'
---

# Performance Optimization

---

## 2026-05-15

### ハーネスを育てすぎたClaude Codeが素のClaude Codeに負ける「naked codex現象」——自己診断と対処法

Claude Code のカスタマイズを過度に行うと、設定ファイルやスキルが肥大化し、素の Claude Code よりパフォーマンスが低下する「naked codex現象」が発生する。CLAUDE.md が400行超、スキル40件超、hook10件超が警戒ライン。原因はコンテキストウィンドウの圧迫と指示の優先順位の乱れ。対処法として、使われていないルールやスキルの定期的な棚卸し、コマンドファイルへの移行、ネガティブルールの削除が推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/60adfc41690c45d59f15)
- **重要度**: 7/10
- **タグ**: claude-code, performance, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-15 | 自動生成 |
