---
title: Claude Code Logging
category: tools
subcategory: claude-code-logging
tags:
- claude-code
- performance
- 新機能
date: '2026-07-08'
updated: '2026-07-08'
sources:
- url: https://qiita.com/Subara3/items/c7b4e38fc4b714b8d876
  title: Claude Codeの全ログをClickHouseで分析したら、6月だけでAPI換算５６万円使っていた
  date: '2026-07-08'
---

# Claude Code Logging

---

## 2026-07-08

### Claude Codeの全ログをClickHouseで分析したら、6月だけでAPI換算５６万円使っていた

Claude Codeの全セッションログ（~/.claude/projects/）をClickHouseで分析するCLI「ccsql」の開発事例。約2ヶ月で289MB・112ファイルのJSONLログを列指向DBに取り込み、コスト・ツール利用・キャッシュ効率をSQLで自由に深堀可能に。埋め込み版chdbを使いサーバーレスで動作し、筆者の実ログでは6月だけでAPI換算56万円の利用実態が判明。

- **ソース**: [Qiita claudecode](https://qiita.com/Subara3/items/c7b4e38fc4b714b8d876)
- **重要度**: 6/10
- **タグ**: claude-code, performance, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-08 | 自動生成 |
