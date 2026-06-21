---
title: Mcp Config Loss
category: troubleshooting
subcategory: mcp-config-loss
tags:
- bugfix
- claude-code
- mcp
date: '2026-06-21'
updated: '2026-06-21'
sources:
- url: https://qiita.com/yurukusa/items/4be11d4ae3bca22fd278
  title: Claude Code の設定ファイルにコメントを1行書いたら MCP サーバーが全部消えた——`.claude.json` の沈黙の全消去 (#69354)
    と予防
  date: '2026-06-21'
---

# Mcp Config Loss

---

## 2026-06-21

### Claude Code の設定ファイルにコメントを1行書いたら MCP サーバーが全部消えた——`.claude.json` の沈黙の全消去 (#69354) と予防

Claude Codeの設定ファイル`~/.claude.json`にJSONで許可されていないコメント（`/* */`）を追加すると、パースエラーが発生しても警告なしに設定が空で上書きされ、登録していたMCPサーバーが全消去される問題が報告された。この記事では、事故の仕組み、復旧方法（シェル履歴からの再登録、バックアップからの復元）、および予防策（JSONコメント禁止、自動バックアップ）を解説している。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/4be11d4ae3bca22fd278)
- **重要度**: 7/10
- **タグ**: mcp, bugfix, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-21 | 自動生成 |
