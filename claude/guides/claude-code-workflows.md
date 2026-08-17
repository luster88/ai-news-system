---
title: Claude Code Workflows
category: guides
subcategory: claude-code-workflows
tags:
- claude-code
- mcp
- opus
- prompt
- 新機能
date: '2026-07-12'
updated: '2026-08-17'
sources:
- url: https://zenn.dev/bentenweb_fumi/articles/7tntag3v6ern
  title: Fable 5の残り時間を最大限活用する方法：ドキュメント監査で見つけた19の致命的欠陥と点検のススメ
  date: '2026-07-12'
- url: https://qiita.com/miyaguchi_kioku/items/c8a026693719f7d9bdf3
  title: AIエージェント設計完全ガイド④-Claude Codeで実践するDynamic Workflows
  date: '2026-07-23'
- url: https://qiita.com/todiii/items/b18f0df1cd6b8462435b
  title: Claude Code Dynamic Workflows（動的ワークフロー）まとめ
  date: '2026-08-17'
---



# Claude Code Workflows

---

## 2026-08-17

### Claude Code Dynamic Workflows（動的ワークフロー）まとめ

Claude Code の Dynamic Workflows（動的ワークフロー）は、大規模タスクを自動分解し数十〜数百のサブエージェントが並列処理する機能。Bun プロジェクトの75万行 Zig→Rust 移植実績あり。一般的な開発は十分カバーできるが、組織固有ルールや個人の癖が強い場合は Agent Teams と併用が有効。Sonnet では思考の深さに物足りなさがあるため Opus 推奨だが、トークン消費が大きいため大規模・高付加価値プロジェクトに絞るべき。

- **ソース**: [Qiita claude](https://qiita.com/todiii/items/b18f0df1cd6b8462435b)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, opus

---

## 2026-07-23

### AIエージェント設計完全ガイド④-Claude Codeで実践するDynamic Workflows

Claude Codeを用いたAIエージェント設計の実践ガイド。Subagents、Skills、Hooks、MCPなどの機能を組み合わせて、複数のAgentが協働する「Dynamic Workflows」を実現する方法を解説。再利用可能なAIワークフローの構築手法と、OpenAI Agents SDKやLangGraphとの比較を含む連載記事の第4回。

- **ソース**: [Qiita claude](https://qiita.com/miyaguchi_kioku/items/c8a026693719f7d9bdf3)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, prompt

---

## 2026-07-12

### Fable 5の残り時間を最大限活用する方法：ドキュメント監査で見つけた19の致命的欠陥と点検のススメ

Claude Code Fable 5の期限前に、生成作業ではなくドキュメント監査などの「点検系タスク」に時間を使うことを推奨。筆者は62ファイルを監査し、実装と真逆の記述を含む19件の重大な欠陥を発見。Fable 5の長文処理能力を活かし、システム全体の整合性チェックやナレッジベース整備を行うことで、期限後も残る資産を構築できると主張。

- **ソース**: [Zenn claude](https://zenn.dev/bentenweb_fumi/articles/7tntag3v6ern)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-12 | 自動生成 |
