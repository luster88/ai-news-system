---
title: Claude Code Windows Encoding
category: troubleshooting
subcategory: claude-code-windows-encoding
tags:
- bugfix
- claude-code
- windows
date: '2026-10-06'
updated: '2026-10-06'
sources:
- url: https://qiita.com/sumitsuke/items/2ae74cfc390dd56a1db5
  title: Windows で AI にファイルを書き換えさせて踏んだ 4 つと防いだ 1 つ——改行・混在・cp932・バックスラッシュ・アンカー
  date: '2026-10-06'
---

# Claude Code Windows Encoding

---

## 2026-10-06

### Windows で AI にファイルを書き換えさせて踏んだ 4 つと防いだ 1 つ——改行・混在・cp932・バックスラッシュ・アンカー

Windows環境でClaude CodeにファイルのAI編集を依頼する際、改行コード(CRLF/LF)の混在、文字コード(UTF-8/cp932)の切り替え、バックスラッシュのエスケープ処理、アンカー検索の部分一致など、テキストI/O周りで遭遇した4つの事故事例と1つの回避事例を、実際の再現手順付きで報告した記事。Pythonのデフォルト動作(newline=None、パイプ時のcp932)が原因で、「差し替え対象の行だけ見れば安全」という前提が崩れるケースを具体的に示している。

- **ソース**: [Qiita claudecode](https://qiita.com/sumitsuke/items/2ae74cfc390dd56a1db5)
- **重要度**: 6/10
- **タグ**: claude-code, windows, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-06 | 自動生成 |
