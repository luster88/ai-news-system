---
title: Mcp Browser Automation
category: tools
subcategory: mcp-browser-automation
tags:
- claude-code
- cowork
- mcp
date: '2026-07-22'
updated: '2026-07-22'
sources:
- url: https://qiita.com/ishizakahiroshi/items/a72e4637bdd7499421be
  title: Codex は API を叩き、Claude は Web でタダだった。多 AI CLI 時代の skill 経路分岐と、次に狙う「browser-delegate」の話
  date: '2026-07-22'
---

# Mcp Browser Automation

---

## 2026-07-22

### Codex は API を叩き、Claude は Web でタダだった。多 AI CLI 時代の skill 経路分岐と、次に狙う「browser-delegate」の話

自作の多AI CLI「many-ai-cli」で、Claude CodeとCodex CLIを比較したところ、同じ画像生成タスクでもClaudeはChrome自動操作で無料枠を使用し、Codexは有料APIを呼び出していた。この差はAnthropicが提供するMCPサーバー「Claude for Chrome」の存在によるもので、月数百円～数千円のコスト差が生じる。次期リリースで「Codexセッションを維持しつつ、ブラウザ操作が必要な時だけClaude子セッションに処理を委譲する」browser-delegate機能の実装を検討中。

- **ソース**: [Qiita claude](https://qiita.com/ishizakahiroshi/items/a72e4637bdd7499421be)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-22 | 自動生成 |
