---
title: Claude Code Bugs
category: troubleshooting
subcategory: claude-code-bugs
tags:
- bugfix
- claude-code
- performance
date: '2026-07-19'
updated: '2026-07-19'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1v0vqik/claude_code_got_stuck_printing_court_burned
  title: Claude Code got stuck printing “court,” burned through tokens, then blamed
    the “long session” it created
  date: '2026-07-19'
---

# Claude Code Bugs

---

## 2026-07-19

### Claude Code got stuck printing “court,” burned through tokens, then blamed the “long session” it created

Claude Code が突然「court」という単語を繰り返し出力し続け、大量のトークンを消費するバグが発生。Claude は「セッションが長く反復的だったため」と説明したが、実際にはこの無限ループ自体がセッションを長くした原因であり、循環論法的な説明となっている。自己回帰的な反復ループ（neural text degeneration）の可能性が指摘されている。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v0vqik/claude_code_got_stuck_printing_court_burned)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-19 | 自動生成 |
