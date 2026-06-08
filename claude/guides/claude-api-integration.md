---
title: Claude Api Integration
category: guides
subcategory: claude-api-integration
tags:
- claude-api
- haiku
- prompt
- sonnet
date: '2026-03-25'
updated: '2026-06-08'
sources:
- url: https://zenn.dev/tradejournal/articles/f886154a9f1ec8
  title: Next.js 16 + Anthropic Claude APIでトレード日記AI分析ツールを作った話
  date: '2026-03-25'
- url: https://zenn.dev/dmiiiiii1116/articles/7cdb8b4b57c976
  title: LINEがAI秘書になった話。Claude × Notion × Googleを繋いで、毎朝8時に予定を送ってくれる仕組みを作った
  date: '2026-06-08'
---


# Claude Api Integration

---

## 2026-06-08

### LINEがAI秘書になった話。Claude × Notion × Googleを繋いで、毎朝8時に予定を送ってくれる仕組みを作った

LINE Messaging API、Claude API、Google Calendar/Gmail、Notion APIを組み合わせて、毎朝8時に予定・タスク・メールのサマリーを自動送信するAI秘書を構築。Claude APIがユーザーの自然言語入力から適切なAPIを判断してルーティングする仕組みを採用し、ConoHa VPS上でsystemdサービスとして24時間稼働させている。

- **ソース**: [Zenn claude](https://zenn.dev/dmiiiiii1116/articles/7cdb8b4b57c976)
- **重要度**: 6/10
- **タグ**: claude-api, sonnet, prompt

---

## 2026-03-25

### Next.js 16 + Anthropic Claude APIでトレード日記AI分析ツールを作った話

個人開発者がNext.js 16、Supabase、Claude APIを組み合わせてトレード記録分析SaaSを構築した事例。週次でClaude APIが統計指標を元にコーチング型レポートを自動生成し、ルール違反を数値化して可視化。RSCとRLSによるマルチテナント設計、claude-haiku-4-5の採用理由、プロンプトエンジニアリングの実装詳細を解説。

- **ソース**: [Zenn claude](https://zenn.dev/tradejournal/articles/f886154a9f1ec8)
- **重要度**: 6/10
- **タグ**: claude-api, haiku, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-25 | 自動生成 |
