---
title: Claude Code Ui
category: tools
subcategory: claude-code-ui
tags:
- claude-code
- mcp
- prompt
- setup
- windows
date: '2026-04-22'
updated: '2026-10-01'
sources:
- url: https://qiita.com/76Hata/items/9954d3763f231b2cc327
  title: Claude CodeのブラウザUI「KBLite」をWindowsでOSS公開しました——軽量化の設計と開発の裏側
  date: '2026-04-22'
- url: https://ai-heartland.com/agent/humanlayer-skills
  title: humanlayer/skillsとは｜6スキルの中身とCLAUDE.mdを条件付きに書き換える一本を自サイトで試算
  date: '2026-10-01'
---


# Claude Code Ui

---

## 2026-10-01

### humanlayer/skillsとは｜6スキルの中身とCLAUDE.mdを条件付きに書き換える一本を自サイトで試算

HumanLayerが公開するClaude Code向けスキル集「humanlayer/skills」の分析記事。6つのスキルで構成され、CLAUDE.mdを条件付きブロックに書き換える「improve-claude-md」が注目される。スキル本体は52,967バイトと軽量だが参照ファイルは99,193バイトと1.87倍重い。自動起動を止める方法が3通り混在しており統一されていない設計上の課題がある。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/humanlayer-skills)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, prompt

---

## 2026-04-22

### Claude CodeのブラウザUI「KBLite」をWindowsでOSS公開しました——軽量化の設計と開発の裏側

Claude CodeにブラウザUIを提供する軽量ツール「KBLite」のWindows版がOSS公開された。RAG・ChromaDB・Dockerを排除し、SQLite + FTS5による全文検索で会話履歴をローカル管理。依存関係を最小化し、Git for Windows環境で動作する初心者フレンドリーな設計。モデル切り替え、セッション管理、会話検索などの機能を搭載している。

- **ソース**: [Qiita claudecode](https://qiita.com/76Hata/items/9954d3763f231b2cc327)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-22 | 自動生成 |
