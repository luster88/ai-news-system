---
title: Claude Code Model Split
category: guides
subcategory: claude-code-model-split
tags:
- claude-code
- opus
- sonnet
date: '2026-11-05'
updated: '2026-11-05'
sources:
- url: https://zenn.dev/scalar_sol_blog/articles/20261103-104939-claude-code-model-split
  title: Claude Code を Sonnet で動かし、判断だけ Opus に相談させ、下働きは Haiku に任せる設定を検証する
  date: '2026-11-05'
---

# Claude Code Model Split

---

## 2026-11-05

### Claude Code を Sonnet で動かし、判断だけ Opus に相談させ、下働きは Haiku に任せる設定を検証する

Claude Codeで「Opus（判断）、Sonnet（作業）、Haiku（サブエージェント）」の役割分担を settings.json で設定する方法と実際の動作を検証。結果、Exploreサブエージェントは仕様によりSonnetのまま動作し、Opusアドバイザーは明示的指示がない限り呼ばれないことが判明。実際の挙動をトランスクリプトやccrecで詳細に分析している。

- **ソース**: [Zenn claude](https://zenn.dev/scalar_sol_blog/articles/20261103-104939-claude-code-model-split)
- **重要度**: 7/10
- **タグ**: claude-code, sonnet, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-05 | 自動生成 |
