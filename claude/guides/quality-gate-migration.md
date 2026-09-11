---
title: Quality Gate Migration
category: guides
subcategory: quality-gate-migration
tags:
- claude-code
- prompt
- setup
date: '2026-09-11'
updated: '2026-09-11'
sources:
- url: https://zenn.dev/yuninaka/articles/guardrail-transplant-mypy-false-positive
  title: CLAUDE.mdに書いた検証習慣は移植できるか——品質ゲートを別プロジェクトに適用して見つかった「静かな誤検知」
  date: '2026-09-11'
---

# Quality Gate Migration

---

## 2026-09-11

### CLAUDE.mdに書いた検証習慣は移植できるか——品質ゲートを別プロジェクトに適用して見つかった「静かな誤検知」

Claude.mdに記録した品質ゲート（Ruff strict、mypy strict、vulture）を別プロジェクト（LangChain+Neo4j+ChromaDB）に移植する実験。「資産化すれば移植できる」という仮説を検証し、おおむね成立したが単純コピペでは済まなかった。特にmypy strictで「存在するはずの引数が存在しない」という偽陽性（false positive）が発生し、型定義の不備が原因と判明。品質ゲートの移植には、既存コードの修正や方針変更も必要となることが明らかになった実地検証の記録。

- **ソース**: [Zenn claude](https://zenn.dev/yuninaka/articles/guardrail-transplant-mypy-false-positive)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-11 | 自動生成 |
