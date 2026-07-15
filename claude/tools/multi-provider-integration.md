---
title: Multi Provider Integration
category: tools
subcategory: multi-provider-integration
tags:
- claude-api
- cowork
- prompt
date: '2026-07-15'
updated: '2026-07-15'
sources:
- url: https://qiita.com/outcast_zari/items/720ef110e5d3be7c20a6
  title: 「OpenAI互換」は痩せていく ―― Claude/GPT/Gemini/Grok を1インターフェースに束ねた配線記録
  date: '2026-07-15'
---

# Multi Provider Integration

---

## 2026-07-15

### 「OpenAI互換」は痩せていく ―― Claude/GPT/Gemini/Grok を1インターフェースに束ねた配線記録

Claude、GPT、Gemini、Grokの4つのLLMプロバイダを統一インターフェースで扱う実装記録。「OpenAI互換」という言葉の範囲は実際には狭く、tool-use（function calling）、JSON Schema、プロンプトキャッシュのレイヤーでプロバイダごとに方言が存在する。各社の仕様差異をアダプタパターンで吸収し、canonical（中立の内部型）を通じて呼び出し側を統一する設計手法を解説。

- **ソース**: [Qiita claude](https://qiita.com/outcast_zari/items/720ef110e5d3be7c20a6)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
