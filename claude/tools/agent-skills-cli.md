---
title: Agent Skills Cli
category: tools
subcategory: agent-skills-cli
tags:
- claude-code
- cowork
- mcp
- prompt
- setup
date: '2026-08-31'
updated: '2026-09-29'
sources:
- url: https://ai-heartland.com/tool/skills-sh
  title: skills.shとは｜npx skills add がディスクに何を書くかを実測
  date: '2026-08-31'
- url: https://ai-heartland.com/tool/code-review-skills
  title: code-review-skillsとは｜根拠のない指摘を封じるAIコードレビュースキルを実測で検証
  date: '2026-09-29'
---


# Agent Skills Cli

---

## 2026-09-29

### code-review-skillsとは｜根拠のない指摘を封じるAIコードレビュースキルを実測で検証

code-review-skillsは、Claude CodeとCodexに「根拠のある指摘だけをさせる」ためのAgent Skill。指摘の強さをMUST/SHOULD/BETTER/NITSの4段階で型付けし、すべてに具体的な契機と影響を要求することで、体裁だけの指摘や裏付けのない推測を排除する。スキル本体はMarkdownから機械生成され、約2,360トークンで常駐し、偽陽性の抑制を独立した工程として明示的に組み込んでいる。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/code-review-skills)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

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
