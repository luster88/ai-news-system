---
title: Agent Frameworks
category: tools
subcategory: agent-frameworks
tags:
- claude-api
- claude-code
- cowork
- mcp
- 新機能
date: '2026-05-20'
updated: '2026-08-20'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/a9086bc305bacbdde213
  title: 話題のHermes Agentを調べたら、Claude Code環境に全部あった件
  date: '2026-05-20'
- url: https://ai-heartland.com/agent/flue-agent-harness-framework
  title: Flue徹底解説｜Astroチーム発、自律エージェントの『ハーネス』フレームワーク
  date: '2026-06-29'
- url: https://ai-heartland.com/agent/trueforge-agent-harness
  title: TrueForgeとは｜LLMを動かすOSSエージェントハーネスの導入手順・サンドボックス・コスト実測
  date: '2026-08-20'
---



# Agent Frameworks

---

## 2026-08-20

### TrueForgeとは｜LLMを動かすOSSエージェントハーネスの導入手順・サンドボックス・コスト実測

TrueForgeは、LLMを実用的なエージェントとして動作させるためのOSSエージェントハーネス（実行環境）。TypeScript製でMITライセンス、2026年7月23日公開。npxコマンド1つでチャットUI付きエージェントサーバーが起動し、セッション管理・ストリーミング・ツール承認・コンテキスト圧縮などの実行基盤を提供。LangGraphやCrewAIのような「書く」フレームワークではなく、即座に「動かす」サーバー型の基盤として位置づけられる。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/trueforge-agent-harness)
- **重要度**: 6/10
- **タグ**: claude-api, mcp, cowork

---

## 2026-06-29

### Flue徹底解説｜Astroチーム発、自律エージェントの『ハーネス』フレームワーク

Astroチームが開発した自律エージェント向けフレームワーク「Flue」の解説記事。FlueはSDKではなく「ハーネス」として、セッション管理・ツール・スキル・サンドボックスなど、エージェント実行に必要な環境一式を提供する。Claude Codeのスキル思想と同様、Markdownスキルを直接インポートでき、宣言的にエージェントを構築できる点が特徴。TypeScript製でApache-2.0ライセンス、GitHub約6,900スター。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/flue-agent-harness-framework)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-05-20

### 話題のHermes Agentを調べたら、Claude Code環境に全部あった件

Hermes Agentの主要機能（SOUL.md、3層メモリ、Curatorスキル整理、GEPA自動進化など）を分析し、Claude Codeの既存機能（CLAUDE.md、MEMORY.md+vault-rag、skill-rotate、scheduled-tasks、Agent Teams）との対応関係を整理。Hermesの優位性はヘッドレス常駐とGrok OAuth連携によるLLM費用ゼロ化だが、既存Claude Code環境では追加コストなしで同等のマルチエージェント基盤を構築可能と結論付けている。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/a9086bc305bacbdde213)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-20 | 自動生成 |
