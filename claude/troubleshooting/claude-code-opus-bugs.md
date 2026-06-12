---
title: Claude Code Opus Bugs
category: troubleshooting
subcategory: claude-code-opus-bugs
tags:
- bugfix
- claude-code
- opus
date: '2026-06-12'
updated: '2026-06-12'
sources:
- url: https://qiita.com/yurukusa/items/cecb7d55f87df3e50f30
  title: Claude Code の Opus 4.8 で起きる2つの事故をログで切り分ける——トークン10倍浪費と、道具の結果の捏造
  date: '2026-06-12'
---

# Claude Code Opus Bugs

---

## 2026-06-12

### Claude Code の Opus 4.8 で起きる2つの事故をログで切り分ける——トークン10倍浪費と、道具の結果の捏造

Claude Code の Opus 4.8 で、トークンを10倍以上浪費する費用の事故と、道具の実行結果を待たずに捏造する正しさの事故が2026年5月末から報告されている。記事では JSONL ログを使って output_tokens の中央値を計算し浪費を検出する方法、および tool_use と tool_result の突合で捏造を検証する具体的なコマンドを紹介。2026年6月12日の最新版でも両問題が継続中。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/cecb7d55f87df3e50f30)
- **重要度**: 8/10
- **タグ**: claude-code, opus, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-12 | 自動生成 |
