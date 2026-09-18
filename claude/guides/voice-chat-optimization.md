---
title: Voice Chat Optimization
category: guides
subcategory: voice-chat-optimization
tags:
- haiku
- performance
- prompt
date: '2026-09-18'
updated: '2026-09-18'
sources:
- url: https://zenn.dev/mskbhd/articles/lab-692-100ms
  title: '発話終端判定にLLMは要るか: STTの句読点だけでHaiku並みだった'
  date: '2026-09-18'
---

# Voice Chat Optimization

---

## 2026-09-18

### 発話終端判定にLLMは要るか: STTの句読点だけでHaiku並みだった

リアルタイム音声チャットの発話終端判定において、Claude Haiku 4.5を用いた判定とSTTの句読点のみを用いたコストゼロのルールベース判定を比較実験。結果、句読点ルールがHaiku並みの精度を示し、判定の遅延が誤判定を隠す効果があること、投機的実行では判定器の効果が消えることが判明。ローカル小モデル(qwen3/gemma4)は判定器として機能しなかった。

- **ソース**: [Zenn claude](https://zenn.dev/mskbhd/articles/lab-692-100ms)
- **重要度**: 6/10
- **タグ**: haiku, performance, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-18 | 自動生成 |
