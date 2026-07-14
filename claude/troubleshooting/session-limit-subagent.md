---
title: Session Limit Subagent
category: troubleshooting
subcategory: session-limit-subagent
tags:
- bugfix
- claude-code
- pricing
date: '2026-07-14'
updated: '2026-07-14'
sources:
- url: https://qiita.com/yurukusa/items/b1add0cb7bd1cf35d096
  title: 「セッション上限です」と言われて追加クレジットを買ったのに、また同じところで止まる——その上限、あなたが当たっている枠とは別かもしれない
  date: '2026-07-14'
---

# Session Limit Subagent

---

## 2026-07-14

### 「セッション上限です」と言われて追加クレジットを買ったのに、また同じところで止まる——その上限、あなたが当たっている枠とは別かもしれない

Claude Code で副作業者（サブエージェント）が「セッション上限」エラーで停止する問題が報告されています。/status では購読枠に余裕があり、追加クレジットを購入しても同じエラーで停止し、使用トークンは課金されます。大量並行処理後の停止は枠枯渇の可能性がありますが、孤立した停止では補助モデル（安全分類器 claude-opus-4-8[1m]）の unavailable が発生しており、表示される上限と実際の制約が異なる可能性が指摘されています。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/b1add0cb7bd1cf35d096)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-14 | 自動生成 |
