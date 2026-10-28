---
title: Cli Structured Output
category: troubleshooting
subcategory: cli-structured-output
tags:
- bugfix
- claude-api
- claude-code
date: '2026-10-28'
updated: '2026-10-28'
sources:
- url: https://zenn.dev/masaki_mori72/articles/7682a6c0f13528
  title: claude -p --json-schema の成否は、終了コードではなく structured_output で判定する
  date: '2026-10-28'
---

# Cli Structured Output

---

## 2026-10-28

### claude -p --json-schema の成否は、終了コードではなく structured_output で判定する

Claude Code CLI の `--json-schema` オプション使用時、終了コード 0 でも構造化出力が取得できない場合がある問題について解説。スクリプトから呼び出す際は `structured_output` キーの有無で成否を判定すべきで、プロンプトに「弾かれたら直してよい」と明記することで AI が諦めるケースを減らせる。Windows では npm 版より公式インストーラー版が安全。

- **ソース**: [Zenn claude](https://zenn.dev/masaki_mori72/articles/7682a6c0f13528)
- **重要度**: 6/10
- **タグ**: claude-code, claude-api, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-28 | 自動生成 |
