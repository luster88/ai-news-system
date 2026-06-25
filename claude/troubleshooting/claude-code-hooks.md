---
title: Claude Code Hooks
category: troubleshooting
subcategory: claude-code-hooks
tags:
- bugfix
- claude-code
- cowork
- setup
date: '2026-06-03'
updated: '2026-06-25'
sources:
- url: https://zenn.dev/gudezou/articles/7e8235a27f0909
  title: Claude Code の終了フックから claude を呼び出すとなぜ暴走するのか
  date: '2026-06-03'
- url: https://qiita.com/yurukusa/items/5a4f67b7e0f732a3f7c4
  title: SubagentStop の hook が、サブエージェントを使っていないメインセッションでも発火する——マルチエージェントを hook で組む人の盲点
  date: '2026-06-25'
---


# Claude Code Hooks

---

## 2026-06-25

### SubagentStop の hook が、サブエージェントを使っていないメインセッションでも発火する——マルチエージェントを hook で組む人の盲点

Claude Code 2.1.186でSubagentStopフックがサブエージェント未使用のメインセッション終了時にも誤発火する回帰バグが報告された。これはマルチエージェント制御でフックを使う開発者にとって、削除・通知などの取り返しのつかない処理が意図せず実行されるリスクがある。対策として、stdinの内容を記録して実際の発火状況を観察し、SubagentStopフック内で文脈確認を行うことが推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/5a4f67b7e0f732a3f7c4)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, cowork

---

## 2026-06-03

### Claude Code の終了フックから claude を呼び出すとなぜ暴走するのか

Claude Code の SessionEnd フックから claude を起動すると無限ループが発生する問題を解説。終了フックは同期実行されるため重い処理で固まる危険性があり、再帰防止には環境変数による入口ガードが有効。実際の事故事例では数百回発火し利用上限に達した。

- **ソース**: [Zenn claude](https://zenn.dev/gudezou/articles/7e8235a27f0909)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-03 | 自動生成 |
