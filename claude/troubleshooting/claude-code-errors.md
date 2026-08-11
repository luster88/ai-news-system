---
title: Claude Code Errors
category: troubleshooting
subcategory: claude-code-errors
tags:
- bugfix
- claude-code
- opus
- setup
date: '2026-06-05'
updated: '2026-08-11'
sources:
- url: https://qiita.com/natume_nat/items/76fe608d570caebb4f4c
  title: Claude Codeで「The model's tool call could not be parsed」エラーを回避する方法
  date: '2026-06-05'
- url: https://qiita.com/homhom44/items/abfa28096475adba1def
  title: Claude Code でつまずいたときの切り分けメモ（2026-08-12）
  date: '2026-08-11'
---


# Claude Code Errors

---

## 2026-08-11

### Claude Code でつまずいたときの切り分けメモ（2026-08-12）

Claude Code利用時のトラブルシューティング集。GitHub Issuesで複数報告がある問題を実際に検証し、OAuth認証エラー、ネットワーク接続障害、起動時の異常終了の3つの主要な問題について、切り分け手順と確認ポイントを整理。設定・権限・環境依存の問題を中心に、実践的な対処方法を提供している。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/abfa28096475adba1def)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-06-05

### Claude Codeで「The model's tool call could not be parsed」エラーを回避する方法

Claude Code（特にOpus 4.8）で日本語環境使用時に発生する「tool call could not be parsed」エラーの回避方法を解説。CLAUDE.mdに「Think in English, interact with the user in Japanese」を追加することで、内部思考を英語化してマルチバイト文字密度を下げ、XMLタグ構造の崩壊を防ぐ。エラー発生時は「Restore conversation」で即座にロールバック可能。

- **ソース**: [Qiita claudecode](https://qiita.com/natume_nat/items/76fe608d570caebb4f4c)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-05 | 自動生成 |
