---
title: Claude In Chrome Automation
category: troubleshooting
subcategory: claude-in-chrome-automation
tags:
- bugfix
- claude-code
- cowork
date: '2026-11-01'
updated: '2026-11-01'
sources:
- url: https://qiita.com/kaiyaku_iyada/items/3366666a2a706f96fe7d
  title: Claude Code で Qiita に投稿、3日とも1回目は空振り：二重投稿を避けて押し直す手順
  date: '2026-11-01'
---

# Claude In Chrome Automation

---

## 2026-11-01

### Claude Code で Qiita に投稿、3日とも1回目は空振り：二重投稿を避けて押し直す手順

Claude Codeを使ってQiitaに自動投稿する際、3日連続で「記事を投稿する」ボタンの1回目クリックが失敗した事例の詳細な記録。公開設定モーダルのdisplayプロパティがnoneの状態でボタンがクリックされていたことが判明し、祖先要素のdisplayを確認してから押す手順に改善した。Chrome拡張機能（Claude in Chrome）のleft_click、find、javascript_toolを使用した実装と、二重投稿を避けるための確認方法を記録。

- **ソース**: [Qiita claude](https://qiita.com/kaiyaku_iyada/items/3366666a2a706f96fe7d)
- **重要度**: 4/10
- **タグ**: claude-code, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-01 | 自動生成 |
