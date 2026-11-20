---
title: Claude Mem Management
category: troubleshooting
subcategory: claude-mem-management
tags:
- claude-code
- mcp
- setup
date: '2026-11-20'
updated: '2026-11-20'
sources:
- url: https://zenn.dev/starken/articles/claude-mem-project-scope-no-delete
  title: Claude Codeのclaude-memの古い記憶は削除しなくてよい理由
  date: '2026-11-20'
---

# Claude Mem Management

---

## 2026-11-20

### Claude Codeのclaude-memの古い記憶は削除しなくてよい理由

Claude Codeのclaude-memプラグインは、削除したプロジェクトの観測データが67%を占めていても、セッションに注入される記憶はプロジェクト単位で管理されるため、実際にはノイズにならない。削除コマンドも提供されておらず、SQLiteとchromaの二重管理のリスクを考えると、ディスク使用量（182MB程度）を容認して放置する方が合理的である。

- **ソース**: [Zenn claude](https://zenn.dev/starken/articles/claude-mem-project-scope-no-delete)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-20 | 自動生成 |
