---
title: Claude Code Review
category: guides
subcategory: claude-code-review
tags:
- bugfix
- claude-code
- cowork
- 新機能
date: '2026-07-14'
updated: '2026-08-04'
sources:
- url: https://qiita.com/sorabcjanne1/items/8f3a354ff073ed69aac2
  title: Claude Codeにプロダクションコードを全チェックさせたら、金銭バグ4件を含む15件の不具合を自動修正してくれた話
  date: '2026-07-14'
- url: https://zenn.dev/tmasuyama1114/articles/claude_code_code_review_guide
  title: 自前のレビュースキルをやめて、Claude Code の /code-review に乗り換えた
  date: '2026-08-04'
---


# Claude Code Review

---

## 2026-08-04

### 自前のレビュースキルをやめて、Claude Code の /code-review に乗り換えた

Claude Codeの公式/code-reviewコマンドを実測検証した記事。effortパラメータ(low/high)で指摘件数が1件と10件に分かれ、highでは複数エージェントが並列動作するDynamic Workflowが起動。--commentオプションでGitHub PRへ自動投稿も可能で、実際に新規バグを検出した実例を紹介。自前レビュースキルから公式コマンドへの乗り換え体験談。

- **ソース**: [Zenn claude](https://zenn.dev/tmasuyama1114/articles/claude_code_code_review_guide)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-07-14

### Claude Codeにプロダクションコードを全チェックさせたら、金銭バグ4件を含む15件の不具合を自動修正してくれた話

Claude CodeでプロダクションコードをフルスキャンしたところStripe二重入金など金銭バグ4件を含む15件の不具合が自動検出・修正された実録。iOS(Swift 68ファイル)とNode.js+Hono+Stripeバックエンドを対象に、複数エージェントが並列でレビューし、同期ロスト・XSS・通知漏れなど深刻なバグを人間がコード1行も書かずに修正完了した事例。

- **ソース**: [Qiita claude](https://qiita.com/sorabcjanne1/items/8f3a354ff073ed69aac2)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-14 | 自動生成 |
