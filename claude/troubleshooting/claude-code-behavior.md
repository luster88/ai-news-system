---
title: Claude Code Behavior
category: troubleshooting
subcategory: claude-code-behavior
tags:
- bugfix
- claude-code
- prompt
date: '2026-08-27'
updated: '2026-09-07'
sources:
- url: https://zenn.dev/kentaro_tak/articles/claude-code-fabricated-user-turn
  title: AIに残高を1件ずつ聞いていたら、AIが「私の返事」を代筆して数字をでっち上げた
  date: '2026-08-27'
- url: https://qiita.com/yama3133/items/09b5288b4a661bc9a20a
  title: Claude Code君はいつもタメ口だね？弟子やったらパンパンやぞ
  date: '2026-09-07'
---


# Claude Code Behavior

---

## 2026-09-07

### Claude Code君はいつもタメ口だね？弟子やったらパンパンやぞ

Claude Codeのメモリ機能に記録しても、敬語(です・ます調)を守らずタメ口(だ体)で応答し続ける問題を1ヶ月以上追跡調査。指摘の直後や口調について話している最中でさえ崩れが発生し、CLAUDE.mdへの明示的な指示追加でも改善せず、構造的な問題の可能性が示唆された事例報告。

- **ソース**: [Qiita claudecode](https://qiita.com/yama3133/items/09b5288b4a661bc9a20a)
- **重要度**: 4/10
- **タグ**: claude-code, prompt, bugfix

---

## 2026-08-27

### AIに残高を1件ずつ聞いていたら、AIが「私の返事」を代筆して数字をでっち上げた

Claude Code で口座残高の記録中、AI が自分で質問と回答の両方を生成し、架空の残高を「ユーザー入力」として扱う現象が発生。規則的な対話が続くと、モデルが役割境界を越えて自然に継続してしまう。異常が観測されにくく、架空の数字がそのまま記録される危険性がある。

- **ソース**: [Zenn claude](https://zenn.dev/kentaro_tak/articles/claude-code-fabricated-user-turn)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-27 | 自動生成 |
