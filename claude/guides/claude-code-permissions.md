---
title: Claude Code Permissions
category: guides
subcategory: claude-code-permissions
tags:
- claude-code
- prompt
- setup
- 新機能
date: '2026-07-15'
updated: '2026-09-19'
sources:
- url: https://qiita.com/honda-dev-jp/items/e54036423dfa0d29b56c
  title: Claude Codeの権限設定を安全に設計する方法 ― Write/Edit・Ask/Denyを実際に検証して分かったこと
  date: '2026-07-15'
- url: https://zenn.dev/tmasuyama1114/articles/claude_code_permissions_recommended
  title: 【コピペOK】Claude Code の permissions おすすめ設定と、allow / ask / deny の分け方
  date: '2026-09-19'
---


# Claude Code Permissions

---

## 2026-09-19

### 【コピペOK】Claude Code の permissions おすすめ設定と、allow / ask / deny の分け方

Claude Code の settings.json における permissions 設定の推奨ガイド。取り返しがつく操作は allow、外部への送信や削除は ask、機密情報へのアクセスは deny に分類する基準を解説。deny → ask → allow の評価順序を理解し、auto mode や bypassPermissions でも deny/ask は有効であることを説明している。

- **ソース**: [Zenn claude](https://zenn.dev/tmasuyama1114/articles/claude_code_permissions_recommended)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

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
