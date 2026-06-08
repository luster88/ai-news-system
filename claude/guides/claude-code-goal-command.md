---
title: Claude Code Goal Command
category: guides
subcategory: claude-code-goal-command
tags:
- claude-code
- prompt
- setup
- 新機能
date: '2026-06-08'
updated: '2026-06-08'
sources:
- url: https://qiita.com/ussu_ussu_ussu/items/c216c970bd84ba0327d7
  title: Claude Code の /goal を使ってみる前に調べたことメモ
  date: '2026-06-08'
- url: https://qiita.com/ussu_ussu_ussu/items/c216c970bd84ba0327d7
  title: Claude Code の /goal を使ってみる前に調べたことメモ
  date: '2026-06-08'
---

# Claude Code Goal Command

---

## 2026-06-08

### Claude Code の /goal を使ってみる前に調べたことメモ

Claude Code v2.1.139 で追加された /goal コマンドの仕組みと使い方をまとめた実践メモ。終了条件を宣言すると作業モデルと判定モデル（Haiku）が分離して動作し、条件達成まで自動実行される。検証可能な明確な条件設定とトークン予算の指定が重要で、曖昧な条件では無限ループのリスクがある。trust dialog 承認済み環境が必須で、Plan mode との組み合わせが推奨される。

- **ソース**: [Qiita claude](https://qiita.com/ussu_ussu_ussu/items/c216c970bd84ba0327d7)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

### Claude Code の /goal を使ってみる前に調べたことメモ

Claude Code v2.1.139で追加された/goalコマンドの使い方を解説。完了条件を宣言すると、条件が満たされるまでClaudeが自動で作業を継続する機能。作業モデルと判定モデル（デフォルトはHaiku）を分離し、各ターン終了時に条件達成を自動判定する仕組み。検証可能な明確な終了状態を持つタスクに適しており、曖昧な条件ではトークンを消費し続けるリスクがある。トークン予算制限、証拠ベースの条件設定、タスク分割が推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/ussu_ussu_ussu/items/c216c970bd84ba0327d7)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-08 | 自動生成 |
