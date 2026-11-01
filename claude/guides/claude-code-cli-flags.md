---
title: Claude Code Cli Flags
category: guides
subcategory: claude-code-cli-flags
tags:
- claude-code
- setup
- 新機能
date: '2026-11-01'
updated: '2026-11-01'
sources:
- url: https://qiita.com/joinclass/items/85b615b453fe5af911b4
  title: Claude Code の --safe-mode と --restricted は別物：「設定を切る」か「手足を縛る」かの使い分け
  date: '2026-11-01'
---

# Claude Code Cli Flags

---

## 2026-11-01

### Claude Code の --safe-mode と --restricted は別物：「設定を切る」か「手足を縛る」かの使い分け

Claude Code の --safe-mode と --restricted の違いを解説。safe-mode は CLAUDE.md や MCP などカスタム設定を無効化して設定起因の問題を切り分けるデバッグ用フラグ。restricted は Bash 等の実行ツールを制限し、設定ファイルへの書き込みを厳格化する本番運用向けセキュリティフラグ。無人実行で git push --force 事故を経験した筆者が、AI に何をさせないかを CLI レベルで制御する重要性を実例とともに説明。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/85b615b453fe5af911b4)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-01 | 自動生成 |
