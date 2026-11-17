---
title: Agent Skills Standard
category: ecosystem
subcategory: agent-skills-standard
tags:
- claude-code
- mcp
- 新機能
date: '2026-06-13'
updated: '2026-11-17'
sources:
- url: https://ai-heartland.com/explain/google-skills-guide
  title: Skillは標準仕様になる｜Googleが公式Agent Skillsリポジトリを公開、npx skillsで何が変わるか
  date: '2026-06-13'
- url: https://qiita.com/sakutto-panda/items/308bcb354f3527d03b09
  title: Agent SkillsがLinux Foundation傘下に——手持ちの27スキルを仕様で検査したら6本が不合格
  date: '2026-11-17'
---


# Agent Skills Standard

---

## 2026-11-17

### Agent SkillsがLinux Foundation傘下に——手持ちの27スキルを仕様で検査したら6本が不合格

2025年10月22日、AnthropicがAgent SkillsをLinux Foundation傘下のAgentic AI Foundationに寄贈し、MCPに続く2つ目の中立的標準となった。筆者が個人開発の27個のスキルを公式仕様で検証したところ、6個がYAMLフロントマター不備で不合格となった。Claude Codeはフロントマターなしでも動作するが、claude.aiやSkills APIでは厳格な扱いが必要で、エージェントの判断材料となるnameとdescriptionの重要性が示された。

- **ソース**: [Qiita claudecode](https://qiita.com/sakutto-panda/items/308bcb354f3527d03b09)
- **重要度**: 7/10
- **タグ**: 新機能, claude-code

---

## 2026-06-13

### Skillは標準仕様になる｜Googleが公式Agent Skillsリポジトリを公開、npx skillsで何が変わるか

GoogleがAIコーディングエージェント向けに公式Agent Skillsリポジトリを公開。AnthropicがClaude向けに始めたSkills形式をVercelがCLI化し、今回Googleが自社製品の公式ドキュメント配布に採用。一社の便利機能だったSkillsが、エージェント間で相互運用可能な標準仕様へと変化しつつある。BigQueryやCloud RunなどGoogle製品の正しい使い方をSKILL.md形式で提供し、npx skills addで導入可能。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/google-skills-guide)
- **重要度**: 6/10
- **タグ**: mcp, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-13 | 自動生成 |
