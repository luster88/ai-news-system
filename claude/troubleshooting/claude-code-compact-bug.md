---
title: Claude Code Compact Bug
category: troubleshooting
subcategory: claude-code-compact-bug
tags:
- bugfix
- claude-code
- performance
date: '2026-06-24'
updated: '2026-06-24'
sources:
- url: https://qiita.com/yurukusa/items/36f7fa231f885575f47b
  title: Claude Codeで「/compactしたのに費用が上がった」のはなぜか——自動圧縮の二重バグと、ccusageでの見分け方
  date: '2026-06-24'
---

# Claude Code Compact Bug

---

## 2026-06-24

### Claude Codeで「/compactしたのに費用が上がった」のはなぜか——自動圧縮の二重バグと、ccusageでの見分け方

Claude Codeの/compactコマンド実行後にトークン費用が上昇する現象について解説。古い事前計算の利用とキャッシュのbreakpoint設定の2つのバグが重なり、圧縮が効かない状態でcache creation（高額）が繰り返される問題を指摘。ccusageツールでcache_creationとcache_readの比率を確認する診断方法と、自動圧縮設定の見直しによる回避策を提示。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/36f7fa231f885575f47b)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-24 | 自動生成 |
