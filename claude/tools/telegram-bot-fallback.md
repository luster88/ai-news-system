---
title: Telegram Bot Fallback
category: tools
subcategory: telegram-bot-fallback
tags:
- claude-api
date: '2026-03-26'
updated: '2026-03-26'
sources:
- url: https://zenn.dev/acropapa330/articles/llm_fallback_bot
  title: Claude障害時でも止まらないTelegramボット：Gemini・OllamaへのLLMフォールバック実装
  date: '2026-03-26'
---

# Telegram Bot Fallback

---

## 2026-03-26

### Claude障害時でも止まらないTelegramボット：Gemini・OllamaへのLLMフォールバック実装

Claude障害時の冗長構成として、Gemini API・Ollama（qwen3.5）へのフォールバック機能を持つTelegramボットを実装。Web検索（Brave Search API）とコード実行も各モードに対応。GeminiとOllamaそれぞれで発生した問題（履歴のロールプレイ誤解、Thinkingモード、gzipエラー等）と解決策を詳述。

- **ソース**: [Zenn claude](https://zenn.dev/acropapa330/articles/llm_fallback_bot)
- **重要度**: 6/10
- **タグ**: claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-26 | 自動生成 |
