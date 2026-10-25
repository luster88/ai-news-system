---
title: Permissions Windows
category: troubleshooting
subcategory: permissions-windows
tags:
- claude-code
- setup
- windows
date: '2026-10-25'
updated: '2026-10-25'
sources:
- url: https://zenn.dev/shingokumon/articles/95dff2530556ce
  title: Claude Code の deny を Windows 実機で測ったら、思っていたより効いていなかった
  date: '2026-10-25'
---

# Permissions Windows

---

## 2026-10-25

### Claude Code の deny を Windows 実機で測ったら、思っていたより効いていなかった

Claude Code の deny 設定を Windows 実機で検証した結果、想定と異なる挙動が複数確認された。特に、settings.json に無効な値が1つでもあるとファイル全体が無視される、Read と Edit の deny が非対称、シェルコマンドは止められないなど、セキュリティ上の注意点が明らかになった。

- **ソース**: [Zenn claude](https://zenn.dev/shingokumon/articles/95dff2530556ce)
- **重要度**: 7/10
- **タグ**: claude-code, setup, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-25 | 自動生成 |
