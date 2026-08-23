---
title: Regional Access Restrictions
category: troubleshooting
subcategory: regional-access-restrictions
tags:
- bugfix
- claude-api
date: '2026-08-23'
updated: '2026-08-23'
sources:
- url: https://qiita.com/yama3133/items/a60835f2c4bc3416a3a1
  title: '香港空港でAmazon Bedrockを4リージョン試してわかったこと: ブロックされるのはAnthropicとOpenAIのモデルだけだった'
  date: '2026-08-23'
---

# Regional Access Restrictions

---

## 2026-08-23

### 香港空港でAmazon Bedrockを4リージョン試してわかったこと: ブロックされるのはAnthropicとOpenAIのモデルだけだった

香港空港のWi-FiからAmazon Bedrock経由で複数リージョン（東京・バージニア北部・シンガポール・台北）のAIモデルをテストした結果、Anthropic ClaudeとOpenAIのプロプライエタリモデルは接続元IPによる地域制限で全て使用不可だった。一方、オープンウェイトモデル（OpenAI gpt-oss-120b）、中国発のKimi K2.5、Amazon自社のNova Proは正常に動作した。請求先住所を日本に設定していても、接続元ネットワークの地理的位置が判定されるため、リージョン選択や請求先設定だけでは地域制限を回避できないことが判明。

- **ソース**: [Qiita claude](https://qiita.com/yama3133/items/a60835f2c4bc3416a3a1)
- **重要度**: 6/10
- **タグ**: claude-api, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-23 | 自動生成 |
