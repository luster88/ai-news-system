---
title: Claude Code Rules
category: troubleshooting
subcategory: claude-code-rules
tags:
- bugfix
- claude-code
- setup
date: '2026-04-10'
updated: '2026-04-10'
sources:
- url: https://zenn.dev/metalels86/articles/2418a39f6057bb
  title: Claude Code の rules を検証した
  date: '2026-04-10'
---

# Claude Code Rules

---

## 2026-04-10

### Claude Code の rules を検証した

Claude Code の paths frontmatter 機能を検証し、Write 操作時にルールがトリガーされない制約を発見。新規ファイル作成時は touch → Read → Write の手順が必要だが、プロジェクト固有ルール管理には branch-rules-auto-loader を構築して対応。グローバルルールとプロジェクト固有ルールの混在問題を解決し、セッション開始時点でルールを確定する仕組みを実装した。

- **ソース**: [Zenn claude](https://zenn.dev/metalels86/articles/2418a39f6057bb)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-10 | 自動生成 |
