---
title: Mcp Server Migration
category: guides
subcategory: mcp-server-migration
tags:
- claude-code
- mcp
- setup
date: '2026-07-31'
updated: '2026-07-31'
sources:
- url: https://zenn.dev/ojisan_ai_lab/articles/mcp-dual-era-20260731
  title: 【実測】MCP 2026-07-28版に対応した自作サーバに、旧仕様のClaude Code 2.1.220を繋いだら動きました
  date: '2026-07-31'
---

# Mcp Server Migration

---

## 2026-07-31

### 【実測】MCP 2026-07-28版に対応した自作サーバに、旧仕様のClaude Code 2.1.220を繋いだら動きました

MCP仕様2026-07-28版への対応実装レポート。28項目の変更のうち、stdio方式の自作サーバでは12項目のみ実装が必要だった。旧仕様のClaude Code 2.1.220でも動作することを実測で確認。ステートレス化、resultType必須化、ttlMs/cacheScope追加などの主要変更点と、新旧クライアント判定の落とし穴（_metaの扱い）を詳説。新仕様のみ対応版では「エラーではなくツールが消える」という失敗パターンも報告。

- **ソース**: [Zenn claude](https://zenn.dev/ojisan_ai_lab/articles/mcp-dual-era-20260731)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-31 | 自動生成 |
