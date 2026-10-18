---
title: Model Comparison
category: releases
subcategory: model-comparison
tags:
- haiku
- opus
- performance
- pricing
- sonnet
- 新機能
date: '2026-04-16'
updated: '2026-10-18'
sources:
- url: https://qiita.com/rikiza1989/items/2889bebbdccf36e95a16
  title: 【検証】Claude Opus 4.7 は本当に "世代的進化" なのか？Opus 4.6・Sonnet 4.6・GPT-5.4・Gemini 3.1
    Pro と徹底比較してわかった3つの真実
  date: '2026-04-16'
- url: https://zenn.dev/shoujiki_panman/articles/claude-sonnet-5-5-or-opus
  title: Opus 5.5とSonnet 5.5、どっちを使う？ 新しいSonnet 5.5を数字で比べた
  date: '2026-10-06'
- url: https://zenn.dev/aimodelrecord/articles/claude-haiku-45-to-55
  title: Claude Haiku 4.5 → 5.5 で答えはどう変わる？同じ100問を11日間聞き比べた
  date: '2026-10-18'
---



# Model Comparison

---

## 2026-10-18

### Claude Haiku 4.5 → 5.5 で答えはどう変わる？同じ100問を11日間聞き比べた

Claude Haiku 4.5から5.5への移行による挙動の変化を、同一の100問を11日間にわたり比較検証した記事。5.5ではtemperature固定により出力の再現性が4.5の96%から46%に低下、コードブロックの扱いが変化、adaptive thinkingがデフォルト有効でmax_tokens制限に影響するなど、実装上の注意点が多数報告されている。特に5.5では同じ質問でも約半分が異なる回答を返すため、キャッシュやテスト実装に影響が出る可能性がある。

- **ソース**: [Zenn claude](https://zenn.dev/aimodelrecord/articles/claude-haiku-45-to-55)
- **重要度**: 8/10
- **タグ**: haiku, 新機能, performance

---

## 2026-10-06

### Opus 5.5とSonnet 5.5、どっちを使う？ 新しいSonnet 5.5を数字で比べた

Anthropicが2026年9月28日にClaude Sonnet 5.5をリリース。Sonnet 5より30%以上高速化し、1回答あたりのトークン数は約4分の1に削減。料金はSonnet 5と同額（入力$2/100万トークン、出力$10/100万トークン）でOpus 5.5の半額。多くのベンチマークでOpus 5.5に迫る性能を示し、コマンド操作を伴うプログラミングではOpus 5.5を上回る結果も。日常的なバグ修正や文書作成にはSonnet 5.5、複雑な設計判断にはOpus 5.5が推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/shoujiki_panman/articles/claude-sonnet-5-5-or-opus)
- **重要度**: 8/10
- **タグ**: sonnet, opus, performance

---

## 2026-04-16

### 【検証】Claude Opus 4.7 は本当に "世代的進化" なのか？Opus 4.6・Sonnet 4.6・GPT-5.4・Gemini 3.1 Pro と徹底比較してわかった3つの真実

Claude Opus 4.7の検証記事。SWE-bench Verifiedで87.6%を達成し、GPT-5.4やGemini 3.1 Proとの比較でコーディング性能の優位性を示す一方、価格は競合の2倍以上。フロンティア3強の棲み分けが明確化し、Opus 4.7はコーディング特化、GPT-5.4はコンピュータ使用、Gemini 3.1 Proはコスパ・長文脈に強みを持つ。Anthropicは安全性ガードレールを本番投入で検証する戦略も採用。

- **ソース**: [Qiita claudecode](https://qiita.com/rikiza1989/items/2889bebbdccf36e95a16)
- **重要度**: 8/10
- **タグ**: opus, performance, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-16 | 自動生成 |
