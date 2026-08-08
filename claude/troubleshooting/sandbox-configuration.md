---
title: Sandbox Configuration
category: troubleshooting
subcategory: sandbox-configuration
tags:
- bugfix
- claude-code
- setup
date: '2026-08-08'
updated: '2026-08-08'
sources:
- url: https://qiita.com/yurukusa/items/216e41649a628f6feb0f
  title: denyに書いたのに読めてしまう——sandbox設定が黙って無効になる条件
  date: '2026-08-08'
---

# Sandbox Configuration

---

## 2026-08-08

### denyに書いたのに読めてしまう——sandbox設定が黙って無効になる条件

Claude Codeのsandbox設定で、denyReadをpermissionsの下に誤って書くと警告なしで無効化される問題を解説。permissionsとsandbox.filesystemは別の仕組みで、パス記法も異なる（//path vs /path）。相対パスは設定ファイルの場所を基準に解決され、誤った場所に書くと意図したパスを保護できない。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/216e41649a628f6feb0f)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-08 | 自動生成 |
