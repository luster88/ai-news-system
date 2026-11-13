---
title: Claude Code Management
category: guides
subcategory: claude-code-management
tags:
- claude-code
- prompt
- setup
date: '2026-11-09'
updated: '2026-11-13'
sources:
- url: https://ai-heartland.com/explain/coding-agents-manager
  title: コーディングエージェントの使い方はマネジメント｜Claude Codeで効く習慣とhookの実測
  date: '2026-11-09'
- url: https://zenn.dev/chukidx_dev/articles/claude-md-user-and-repo-split
  title: CLAUDE.md をユーザー共通とリポジトリごとに分けて運用している話 — 何をどちらに書くか
  date: '2026-11-13'
---


# Claude Code Management

---

## 2026-11-13

### CLAUDE.md をユーザー共通とリポジトリごとに分けて運用している話 — 何をどちらに書くか

Claude Code で複数リポジトリを管理する際の CLAUDE.md の運用方法を解説。ユーザー共通の ~/.claude/CLAUDE.md には全リポジトリ共通のルール（コミット方針、記録の振り分けなど）を記載し、各リポジトリの CLAUDE.md にはそのツール固有の構成・コマンド・禁止事項を記載する方法を提案。判断基準は「別のリポジトリでこの1行を読んで困るか」で振り分ける。実際の運用例と /context コマンドでの確認方法も紹介している。

- **ソース**: [Zenn claude](https://zenn.dev/chukidx_dev/articles/claude-md-user-and-repo-split)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-11-09

### コーディングエージェントの使い方はマネジメント｜Claude Codeで効く習慣とhookの実測

コーディングエージェント（Claude Code）の効果的な使い方は、プロンプトの技巧ではなくマネジメント的な「任せ方」にある。最も重要なのはテスト・ビルド・スクショなどの「確かめる手段」を用意し、エージェントに証拠を見せてもらうこと。CLAUDE.mdには確認コマンドやリポジトリ外の決定事項を記載し、Hookで最小限の制約を設け、任せるべきものと任せないもの（製品判断・セキュリティ・出荷判断）を明確に分ける実践的アプローチが解説されている。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/coding-agents-manager)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-09 | 自動生成 |
