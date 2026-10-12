---
title: Claude Code Agents
category: guides
subcategory: claude-code-agents
tags:
- claude-code
- cowork
- mcp
date: '2026-10-12'
updated: '2026-10-12'
sources:
- url: https://qiita.com/joinclass/items/78fb590dcbaca1ebf767
  title: Claude Codeのサブエージェントを設計する — 責務分割とツール権限の絞り方
  date: '2026-10-12'
---

# Claude Code Agents

---

## 2026-10-12

### Claude Codeのサブエージェントを設計する — 責務分割とツール権限の絞り方

合同会社ジョインクラスがClaude Codeで17個のサブエージェントを運用する実践例。責務を分割し、`.claude/agents/*.md`でツール権限を絞る設計を紹介。1,000行超のCLAUDE.mdが矛盾した失敗から、書き込み先ファイルで分割する方法へ移行。無人実行では`--allowedTools`で二重制限し、コスト管理には`--max-budget-usd`と`--output-format json`を活用。呼び出し回数削減が最も効果的なコスト削減策と結論。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/78fb590dcbaca1ebf767)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-12 | 自動生成 |
