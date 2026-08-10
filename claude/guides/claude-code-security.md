---
title: Claude Code Security
category: guides
subcategory: claude-code-security
tags:
- claude-code
- opus
- prompt
- setup
- 新機能
date: '2026-05-01'
updated: '2026-08-10'
sources:
- url: https://zenn.dev/yuzzzn/articles/45626e1ab08e3c
  title: AIコーディングエージェントをセキュアに使うためのハーネス設計
  date: '2026-05-01'
- url: https://qiita.com/Tadashi_Kudo/items/ffc79c01f54909974075
  title: Claude Codeのpermissions.denyを厚く書いてる人へ：たぶん全部デフォルトで防がれてる
  date: '2026-05-18'
- url: https://zenn.dev/yuzzzn/articles/29b0538948b3d1
  title: 再掲]ClaudeCodeの環境構築,使い方入門
  date: '2026-05-27'
- url: https://zenn.dev/st_27/articles/efb2436a8cd8e0
  title: ハーネスについての備忘録
  date: '2026-08-10'
---




# Claude Code Security

---

## 2026-08-10

### ハーネスについての備忘録

Claude Codeにおけるハーネス（ツール呼び出しの制御システム）について解説した技術記事。CLAUDE.md、permissions、hooks、sandboxの4層構造と、それぞれの強制力・役割の違いを整理している。CLAUDE.mdはモデルの意図生成に影響するがハーネスの判定ロジックには介入せず、技術的な制御にはpermissions/hooks/sandboxが必要であることを強調。

- **ソース**: [Zenn claude](https://zenn.dev/st_27/articles/efb2436a8cd8e0)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-05-27

### 再掲]ClaudeCodeの環境構築,使い方入門

Claude Code の安全な環境構築ガイド。settings.json による機械的アクセス制御、PreToolUse hook による二重チェック、Docker コンテナによる隔離の3層防御を解説。200行を超えると無視されるCLAUDE.mdの制限への対処法、Claude Opus 4.7ではSubAgent呼び出しが逆効果になる点、Goal-Driven Executionによる自律実行の最適化など、最新バージョンに対応した実践的な設定方法を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/yuzzzn/articles/29b0538948b3d1)
- **重要度**: 7/10
- **タグ**: claude-code, setup, opus

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
