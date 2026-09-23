---
title: Claude Api Tool Use
category: troubleshooting
subcategory: claude-api-tool-use
tags:
- bugfix
- claude-api
- performance
- setup
date: '2026-09-03'
updated: '2026-09-23'
sources:
- url: https://qiita.com/yureki_lab/items/d97ef5333abb54319140
  title: Claude API の並列ツール実行(parallel tool use)を正しく実装する — tool_result を分けて送ると 400
    になる等3つのハマりどころ【2026】
  date: '2026-09-03'
- url: https://qiita.com/yureki_lab/items/09f6ed07a52c78b1363b
  title: Claude API の stop_reason を全パターン処理する実装手順 — max_tokens で切れても HTTP 200・stop_details
    は refusal のときだけ・pause_turn の再開、3つのハマりどころ【2026】
  date: '2026-09-23'
---


# Claude Api Tool Use

---

## 2026-09-23

### Claude API の stop_reason を全パターン処理する実装手順 — max_tokens で切れても HTTP 200・stop_details は refusal のときだけ・pause_turn の再開、3つのハマりどころ【2026】

Claude APIの応答処理における重要な注意点を解説。stop_reasonが6種類あり、max_tokensで切れても例外が発生せずHTTP 200が返るため、JSONパースエラーが発生しやすい。stop_detailsはrefusal時のみ値を持ち、pause_turn時は再送が必要。実装者向けに全パターンを安全に処理するディスパッチャ関数の実装例を提供。

- **ソース**: [Qiita claude](https://qiita.com/yureki_lab/items/09f6ed07a52c78b1363b)
- **重要度**: 7/10
- **タグ**: claude-api, bugfix, setup

---

## 2026-09-03

### Claude API の並列ツール実行(parallel tool use)を正しく実装する — tool_result を分けて送ると 400 になる等3つのハマりどころ【2026】

Claude API の並列ツール実行(parallel tool use)実装時の3つの典型的な失敗パターンとその回避策を解説。複数の tool_use が返された際、1個ずつ分割送信すると 400 エラーになる問題、例外処理を誤ると会話が止まる問題、ストリーム時の JSON 混在問題について、具体的なコード例と共に正しい実装方法を示している。並列実行を無効化する disable_parallel_tool_use オプションの使い方も紹介。

- **ソース**: [Qiita claude](https://qiita.com/yureki_lab/items/d97ef5333abb54319140)
- **重要度**: 7/10
- **タグ**: claude-api, bugfix, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-03 | 自動生成 |
