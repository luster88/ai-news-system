---
title: Claude Code Settings
category: guides
subcategory: claude-code-settings
tags:
- claude-code
- prompt
- setup
- vscode
- 新機能
date: '2026-03-31'
updated: '2026-08-21'
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
- url: https://ai-heartland.com/explain/claude-code-settings-guide
  title: Claude Code 設定ガイド｜settings.jsonのスコープ優先順位とpermissions設計
  date: '2026-08-12'
- url: https://zenn.dev/manntera/articles/9e98c6850f63c7
  title: Claude Codeの回答がイマイチだなぁ？って思った時に読む記事(非エンジニア向け)
  date: '2026-08-21'
---




# Claude Code Settings

---

## 2026-08-21

### Claude Codeの回答がイマイチだなぁ？って思った時に読む記事(非エンジニア向け)

Claude Codeのeffort設定（低～最大の5段階）は「頭の良さ」ではなく「どこまで手間をかけるか」を制御する。最大設定にすると、指示があいまいな場合に推測で余計な作業をして長文で的外れな回答になることがある。迷ったらmedium/highを選び、maxは一時的な使用に留める。より良い回答を得るには、effortを上げるより指示を具体的にすることが重要。

- **ソース**: [Zenn claude](https://zenn.dev/manntera/articles/9e98c6850f63c7)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

## 2026-08-12

### Claude Code 設定ガイド｜settings.jsonのスコープ優先順位とpermissions設計

Claude Code の設定ファイル（settings.json）は5段階のスコープ（Managed > コマンドライン引数 > Local > Project > User）で構成され、権限（permissions）は上書きではなくマージされる仕組みを持つ。各スコープの優先順位と適用範囲を理解し、組織・チーム・個人それぞれのレベルで適切に設定を管理する必要がある。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-settings-guide)
- **重要度**: 6/10
- **タグ**: claude-code, setup, vscode

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
