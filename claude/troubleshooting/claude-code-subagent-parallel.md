---
title: Claude Code Subagent Parallel
category: troubleshooting
subcategory: claude-code-subagent-parallel
tags:
- bugfix
- claude-code
- cowork
date: '2026-08-20'
updated: '2026-08-20'
sources:
- url: https://zenn.dev/playpark/articles/claude-code-subagent-parallel-git-isolation
  title: Claude Codeのsubagentを並列でgit操作させたら、コミットが混ざった話
  date: '2026-08-20'
---

# Claude Code Subagent Parallel

---

## 2026-08-20

### Claude Codeのsubagentを並列でgit操作させたら、コミットが混ざった話

Claude CodeのAgent toolで複数subagentを並列実行する際、git操作やファイル書き込みを伴うと、同一working directoryでの競合によりコミットが混在する問題が発生する。isolation: 'worktree'パラメータで各subagentに独立したgit worktreeを割り当てることで競合を回避できるが、依存関係の再インストールが必要になるコストがある。実践的な判断基準として、読み取り専用タスクにはisolationを付けず、書き込み・git操作を伴う場合のみisolationまたは直列化を選択することが推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/playpark/articles/claude-code-subagent-parallel-git-isolation)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-20 | 自動生成 |
