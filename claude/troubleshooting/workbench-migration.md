---
title: Workbench Migration
category: troubleshooting
subcategory: workbench-migration
tags:
- claude-console
- mcp
- prompt
date: '2026-08-29'
updated: '2026-08-29'
sources:
- url: https://zenn.dev/aimakerlab/articles/7ba7a136dcbd70
  title: Claude Workbench廃止でAI会社の自動化フローを見直した記録——launchd+MCP構成は壊れなかったが、失ったものがあった
  date: '2026-08-29'
---

# Workbench Migration

---

## 2026-08-29

### Claude Workbench廃止でAI会社の自動化フローを見直した記録——launchd+MCP構成は壊れなかったが、失ったものがあった

Anthropic が Claude Workbench を廃止し Console に統合。AI Maker Lab では launchd + MCP Server + Claude Code の自動化ジョブが稼働中だったが、API キー経由のため影響はなかった。しかし Workbench に保存していたプロンプトバリエーションが移行されず消失。今後は CLAUDE.md をプロンプト管理の唯一の情報源とし Git で管理する方針に。

- **ソース**: [Zenn claude](https://zenn.dev/aimakerlab/articles/7ba7a136dcbd70)
- **重要度**: 6/10
- **タグ**: claude-console, mcp, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-29 | 自動生成 |
