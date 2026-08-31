---
title: Agent Skills Cli
category: tools
subcategory: agent-skills-cli
tags:
- claude-code
- mcp
- setup
date: '2026-08-31'
updated: '2026-08-31'
sources:
- url: https://ai-heartland.com/tool/skills-sh
  title: skills.shとは｜npx skills add がディスクに何を書くかを実測
  date: '2026-08-31'
---

# Agent Skills Cli

---

## 2026-08-31

### skills.shとは｜npx skills add がディスクに何を書くかを実測

skills.shは、Agent Skills（SKILL.md）を複数のAIエージェントに配布するためのVercel LabsのCLIツール。npx skills add コマンドで、Claude Code、Windsurf、Rooなど77のエージェントにスキルをインストールできる。実測により、エージェント数に応じて書き込み先が切り替わること（1つなら直接コピー、2つ以上なら.agents/skills/とsymlink）、Windsurf・Roo・Gooseではsymlinkモードで問題があること、--copyオプションで回避可能なことが判明した。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/skills-sh)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-31 | 自動生成 |
