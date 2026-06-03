---
title: Cost Optimization
category: troubleshooting
subcategory: cost-optimization
tags:
- claude-code
- performance
- pricing
date: '2026-06-03'
updated: '2026-06-03'
sources:
- url: https://qiita.com/yurukusa/items/fb434ab7d0cb72bc3af2
  title: Claude Codeのスキルを95個入れていたのに、実際に動いていたのは数個だった——使われないスキルの見つけ方
  date: '2026-06-03'
---

# Cost Optimization

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
