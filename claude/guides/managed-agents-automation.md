---
title: Managed Agents Automation
category: guides
subcategory: managed-agents-automation
tags:
- claude-api
- mcp
- setup
- 新機能
date: '2026-05-05'
updated: '2026-10-03'
sources:
- url: https://zenn.dev/genda_jp/articles/8038f227ba9bdf
  title: 'Claude Managed Agents で消える層、残る層: 業務自動化エージェントの視点から'
  date: '2026-05-05'
- url: https://zenn.dev/persimmoq/articles/claude-managed-agents-daily-report
  title: Claude Managed Agents で「毎朝サイトを巡回して日報を書く」エージェントを30分で動かす
  date: '2026-10-03'
---


# Managed Agents Automation

---

## 2026-10-03

### Claude Managed Agents で「毎朝サイトを巡回して日報を書く」エージェントを30分で動かす

Anthropic の Claude Managed Agents を使って、サーバー不要でWeb巡回・日報作成エージェントを30分で構築する方法を解説。Python SDK のみで Agent/Session/Container の仕組みを実装し、スケジュール実行や結果回収までカバー。実運用時の Webhook、Vault、MCP 連携、multiagent などの発展トピックも紹介。

- **ソース**: [Zenn claude](https://zenn.dev/persimmoq/articles/claude-managed-agents-daily-report)
- **重要度**: 8/10
- **タグ**: claude-api, 新機能, setup

---

## 2026-05-05

### Claude Managed Agents で消える層、残る層: 業務自動化エージェントの視点から

Anthropicが公開したClaude Managed Agentsについて、コーディングエージェントではなく業務自動化エージェントの視点から分析。TTFT（Time To First Token）が60-90%改善された技術的進歩を解説しつつ、Markdown+MCPで構築した自前ハーネスとManaged Agentsの使い分けを検討。朝のブリーフィング、月次経理、QA運用など15個のロール別エージェントを運用する著者が、どの層をManaged Agentsに乗せるべきか、どの層を自前で保持すべきかを実例ベースで整理している。

- **ソース**: [Zenn claude](https://zenn.dev/genda_jp/articles/8038f227ba9bdf)
- **重要度**: 7/10
- **タグ**: claude-api, mcp, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-05 | 自動生成 |
