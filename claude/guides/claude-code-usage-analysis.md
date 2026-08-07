---
title: Claude Code Usage Analysis
category: guides
subcategory: claude-code-usage-analysis
tags:
- claude-code
- performance
- prompt
date: '2026-08-07'
updated: '2026-08-07'
sources:
- url: https://zenn.dev/flipslidersand/articles/claude-code-1b-tokens
  title: Claude Codeで1週間に1Bトークン使ったと思ったら、97%がキャッシュだった
  date: '2026-08-07'
---

# Claude Code Usage Analysis

---

## 2026-08-07

### Claude Codeで1週間に1Bトークン使ったと思ったら、97%がキャッシュだった

Claude Codeで1週間に1.36Bトークンを使用したが、その97.4%はPrompt Cachingによるcache_readだった。実際に新規生成されたトークンは36M程度で、Claude Codeは巨大なコンテキストをキャッシュから効率的に再利用しながら動作している。読み込み量は出力量の230倍に達し、膨大な情報を参照しながら少量の判断を出力する動作パターンが明らかになった。

- **ソース**: [Zenn claude](https://zenn.dev/flipslidersand/articles/claude-code-1b-tokens)
- **重要度**: 7/10
- **タグ**: claude-code, performance, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-07 | 自動生成 |
