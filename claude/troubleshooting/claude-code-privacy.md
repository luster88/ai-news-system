---
title: Claude Code Privacy
category: troubleshooting
subcategory: claude-code-privacy
tags:
- bugfix
- claude-code
- setup
date: '2026-08-31'
updated: '2026-08-31'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1w2omfu/claude_code_is_silently_adding_session_urls
  title: Claude Code is silently adding session URLs (claude.ai/code/session_...)
    to the bottom of every single commit and PR description you make.
  date: '2026-08-31'
---

# Claude Code Privacy

---

## 2026-08-31

### Claude Code is silently adding session URLs (claude.ai/code/session_...) to the bottom of every single commit and PR description you make.

Claude Code が、ユーザーに通知することなく、すべてのコミットと PR の説明文の末尾に claude.ai/code/session_... の公開セッション URL を自動的に追加している問題が報告されています。回避策として、.claude/settings.json で attribution.commit を空文字列に設定することで無効化できます。プライバシーに関わる重要な挙動のため、git 履歴と PR を確認することが推奨されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1w2omfu/claude_code_is_silently_adding_session_urls)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-31 | 自動生成 |
