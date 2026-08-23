---
title: Cloud Routine Skills
category: troubleshooting
subcategory: cloud-routine-skills
tags:
- claude-code
- cowork
date: '2026-08-23'
updated: '2026-08-23'
sources:
- url: https://qiita.com/YujiNaramoto/items/b3cbc1e2c581aa50aced
  title: なぜClaude Codeのcloud routineはローカルのスキルを読まないのか
  date: '2026-08-23'
---

# Cloud Routine Skills

---

## 2026-08-23

### なぜClaude Codeのcloud routineはローカルのスキルを読まないのか

Claude Codeのcloud routineやCoworkセッションが ~/.claude/skills/ のローカルスキルを読み込まない理由と、3つの回避策を解説。cloud routineは新しいリモートセッションとして起動するため、ローカルファイルシステムにアクセスできない。解決策として、アカウント側でのスキル有効化、repoの.claude/skills/へのcommit、pluginのrepo側設定の3つを提示。

- **ソース**: [Qiita claudecode](https://qiita.com/YujiNaramoto/items/b3cbc1e2c581aa50aced)
- **重要度**: 7/10
- **タグ**: claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-23 | 自動生成 |
