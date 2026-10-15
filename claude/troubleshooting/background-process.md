---
title: Background Process
category: troubleshooting
subcategory: background-process
tags:
- bugfix
- claude-code
- windows
date: '2026-10-15'
updated: '2026-10-15'
sources:
- url: https://qiita.com/suwa_nobu/items/3a34591f130da2f570f5
  title: Claude Code を閉じても、裏で起動したサーバーが残ることがある。見分け方は画面下の「1 shell」
  date: '2026-10-15'
---

# Background Process

---

## 2026-10-15

### Claude Code を閉じても、裏で起動したサーバーが残ることがある。見分け方は画面下の「1 shell」

Claude Codeを閉じた後もバックグラウンドサーバーが残る場合がある問題を検証。Windows環境で44回測定し、バックグラウンド実行で起動したサーバーは通常停止するが、&やStart-Processで切り離したプロセスは残ることを確認。画面下の「1 shell」表示でサーバーが残るかどうか判別可能。確認ダイアログで「2. Move to background and exit」を選ぶとスーパーバイザープロセスも常駐する。

- **ソース**: [Qiita claudecode](https://qiita.com/suwa_nobu/items/3a34591f130da2f570f5)
- **重要度**: 6/10
- **タグ**: claude-code, windows, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-15 | 自動生成 |
