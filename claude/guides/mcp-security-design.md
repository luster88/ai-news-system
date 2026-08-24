---
title: Mcp Security Design
category: guides
subcategory: mcp-security-design
tags:
- mcp
- prompt
- 新機能
date: '2026-08-24'
updated: '2026-08-24'
sources:
- url: https://zenn.dev/ma2no4413/articles/mcp-no-send-tool-by-design
  title: 送信できない Outlook MCP を作った — 「機能の不在」でプロンプトインジェクションに備える
  date: '2026-08-24'
---

# Mcp Security Design

---

## 2026-08-24

### 送信できない Outlook MCP を作った — 「機能の不在」でプロンプトインジェクションに備える

MCP（Model Context Protocol）サーバーを実装する際のセキュリティ設計について、Outlook連携を例に解説。メール送信機能を「実装しない」のではなく「権限レベルで要求しない」ことで、プロンプトインジェクション攻撃を根本的に防ぐ設計思想を提示。アプリケーション層のガードではなく、ID層での権限制御によって安全性を担保し、下書き機能で実用性も確保している。

- **ソース**: [Zenn claude](https://zenn.dev/ma2no4413/articles/mcp-no-send-tool-by-design)
- **重要度**: 7/10
- **タグ**: mcp, prompt, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-24 | 自動生成 |
