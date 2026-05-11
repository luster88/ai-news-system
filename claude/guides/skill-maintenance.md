---
title: Skill Maintenance
category: guides
subcategory: skill-maintenance
tags:
- claude-code
- prompt
- setup
date: '2026-05-11'
updated: '2026-05-11'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/c7728cb2011c8f6d7c82
  title: 「スクリプトはあるがスキルから参照されない」を防ぐ：技術的負債を自動解消する統合ルール
  date: '2026-05-11'
---

# Skill Maintenance

---

## 2026-05-11

### 「スクリプトはあるがスキルから参照されない」を防ぐ：技術的負債を自動解消する統合ルール

Claude Code等のAI AgentでSKILL.mdに記載されたスクリプトパスと実体が乖離する技術的負債問題を解決する3つの統合ルール。スクリプトを1箇所に集約（~/workspace/scripts/）し、SKILL.mdには実在パスのみ記載、CLIインベントリを自動生成、週次でドリフト検知を行うことで、Agentのサイレント失敗を防止する実践的な運用方法。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/c7728cb2011c8f6d7c82)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-11 | 自動生成 |
