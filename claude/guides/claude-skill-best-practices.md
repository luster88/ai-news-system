---
title: Claude Skill Best Practices
category: guides
subcategory: claude-skill-best-practices
tags:
- claude-code
- prompt
- 新機能
date: '2026-08-24'
updated: '2026-08-24'
sources:
- url: https://ai-heartland.com/explain/claude-skill-naming-description-limits
  title: SKILL.mdのdescriptionは1024字上限｜Claude Skill命名規則と公式19本の検査結果
  date: '2026-08-24'
---

# Claude Skill Best Practices

---

## 2026-08-24

### SKILL.mdのdescriptionは1024字上限｜Claude Skill命名規則と公式19本の検査結果

Claude Skillの自作において、SKILL.mdのdescriptionには1,024文字の厳格な上限があり、超過分は切り捨てられる。nameは64文字以内でkebab-case形式が必須。Anthropic公式の19スキルを公式バリデータで検証した結果、claude-apiスキルが1,068文字で44文字超過し不合格となった。公式自身が「精度を犠牲にしても短くせよ」と推奨しており、これは全クエリに常駐する約300トークン分に相当するためである。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-skill-naming-description-limits)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-24 | 自動生成 |
