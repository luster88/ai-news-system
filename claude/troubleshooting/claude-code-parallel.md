---
title: Claude Code Parallel
category: troubleshooting
subcategory: claude-code-parallel
tags:
- bugfix
- claude-code
- cowork
date: '2026-08-24'
updated: '2026-08-24'
sources:
- url: https://qiita.com/YujiNaramoto/items/b3acc07ae05e4b84e487
  title: 'なぜClaude Codeのsubagent並列実行にisolation: ''worktree''が必要なのか'
  date: '2026-08-24'
---

# Claude Code Parallel

---

## 2026-08-24

### なぜClaude Codeのsubagent並列実行にisolation: 'worktree'が必要なのか

Claude CodeのAgent toolで複数のsubagentを並列実行する際、git操作やファイル書き換えを伴う場合は isolation: 'worktree' の指定が必須となる。同一working directoryでgit操作を行うと.gitディレクトリのHEADが競合し、コミット内容が混在する問題が発生する。読み取り専用タスクではisolationは不要だが、書き込み操作では各subagentに独立したworktreeを割り当てることで競合を回避できる。ただしworktree作成には依存関係の再インストールコストがあり、タスクの性質によっては直列実行の方が適切な場合もある。

- **ソース**: [Qiita claude](https://qiita.com/YujiNaramoto/items/b3acc07ae05e4b84e487)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-24 | 自動生成 |
