---
title: Security Subprocess
category: troubleshooting
subcategory: security-subprocess
tags:
- claude-code
- mcp
- setup
date: '2026-09-08'
updated: '2026-09-08'
sources:
- url: https://qiita.com/akihidem/items/8fba54e72f69fd1828a9
  title: 'サブプロセスに親の認証情報を継承させない: Claude Code の環境スクラブを実装して検証する'
  date: '2026-09-08'
---

# Security Subprocess

---

## 2026-09-08

### サブプロセスに親の認証情報を継承させない: Claude Code の環境スクラブを実装して検証する

Claude Codeで子プロセスが親の認証情報（API KEYやクラウド認証情報）を継承してしまう問題に対処するため、CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1による環境変数スクラブを実装・検証する手順を解説。Bashツール・フック・MCPサーバーから認証情報を削除し、プロンプトインジェクション攻撃による情報流出を防ぐ。CLAUDE_CODE_MCP_ALLOWLIST_ENVによるMCPサーバーのホワイトリスト化や、CLAUDE_CODE_SCRIPT_CAPSによるスクリプト実行回数制限も紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/akihidem/items/8fba54e72f69fd1828a9)
- **重要度**: 8/10
- **タグ**: claude-code, mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-08 | 自動生成 |
