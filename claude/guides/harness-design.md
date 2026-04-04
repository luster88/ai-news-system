---
title: Harness Design
category: guides
subcategory: harness-design
tags:
- claude-code
- cowork
- prompt
date: '2026-04-04'
updated: '2026-04-04'
sources:
- url: https://qiita.com/naokami/items/b2cd50956ebfe4a05f4a
  title: ハーネス設計のブログを見てコードレビューを工夫したら、単独エージェントが見逃したバグを拾えた話
  date: '2026-04-04'
---

# Harness Design

---

## 2026-04-04

### ハーネス設計のブログを見てコードレビューを工夫したら、単独エージェントが見逃したバグを拾えた話

Claude Code を使ったコードレビューにおいて、単独エージェントによるレビューと、Generator（実装）と Evaluator（レビュー）を分離したハーネス設計によるレビューを比較。単独エージェントはコードを読んで推測ベースの指摘に留まったが、別セッションで起動した Evaluator エージェントは実際に Docker を起動して API を叩きながら検証し、JWT 検証スキップや IDOR 脆弱性などのバグを実動作ベースで検出できた。

- **ソース**: [Qiita claudecode](https://qiita.com/naokami/items/b2cd50956ebfe4a05f4a)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-04 | 自動生成 |
