---
title: Nvim Herdr Integration
category: tools
subcategory: nvim-herdr-integration
tags:
- claude-code
- mcp
- prompt
- vscode
- 新機能
date: '2026-08-01'
updated: '2026-08-13'
sources:
- url: https://qiita.com/r12tkmt/items/27da966a15b59c81589c
  title: herdrでnvimから隣のAIエージェントにファイル参照を送れるプラグインを作った
  date: '2026-08-01'
- url: https://zenn.dev/mostlyfine/articles/c4978481603b47
  title: Herdrのサイドバーに要約とプロンプトを出す
  date: '2026-08-13'
---


# Nvim Herdr Integration

---

## 2026-08-13

### Herdrのサイドバーに要約とプロンプトを出す

Herdr（Claude連携ツール）で大量のClaude実行時に何をしているか分からなくなる問題を解決するため、hooksを使って入力プロンプトと直近の会話から要約をサイドバーに表示するスクリプトが公開された。設定ファイルへの追加のみで動作し、エージェントに依頼してカスタマイズも可能。現在はClaude専用だが他のエージェントにも対応可能。

- **ソース**: [Zenn claude](https://zenn.dev/mostlyfine/articles/c4978481603b47)
- **重要度**: 4/10
- **タグ**: prompt, 新機能

---

## 2026-08-01

### herdrでnvimから隣のAIエージェントにファイル参照を送れるプラグインを作った

Neovim から herdr 上の Claude Code などの AI エージェントに直接ファイル参照やプロンプトを送信できる Neovim プラグインの開発記事。選択範囲やバッファ内容を @path 構文でエージェントに渡せるほか、エージェントが起動していない場合は自動的にペイン分割・起動する機能を実装。herdr CLI の agent list や pane send-text を活用し、わずか数十行で Nvim と AI エージェントの並行作業を効率化した。

- **ソース**: [Qiita claudecode](https://qiita.com/r12tkmt/items/27da966a15b59c81589c)
- **重要度**: 5/10
- **タグ**: claude-code, mcp, vscode

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-01 | 自動生成 |
