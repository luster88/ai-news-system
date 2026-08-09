---
title: Claude Code Rules
category: guides
subcategory: claude-code-rules
tags:
- claude-code
- cowork
- prompt
date: '2026-07-27'
updated: '2026-08-09'
sources:
- url: https://qiita.com/Rapls/items/87b74814e41f4e7bd852
  title: CLAUDE.mdを二層に分ける。「毎回復唱させるルール」と「廃止した方針」を別々に持つ型
  date: '2026-07-27'
- url: https://qiita.com/kkaattoo/items/4a1e1c60a4c50dda6370
  title: 実際のレビュー指摘から Claude Code のルールを改善する
  date: '2026-08-09'
---


# Claude Code Rules

---

## 2026-08-09

### 実際のレビュー指摘から Claude Code のルールを改善する

チームの実際のレビュー指摘約400件を分析し、Claude Code のルール（.claude/rules/）を改善した事例。頻出バグパターンを抽出して新ルールファイルを作成し、標準知識や重複記載を削除。過去のPRで新旧規約を比較検証した結果、新規約では検出漏れが減り、レビュー結果が安定した。ルールに載せるのは「実際に繰り返し起きていること」と「AIが推測できない情報」のみとする基準を確立。

- **ソース**: [Qiita claude](https://qiita.com/kkaattoo/items/4a1e1c60a4c50dda6370)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-07-27

### CLAUDE.mdを二層に分ける。「毎回復唱させるルール」と「廃止した方針」を別々に持つ型

Claude Code で CLAUDE.md を「毎回復唱させる振る舞いルール（現在形）」と「廃止した方針の履歴（過去形）」の二層構造で運用する手法を紹介。原則の中に「毎回出力せよ」を含めることで自己維持させ、廃止リストを原則から参照させることで過去の決定が戻ってくるのを防ぐ。1年の運用で、復唱のコンテキスト消費は誤差レベルで、むしろファイル読み込みとツール実行が主な消費源だと判明。

- **ソース**: [Qiita claudecode](https://qiita.com/Rapls/items/87b74814e41f4e7bd852)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-27 | 自動生成 |
