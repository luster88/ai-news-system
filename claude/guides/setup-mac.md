---
title: Setup Mac
category: guides
subcategory: setup-mac
tags:
- claude-code
- mac
- mcp
- setup
- vscode
date: '2026-03-25'
updated: '2026-10-23'
sources:
- url: https://zenn.dev/fivot/articles/0392437670c826
  title: Claude Code / Claude Desktopで音声対話環境を構築する【Mac】
  date: '2026-03-25'
- url: https://qiita.com/OnuuuumaX/items/265c2d0b2b9b131b4aa6
  title: 【Axmol Engine】macOSでVSCodeを使ってiOS/Androidアプリを開発する（プロジェクト作成〜Claude Code連携まで）
  date: '2026-06-18'
- url: https://qiita.com/joinclass/items/5558c5fc23788c4c082a
  title: launchdで定期実行するClaude Code — 33ジョブを回して分かったplist設計とログ設計
  date: '2026-10-23'
---



# Setup Mac

---

## 2026-10-23

### launchdで定期実行するClaude Code — 33ジョブを回して分かったplist設計とログ設計

Mac の launchd で Claude Code を定期実行する実践例。33個のジョブを運用する中で得られた知見として、plist にはスケジュールのみを記述しシェル側にロジックを集約する設計、Disabled の代わりにファイル名変更で停止管理、PATH や環境変数を common.sh に集約する手法、コスト追跡ラッパーによる月額制限の実装などを解説。launchd 特有の落とし穴（フルディスクアクセス、PATH 不継承、エラー通知の欠如）への対処法も示されている。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/5558c5fc23788c4c082a)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 2026-06-18

### 【Axmol Engine】macOSでVSCodeを使ってiOS/Androidアプリを開発する（プロジェクト作成〜Claude Code連携まで）

macOS環境でAxmol Engineを使ったiOS/Androidアプリ開発をVSCodeで行う方法を解説。プロジェクト作成からClaude Code連携までのセットアップ手順、推奨拡張機能、IntelliSense設定、Claude Code拡張機能とCLIの導入方法を詳しく説明。AIペアプログラミングでゲーム開発を効率化する実践的なガイド。

- **ソース**: [Qiita claude](https://qiita.com/OnuuuumaX/items/265c2d0b2b9b131b4aa6)
- **重要度**: 5/10
- **タグ**: claude-code, vscode, setup

---

### 【Axmol Engine】macOSでVSCodeを使ってiOS/Androidアプリを開発する（プロジェクト作成〜Claude Code連携まで）

macOSとVSCodeを使ってAxmol Engine（Cocos2d-xの後継）でiOS/Androidアプリを開発する環境を構築し、Claude Code拡張機能を導入する手順を解説。プロジェクト作成、VSCode設定、Claude Code（拡張機能版とCLI版）のセットアップ、AIペアプログラミングの実践方法までカバー。CMake Toolsとの組み合わせで、コーディングからデバッグまでVSCode上で完結できる。

- **ソース**: [Qiita claudecode](https://qiita.com/OnuuuumaX/items/265c2d0b2b9b131b4aa6)
- **重要度**: 6/10
- **タグ**: claude-code, setup, vscode

---

## 2026-03-25

### Claude Code / Claude Desktopで音声対話環境を構築する【Mac】

Mac環境でClaude Code/Claude Desktopに音声対話機能を実装する方法を解説。Superwhisperによる音声入力とMCP+sayコマンドによる音声読み上げを組み合わせ、キーボードを使わずに声で操作・耳で返答を聞く環境を構築する。Custom Instructionsの設定とclaude.jsonへのMCP登録が必要。

- **ソース**: [Zenn claude](https://zenn.dev/fivot/articles/0392437670c826)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-25 | 自動生成 |
