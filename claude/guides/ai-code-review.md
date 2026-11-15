---
title: Ai Code Review
category: guides
subcategory: ai-code-review
tags:
- claude-code
- cowork
- prompt
date: '2026-11-11'
updated: '2026-11-15'
sources:
- url: https://qiita.com/nagilabo/items/e2404f3dc1fc6c9814a1
  title: テストは全部緑だった ― AIが書いたコードのレビューで、実際に効いたこと
  date: '2026-11-11'
- url: https://qiita.com/oosawak@github/items/a93703112834983bc1f1
  title: AIが書いたコードは使って確かめる ― 舞台アプリ開発のレビュー記録
  date: '2026-11-15'
---


# Ai Code Review

---

## 2026-11-15

### AIが書いたコードは使って確かめる ― 舞台アプリ開発のレビュー記録

AI生成コードのレビュー手法として、コードの静的検査ではなく実際の動作確認を重視する開発プロセスを紹介。舞台アプリ開発において、画面からの情報取得（十数秒）からファイル直接書き込み（0.7秒間隔）への方針転換など、実用性を軸にした判断の重要性を説く。Claude、Codex、Copilotを使い分けながら、動作確認と記録を徹底することで、AIとの協働開発を効率化。

- **ソース**: [Qiita claudecode](https://qiita.com/oosawak@github/items/a93703112834983bc1f1)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-11-11

### テストは全部緑だった ― AIが書いたコードのレビューで、実際に効いたこと

個人開発でClaude CodeやCodexを活用する際、テストが全て通過しても実際には壊れているケースがある。pepper値の設定ミス、データ同期の和集合問題など2つの実例を紹介し、敵対的レビュー、別AIによる差分レビュー、事前の脅威モデリングなど効果的なレビュー手法を解説。テストの緑は正しさの証拠ではなく、想定外を見つけるために複数の視点が必要と強調。

- **ソース**: [Qiita claudecode](https://qiita.com/nagilabo/items/e2404f3dc1fc6c9814a1)
- **重要度**: 7/10
- **タグ**: claude-code, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-11 | 自動生成 |
