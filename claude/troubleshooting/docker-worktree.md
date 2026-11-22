---
title: Docker Worktree
category: troubleshooting
subcategory: docker-worktree
tags:
- bugfix
- claude-code
- setup
date: '2026-11-22'
updated: '2026-11-22'
sources:
- url: https://qiita.com/phibi-soon/items/eb49af18ba1918d24aef
  title: worktreeにマウントを切り替えたのに、前のブランチのクラスが動いた！？
  date: '2026-11-22'
---

# Docker Worktree

---

## 2026-11-22

### worktreeにマウントを切り替えたのに、前のブランチのクラスが動いた！？

git worktree使用時にDocker Composeでソースマウントをブランチごとに切り替える手法を解説。targetやnode_modulesなどビルド成果物を名前付きボリュームで共有すると、前のブランチの古いクラスファイルが残り続ける問題とその対処法を紹介。APP_SRC環境変数とスクリプトでマウント元を切り替え、ボリュームもブランチごとに分離する実装例を共有。

- **ソース**: [Qiita claudecode](https://qiita.com/phibi-soon/items/eb49af18ba1918d24aef)
- **重要度**: 4/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-22 | 自動生成 |
