---
title: Memory Context Management
category: guides
subcategory: memory-context-management
tags:
- claude-console
- cowork
- prompt
date: '2026-08-14'
updated: '2026-08-14'
sources:
- url: https://zenn.dev/every_ai_recipe/articles/ai-memory-work-mode-settings
  title: 自動検索されるLLMメモリと、明示的呼び出しのメモリの設計差
  date: '2026-08-14'
---

# Memory Context Management

---

## 2026-08-14

### 自動検索されるLLMメモリと、明示的呼び出しのメモリの設計差

ChatGPT・Geminiは過去の会話から個人情報を自動抽出し無関係なタスクにも暗黙にコンテキスト注入する「自動検索型メモリ」を採用。対してClaudeは2026年3月に全プラン展開されたメモリ機能で「明示的呼び出し」方式を採用し、ユーザーが参照を指示しない限りコンテキストに含まれない設計でコンテキスト汚染を構造的に回避。検証により、ChatGPTでは会議メモ要約時に転職相談の文脈が意図せず混入したが、Claudeは過去の個人的相談への言及を含まなかった。

- **ソース**: [Zenn claude](https://zenn.dev/every_ai_recipe/articles/ai-memory-work-mode-settings)
- **重要度**: 7/10
- **タグ**: claude-console, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-14 | 自動生成 |
