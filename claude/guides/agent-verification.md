---
title: Agent Verification
category: guides
subcategory: agent-verification
tags:
- claude-code
- cowork
- prompt
date: '2026-10-15'
updated: '2026-10-15'
sources:
- url: https://zenn.dev/liatris/articles/20261015-agent-completion-proof
  title: AIエージェントの「完了しました」を、実行ログの証拠で検証する
  date: '2026-10-15'
---

# Agent Verification

---

## 2026-10-15

### AIエージェントの「完了しました」を、実行ログの証拠で検証する

AIエージェントの「完了しました」報告を鵜呑みにせず、実行ログという独立した証拠と突き合わせて検証する仕組みの実装例。Taskの仕様・Agentの完了報告・ExecutionLoggerの記録の3者を照合し、VERIFIED/UNVERIFIED/MISMATCHの3値で判定する。エージェントの自然文報告に依存せず、実行ログのみを証拠とすることで「自己採点」構造から脱却している。

- **ソース**: [Zenn claude](https://zenn.dev/liatris/articles/20261015-agent-completion-proof)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-15 | 自動生成 |
