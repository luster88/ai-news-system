---
title: Context Engineering
category: prompts
subcategory: context-engineering
tags:
- claude-api
- opus
- prompt
- sonnet
date: '2026-07-27'
updated: '2026-08-02'
sources:
- url: https://zenn.dev/lingmu/articles/2026-07-28-claude-5-context-engineering
  title: Claude 5時代の「文脈設計」が勝敗を決める
  date: '2026-07-27'
- url: https://zenn.dev/frb_tamasub/articles/context-diff-01
  title: 'CONTEXT DIFF #1 — 同じ画像・同じ質問でも、AIが見る「本質」は変わる？——判断軸と制約を分けるまでの5つの失敗'
  date: '2026-08-02'
---


# Context Engineering

---

## 2026-08-02

### CONTEXT DIFF #1 — 同じ画像・同じ質問でも、AIが見る「本質」は変わる？——判断軸と制約を分けるまでの5つの失敗

Claude Sonnet 4.6 を使った実験記事。同じ画像・同じ質問でも、事前に与えた「判断軸」の文脈によってAIの解釈や言葉選びが変わることを検証。Yes/No形式では結論は同じでも理由の表現が変化し、3枚比較では文脈の有無で選択結果が逆転するなど、プロンプトの指示文以外にも文脈が挙動に影響することを5つの失敗を通じて示した実験報告。

- **ソース**: [Zenn claude](https://zenn.dev/frb_tamasub/articles/context-diff-01)
- **重要度**: 6/10
- **タグ**: prompt, sonnet, claude-api

---

## 2026-07-27

### Claude 5時代の「文脈設計」が勝敗を決める

Claude Opus 5のリリース後、同じモデルでも結果に差が出る原因は「コンテキスト工学」にあることが判明。Anthropic公式が提唱する3層のコンテキスト設計（指示層・会話層・構造層）が重要で、システムプロンプトに「役割・制約・出力形式」を明示し、重要情報を先頭や末尾に配置することで精度が劇的に向上する。Claude Cookbookの実装パターンを活用することが最速の改善方法として推奨されている。

- **ソース**: [Zenn claude](https://zenn.dev/lingmu/articles/2026-07-28-claude-5-context-engineering)
- **重要度**: 8/10
- **タグ**: prompt, opus, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-27 | 自動生成 |
