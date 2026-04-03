---
title: Claude Desktop Extension
category: tools
subcategory: claude-desktop-extension
tags:
- claude-code
- vscode
- 新機能
date: '2026-04-03'
updated: '2026-04-03'
sources:
- url: https://zenn.dev/saqoosha/articles/ccdex-claude-desktop-context-indicator
  title: Claude Desktop にコンテキスト残量メーターを生やした話
  date: '2026-04-03'
---

# Claude Desktop Extension

---

## 2026-04-03

### Claude Desktop にコンテキスト残量メーターを生やした話

Claude Desktop の Code タブにコンテキスト使用量とレートリミット状況をリアルタイム表示する拡張 CCDEX を開発。Electron の Fuse によるセキュリティ制限を回避するため、バイナリレベルでの ASAR パッチという力技で実装。IPC イベントからトークン使用量を取得し、Claude.ai の API を利用してレートリミット情報を表示する。

- **ソース**: [Zenn claude](https://zenn.dev/saqoosha/articles/ccdex-claude-desktop-context-indicator)
- **重要度**: 6/10
- **タグ**: claude-code, vscode, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-03 | 自動生成 |
