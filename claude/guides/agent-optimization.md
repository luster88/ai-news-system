---
title: Agent Optimization
category: guides
subcategory: agent-optimization
tags:
- claude-code
- opus
- prompt
date: '2026-10-15'
updated: '2026-10-15'
sources:
- url: https://zenn.dev/i_ichi/articles/agent-rebuild-hooks-70-to-zero
  title: Claude Codeの常駐エージェントを作り直した。トークン71%減、同じ間違いは残った
  date: '2026-10-15'
---

# Agent Optimization

---

## 2026-10-15

### Claude Codeの常駐エージェントを作り直した。トークン71%減、同じ間違いは残った

Claude Codeエージェントを半年運用後、hookが70本・指示ファイル83KBまで肥大化し判断ミスが頻発。新エージェントを0から構築し、hook6本・指示ファイル6.7KBに削減。トークン使用量は71%減少したが、「確かめずに言い切る」というミスの傾向は変わらず、知識量削減による精度向上は確認できなかった。

- **ソース**: [Zenn claude](https://zenn.dev/i_ichi/articles/agent-rebuild-hooks-70-to-zero)
- **重要度**: 6/10
- **タグ**: claude-code, opus, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-15 | 自動生成 |
