---
title: Mcp Error Handling
category: guides
subcategory: mcp-error-handling
tags:
- claude-code
- mcp
date: '2026-09-20'
updated: '2026-09-20'
sources:
- url: https://qiita.com/yukihayama/items/60233da442ef134d64d5
  title: MCPサーバーのエラーハンドリング — AIが自力で復帰する5つの設計パターン
  date: '2026-09-20'
---

# Mcp Error Handling

---

## 2026-09-20

### MCPサーバーのエラーハンドリング — AIが自力で復帰する5つの設計パターン

MCPサーバーでエラーが発生すると、Claude Codeが同じツールを呼び続けて会話が使えなくなる問題への対処法を解説。例外をそのまま投げるのではなく、エラーを分類し「retryable」フラグと「suggested_action」を含むJSON形式で返すことで、AIが自力で復旧できる設計を提案。safe_toolデコレータによる例外のラップ、サーキットブレーカーパターン、エラー種別の正しい設定など、5つの設計パターンを実装コード付きで紹介している。

- **ソース**: [Qiita claude](https://qiita.com/yukihayama/items/60233da442ef134d64d5)
- **重要度**: 7/10
- **タグ**: mcp, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-20 | 自動生成 |
