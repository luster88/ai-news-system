---
title: Claude Api Integration
category: guides
subcategory: claude-api-integration
tags:
- claude-api
- haiku
- prompt
- setup
- sonnet
- windows
date: '2026-03-25'
updated: '2026-09-01'
sources:
- url: https://zenn.dev/tradejournal/articles/f886154a9f1ec8
  title: Next.js 16 + Anthropic Claude APIでトレード日記AI分析ツールを作った話
  date: '2026-03-25'
- url: https://zenn.dev/dmiiiiii1116/articles/7cdb8b4b57c976
  title: LINEがAI秘書になった話。Claude × Notion × Googleを繋いで、毎朝8時に予定を送ってくれる仕組みを作った
  date: '2026-06-08'
- url: https://zenn.dev/h2k0430/articles/d77b8b2708751e
  title: Pixel Tablet + Google Home AssistantでClaude APIをバックエンドにした話
  date: '2026-07-27'
- url: https://zenn.dev/t_okubo/articles/3a74889e628741
  title: 英語コロケーションをAIと練習できる学習アプリをひとりで作った話（Next.js + Claude API）
  date: '2026-09-01'
---




# Claude Api Integration

---

## 2026-09-01

### 英語コロケーションをAIと練習できる学習アプリをひとりで作った話（Next.js + Claude API）

個人開発者がNext.js + Claude APIを使用して英語コロケーション学習アプリ「Colloquy」を開発。Claude APIのストリーミング機能とNDJSON形式を活用し、コロケーション生成結果を逐次表示することで体感速度を改善。Redisキャッシュによるコスト削減、Next.js App RouterでのSSR最適化、翻訳アシスタント機能の実装など、実践的な技術選定と課題解決の経緯が詳しく解説されている。

- **ソース**: [Zenn claude](https://zenn.dev/t_okubo/articles/3a74889e628741)
- **重要度**: 6/10
- **タグ**: claude-api, haiku, setup

---

## 2026-07-27

### Pixel Tablet + Google Home AssistantでClaude APIをバックエンドにした話

Google Pixel TabletのHome AssistantでClaude APIをバックエンドに統合する手順を解説。WSL2上でDockerを使用してHome Assistantを構築し、Wyoming ProtocolとVOICEVOX TTSでずんだもんの音声を実装。タスクスケジューラでWSLを常駐化し、AnthropicのClaude Conversationを音声アシスタントに設定する方法を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/h2k0430/articles/d77b8b2708751e)
- **重要度**: 6/10
- **タグ**: claude-api, setup, windows

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
