---
title: Claude Code Integration
category: guides
subcategory: claude-code-integration
tags:
- claude-code
- cowork
- mcp
- prompt
date: '2026-04-02'
updated: '2026-04-24'
sources:
- url: https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code
  title: Claude CodeでAI RSSリーダーを作ったら、その日にInoreaderを解約した
  date: '2026-04-02'
- url: https://qiita.com/Tadashi_Kudo/items/c35c0aaed00878d88b05
  title: ObsidianとClaude Codeで作る「第二の脳」——Vault自動管理の全体設計
  date: '2026-04-24'
---


# Claude Code Integration

---

## 2026-04-24

### ObsidianとClaude Codeで作る「第二の脳」——Vault自動管理の全体設計

ObsidianとClaude Codeを組み合わせ、AIエージェントが自動的にVaultを管理する「第二の脳」システムの設計を紹介。CLAUDE.mdによる行動ルール明文化、MEMORY.mdでの状態永続化、scheduled-tasksによる定期メンテ自動化、ベクトル検索MCPによる概念検索、Gitによる変更履歴管理の5つの要素で構成される。AIに整理・検索・連携を任せることで、ノート作成に集中できる環境を実現する。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/c35c0aaed00878d88b05)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-04-02

### Claude CodeでAI RSSリーダーを作ったら、その日にInoreaderを解約した

Claude Code CLIの-pオプションを活用したパーソナライズRSSリーダー「Feed Curator」の開発事例。APIキー不要でClaude Codeの認証を流用し、既読履歴から嗜好を学習して技術ブリーフィングを自動生成。トークン消費を抑えるため記事全文ではなく先頭500文字+末尾300文字のみ送信し、1日2-4万トークンで運用可能。開発当日にInoreaderを解約した実体験レポート。

- **ソース**: [Zenn claude](https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
