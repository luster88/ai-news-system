---
title: Claude Code Logs
category: troubleshooting
subcategory: claude-code-logs
tags:
- bugfix
- claude-code
- performance
- setup
date: '2026-08-24'
updated: '2026-10-24'
sources:
- url: https://qiita.com/chiisanasoft/items/de047ac451a8b49c740c
  title: Claude Code のログでブランチ運用を数えたら、git_branch の "HEAD" が2つの意味を持っていた
  date: '2026-08-24'
- url: https://qiita.com/kaiyaku_iyada/items/cbadd82923bd7fcee3b3
  title: AIの報告「約5時間止まっていた」は約2分だった：Claude Code の JSONL で照合
  date: '2026-10-24'
---


# Claude Code Logs

---

## 2026-10-24

### AIの報告「約5時間止まっていた」は約2分だった：Claude Code の JSONL で照合

Claude Code デスクトップアプリのセッション記録（JSONL形式）の詳細な読み方と分析手法を解説。AI自身が「約5時間停止」と報告した障害が、実際にはレート制限による約2分の停止だったことを、uuid・timestamp・parentUuidなどの記録から検証。user/assistant/attachment/systemの各行タイプの意味や、エラー検出方法を具体例とともに説明。

- **ソース**: [Qiita claude](https://qiita.com/kaiyaku_iyada/items/cbadd82923bd7fcee3b3)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, performance

---

### AIの報告「約5時間止まっていた」は約2分だった：Claude Code の JSONL で照合

Claude Codeのセッション記録（JSONL）を解析し、AIが「約5時間停止」と報告した障害が実際には約2分間のrate_limit errorだったことを検証。user/assistant/attachment/systemの各typeの構造や、parentUuidによる会話の連鎖、stop_hook_summaryの有無による停止判定方法を詳説。JSONLファイルには同じ行が複数回重複記録される特性があり、時系列順とは限らない点も指摘。

- **ソース**: [Qiita claudecode](https://qiita.com/kaiyaku_iyada/items/cbadd82923bd7fcee3b3)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-08-24

### Claude Code のログでブランチ運用を数えたら、git_branch の "HEAD" が2つの意味を持っていた

Claude Code のログ分析で、436セッション中12件のみが名前付きブランチで作業していたことが判明。git_branch の "HEAD" は detached HEAD とリポジトリ外の2つの意味を持ち、198件の HEAD のうち66件が detached HEAD、132件はリポジトリ外だった。セッション単位のブランチ記録の制約や、集計時点での状態判定など、ログ分析における3つの注意点を解説。

- **ソース**: [Qiita claudecode](https://qiita.com/chiisanasoft/items/de047ac451a8b49c740c)
- **重要度**: 4/10
- **タグ**: claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-24 | 自動生成 |
