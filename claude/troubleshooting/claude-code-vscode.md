---
title: Claude Code Vscode
category: troubleshooting
subcategory: claude-code-vscode
tags:
- claude-code
- setup
- vscode
date: '2026-05-10'
updated: '2026-05-10'
sources:
- url: https://qiita.com/jayemdot/items/c36153175267dfa209ca
  title: tmux + Claude Codeで、VS Codeに差分が表示されない問題を解決する
  date: '2026-05-10'
---

# Claude Code Vscode

---

## 2026-05-10

### tmux + Claude Codeで、VS Codeに差分が表示されない問題を解決する

VS Code統合ターミナル経由でtmuxを使用している際、Claude Codeの編集差分が表示されない問題の解決方法を解説。tmuxセッション内の古い環境変数が原因で、VS Codeを認識できないことが問題。tmux show-environmentとcommand claudeを使ったラッパースクリプトで、Claude起動前に最新の環境変数を読み込ませることで解決できる。

- **ソース**: [Qiita claudecode](https://qiita.com/jayemdot/items/c36153175267dfa209ca)
- **重要度**: 6/10
- **タグ**: claude-code, vscode, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-10 | 自動生成 |
