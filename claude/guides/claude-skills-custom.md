---
title: Claude Skills Custom
category: guides
subcategory: claude-skills-custom
tags:
- claude-code
- cowork
- mcp
- prompt
- setup
- 新機能
date: '2026-08-08'
updated: '2026-09-25'
sources:
- url: https://qiita.com/ljourm/items/be5fdf8043de545969d9
  title: Claude Skillsを自作して、AWS構成図を運用も見据えて作成してみる - ClaudeCode+Skills→draw.io+仕様書Markdown
  date: '2026-08-08'
- url: https://qiita.com/ljourm/items/be5fdf8043de545969d9
  title: Claude Skillsを自作して、AWS構成図を運用も見据えて作成してみる - ClaudeCode+Skills→draw.io+仕様書Markdown
  date: '2026-08-08'
- url: https://qiita.com/caymezon/items/d82d0e2d30d2647293dc
  title: CLAUDE.mdが肥大化してきたら、手順はSKILL.mdに切り出す
  date: '2026-09-25'
---


# Claude Skills Custom

---

## 2026-09-25

### CLAUDE.mdが肥大化してきたら、手順はSKILL.mdに切り出す

Claude Code/Claude.aiのClaude Skillsについて、CLAUDE.mdとSKILL.mdの使い分けを解説。SKILL.mdは呼び出し時のみ読み込まれるため、詳細な手順書に最適。descriptionフィールドで実行条件を明示し、disable-model-invocation:trueで誤実行を防ぐことが重要。チーム共有も可能で、トークン消費を抑えながら専門的な作業を実行できる。

- **ソース**: [Qiita claudecode](https://qiita.com/caymezon/items/d82d0e2d30d2647293dc)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-08-08

### Claude Skillsを自作して、AWS構成図を運用も見据えて作成してみる - ClaudeCode+Skills→draw.io+仕様書Markdown

AWS構成図作成のためのClaude Skillsカスタマイズ事例。AWS公式Skillをベースに、draw.io形式での図作成とMarkdown仕様書の同時生成を実現。サービス名の簡略化、リソース名表示、矢印接続の改善など5つのカスタマイズを実装し、IaC開発での活用を想定した運用フローを構築。

- **ソース**: [Qiita claude](https://qiita.com/ljourm/items/be5fdf8043de545969d9)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

### Claude Skillsを自作して、AWS構成図を運用も見据えて作成してみる - ClaudeCode+Skills→draw.io+仕様書Markdown

AWS公式のClaudeSkillをベースに、draw.io形式のAWS構成図と仕様書Markdownを同時生成するカスタムSkillを作成。サービス名の簡略化、リソース名の表示、矢印接続の改善など5つのカスタマイズを実施し、IaC開発での活用を想定した運用フローを構築。GitHubで公開済み。

- **ソース**: [Qiita claudecode](https://qiita.com/ljourm/items/be5fdf8043de545969d9)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-08 | 自動生成 |
