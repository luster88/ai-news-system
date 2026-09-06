---
title: Github Cli Agent Skills
category: tools
subcategory: github-cli-agent-skills
tags:
- claude-code
- copilot
- cursor
- mcp
- prompt
- setup
- 新機能
date: '2026-04-22'
updated: '2026-09-06'
sources:
- url: https://ai-heartland.com/tool/gh-skill-github-cli-agent-skills
  title: gh skill完全ガイド：GitHub CLIでAgent Skillsを管理する公式コマンド入門
  date: '2026-04-22'
- url: https://zenn.dev/maronsan/articles/skills-lint-collision-linter
  title: そのSKILL.md、別のスキルと発火が被ってない？ 衝突と壊れた参照をCIで落とすリンタを作った
  date: '2026-07-20'
- url: https://ai-heartland.com/agent/oi-owarasero
  title: oi-owarasero解説｜書籍発の対話型Agent Skillをインストールから実測
  date: '2026-09-06'
---



# Github Cli Agent Skills

---

## 2026-09-06

### oi-owarasero解説｜書籍発の対話型Agent Skillをインストールから実測

書籍『おい、とりあえず終わらせろ』を基にした対話型Agent Skill「oi-owarasero」の解説記事。作業を引き取らずに問いだけを返す特徴的なSkillで、SKILL.md 1枚（231行）のみで構成され、Claude Code/Codex両対応。著者自身が書籍の5ステップ方法論をSkill化し、実行可能コードを含まずプロンプトのみで動作する珍しい実装例。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/oi-owarasero)
- **重要度**: 5/10
- **タグ**: claude-code, mcp, prompt

---

## 2026-07-20

### そのSKILL.md、別のスキルと発火が被ってない？ 衝突と壊れた参照をCIで落とすリンタを作った

Claude の Agent Skills（SKILL.md）における「参照の腐り」と「スキル同士の発火トリガ衝突」を CI で自動検出するリンタ skills-lint が公開された。文字バイグラムの Jaccard 類似度でトリガ文の衝突を検出し、ファイル参照の整合性も検証。依存ゼロで GitHub Actions に統合でき、PR ごとに自動チェックが走る。同作者による llms.txt 向けリンタ reflint も同時アップデートされ、リポジトリ内参照の整合性検証機能が追加された。

- **ソース**: [Zenn claude](https://zenn.dev/maronsan/articles/skills-lint-collision-linter)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-04-22

### gh skill完全ガイド：GitHub CLIでAgent Skillsを管理する公式コマンド入門

2026年4月にGitHub公式がgh CLIに追加した新サブコマンド「gh skill」の解説記事。AIエージェント向けのAgent Skillsを統一的に管理できる仕組みで、Claude Code、GitHub Copilot、Cursorなど複数のエージェントで共通のスキルパッケージを検索・インストール・公開できる。install、search、publish、update、previewの5つのサブコマンドを提供し、awesome-copilotリポジトリと連携する。サプライチェーン攻撃のリスクにも言及。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/gh-skill-github-cli-agent-skills)
- **重要度**: 7/10
- **タグ**: claude-code, copilot, cursor

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-22 | 自動生成 |
