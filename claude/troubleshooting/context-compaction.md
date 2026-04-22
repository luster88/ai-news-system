---
title: Context Compaction
category: troubleshooting
subcategory: context-compaction
tags:
- bugfix
- claude-code
- setup
date: '2026-04-22'
updated: '2026-04-22'
sources:
- url: https://zenn.dev/ai_arai_ally/articles/20260421-1601-claude-code-precompact-hook
  title: Claude Code の PreCompact hook で『幻覚編集』を封じた話
  date: '2026-04-22'
---

# Context Compaction

---

## 2026-04-22

### Claude Code の PreCompact hook で『幻覚編集』を封じた話

Claude Code でコンテキスト圧縮後に発生する「存在しないファイルへの編集」という幻覚問題と、その対策を解説。v2.1.83 で追加された PreCompact hook を使い、圧縮直前に git チェックポイントを自動作成することで、幻覚編集を検出・防止する仕組みを実装。CLAUDE.md への防御指示と git による外部事実の参照を組み合わせた3段構えの運用パターンを紹介している。

- **ソース**: [Zenn claude](https://zenn.dev/ai_arai_ally/articles/20260421-1601-claude-code-precompact-hook)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-22 | 自動生成 |
