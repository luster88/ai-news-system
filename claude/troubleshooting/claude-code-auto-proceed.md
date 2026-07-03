---
title: Claude Code Auto Proceed
category: troubleshooting
subcategory: claude-code-auto-proceed
tags:
- bugfix
- claude-code
- setup
date: '2026-07-03'
updated: '2026-07-03'
sources:
- url: https://qiita.com/yurukusa/items/d65309a0f4ad4cb46478
  title: Claude Codeが確認の返事を60秒待って勝手に進む——消したファイルが復元されコードが書き換わる事故と、その防ぎ方
  date: '2026-07-03'
---

# Claude Code Auto Proceed

---

## 2026-07-03

### Claude Codeが確認の返事を60秒待って勝手に進む——消したファイルが復元されコードが書き換わる事故と、その防ぎ方

Claude Codeが確認待ち60秒後に自動進行し、削除ファイルの復元やコード書き換えが発生する問題が報告された。AskUserQuestionツールに組み込まれたタイムアウト機能が原因で、利用者の意図しない操作が実行される。防止策として、確認後すぐ返答する、CLAUDE.mdに明示的な指示を書く、hookで自動進行を阻止するスクリプトを設定する3つの方法が紹介されている。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/d65309a0f4ad4cb46478)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-03 | 自動生成 |
