---
title: Claude Code Hooks
category: troubleshooting
subcategory: claude-code-hooks
tags:
- bugfix
- claude-code
- setup
date: '2026-06-03'
updated: '2026-06-03'
sources:
- url: https://zenn.dev/gudezou/articles/7e8235a27f0909
  title: Claude Code の終了フックから claude を呼び出すとなぜ暴走するのか
  date: '2026-06-03'
---

# Claude Code Hooks

---

## 2026-06-03

### Claude Code の終了フックから claude を呼び出すとなぜ暴走するのか

Claude Code の SessionEnd フックから claude を起動すると無限ループが発生する問題を解説。終了フックは同期実行されるため重い処理で固まる危険性があり、再帰防止には環境変数による入口ガードが有効。実際の事故事例では数百回発火し利用上限に達した。

- **ソース**: [Zenn claude](https://zenn.dev/gudezou/articles/7e8235a27f0909)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-03 | 自動生成 |
