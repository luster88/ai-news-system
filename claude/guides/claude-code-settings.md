---
title: Claude Code Settings
category: guides
subcategory: claude-code-settings
tags:
- claude-code
- setup
- vscode
- 新機能
date: '2026-03-31'
updated: '2026-07-23'
sources:
- url: https://qiita.com/makoto-ogata@github/items/641a26f0d5d40aa1c0c4
  title: Claude Codeのsettings.jsonの設定をしよう
  date: '2026-03-31'
- url: https://qiita.com/makoto-ogata@github/items/641a26f0d5d40aa1c0c4
  title: Claude Codeのsettings.jsonの設定をしよう
  date: '2026-03-31'
- url: https://zenn.dev/kuzzken/articles/5c73122da6b93b
  title: Claude Code の settings.json を棚卸ししたら、許可ルールの9割が消せた
  date: '2026-07-23'
---


# Claude Code Settings

---

## 2026-07-23

### Claude Code の settings.json を棚卸ししたら、許可ルールの9割が消せた

Claude Code の settings.json を数ヶ月分棚卸ししたところ、45個の許可ルールのうち32個が不要なゴミだった。特定URLのcurlや一時的なプロセスIDのkillなど、二度と実行されないコマンドが大半を占め、5つの分類パターン（一時的コマンド、旧環境のパス、古いMCPサーバID、壊れたパターン、重複ルール）で整理できた。Claude Codeは読み取り専用コマンドを自動許可しており、グローバルのdenyが全レイヤーで優先されるため、安全側の設定はグローバルdenyに置くのが基本。

- **ソース**: [Zenn claude](https://zenn.dev/kuzzken/articles/5c73122da6b93b)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-03-31

### Claude Codeのsettings.jsonの設定をしよう

Claude Code の settings.json 設定ガイド。設定ファイルは「何ができるかを制御する（権限・動作）」がメインで、指示内容は CLAUDE.md に記載すべきという基本方針を解説。コンテキスト自動圧縮（70%）、処理時間表示、Git 連携、日本語設定など実用的な設定例を紹介している。

- **ソース**: [Qiita claude](https://qiita.com/makoto-ogata@github/items/641a26f0d5d40aa1c0c4)
- **重要度**: 6/10
- **タグ**: claude-code, setup, vscode

---

### Claude Codeのsettings.jsonの設定をしよう

Claude Codeのsettings.jsonの設定方法についての初心者向けガイド。settings.jsonは権限・動作の制御がメイン、指示はCLAUDE.mdに書くべきと解説。コンテキスト圧縮タイミング(70%)、タイマー表示、Git連携、言語設定など実用的な設定例を紹介。gitコマンドは閲覧のみallow、push/削除は確認付きにする運用を推奨している。

- **ソース**: [Qiita claudecode](https://qiita.com/makoto-ogata@github/items/641a26f0d5d40aa1c0c4)
- **重要度**: 6/10
- **タグ**: claude-code, setup, vscode

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-31 | 自動生成 |
