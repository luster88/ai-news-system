---
title: Claude Cowork Sandbox
category: troubleshooting
subcategory: claude-cowork-sandbox
tags:
- bugfix
- claude-code
- cowork
date: '2026-08-01'
updated: '2026-08-01'
sources:
- url: https://qiita.com/ryoji9702/items/331efcef91889c593100
  title: Claude coworkが削除できない環境で git を自動化したら .git にゴミが98個溜まった話
  date: '2026-08-01'
---

# Claude Cowork Sandbox

---

## 2026-08-01

### Claude coworkが削除できない環境で git を自動化したら .git にゴミが98個溜まった話

Claude coworkなど削除保護があるサンドボックス環境でgitを自動実行すると、.git/index.lockなどのロックファイルがunlinkできず蓄積する問題の調査報告。gitはunlink成功を前提に設計されているため、削除保護環境では3か月で98個のゴミファイルが溜まり、対症療法のリネーム退避が原因を再生産するループを生んでいた。

- **ソース**: [Qiita claude](https://qiita.com/ryoji9702/items/331efcef91889c593100)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-01 | 自動生成 |
