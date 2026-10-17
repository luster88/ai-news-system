---
title: Claude Code Workspace
category: guides
subcategory: claude-code-workspace
tags:
- claude-code
- prompt
- setup
date: '2026-10-17'
updated: '2026-10-17'
sources:
- url: https://zenn.dev/tmiyachi/articles/folder-design-claude-md-loading
  title: Claude Codeのフォルダ設計は、CLAUDE.mdが「いつ読まれるか」から逆算する ― ルートに地図、部署に部署のルール
  date: '2026-10-17'
---

# Claude Code Workspace

---

## 2026-10-17

### Claude Codeのフォルダ設計は、CLAUDE.mdが「いつ読まれるか」から逆算する ― ルートに地図、部署に部署のルール

Claude Codeのフォルダ設計において、CLAUDE.mdが読み込まれるタイミング（ルートは起動時、サブフォルダはファイル参照時）を理解することが重要。ルートには全体共通ルールと各フォルダの「地図」を置き、各部署フォルダには部署固有のルールを配置する。この設計により、AIが適切なフォルダにたどり着き、必要なルールだけを効率的に読み込める。200行以下の目安を守ることでコンテキスト効率を最適化し、指示が守られやすくなる。

- **ソース**: [Zenn claude](https://zenn.dev/tmiyachi/articles/folder-design-claude-md-loading)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-17 | 自動生成 |
