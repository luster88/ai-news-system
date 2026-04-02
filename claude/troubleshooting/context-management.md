---
title: Context Management
category: troubleshooting
subcategory: context-management
tags:
- claude-code
- mcp
- vscode
date: '2026-04-02'
updated: '2026-04-02'
sources:
- url: https://qiita.com/MirabelleQuest/items/f3b27e9740d4b22135fc
  title: '# Claude Code でセッション開始直後から Context 使用率が高かったので確認した'
  date: '2026-04-02'
---

# Context Management

---

## 2026-04-02

### # Claude Code でセッション開始直後から Context 使用率が高かったので確認した

Claude Code のセッション開始直後に Context 使用率が 40% を超えていた原因を調査したところ、MCP Tools が大きな割合を占めていることが判明。MCP サーバーの有効/無効の切り替えは、セッション開始時点で読み込まれたツール定義に影響し、途中で変更しても即座には反映されない挙動を確認。不要な MCP 接続を外してからセッションを開始することで、初期 Context 使用率を抑えられることがわかった。

- **ソース**: [Qiita claudecode](https://qiita.com/MirabelleQuest/items/f3b27e9740d4b22135fc)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, vscode

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
