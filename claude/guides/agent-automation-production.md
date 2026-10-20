---
title: Agent Automation Production
category: guides
subcategory: agent-automation-production
tags:
- claude-api
- cowork
- mcp
date: '2026-10-20'
updated: '2026-10-20'
sources:
- url: https://qiita.com/joinclass/items/5bd49d75c3f6d2182849
  title: Claude Agent SDK + MCPで業務エージェントを作る — 本番運用中のシェル実装から移植した最小構成
  date: '2026-10-20'
---

# Agent Automation Production

---

## 2026-10-20

### Claude Agent SDK + MCPで業務エージェントを作る — 本番運用中のシェル実装から移植した最小構成

合同会社ジョインクラスが本番運用している業務自動化エージェントの実装事例。Claude Agent SDK + MCPを使い、営業リード収集やSNS監視などを自動化率98%で運用。allowedToolsによる許可リスト方式、maxBudgetUsdでの予算上限設定、社内データへの安全な窓口をMCPツールで提供する実践的な設計パターンを紹介。誤送信やgit push --forceなどの事故経験から、書き込み系ツールは慎重に扱い、承認フローを挟む構成を推奨している。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/5bd49d75c3f6d2182849)
- **重要度**: 7/10
- **タグ**: claude-api, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-20 | 自動生成 |
