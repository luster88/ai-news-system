---
title: Claude Code Regression
category: troubleshooting
subcategory: claude-code-regression
tags:
- bugfix
- claude-code
- performance
date: '2026-04-24'
updated: '2026-04-24'
sources:
- url: https://qiita.com/yurukusa/items/034736162c7637212e32
  title: Claude Codeが2ヶ月劣化していた正体：Anthropic公式postmortem（4/23）の3 bugsを日本語解説＋自衛策3つ
  date: '2026-04-24'
---

# Claude Code Regression

---

## 2026-04-24

### Claude Codeが2ヶ月劣化していた正体：Anthropic公式postmortem（4/23）の3 bugsを日本語解説＋自衛策3つ

Anthropicが公式postmortemで、2026年3月から4月にかけてのClaude Code品質低下の原因を3つのバグ（Reasoning effort downgrade、Caching bug、Verbosity instruction）として発表。全subscriberにusage limits resetで補償。独立調査勢はCache TTL 1h→5mへの変更も指摘しており、公式発表とは別の問題の可能性がある。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/034736162c7637212e32)
- **重要度**: 9/10
- **タグ**: claude-code, bugfix, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-24 | 自動生成 |
