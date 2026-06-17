---
title: Auto Accept Risks
category: troubleshooting
subcategory: auto-accept-risks
tags:
- bugfix
- claude-code
- setup
date: '2026-06-17'
updated: '2026-06-17'
sources:
- url: https://qiita.com/yurukusa/items/a8ba73afd314b7fb822d
  title: '`migrate:fresh`で本番DBが消える——Claude Codeの自動承認とフレームワークの破壊コマンド'
  date: '2026-06-17'
---

# Auto Accept Risks

---

## 2026-06-17

### `migrate:fresh`で本番DBが消える——Claude Codeの自動承認とフレームワークの破壊コマンド

Claude Codeの自動承認モードで`migrate:fresh`等のフレームワーク固有の破壊コマンドが確認なしに実行され、本番DBが削除される事故が多発。`rm -rf`等のシェルコマンド保護では防げないため、PreToolUseフックで破壊動詞を検出するcc-safe-setupの導入が推奨される。事前バックアップがない場合、復旧は困難。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/a8ba73afd314b7fb822d)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-17 | 自動生成 |
