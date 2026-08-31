---
title: Claude Code Context
category: guides
subcategory: claude-code-context
tags:
- claude-code
- performance
- prompt
date: '2026-08-31'
updated: '2026-08-31'
sources:
- url: https://ai-heartland.com/explain/claude-code-compact-guide
  title: Claude Code compact｜圧縮で何が残り何が消えるか、5,000トークンの閾値を実測で検証
  date: '2026-08-31'
---

# Claude Code Context

---

## 2026-08-31

### Claude Code compact｜圧縮で何が残り何が消えるか、5,000トークンの閾値を実測で検証

Claude Code compactコマンドの圧縮挙動を詳細に検証した記事。CLAUDE.mdはディスクから再注入されるため残るが、paths:付きルールは会話履歴ごと要約され消える。ファイルの読み直しは最大5件で、5,000トークン超のファイルは参照のみとなり中身は戻らない。日本語文書は中央値11,953トークンで閾値を超えるが、Pythonソースは中央値3,799トークンで多くが閾値内。スキルも1つあたり5,000トークン・合計25,000トークンで打ち切られる。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-compact-guide)
- **重要度**: 7/10
- **タグ**: claude-code, performance, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-31 | 自動生成 |
