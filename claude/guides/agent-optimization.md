---
title: Agent Optimization
category: guides
subcategory: agent-optimization
tags:
- claude-code
- opus
- performance
- prompt
date: '2026-10-15'
updated: '2026-10-29'
sources:
- url: https://zenn.dev/i_ichi/articles/agent-rebuild-hooks-70-to-zero
  title: Claude Codeの常駐エージェントを作り直した。トークン71%減、同じ間違いは残った
  date: '2026-10-15'
- url: https://zenn.dev/tappers/articles/ai-labo-agent-harness-patterns-omnibus
  title: SNSで話題のAIエージェント設計論を片っ端から実機A/B検証してわかった「トークン90%削減・品質100%」の黄金パターン総集編
  date: '2026-10-29'
---


# Agent Optimization

---

## 2026-10-29

### SNSで話題のAIエージェント設計論を片っ端から実機A/B検証してわかった「トークン90%削減・品質100%」の黄金パターン総集編

AIエージェント設計における21パターンの実機検証結果をまとめた総集編。モジュール分割による74.4%のトークン削減、Blind TDDによるミュータント撃破率100%達成、コンテキスト浪費の原因特定など、実測データに基づく「ハーネス（制御構造）」の最適化手法を解説。役割分割の逆効果やセルフレビューの問題点など、5つの構造的アンチパターンと解決策を提示。

- **ソース**: [Zenn claude](https://zenn.dev/tappers/articles/ai-labo-agent-harness-patterns-omnibus)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

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
