---
title: Claude Code Performance
category: guides
subcategory: claude-code-performance
tags:
- claude-code
- performance
- 新機能
date: '2026-09-01'
updated: '2026-09-01'
sources:
- url: https://qiita.com/jqit_suwa/items/5fe930eb46d064b3da06
  title: Claude Code でモデルを切り替えると、そのターンだけ書き直しが287倍
  date: '2026-09-01'
---

# Claude Code Performance

---

## 2026-09-01

### Claude Code でモデルを切り替えると、そのターンだけ書き直しが287倍

Claude Code 2.1.251で追加されたプロンプトキャッシュの可視化機能を使い、モデル切り替え時のキャッシュ動作を詳細に検証。モデル切り替え時は書き直しが287倍に増加するが、戻す際は67トークンと少ない。TTL変更でキャッシュが分離し、-pの繰り返しはヒット率32.5%だがセッション継続で99.8%に改善することを実証。

- **ソース**: [Qiita claudecode](https://qiita.com/jqit_suwa/items/5fe930eb46d064b3da06)
- **重要度**: 7/10
- **タグ**: claude-code, performance, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-01 | 自動生成 |
