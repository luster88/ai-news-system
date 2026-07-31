---
title: Mcp Tools
category: troubleshooting
subcategory: mcp-tools
tags:
- claude-code
- mcp
date: '2026-07-31'
updated: '2026-07-31'
sources:
- url: https://qiita.com/shu15511551/items/d97eadd8833d818aa9cc
  title: フォームの中の AI は、目隠しをした普通の Claude だった ── 「AI要約説明」をようやく書く話
  date: '2026-07-31'
---

# Mcp Tools

---

## 2026-07-31

### フォームの中の AI は、目隠しをした普通の Claude だった ── 「AI要約説明」をようやく書く話

VBAから呼び出すClaude要約フォームを作成した際、AIがツール使用許可を繰り返し求める現象が発生。調査の結果、ヘッドレス起動のClaude CodeはMCPツールがデフォルトで封鎖されており、毎回新規セッションのため会話が継続していないことが判明。起動引数でツール許可を渡すことで、マクロ検索などの機能が有効化され、真の会話継続が可能になった。

- **ソース**: [Qiita claudecode](https://qiita.com/shu15511551/items/d97eadd8833d818aa9cc)
- **重要度**: 6/10
- **タグ**: mcp, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-31 | 自動生成 |
