---
title: Unity Mcp Automation
category: tools
subcategory: unity-mcp-automation
tags:
- claude-code
- cowork
- mcp
date: '2026-03-29'
updated: '2026-11-25'
sources:
- url: https://zenn.dev/acropapa330/articles/unity_recorder_ai_studio
  title: Unity Recorder × MCP × Telegram で、AIバーチャルニューススタジオの録画を自動化する
  date: '2026-03-29'
- url: https://zenn.dev/gear_aiteam/articles/ai-to-ai-dengon-relay
  title: Claude Codeから、ChatGPTやclaude.aiの会話へ「伝言」を届ける仕組み
  date: '2026-11-25'
---


# Unity Mcp Automation

---

## 2026-11-25

### Claude Codeから、ChatGPTやclaude.aiの会話へ「伝言」を届ける仕組み

Claude Code（MCP経由）から ChatGPT や claude.ai の会話窓へ「伝言」を自動配達する仕組みの実装例。見張り役（Python）が掲示板を監視し、伝言を検知したら配達係（Claude Cowork のタスク）が Chrome 操作で会話窓に書き込む。AI 同士の非同期コミュニケーションを実現し、手動コピペ作業をほぼ撲滅した事例。

- **ソース**: [Zenn claude](https://zenn.dev/gear_aiteam/articles/ai-to-ai-dengon-relay)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, cowork

---

## 2026-03-29

### Unity Recorder × MCP × Telegram で、AIバーチャルニューススタジオの録画を自動化する

Unity RecorderとMCP、Telegramを連携させてAIバーチャルニューススタジオの録画を自動化する実装例。Unity RecorderのセットアップからMCP経由での制御方針、C#スクリプトによるメニュー呼び出し、カメラ調整の自動化までを解説。WSL2環境からClaude Code + MCPでUnity操作を実現し、Telegramから録画開始・停止を制御する仕組みを構築。

- **ソース**: [Zenn claude](https://zenn.dev/acropapa330/articles/unity_recorder_ai_studio)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-29 | 自動生成 |
