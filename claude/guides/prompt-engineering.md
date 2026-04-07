---
title: Prompt Engineering
category: guides
subcategory: prompt-engineering
tags:
- claude-code
- performance
- prompt
date: '2026-04-07'
updated: '2026-04-07'
sources:
- url: https://zenn.dev/analysis/articles/thought-analyzer-agents-md
  title: コンテキストファイルは、エージェントを賢くしない ── AGENTS.mdの効果を初めて測った研究
  date: '2026-04-07'
---

# Prompt Engineering

---

## 2026-04-07

### コンテキストファイルは、エージェントを賢くしない ── AGENTS.mdの効果を初めて測った研究

ETH Zurichの研究により、CLAUDE.mdやAGENTS.mdなどのコンテキストファイルがエージェントのタスク成功率を平均3%低下させ、コストを20%以上増加させることが判明。LLMが自動生成したコンテキストファイルは特に効果が低く、人間が書く場合も「LLMが推論できない固有情報」のみに絞るべきと結論。thought-analyzerのskill.md v3.0設計も同様の知見に基づき、不要な指示を削除して簡略化している。

- **ソース**: [Zenn claude](https://zenn.dev/analysis/articles/thought-analyzer-agents-md)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-07 | 自動生成 |
