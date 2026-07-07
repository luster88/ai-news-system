---
title: Bedrock Access Error
category: troubleshooting
subcategory: bedrock-access-error
tags:
- bugfix
- claude-api
- sonnet
date: '2026-07-07'
updated: '2026-07-07'
sources:
- url: https://qiita.com/ss_IT_study/items/e9a13fb9d6695b4c76ae
  title: Amazon BedrockでClaude 3.5 Sonnetが突然利用できなくなったのでCloudTrailから原因を調査してみた
  date: '2026-07-07'
---

# Bedrock Access Error

---

## 2026-07-07

### Amazon BedrockでClaude 3.5 Sonnetが突然利用できなくなったのでCloudTrailから原因を調査してみた

Amazon BedrockでClaude 3.5 Sonnetが突然利用不可になった事例の調査記事。CloudTrailログから、Legacyモデルは30日間未使用でアクセス権を失うことが判明。公式ドキュメントでは15日と記載されているが、実際の挙動は異なる可能性がある。提供終了日前でも未使用期間によりアクセスできなくなるため、早めのモデル更新が推奨される。

- **ソース**: [Qiita claude](https://qiita.com/ss_IT_study/items/e9a13fb9d6695b4c76ae)
- **重要度**: 6/10
- **タグ**: claude-api, sonnet, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-07 | 自動生成 |
