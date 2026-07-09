---
title: Screenshot Automation
category: tools
subcategory: screenshot-automation
tags:
- claude-code
- mac
- setup
date: '2026-07-09'
updated: '2026-07-09'
sources:
- url: https://qiita.com/mfuad16/items/0a5ca36a36963278c668
  title: CodexのAppshotが便利すぎたので、Claude用にメニューバーアプリを作った話
  date: '2026-07-09'
---

# Screenshot Automation

---

## 2026-07-09

### CodexのAppshotが便利すぎたので、Claude用にメニューバーアプリを作った話

macOS用メニューバーアプリ「ClaudeShot」の開発記事。CodexのAppshot機能（ショートカット一発でウィンドウをAIに送る）がClaudeに無いため、外部から実装。SwiftUIとScreenCaptureKitを使い、グローバルショートカット（⇧⌘1）でキャプチャしクリップボード経由でClaude入力欄に貼り付ける仕組み。キャプチャ時のフラッシュ演出の実装とバグ修正についても詳述。

- **ソース**: [Qiita claudecode](https://qiita.com/mfuad16/items/0a5ca36a36963278c668)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-09 | 自動生成 |
