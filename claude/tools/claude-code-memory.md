---
title: Claude Code Memory
category: tools
subcategory: claude-code-memory
tags:
- claude-code
- mcp
- performance
- setup
- 新機能
date: '2026-03-28'
updated: '2026-04-10'
sources:
- url: https://zenn.dev/okamyuji/articles/engram-claude-code-local-memory
  title: Engram - Claude Codeの会話を自動記録し、過去の記憶を検索・注入するローカル長期記憶システム
  date: '2026-03-28'
- url: https://qiita.com/taketsuyo/items/c9024c668861d56975a9
  title: Claude Codeの本当の敵は性能不足じゃない。毎回「思い出し直し」が発生することだ
  date: '2026-04-10'
---


# Claude Code Memory

---

## 2026-04-10

### Claude Codeの本当の敵は性能不足じゃない。毎回「思い出し直し」が発生することだ

Claude Codeの実用上の課題は性能ではなく、セッションごとに文脈を再構築する「思い出し直し」のコストであると指摘。claude-memは検索→タイムライン→詳細取得の段階的読み出しで約10倍のトークン節約を実現し、48時間で46,000スターを獲得。公式のauto memoryに検索性と可搬性を追加し、記憶層をインフラとして切り出す設計が評価されている。

- **ソース**: [Qiita claudecode](https://qiita.com/taketsuyo/items/c9024c668861d56975a9)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, performance

---

## 2026-03-28

### Engram - Claude Codeの会話を自動記録し、過去の記憶を検索・注入するローカル長期記憶システム

Claude Codeのセッション会話を自動記録し、過去の議論や設計判断を検索・参照できるローカル長期記憶システム「Engram」の紹介記事。sui-memoryの設計思想をTypeScriptで再実装し、SQLite単一ファイルとhookだけで動作。claude-memの課題（ディスク肥大化、記憶参照の不確実性、トークン消費）を解決し、UserPromptSubmit hookによる「常時参照」で明示的検索なしに関連記憶を自動注入する。

- **ソース**: [Zenn claude](https://zenn.dev/okamyuji/articles/engram-claude-code-local-memory)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-28 | 自動生成 |
