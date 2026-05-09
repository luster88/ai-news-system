---
title: Claude Code Safety
category: guides
subcategory: claude-code-safety
tags:
- claude-code
- setup
date: '2026-05-09'
updated: '2026-05-09'
sources:
- url: https://qiita.com/Ngen/items/dd5090c6d05ec9c7994c
  title: Claude Codeのフック5個で「うっかり事故」を本気で潰した話
  date: '2026-05-09'
---

# Claude Code Safety

---

## 2026-05-09

### Claude Codeのフック5個で「うっかり事故」を本気で潰した話

Claude Codeが危険なコマンド（rm -rf /等）を実行しかける事故を防ぐため、5種類のフック（PreToolUse/PostToolUse/PreEdit/PostEdit/Stop）を実装した実践ログ。プロンプトでの「お願い」は5回に1回突破されるため、物理的なガードとしてフックで危険コマンド検知・秘密ファイル保護・通知を行う。stdin からのJSON読み取り、exit 0 でのblock返却、reasonの明示が重要なポイント。

- **ソース**: [Qiita claude](https://qiita.com/Ngen/items/dd5090c6d05ec9c7994c)
- **重要度**: 7/10
- **タグ**: claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-09 | 自動生成 |
