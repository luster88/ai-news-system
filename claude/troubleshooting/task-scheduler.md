---
title: Task Scheduler
category: troubleshooting
subcategory: task-scheduler
tags:
- bugfix
- claude-code
- setup
date: '2026-10-06'
updated: '2026-10-06'
sources:
- url: https://qiita.com/Kujira_AI/items/9fba279a3d3e6a6016ad
  title: claude -p の定期実行が失敗しても終了コードは0。報告末尾の状態行で異常を拾う
  date: '2026-10-06'
---

# Task Scheduler

---

## 2026-10-06

### claude -p の定期実行が失敗しても終了コードは0。報告末尾の状態行で異常を拾う

Claude Code を定期実行する際、処理が失敗しても終了コード0で返るため、タスクの成否を終了コードで判定できない問題への対策記事。報告の最終行に「ROUTINE-STATUS: OK/ALERT」という状態行を書かせ、ランチャー側で正規表現で抽出して判定する方法を解説。エージェントは状態を書くだけ、通知はランチャーが行うという役割分担を推奨。

- **ソース**: [Qiita claudecode](https://qiita.com/Kujira_AI/items/9fba279a3d3e6a6016ad)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-06 | 自動生成 |
