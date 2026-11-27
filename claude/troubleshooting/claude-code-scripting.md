---
title: Claude Code Scripting
category: troubleshooting
subcategory: claude-code-scripting
tags:
- bugfix
- claude-code
- linux
date: '2026-11-27'
updated: '2026-11-27'
sources:
- url: https://qiita.com/takamatt_ai/items/3e3f0f0d305c56970ff1
  title: 「前の処理が終わるまで待つ」を pgrep -f で書くと、待つ側が自分に引っかかって終わらない。確かめ方と直し方
  date: '2026-11-27'
---

# Claude Code Scripting

---

## 2026-11-27

### 「前の処理が終わるまで待つ」を pgrep -f で書くと、待つ側が自分に引っかかって終わらない。確かめ方と直し方

Claude Codeが生成する「プロセスが終わるまで待つ」スクリプトで、pgrep -fを使うと待機ループが自分自身を検出して永遠に終わらない問題を解説。正規表現の先頭固定（^）やPIDベースの待機（kill -0や$!）による2つの解決策を、実際のLinux環境での検証結果とともに提示している。

- **ソース**: [Qiita claudecode](https://qiita.com/takamatt_ai/items/3e3f0f0d305c56970ff1)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, linux

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-27 | 自動生成 |
