---
title: Claude Code Disaster
category: troubleshooting
subcategory: claude-code-disaster
tags:
- bugfix
- claude-code
- windows
date: '2026-05-10'
updated: '2026-05-10'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1t923er/i_deleted_a_guys_entire_windows_install_with_one
  title: I deleted a guy's entire Windows install with one backslash. 717 GB. Gone.
    I am the AI.
  date: '2026-05-10'
---

# Claude Code Disaster

---

## 2026-05-10

### I deleted a guy's entire Windows install with one backslash. 717 GB. Gone. I am the AI.

Claude が SSH 経由で Windows のルートディレクトリを誤って削除した事例。エスケープ文字の扱いの違いにより `rd /S /Q \` が実行され、717GB のデータが消失。バックアップがあったため論文データは無事だったが、重大なトラブルシューティング事例として注目を集めている。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1t923er/i_deleted_a_guys_entire_windows_install_with_one)
- **重要度**: 7/10
- **タグ**: claude-code, windows, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-10 | 自動生成 |
