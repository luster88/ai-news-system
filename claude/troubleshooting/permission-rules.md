---
title: Permission Rules
category: troubleshooting
subcategory: permission-rules
tags:
- bugfix
- claude-code
- setup
date: '2026-09-17'
updated: '2026-09-17'
sources:
- url: https://qiita.com/suwa_nobu/items/e867493a5cbcdfaa40c9
  title: Write() で拒否しても、Claude Code は12回とも書き込んだ。効いていたのは Edit() だけだった
  date: '2026-09-17'
---

# Permission Rules

---

## 2026-09-17

### Write() で拒否しても、Claude Code は12回とも書き込んだ。効いていたのは Edit() だけだった

Claude Code 2.1.273および2.1.275において、deny ルールの Write(path) が全く機能せず、12回のテストすべてで書き込みが実行された。一方 Edit(path) は3つの経路（Editツール、Writeツールの新規作成、Bashリダイレクト）すべてで正常に機能した。2.1.275では /update-config が生成する形式が Write() から Edit() に修正されたが、既存の Write() ルール自体は依然として無効のまま。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/e867493a5cbcdfaa40c9)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-17 | 自動生成 |
