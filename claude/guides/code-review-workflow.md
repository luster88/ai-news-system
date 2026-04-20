---
title: Code Review Workflow
category: guides
subcategory: code-review-workflow
tags:
- claude-code
- cowork
- prompt
- sonnet
date: '2026-03-31'
updated: '2026-04-20'
sources:
- url: https://zenn.dev/whipea/articles/e63135d29f8e1f
  title: Claude Codeに課金してみたので、無料プランのAIで作った日記アプリのコードを本気レビューしてもらった
  date: '2026-03-31'
- url: https://zenn.dev/penpeen/articles/844f0773d5e018
  title: AIレビューの精度を上げたいなら、批判的観点でセルフレビューさせよ
  date: '2026-04-20'
---


# Code Review Workflow

---

## 2026-04-20

### AIレビューの精度を上げたいなら、批判的観点でセルフレビューさせよ

Claude による PR レビューで、2パス構成（網羅的レビュー→批判的検証）を導入したが、人間の吟味コストが課題に。LLM は一度出した判断を正当化しやすいため、通常のセルフレビューでは効果が薄い。そこで「批判的観点」でのセルフレビューを実施させ、その結果をコメントに併記することで、指摘の妥当性判断が容易になり、確認時間が大幅に削減された。プロジェクト独自の慣習に関する批判的指摘も得られるようになった。

- **ソース**: [Zenn claude](https://zenn.dev/penpeen/articles/844f0773d5e018)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-03-31

### Claude Codeに課金してみたので、無料プランのAIで作った日記アプリのコードを本気レビューしてもらった

初学者がClaude Code（Sonnet 4.6）に課金し、無料AIで作成した日記アプリのコードレビューを依頼した体験記。詳細な解説や改善提案を得られた一方、AIから適切な回答を引き出すには「具体的な指示を出す力」が重要であることを実感。Notion API連携やLintエラー解決なども含め、課金モデルの丁寧さと深さを確認した。

- **ソース**: [Zenn claude](https://zenn.dev/whipea/articles/e63135d29f8e1f)
- **重要度**: 5/10
- **タグ**: claude-code, sonnet, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-31 | 自動生成 |
