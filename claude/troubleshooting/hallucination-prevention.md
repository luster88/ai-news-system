---
title: Hallucination Prevention
category: troubleshooting
subcategory: hallucination-prevention
tags:
- bugfix
- claude-code
- prompt
date: '2026-09-06'
updated: '2026-09-06'
sources:
- url: https://zenn.dev/kentaro_tak/articles/llm-guardrail-beats-prompt-rule
  title: AIの捏造を「プロンプトの約束」で直したつもりが、翌月また同じ事故が起きた
  date: '2026-09-06'
---

# Hallucination Prevention

---

## 2026-09-06

### AIの捏造を「プロンプトの約束」で直したつもりが、翌月また同じ事故が起きた

Claude を使った口座残高記録で、プロンプトルールで捏造を防いだつもりが翌月に再発。プロンプトは確率を上げるだけで制約にならないことを痛感し、出力側に機械ガード（生ログの user ターンに実在するか検証）を実装。記録系 AI 利用では「原文への忠実性検証」が有効だが、要約や複雑な導出には適用できない限界も明記。

- **ソース**: [Zenn claude](https://zenn.dev/kentaro_tak/articles/llm-guardrail-beats-prompt-rule)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-06 | 自動生成 |
