---
title: Cost Monitoring
category: tools
subcategory: cost-monitoring
tags:
- claude-code
- mcp
- pricing
date: '2026-11-09'
updated: '2026-11-09'
sources:
- url: https://zenn.dev/kazusa_nakagawa/articles/202610-model-rate-check
  title: Claude の新モデルが $0 で集計されていたら、翌朝のバッチで気づけるようにした
  date: '2026-11-09'
---

# Cost Monitoring

---

## 2026-11-09

### Claude の新モデルが $0 で集計されていたら、翌朝のバッチで気づけるようにした

Claude Code のトークン使用量を API 料金換算で表示する自作モニターで、新モデルが料金表にないと $0 として集計される問題が発生。1 億 2,600 万トークンが 3 週間 $0 扱いになった経験から、料金表にないモデルが使われたら翌朝のバッチを失敗させるチェックを実装。料金 API がないため手動管理を継続し、トランスクリプトの cost-state を使って料金未設定とずれの 2 種類をチェックする仕組みを構築した。

- **ソース**: [Zenn claude](https://zenn.dev/kazusa_nakagawa/articles/202610-model-rate-check)
- **重要度**: 5/10
- **タグ**: claude-code, pricing, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-09 | 自動生成 |
