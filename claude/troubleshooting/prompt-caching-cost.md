---
title: Prompt Caching Cost
category: troubleshooting
subcategory: prompt-caching-cost
tags:
- claude-api
- claude-code
- performance
- pricing
- 新機能
date: '2026-07-15'
updated: '2026-08-07'
sources:
- url: https://zenn.dev/takna/articles/claude-code-model-switch-cache-cost
  title: プロンプトキャッシュは通信ではなく計算を省いている ─ Claude Code のモデル・エフォート切り替えが高くつく
  date: '2026-07-15'
- url: https://qiita.com/okssusucha/items/b461e94f1edb67777b9c
  title: 途中でツールを足すとClaudeのプロンプトキャッシュが全部飛ぶ問題と回避策
  date: '2026-08-07'
---


# Prompt Caching Cost

---

## 2026-08-07

### 途中でツールを足すとClaudeのプロンプトキャッシュが全部飛ぶ問題と回避策

Claude API でツール定義を途中変更するとプロンプトキャッシュが全消失する問題と、2026年7月導入の mid-conversation tool changes / system messages 機能による回避策を解説。tools 配列は固定し、tool_addition / tool_removal ブロックで動的に見せ分けることでキャッシュを維持できる。長時間動作するエージェント開発における重要な設計変更。

- **ソース**: [Qiita claude](https://qiita.com/okssusucha/items/b461e94f1edb67777b9c)
- **重要度**: 7/10
- **タグ**: claude-api, 新機能, performance

---

## 2026-07-15

### プロンプトキャッシュは通信ではなく計算を省いている ─ Claude Code のモデル・エフォート切り替えが高くつく

Claude Codeでモデルやエフォートを切り替えると、プロンプトキャッシュが無効化され、会話履歴の再計算コストが発生する。キャッシュが省いているのは通信ではなく計算（KVテンソルの再計算）であり、頻繁な切り替えは高コストになる。モデル切り替えは全キャッシュを破棄し、エフォート切り替えは会話履歴分を破棄するため、数ターンごとの上下動は避けるべき。

- **ソース**: [Zenn claude](https://zenn.dev/takna/articles/claude-code-model-switch-cache-cost)
- **重要度**: 7/10
- **タグ**: claude-code, pricing, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
