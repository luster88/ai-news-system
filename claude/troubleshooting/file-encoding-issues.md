---
title: File Encoding Issues
category: troubleshooting
subcategory: file-encoding-issues
tags:
- bugfix
- claude-code
- windows
date: '2026-10-13'
updated: '2026-10-13'
sources:
- url: https://qiita.com/suwa_nobu/items/365d2561809fe1da8541
  title: Shift-JIS のファイルを Claude Code で1か所直したら、日本語が全部壊れて戻せなくなった
  date: '2026-10-13'
---

# File Encoding Issues

---

## 2026-10-13

### Shift-JIS のファイルを Claude Code で1か所直したら、日本語が全部壊れて戻せなくなった

Claude Code 2.1.295以前では、Shift-JISファイルをEditツールで編集すると、日本語が全て置換文字（U+FFFD）に変換され、元のバイト列が失われる問題が発生していた。2.1.296でこの問題が修正され、非UTF-8ファイルの編集時にはエラーを返すようになった。シェルツールを使用すれば文字コードを保持した編集が可能。Readツールでは編集前後で同じ文字化け表示となるため、Claudeは破損に気づけない。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/365d2561809fe1da8541)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-13 | 自動生成 |
