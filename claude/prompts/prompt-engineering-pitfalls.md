---
title: Prompt Engineering Pitfalls
category: prompts
subcategory: prompt-engineering-pitfalls
tags:
- claude-code
- prompt
- sonnet
date: '2026-08-18'
updated: '2026-09-01'
sources:
- url: https://zenn.dev/motimotinotch/articles/cd448e3f00a0af
  title: 禁止すれば安全、良い例を見せれば的確、資料を読ませれば賢くなる——本当に？
  date: '2026-08-18'
- url: https://qiita.com/tomada/items/9810d4ef764c12fb4a21
  title: 伝わる指示・伝わらない指示：悪い例と良い例で学ぶClaude Codeへの頼み方
  date: '2026-08-23'
- url: https://zenn.dev/nekoemon/articles/1ba734b11fb487
  title: 『書いていない基準は毎回その場で埋められる』ーーLLM脆弱性トリアージの揺れをプロンプトの「境界設定」で止めた話
  date: '2026-09-01'
---



# Prompt Engineering Pitfalls

---

## 2026-09-01

### 『書いていない基準は毎回その場で埋められる』ーーLLM脆弱性トリアージの揺れをプロンプトの「境界設定」で止めた話

LLMによるCVE脆弱性トリアージで判定が揺れる問題に対し、プロンプトに「具体的なキー名を指摘できない場合は要確認を選ばない」という境界設定ルールを導入して解決した事例。Claude Sonnet 3.5を使い、同一入力で判定が分かれる原因を「書いていない基準をLLMが自動補完する」と特定し、厳格な制約を追加することで再現性を高めた。構成情報の改善ループにより、過剰アラートを削減できることを実証。

- **ソース**: [Zenn claude](https://zenn.dev/nekoemon/articles/1ba734b11fb487)
- **重要度**: 7/10
- **タグ**: prompt, sonnet

---

## 2026-08-23

### 伝わる指示・伝わらない指示：悪い例と良い例で学ぶClaude Codeへの頼み方

Claude Codeへの指示文の書き方を検証した実践記事。曖昧な一言指示と「何を・どこに・どう・制約は」の4観点で構造化した指示を比較し、同じ依頼でも返答が変わる問題を指摘。具体例として集計機能追加やコード流儀の統一を扱い、明確な指示が往復回数とコンテキスト消費を削減することを実証している。

- **ソース**: [Qiita claudecode](https://qiita.com/tomada/items/9810d4ef764c12fb4a21)
- **重要度**: 7/10
- **タグ**: claude-code, prompt

---

## 2026-08-18

### 禁止すれば安全、良い例を見せれば的確、資料を読ませれば賢くなる——本当に？

AIに禁止事項を与えると意味を保ったまま表現を変えて回避する「もぐらたたき」現象、良い例への過学習、情報過多による精度低下など、実運用で遭遇した4つの落とし穴を実測ログで解説。禁止は表層パターンではなく意味レベルで、またはホワイトリスト方式で設計すべきと提言。

- **ソース**: [Zenn claude](https://zenn.dev/motimotinotch/articles/cd448e3f00a0af)
- **重要度**: 6/10
- **タグ**: prompt, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-18 | 自動生成 |
