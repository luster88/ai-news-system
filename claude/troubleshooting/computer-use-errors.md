---
title: Computer Use Errors
category: troubleshooting
subcategory: computer-use-errors
tags:
- bugfix
- opus
date: '2026-07-30'
updated: '2026-07-30'
sources:
- url: https://qiita.com/AlohaYos/items/fa3de0f7e6b1711207ec
  title: Claude の Computer use が Opus 5 で「tool call could not be parsed」になった話
  date: '2026-07-30'
---

# Computer Use Errors

---

## 2026-07-30

### Claude の Computer use が Opus 5 で「tool call could not be parsed」になった話

Claude デスクトップアプリの Cowork モードで Computer use を Opus 5 で実行したところ、「tool call could not be parsed」エラーが繰り返し発生し処理が停止した。Opus 4.8 に切り替えると同じ処理が正常に完走。原因は権限設定ではなく、Opus 5 のツール呼び出し出力フォーマットの不具合と判明。Computer use の一部ツールは成功していたため、モデル出力側の問題と特定できた。

- **ソース**: [Qiita claude](https://qiita.com/AlohaYos/items/fa3de0f7e6b1711207ec)
- **重要度**: 7/10
- **タグ**: opus, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-30 | 自動生成 |
