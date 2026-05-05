---
title: Bedrock Jp Cris
category: guides
subcategory: bedrock-jp-cris
tags:
- claude-api
- opus
- setup
date: '2026-05-05'
updated: '2026-05-05'
sources:
- url: https://zenn.dev/nemutaizo/articles/afe031ef2310ea
  title: 規制業界のデータレジデンシー要件下で AIエージェントの推論を日本国内に閉じる
  date: '2026-05-05'
---

# Bedrock Jp Cris

---

## 2026-05-05

### 規制業界のデータレジデンシー要件下で AIエージェントの推論を日本国内に閉じる

Amazon Bedrock の JP CRIS（Japan Geo Cross-Region Inference）により、Claude の推論を東京・大阪リージョン内に閉じることが可能。金融・医療・公共など規制業界では、Kiro CLI が inference profile 指定に非対応のため選択肢から外れ、Claude Code on AWS が唯一の現実解となる。Opus 4.7 / Sonnet 4.6 / Sonnet 4.5 が JP CRIS 対応モデルで、SCP による us.* / global.* プレフィックスの明示ブロックが運用上必須。

- **ソース**: [Zenn claude](https://zenn.dev/nemutaizo/articles/afe031ef2310ea)
- **重要度**: 7/10
- **タグ**: claude-api, opus, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-05 | 自動生成 |
