---
title: Claude Code Optimization
category: troubleshooting
subcategory: claude-code-optimization
tags:
- claude-code
- performance
- pricing
date: '2026-09-30'
updated: '2026-09-30'
sources:
- url: https://zenn.dev/yuu_inaka/articles/claude-subagent-model-inherit
  title: Claude Codeのサブエージェントはmodelを書かないと親を継ぐ：未指定の3経路と部下1人9万トークンの実測
  date: '2026-09-30'
---

# Claude Code Optimization

---

## 2026-09-30

### Claude Codeのサブエージェントはmodelを書かないと親を継ぐ：未指定の3経路と部下1人9万トークンの実測

Claude Codeのサブエージェント定義でmodelパラメータを省略すると親エージェントのモデル（この場合opus）を継承してしまい、シンプルなタスクでも高コストなモデルが使われる問題が報告されています。実測では単純なechoコマンド実行だけで101,418トークン（うち約9万がCLAUDE.mdの読み込み）を消費し、4時間ごとの改善ループが8回連続でusage_limitに到達して2日間停止していました。解決策として全エージェントとワークフローでモデルを明示的に指定し、選定理由をコメントで記録する運用に変更しています。

- **ソース**: [Zenn claude](https://zenn.dev/yuu_inaka/articles/claude-subagent-model-inherit)
- **重要度**: 7/10
- **タグ**: claude-code, performance, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-30 | 自動生成 |
