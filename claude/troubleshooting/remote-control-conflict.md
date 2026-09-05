---
title: Remote Control Conflict
category: troubleshooting
subcategory: remote-control-conflict
tags:
- bugfix
- claude-code
- mac
date: '2026-09-05'
updated: '2026-09-05'
sources:
- url: https://zenn.dev/m0370/articles/cf8aeb3a8154ee
  title: 2台のMacでClaudeデスクトップのディスパッチをオンにすると、Remote Controlの登録枠を奪い合って409エラーになる話
  date: '2026-09-05'
---

# Remote Control Conflict

---

## 2026-09-05

### 2台のMacでClaudeデスクトップのディスパッチをオンにすると、Remote Controlの登録枠を奪い合って409エラーになる話

Claudeデスクトップアプリで複数Mac間のRemote Control登録が競合し409エラーが発生する問題を報告。原因はサーバー側の環境登録がアカウントにつき1台のみで、UIから解除手段が提供されていないため。解決にはDELETE /v1/environments/bridge/{id} APIの直接呼び出しが必要。公式サポートへの依頼も可能だが、bridge-state.jsonの環境IDとKeychainのトークンを使い自力で解除することもできる。

- **ソース**: [Zenn claude](https://zenn.dev/m0370/articles/cf8aeb3a8154ee)
- **重要度**: 6/10
- **タグ**: claude-code, mac, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-05 | 自動生成 |
