---
title: Extended Thinking
category: guides
subcategory: extended-thinking
tags:
- claude-api
- setup
- 新機能
date: '2026-09-08'
updated: '2026-09-08'
sources:
- url: https://qiita.com/yureki_lab/items/71290ff34d4160124d96
  title: Claude API の拡張思考(Extended Thinking)を実装する — budget_tokens の下限、tool use で thinking
    ブロックを返し忘れて 400、temperature 非対応の3つのハマりどころ【2026】
  date: '2026-09-08'
---

# Extended Thinking

---

## 2026-09-08

### Claude API の拡張思考(Extended Thinking)を実装する — budget_tokens の下限、tool use で thinking ブロックを返し忘れて 400、temperature 非対応の3つのハマりどころ【2026】

Claude APIの拡張思考(Extended Thinking)機能を実装する際の3つの落とし穴を解説。budget_tokensは1024以上かつmax_tokens未満が必須、tool use併用時はthinkingブロックをsignature含め無改変で返す必要がある、temperature/top_p/top_kは非対応という制約がある。実装時にはblock.typeで分岐する処理が必要。

- **ソース**: [Qiita claude](https://qiita.com/yureki_lab/items/71290ff34d4160124d96)
- **重要度**: 7/10
- **タグ**: claude-api, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-08 | 自動生成 |
