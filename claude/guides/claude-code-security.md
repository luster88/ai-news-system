---
title: Claude Code Security
category: guides
subcategory: claude-code-security
tags:
- claude-code
- setup
- 新機能
date: '2026-05-01'
updated: '2026-05-18'
sources:
- url: https://zenn.dev/yuzzzn/articles/45626e1ab08e3c
  title: AIコーディングエージェントをセキュアに使うためのハーネス設計
  date: '2026-05-01'
- url: https://qiita.com/Tadashi_Kudo/items/ffc79c01f54909974075
  title: Claude Codeのpermissions.denyを厚く書いてる人へ：たぶん全部デフォルトで防がれてる
  date: '2026-05-18'
---


# Claude Code Security

---

## 2026-05-18

### Claude Codeのpermissions.denyを厚く書いてる人へ：たぶん全部デフォルトで防がれてる

Claude Code の permissions.deny 設定について、デフォルトモードではClaude自身が危険な操作を確認してくるため、denyリストは重複防御になりがち。しかし bypassPermissions モード（自動実行・Agentic実行）では確認プロンプトが出ないため、denyリストが最後の砦となる。rm -rf系の破壊的コマンドやgit操作の誤実行防止には、deny設定とhooksの組み合わせが有効。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/ffc79c01f54909974075)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-01

### AIコーディングエージェントをセキュアに使うためのハーネス設計

Claude Code などの AI コーディングエージェントをセキュアに運用するためのハーネス設計手法を解説。Docker コンテナ隔離・ファイアウォール制御・ファイルアクセス制限・コマンド実行制限・プロンプト設計の 5 層防御アーキテクチャを構築し、プロンプトインジェクション・機密情報漏洩・意図しないコマンド実行のリスクに対処する多層防御を実現。

- **ソース**: [Zenn claude](https://zenn.dev/yuzzzn/articles/45626e1ab08e3c)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-01 | 自動生成 |
