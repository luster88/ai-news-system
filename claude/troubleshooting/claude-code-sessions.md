---
title: Claude Code Sessions
category: troubleshooting
subcategory: claude-code-sessions
tags:
- bugfix
- claude-code
- mac
date: '2026-11-07'
updated: '2026-11-07'
sources:
- url: https://zenn.dev/starken/articles/claude-code-remote-control-stale-sessions
  title: Claude Codeで、デスクトップアプリに空のセッションが大量に並ぶ原因
  date: '2026-11-07'
---

# Claude Code Sessions

---

## 2026-11-07

### Claude Codeで、デスクトップアプリに空のセッションが大量に並ぶ原因

Claude Codeのデスクトップアプリで、開いた覚えのない空のセッションが大量に表示される問題を調査。Remote Control機能の既知のバグで、~/.claude/session-env/に終了したセッションのメタデータが削除されず蓄積（2632件）し、それをRemote Controlが読み込んでサイドバーに表示していた。当初疑った自作の定期実行スクリプトは、実測で無関係と判明。

- **ソース**: [Zenn claude](https://zenn.dev/starken/articles/claude-code-remote-control-stale-sessions)
- **重要度**: 5/10
- **タグ**: claude-code, bugfix, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-07 | 自動生成 |
