---
title: Git Conflict
category: troubleshooting
subcategory: git-conflict
tags:
- bugfix
- claude-code
- cowork
date: '2026-10-10'
updated: '2026-10-10'
sources:
- url: https://qiita.com/sumitsuke/items/b941d1db69f2ce553806
  title: 2 つの AI セッションが同じ作業コピーを触ると、index まで共有される——「自分のファイルだけ add」は安全ではない
  date: '2026-10-10'
---

# Git Conflict

---

## 2026-10-10

### 2 つの AI セッションが同じ作業コピーを触ると、index まで共有される——「自分のファイルだけ add」は安全ではない

Claude Code で同じ作業コピーを2つのセッションで共有すると、git の index（stage）も共有されるため、意図しないファイルが他方の commit に混入する問題が発生。実例として24本のファイルが他セッションの commit に含まれたケースを報告。`git add` で自分のファイルのみを指定しても index 全体が commit されるため、`git commit --only` や `git worktree` による隔離が必要。

- **ソース**: [Qiita claudecode](https://qiita.com/sumitsuke/items/b941d1db69f2ce553806)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-10 | 自動生成 |
