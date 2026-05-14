---
title: Context Management
category: guides
subcategory: context-management
tags:
- claude-code
- cowork
- prompt
date: '2026-05-14'
updated: '2026-05-14'
sources:
- url: https://zenn.dev/ksuzu/articles/14bd965827418d
  title: Claude Code で前回の続きをチケット番号から復元する
  date: '2026-05-14'
---

# Context Management

---

## 2026-05-14

### Claude Code で前回の続きをチケット番号から復元する

Claude Codeで作業文脈を復元する仕組みの実装例。チケット番号をキーに、Obsidian Vault内のtasks/<TICKET>ディレクトリに設計判断・進捗・引き継ぎメモを保存し、グローバルCLAUDE.mdの自動参照ルールで/compact後も前提を復元できるようにした運用方法。1サブチケット=1PR=1検証可能な成果物というルールで、worktreeとbranchを<TICKET>/<desc>形式で統一し、/task-initスキルでディレクトリ初期化を自動化している。

- **ソース**: [Zenn claude](https://zenn.dev/ksuzu/articles/14bd965827418d)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-14 | 自動生成 |
