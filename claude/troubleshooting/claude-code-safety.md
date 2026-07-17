---
title: Claude Code Safety
category: troubleshooting
subcategory: claude-code-safety
tags:
- bugfix
- claude-code
- setup
date: '2026-07-17'
updated: '2026-07-17'
sources:
- url: https://qiita.com/yurukusa/items/b9b1360e3698be50bd9f
  title: 「安全フックを入れたから rm 事故は防げる」と思っていたら、ホームディレクトリへの削除が素通りした——実際の事故で自分の無料フックを手元で試し、穴を見つけて直した話
  date: '2026-07-17'
---

# Claude Code Safety

---

## 2026-07-17

### 「安全フックを入れたから rm 事故は防げる」と思っていたら、ホームディレクトリへの削除が素通りした——実際の事故で自分の無料フックを手元で試し、穴を見つけて直した話

Claude Code の rm コマンド事故報告を受け、著者が配布する無料安全フック cc-safe-setup に重大な穴を発見。ホームディレクトリの環境変数（$HOME）への削除が素通りしていた問題を、手元の実測で確認し修正。チルダ（~）は止まるのに $HOME は止まらないという一貫性の欠けが原因で、正規表現を改修して v30.0.2 で対応済み。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/b9b1360e3698be50bd9f)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-17 | 自動生成 |
