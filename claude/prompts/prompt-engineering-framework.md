---
title: Prompt Engineering Framework
category: prompts
subcategory: prompt-engineering-framework
tags:
- claude-code
- haiku
- opus
- prompt
- 新機能
date: '2026-03-30'
updated: '2026-06-02'
sources:
- url: https://zenn.dev/analysis/articles/prompt-master-thought-analyzer
  title: 「プロンプトを最適化する」とは何か──prompt-masterを3層フレームワークで解剖する
  date: '2026-03-30'
- url: https://zenn.dev/owl7628/articles/3c7fd4da4edcac
  title: Opus 4.6 / 4.8 / GPT 5.5での推奨プロンプトの書き方の違いについて
  date: '2026-06-01'
- url: https://zenn.dev/jun_eng/articles/0ae1fa121377a7
  title: 副業ライターの朝30分を15分に縮める「3段連鎖プロンプト」設計
  date: '2026-06-02'
---



# Prompt Engineering Framework

---

## 2026-06-02

### 副業ライターの朝30分を15分に縮める「3段連鎖プロンプト」設計

副業ライターが記事執筆時間を45分から15分に短縮した3段階プロンプト設計手法。リサーチ→構成→下書きに分解し、各段階で出力品質を制御することでLLMの「抽象化」と「論理飛躍」を防ぐ。シーン指定・数値制約・紋切り型フレーズ禁止などの具体的なプロンプト設計理由と、モデル使い分け（Haiku/Opus）やワークフロー自動化の実践手法を解説。

- **ソース**: [Zenn claude](https://zenn.dev/jun_eng/articles/0ae1fa121377a7)
- **重要度**: 6/10
- **タグ**: prompt, haiku, opus

---

## 2026-06-01

### Opus 4.6 / 4.8 / GPT 5.5での推奨プロンプトの書き方の違いについて

Claude Opus 4.6以前と4.7/4.8、GPT 5.5では推奨プロンプトの書き方が大きく異なる。Opus 4.6は曖昧な指示でも文脈を推論して補完するが、4.7以降は文字通りの解釈を重視し、詳細な指示が必要。4.7では新トークナイザー採用により最大35%トークン消費が増加。GPT 5.5はoutcome-firstのアプローチを推奨している。

- **ソース**: [Zenn claude](https://zenn.dev/owl7628/articles/3c7fd4da4edcac)
- **重要度**: 7/10
- **タグ**: opus, prompt, 新機能

---

## 2026-03-30

### 「プロンプトを最適化する」とは何か──prompt-masterを3層フレームワークで解剖する

prompt-masterというClaudeスキルを「発想力・構想力・指示力」の3層フレームワークで分析した記事。CO-STARやRISENなど12のテンプレートを備えるが、これは構造化であり思考改善ではないと指摘。アンチパターン検出やツール固有知識の管理は有効だが、ユーザーの指示力そのものを向上させるわけではないと結論づける。プロンプト最適化の本質的な問題提起を行う。

- **ソース**: [Zenn claude](https://zenn.dev/analysis/articles/prompt-master-thought-analyzer)
- **重要度**: 6/10
- **タグ**: prompt, claude-code, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-30 | 自動生成 |
