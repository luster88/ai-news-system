---
title: Cost Optimization
category: troubleshooting
subcategory: cost-optimization
tags:
- claude-code
- performance
- pricing
date: '2026-06-03'
updated: '2026-09-22'
sources:
- url: https://qiita.com/yurukusa/items/fb434ab7d0cb72bc3af2
  title: Claude Codeのスキルを95個入れていたのに、実際に動いていたのは数個だった——使われないスキルの見つけ方
  date: '2026-06-03'
- url: https://www.reddit.com/r/ClaudeAI/comments/1wm8adm/psa_claude_code_turn_off_prompt_suggestions_save
  title: 'PSA - Claude Code: Turn off Prompt Suggestions, save ~10% of your limits/spend'
  date: '2026-09-22'
---


# Cost Optimization

---

## 2026-09-22

### PSA - Claude Code: Turn off Prompt Suggestions, save ~10% of your limits/spend

Claude Code のプロンプト提案機能（Prompt Suggestions）は、コンテキスト全体のキャッシュ読み取りを行うため、週間使用制限の最大10%を消費する可能性がある。ユーザーの実測では、提案機能のコストが通常のプロンプトコストの91%に達するケースも確認された。この機能をオフにすることで、大幅なコスト削減が可能。高コンテキスト長の状況では特に影響が大きく、実際のプロンプトと同等のコストがかかることもある。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wm8adm/psa_claude_code_turn_off_prompt_suggestions_save)
- **重要度**: 7/10
- **タグ**: claude-code, performance, pricing

---

## 2026-06-03

### Claude Codeのスキルを95個入れていたのに、実際に動いていたのは数個だった——使われないスキルの見つけ方

Claude Codeで95個のスキルを登録していたが、実際に使われていたのは数個だけだった事例。スキルは呼ばれなくても説明文が毎セッションのコンテキストに読み込まれるため、未使用スキルが固定費として蓄積する。セッションログ（JSONL）をjqで解析することで実際の起動回数を調査でき、使われないスキルを「中核/退避/削除」に分類して整理することで、コンテキストと費用を削減できる。6月15日の課金分離前の棚卸しを推奨。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/fb434ab7d0cb72bc3af2)
- **重要度**: 7/10
- **タグ**: claude-code, performance, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-03 | 自動生成 |
