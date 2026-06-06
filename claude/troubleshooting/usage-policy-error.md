---
title: Usage Policy Error
category: troubleshooting
subcategory: usage-policy-error
tags:
- bugfix
- claude-code
- setup
date: '2026-06-06'
updated: '2026-06-06'
sources:
- url: https://qiita.com/yurukusa/items/ab42f8178efc73db51b6
  title: Claude Codeが突然「Usage Policy違反」で止まったときの原因と回復方法【2026年6月】
  date: '2026-06-06'
---

# Usage Policy Error

---

## 2026-06-06

### Claude Codeが突然「Usage Policy違反」で止まったときの原因と回復方法【2026年6月】

Claude Codeで2026年6月以降、Usage Policy違反の誤検知により正常な開発作業でもセッション全体がブロックされる問題が多発。原因は文脈全体を再判定する分類器の仕様で、セキュリティ関連語彙がなくても発火。回復には設定を退避した「まっさらな状態」での起動テストでローカル/サーバー側を切り分け、無害なターンのrequest_idをGitHub issueに報告することが有効。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/ab42f8178efc73db51b6)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-06 | 自動生成 |
