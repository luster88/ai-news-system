---
title: Context Management
category: prompts
subcategory: context-management
tags:
- claude-api
- prompt
- 新機能
date: '2026-06-12'
updated: '2026-06-12'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1u450lw/claude_gives_zero_warning_before_it_starts
  title: Claude gives zero warning before it starts getting dumber. so I gave it a
    canary.
  date: '2026-06-12'
---

# Context Management

---

## 2026-06-12

### Claude gives zero warning before it starts getting dumber. so I gave it a canary.

Claudeのコンテキスト劣化を早期検知する実践的テクニック。「返信の冒頭に名前を入れる」という無意味なルールをシステムプロンプトに追加し、コンテキストが重くなると最初に削除されるこのルールの消失を「カナリア」として利用。名前が消えた時点でセッションをリロードすることで、その後の品質低下（API捏造など）を未然に防ぐ方法を紹介。重要なルールは守られるが、意図的に設定した捨てルールが最初に犠牲になる特性を活用している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1u450lw/claude_gives_zero_warning_before_it_starts)
- **重要度**: 6/10
- **タグ**: prompt, claude-api, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-12 | 自動生成 |
