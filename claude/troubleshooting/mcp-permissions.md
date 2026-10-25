---
title: Mcp Permissions
category: troubleshooting
subcategory: mcp-permissions
tags:
- claude-code
- mcp
- setup
date: '2026-10-25'
updated: '2026-10-25'
sources:
- url: https://zenn.dev/outsidernotes/articles/933adb87f7e8de
  title: Claude Code の自動モードで、MCP の作成・削除が承認なしで通った：書き込みだけ毎回確認にする設定
  date: '2026-10-25'
---

# Mcp Permissions

---

## 2026-10-25

### Claude Code の自動モードで、MCP の作成・削除が承認なしで通った：書き込みだけ毎回確認にする設定

Claude Code の自動モードで freee 公式 MCP を使用したところ、取引の作成・更新・削除が承認なしで実行された事例の報告。設定ファイルの permissions.ask に書き込み系ツール（freee_api_post, freee_api_put, freee_api_delete など）を個別に指定することで、読み取り操作は即座に実行し、書き込み操作のみ毎回承認画面を表示させる対策が有効だった。MCP ツールの権限管理における重要な注意喚起。

- **ソース**: [Zenn claude](https://zenn.dev/outsidernotes/articles/933adb87f7e8de)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-25 | 自動生成 |
