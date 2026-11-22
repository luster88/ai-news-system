---
title: Memory Errors
category: troubleshooting
subcategory: memory-errors
tags:
- bugfix
- claude-code
- setup
date: '2026-11-22'
updated: '2026-11-22'
sources:
- url: https://qiita.com/homhom44/items/e41dca096fb741f1b3b0
  title: Claude Code で "JavaScript heap out of memory" が出て落ちるときの対処(再起動・/compact・--safe-mode・/heapdump)
  date: '2026-11-22'
---

# Memory Errors

---

## 2026-11-22

### Claude Code で "JavaScript heap out of memory" が出て落ちるときの対処(再起動・/compact・--safe-mode・/heapdump)

Claude Code で Node.js プロセスがメモリ上限に達して落ちる問題の対処法を解説。再起動して claude --continue で会話を戻し、再発する場合は claude --safe-mode で設定側の問題を切り分ける。過去には v2.1.27 のバグや並列サブエージェント、長時間セッションが原因となったケースが報告されている。警告が出た段階で /compact コマンドを使うことでメモリを解放できる。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/e41dca096fb741f1b3b0)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-22 | 自動生成 |
