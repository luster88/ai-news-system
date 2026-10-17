---
title: Model Deprecation
category: releases
subcategory: model-deprecation
tags:
- claude-api
- haiku
- opus
- release
- sonnet
date: '2026-05-03'
updated: '2026-10-17'
sources:
- url: https://qiita.com/tai0921/items/fe20f48cf99d3bd336df
  title: Claude Sonnet 4 / Opus 4が6月15日に終わる — 今すぐ始める移行3ステップ
  date: '2026-05-03'
- url: https://qiita.com/picnic/items/fce93bb7d299ba16c613
  title: Claude Opus 4 廃止まで2週間：Opus 4.8移行と最新API変更まとめ
  date: '2026-06-02'
- url: https://qiita.com/YushiYamamoto/items/132e5ae5e4c0b77c4741
  title: 2026年6月のLLM提供停止ラッシュ：GPT-5・o3スナップショット非推奨とClaude 4退役、本番コードで今すぐ直すこと
  date: '2026-06-20'
- url: https://www.reddit.com/r/ClaudeAI/comments/1x7rzpe/that_didnt_take_long_claude_haiku_45_is_leaving
  title: That didn't take long - Claude Haiku 4.5 is leaving the model selector October
    29th
  date: '2026-10-17'
---




# Model Deprecation

---

## 2026-10-17

### That didn't take long - Claude Haiku 4.5 is leaving the model selector October 29th

Claude Haiku 4.5が10月29日にモデルセレクターから削除されることが発表されました。リリースから比較的短期間での終了となり、コミュニティで議論を呼んでいます。この変更により、ユーザーは他のモデル（Sonnetなど）への移行を検討する必要があります。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1x7rzpe/that_didnt_take_long_claude_haiku_45_is_leaving)
- **重要度**: 7/10
- **タグ**: haiku, release, claude-api

---

## 2026-06-20

### 2026年6月のLLM提供停止ラッシュ：GPT-5・o3スナップショット非推奨とClaude 4退役、本番コードで今すぐ直すこと

2026年6月、OpenAIとAnthropicが相次いでモデル退役を発表。OpenAIはGPT-5・o3スナップショットを7月23日に停止、AnthropicはClaude Sonnet 4/Opus 4を6月15日に退役済み。本番環境で日付付きスナップショットIDをハードコードしているコードは即座に対処が必要。さらに米政府の輸出規制によりClaude Fable 5/Mythos 5が公開3日後に停止される事態も発生しており、予告なし停止へのフォールバック設計の重要性が増している。

- **ソース**: [Qiita claude](https://qiita.com/YushiYamamoto/items/132e5ae5e4c0b77c4741)
- **重要度**: 9/10
- **タグ**: claude-api, opus, sonnet

---

## 2026-06-02

### Claude Opus 4 廃止まで2週間：Opus 4.8移行と最新API変更まとめ

2026年6月15日にClaude Opus 4 / Sonnet 4が廃止されるため、移行が必要です。移行先はOpus 4.8（旧4.7から変更）とSonnet 4.6で、Opus 4.8は1Mトークンコンテキストと128k最大出力に対応していますが、Microsoft Foundryでは200k制限があります。stop_detailsフィールドの公式ドキュメント化、会話途中のシステムメッセージ配置ルール明確化、advisor toolへのmax_tokensパラメータ追加などの改善も含まれています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/fce93bb7d299ba16c613)
- **重要度**: 9/10
- **タグ**: opus, sonnet, release

---

## 2026-05-03

### Claude Sonnet 4 / Opus 4が6月15日に終わる — 今すぐ始める移行3ステップ

AnthropicがClaude Sonnet 4とOpus 4を2026年6月15日に廃止することを発表。移行先はClaude Opus 4.7またはSonnet 5が推奨される。コーディング・複雑な推論タスクにはOpus 4.7、高速・低コストのテキスト処理にはSonnet 5が適している。モデルIDの変更とテストを今すぐ開始し、本番環境への影響を避けることが重要。

- **ソース**: [Qiita claude](https://qiita.com/tai0921/items/fe20f48cf99d3bd336df)
- **重要度**: 9/10
- **タグ**: opus, sonnet, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-03 | 自動生成 |
