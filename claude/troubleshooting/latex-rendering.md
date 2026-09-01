---
title: Latex Rendering
category: troubleshooting
subcategory: latex-rendering
tags:
- bugfix
- claude-console
- prompt
date: '2026-09-01'
updated: '2026-09-01'
sources:
- url: https://zenn.dev/artemis_rh/articles/1b6230c496e902
  title: 'LLMチャットの数式が崩れるのは乱数ではない: 再現条件を実験で特定して、プロフィールに貼るルールにした'
  date: '2026-09-01'
---

# Latex Rendering

---

## 2026-09-01

### LLMチャットの数式が崩れるのは乱数ではない: 再現条件を実験で特定して、プロフィールに貼るルールにした

LLMチャットで数式が崩れる現象は乱数ではなく、再現条件が特定できる。実験により、自動サイズ括弧（\left \right）内に上付き・下付き・分数を含むと崩れることが判明。20項目の回避ルールをプロフィールに追加することで、数式の崩れをほぼ解消できた。モデルは自分の出力を観測できないため、人間がレンダラー側として検証する実験設計が重要。

- **ソース**: [Zenn claude](https://zenn.dev/artemis_rh/articles/1b6230c496e902)
- **重要度**: 6/10
- **タグ**: claude-console, bugfix, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-01 | 自動生成 |
