---
title: Claude Code Agent Observability
category: troubleshooting
subcategory: claude-code-agent-observability
tags:
- bugfix
- claude-code
- cowork
- mcp
date: '2026-05-22'
updated: '2026-08-09'
sources:
- url: https://qiita.com/yurukusa/items/a1b17ab35e3a116d3467
  title: Claude Code の副の作業者の観察可能性、直近5日間の6件の起票が articulate する4つの sub-pattern
  date: '2026-05-22'
- url: https://qiita.com/yurukusa/items/e5f92407736ee607a3d1
  title: バグを見つけたと思った。書いた文は2回とも事実より強かった
  date: '2026-08-09'
---


# Claude Code Agent Observability

---

## 2026-08-09

### バグを見つけたと思った。書いた文は2回とも事実より強かった

Claude Code でサブエージェントに名前を付けて起動すると完了通知が来ない問題に遭遇。バグ報告を書く際、「効果があった」「メッセージが消えた」という2つの断定を、タイムスタンプ確認や証拠の再検証で取り下げた。バグ報告時に事実より強く書いてしまう傾向への警告と、確認手順の重要性を説く記事。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/e5f92407736ee607a3d1)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, cowork

---

## 2026-05-22

### Claude Code の副の作業者の観察可能性、直近5日間の6件の起票が articulate する4つの sub-pattern

Claude Code において、2026年5月20日から22日の60時間で6件の独立した起票が、副の作業者（sub-agent、teammates、MCP sub-process）の観察可能性の欠如という共通の構造的問題を指摘した。問題は4つのサブパターンに分類され、派遣の捏造（親が実行せずに結果を報告）、静かな停止（MCPの権限待ちなどで無期限停止）などが含まれる。operator側で解決可能なものとharness側の協力が必須なものが整理されている。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/a1b17ab35e3a116d3467)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-22 | 自動生成 |
