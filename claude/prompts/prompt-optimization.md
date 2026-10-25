---
title: Prompt Optimization
category: prompts
subcategory: prompt-optimization
tags:
- claude-api
- claude-code
- performance
- prompt
date: '2026-04-07'
updated: '2026-10-25'
sources:
- url: https://zenn.dev/mikana0918/articles/7ad57493a04f88
  title: 'Claudeトークン消費を抑えて５倍使う: 「原始人」口調が80%削減'
  date: '2026-04-07'
- url: https://qiita.com/R-You/items/690c9f2c95b7019732ca
  title: AIに自分のプロンプトを改善させたら、長くなりすぎたので進化的最適化してみた
  date: '2026-10-25'
---


# Prompt Optimization

---

## 2026-10-25

### AIに自分のプロンプトを改善させたら、長くなりすぎたので進化的最適化してみた

AWS Bedrockの記事を参考に、AIに自身のプロンプトを自動改善させる実験を実施。最初の改善で精度100%に達したが、プロンプトが8倍に膨張。失敗情報がなくなると改善が停止する問題を発見。明示的に圧縮指示を追加することで43%の圧縮に成功。進化的最適化（交叉・突然変異）を導入し、より短く安価なプロンプトで同等精度を達成した。

- **ソース**: [Qiita claude](https://qiita.com/R-You/items/690c9f2c95b7019732ca)
- **重要度**: 6/10
- **タグ**: prompt, claude-api, performance

---

## 2026-04-07

### Claudeトークン消費を抑えて５倍使う: 「原始人」口調が80%削減

Claude Code向けのトークン削減プロンプトテクニック「caveman」と日本語版「genshijin（原始人）」の紹介記事。敬語や冗長表現を削除し、日本語で約80%のトークン削減を実現。トークナイザの仕組みと日本語の言語構造を分析し、出力コスト削減方法を解説している。

- **ソース**: [Zenn claude](https://zenn.dev/mikana0918/articles/7ad57493a04f88)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-07 | 自動生成 |
