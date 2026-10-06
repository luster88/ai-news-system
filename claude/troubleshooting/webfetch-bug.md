---
title: Webfetch Bug
category: troubleshooting
subcategory: webfetch-bug
tags:
- bugfix
- claude-code
date: '2026-10-06'
updated: '2026-10-06'
sources:
- url: https://qiita.com/suwa_nobu/items/35a1824f5b1d41caa10f
  title: Claude Code の WebFetch は、長いページの10万字より後ろを読まずに「書いていない」と答えていた
  date: '2026-10-06'
---

# Webfetch Bug

---

## 2026-10-06

### Claude Code の WebFetch は、長いページの10万字より後ろを読まずに「書いていない」と答えていた

Claude Code 2.1.290で修正された重大なバグについての詳細な検証記事。WebFetchツールが10万字を超えるページを黙って切り捨て、Claude本体に「見つからない」と誤った回答をさせていた問題を、実際のCHANGELOG.mdファイル（93万字）を使って36回の測定で実証。修正版では切り捨てを通知し続きを読めるようになったが、費用は約6倍、時間は約3.8倍に増加した。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/35a1824f5b1d41caa10f)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-06 | 自動生成 |
