---
title: Multi Cli Management
category: guides
subcategory: multi-cli-management
tags:
- claude-code
- cowork
- setup
date: '2026-08-29'
updated: '2026-08-29'
sources:
- url: https://qiita.com/ishizakahiroshi/items/ffecb88684c29803b3c6
  title: CLAUDE.md と AGENTS.md と GEMINI.md を全部書くのをやめた。どの AI CLI が何を読むか実測して正本 1 本に寄せる
  date: '2026-08-29'
---

# Multi Cli Management

---

## 2026-08-29

### CLAUDE.md と AGENTS.md と GEMINI.md を全部書くのをやめた。どの AI CLI が何を読むか実測して正本 1 本に寄せる

複数のAI CLI（Claude Code、Codex、OpenCode、Copilot CLI、Grok、Cursor Agent）でルールファイルが乱立する問題に対処した記事。各CLIが読むファイル名（CLAUDE.md、AGENTS.md、GEMINI.md等）を実測し、~/.claude/CLAUDE.mdを正本として他のファイルからリンクする構成に統一。これによりルール更新を1箇所で管理できるようになった。実測の結果、Claude CodeはAGENTS.mdを読まず、CodexはCLAUDE.mdを読まないなど、各CLIの挙動の違いが明らかになった。

- **ソース**: [Qiita claudecode](https://qiita.com/ishizakahiroshi/items/ffecb88684c29803b3c6)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-29 | 自動生成 |
