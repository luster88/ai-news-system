---
title: Skill Portability
category: tools
subcategory: skill-portability
tags:
- claude-code
- cowork
- 新機能
date: '2026-07-22'
updated: '2026-07-22'
sources:
- url: https://zenn.dev/maronsan/articles/carrylint-runtime-portability
  title: その神スキル、あなたのマシンでしか動かない。実行時の可搬性をCIで落とすリンタを作った
  date: '2026-07-22'
---

# Skill Portability

---

## 2026-07-22

### その神スキル、あなたのマシンでしか動かない。実行時の可搬性をCIで落とすリンタを作った

Claude Code などで量産したスキルが「作者の環境でしか動かない」問題を解決するため、carrylint という静的解析リンタを開発。絶対パスや未宣言 CLI、環境変数の焼き込みを CI で検出し、PR を落とす仕組み。公開後に 230 件の実在スキルで検証し、85% が誤検知だったため、$HOME やプレースホルダの扱いを修正した。Agent Skills 標準の「形式の可搬性」に対し、「実行時の可搬性」を保証する点が特徴。

- **ソース**: [Zenn claude](https://zenn.dev/maronsan/articles/carrylint-runtime-portability)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-22 | 自動生成 |
