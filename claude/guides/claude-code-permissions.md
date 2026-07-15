---
title: Claude Code Permissions
category: guides
subcategory: claude-code-permissions
tags:
- claude-code
- setup
- 新機能
date: '2026-07-15'
updated: '2026-07-15'
sources:
- url: https://qiita.com/honda-dev-jp/items/e54036423dfa0d29b56c
  title: Claude Codeの権限設定を安全に設計する方法 ― Write/Edit・Ask/Denyを実際に検証して分かったこと
  date: '2026-07-15'
---

# Claude Code Permissions

---

## 2026-07-15

### Claude Codeの権限設定を安全に設計する方法 ― Write/Edit・Ask/Denyを実際に検証して分かったこと

Claude Codeの権限設定（Write/Edit・Ask/Deny）を実際に検証した記事。調査専用セッションと通常セッションで権限境界を分ける方法を解説。Write(path)は起動時に警告が出るため、ファイル編集にはEdit(path)を使う必要があること、Denyルールがモデルではなくアプリ側で強制されることを確認。検証用Settingsを分離する手法も紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/honda-dev-jp/items/e54036423dfa0d29b56c)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
