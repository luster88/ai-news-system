---
title: Aws Bedrock Billing
category: troubleshooting
subcategory: aws-bedrock-billing
tags:
- claude-api
- haiku
- pricing
date: '2026-11-20'
updated: '2026-11-20'
sources:
- url: https://qiita.com/A-nkt/items/f3a12134d0d3e9ff2668
  title: Bedrock の Claude は「Amazon Bedrock」として請求されない。AWS Budgets の自動停止が 1 セントも数えていなかった話
  date: '2026-11-20'
---

# Aws Bedrock Billing

---

## 2026-11-20

### Bedrock の Claude は「Amazon Bedrock」として請求されない。AWS Budgets の自動停止が 1 セントも数えていなかった話

AWS Bedrock経由でClaudeを利用する際、請求が「Amazon Bedrock」ではなく「Claude Haiku 4.5 (Amazon Bedrock Edition)」など個別モデル名で計上されるため、AWS Budgetsのフィルター設定を誤ると予算管理が機能しない問題が報告されています。個人開発者が家計簿アプリにレシート読み取り機能を実装する中で発見し、適切なフィルター設定、画像の事前縮小、Structured Outputsの活用、API Gatewayのタイムアウト対策など実践的なTipsも共有されています。Haiku 4.5は1枚あたり0.0017〜0.0035ドルで、月10ドルで約2,800〜5,700枚のレシート処理が可能という実測データも提示されています。

- **ソース**: [Qiita claude](https://qiita.com/A-nkt/items/f3a12134d0d3e9ff2668)
- **重要度**: 7/10
- **タグ**: claude-api, haiku, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-20 | 自動生成 |
