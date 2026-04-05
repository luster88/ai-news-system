---
title: Claude Code Automation
category: guides
subcategory: claude-code-automation
tags:
- claude-code
- cowork
- mcp
- setup
- 新機能
date: '2026-03-28'
updated: '2026-04-05'
sources:
- url: https://qiita.com/kenji_harada/items/58b8dbb395199bbe9f1e
  title: Claude Codeで「AI同士の会話」によるブログ自動生成システムを作ってみた
  date: '2026-03-28'
- url: https://qiita.com/kenji_harada/items/ce01ef8185b48da92013
  title: 【やってみた】Claude Codeで作るSEO自動分析システム - GSC×GA4データを毎朝Slackに通知
  date: '2026-04-05'
- url: https://qiita.com/Kosei0412/items/d259982604a0186a7d8b
  title: GPTに切られたカウンセラーがClaudeCodeで自動化ラインを作った話
  date: '2026-04-05'
---


# Claude Code Automation

---

## 2026-04-05

### 【やってみた】Claude Codeで作るSEO自動分析システム - GSC×GA4データを毎朝Slackに通知

Claude Codeを使ってGSC（Google Search Console）とGA4のデータを自動取得し、全記事をAIがスコアリングして改善すべき記事をSlackに毎朝通知するSEO自動分析システムの構築事例。月間4,000表示でCTR 0.02%という手動では見落としていたボトルネックを検出し、21件の改善機会を発見。googleapis とGoogle Analytics Data APIを使用し、OAuth2認証とサービスアカウント設定で実装。

- **ソース**: [Qiita claude](https://qiita.com/kenji_harada/items/ce01ef8185b48da92013)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

### GPTに切られたカウンセラーがClaudeCodeで自動化ラインを作った話

メンタルヘルス領域でGPTの利用制限を受けたカウンセラーが、ClaudeCodeを中心に5重監査・Slack承認・証跡保存を備えた業務自動化システムを再構築。「AIを信用しない」「止めるべきものは構造で止める」をコンセプトに、全工程に人間承認を必須とし、GPT・Claude・Geminiを直列配置した多層チェック機構を実装。福祉現場の事務作業効率化を、安全性を担保しながら実現した事例。

- **ソース**: [Qiita claudecode](https://qiita.com/Kosei0412/items/d259982604a0186a7d8b)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, setup

---

## 2026-03-28

### Claude Codeで「AI同士の会話」によるブログ自動生成システムを作ってみた

Claude Code Channelsを活用し、2つのAIエージェント（ライター役と編集者役）がDiscord上で会話しながらブログ記事を自動生成・改善するシステムの実装例。従来の「AIに一発で完璧な記事を書かせる」アプローチではなく、段階的な批評・推敲プロセスを導入することで読みやすさが大幅に向上。ローカル実行のためAPI料金がかからず、Brave SearchやSupabaseとMCP連携してトレンド調査からSNS展開まで自動化。

- **ソース**: [Qiita claude](https://qiita.com/kenji_harada/items/58b8dbb395199bbe9f1e)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-28 | 自動生成 |
