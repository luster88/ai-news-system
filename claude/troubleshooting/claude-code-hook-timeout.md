---
title: Claude Code Hook Timeout
category: troubleshooting
subcategory: claude-code-hook-timeout
tags:
- bugfix
- claude-code
- setup
date: '2026-07-15'
updated: '2026-07-15'
sources:
- url: https://qiita.com/yurukusa/items/fa98b2a84314121ccd02
  title: 無人のClaude Codeが、誰も拒否していないのに黙って止まる（2.1.210）——怖くなって、自分のhookを58個ぜんぶ数えた
  date: '2026-07-15'
---

# Claude Code Hook Timeout

---

## 2026-07-15

### 無人のClaude Codeが、誰も拒否していないのに黙って止まる（2.1.210）——怖くなって、自分のhookを58個ぜんぶ数えた

Claude Code 2.1.210より前のバージョンで、hookのタイムアウトが誤って「ユーザーによる却下」と解釈され、無人セッションが静かに停止するバグが報告された。筆者は自環境の58個のhookを点検し、全てが高速なローカル照合であるため影響は低いと判明。対策として、バージョンアップとネットワーク系hookへの明示的なtimeout設定を推奨している。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/fa98b2a84314121ccd02)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
