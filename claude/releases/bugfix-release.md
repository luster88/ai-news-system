---
title: Bugfix Release
category: releases
subcategory: bugfix-release
tags:
- bugfix
- claude-code
- mac
date: '2026-09-02'
updated: '2026-09-02'
sources:
- url: https://qiita.com/moha0918_/items/9cdc566dadb9a8e30e1a
  title: Claude Code v2.1.258｜macOS 12 で起動できない退行が直る｜毎日Changelog解説
  date: '2026-09-02'
---

# Bugfix Release

---

## 2026-09-02

### Claude Code v2.1.258｜macOS 12 で起動できない退行が直る｜毎日Changelog解説

Claude Code v2.1.258 がリリースされ、macOS 12 (Monterey) で起動できなくなっていた退行バグが修正されました。v2.1.255 で発生したこの問題は、macOS 12 環境でのアプリ起動を完全に阻害していました。また、リモートセッションとスケジュールセッションが「user messages must have non-empty content」エラーで失敗する問題も修正されています。権限承認の再送時に空のユーザーメッセージがAPIに渡されていたことが原因でした。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/9cdc566dadb9a8e30e1a)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-02 | 自動生成 |
