---
title: Llm Reasoning Limits
category: troubleshooting
subcategory: llm-reasoning-limits
tags:
- claude-api
- opus
- sonnet
date: '2026-09-22'
updated: '2026-09-22'
sources:
- url: https://zenn.dev/kana001_bit/articles/ai-werewolf-less-llm
  title: AI 人狼で LLM に決めさせることを 1 つずつ機械に移したら、残ったのは『候補から選ぶ』と『文章にする』だけだった
  date: '2026-09-22'
---

# Llm Reasoning Limits

---

## 2026-09-22

### AI 人狼で LLM に決めさせることを 1 つずつ機械に移したら、残ったのは『候補から選ぶ』と『文章にする』だけだった

8cfo配役のAI人狼でClaude（Opus/Sonnet 5）に戦略を決めさせたところ、LLMは定石を教えても通常人狼の常識に固執し、この配役で最強の「共有者ペア騙り」を選ばなかった。そこで段階的にLLMの判断範囲を縮小し、最終的に「候補から選ぶ」と「文章生成」のみをLLMに任せ、戦略判断は機械的に決定する形に移行した記録。LLMは配役固有のルールより学習データの一般論を優先する傾向が明らかになった。

- **ソース**: [Zenn claude](https://zenn.dev/kana001_bit/articles/ai-werewolf-less-llm)
- **重要度**: 6/10
- **タグ**: claude-api, opus, sonnet

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-22 | 自動生成 |
