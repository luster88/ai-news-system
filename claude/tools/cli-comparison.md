---
title: Cli Comparison
category: tools
subcategory: cli-comparison
tags:
- claude-code
- copilot
- cowork
- cursor
- opus
- performance
date: '2026-06-07'
updated: '2026-11-18'
sources:
- url: https://zenn.dev/omohikane/articles/endeavour-antigravity-cli
  title: Antigravity-cliを試してみる
  date: '2026-06-07'
- url: https://zenn.dev/kuwashima/articles/ax-28-coding-agents-comparison
  title: 28種のAIコーディングCLIを徹底比較！ハーネスの性格と裏の顔
  date: '2026-11-18'
---


# Cli Comparison

---

## 2026-11-18

### 28種のAIコーディングCLIを徹底比較！ハーネスの性格と裏の顔

AIコーディングエージェント28種類を横断検索できるツール「ax」の紹介記事。Claude Code、Codex、Gemini、GitHub Copilotなど主要なCLIツールについて、ハーネスとしての性能、ストレージ仕様、セッション管理の特徴を詳細に比較分析。各ツールの強みと運用上の課題（履歴管理の複雑さ、ログの散在など）を解説している。

- **ソース**: [Zenn claude](https://zenn.dev/kuwashima/articles/ax-28-coding-agents-comparison)
- **重要度**: 6/10
- **タグ**: claude-code, copilot, cursor

---

## 2026-06-07

### Antigravity-cliを試してみる

Google I/O で gemini-cli が終了し、後継の Antigravity-CLI が登場。複数モデル選択可能になったが、実際のコード生成テストでは Gemini 3.5 Flash は動作するコードは出すものの設計判断が浅く、メモリ管理やストリーミング処理に問題があることが判明。Claude Opus 4.6 との比較では、Opus が設計の穴を自力で指摘・修正する点で優れていた。Antigravity CLI の利点は Flash の無料枠が1日1,000リクエストと多い点で、雑用やスキャフォールド生成に向き、設計判断が必要な場面では Aider や Claude Code を使い分けるべきという結論。

- **ソース**: [Zenn claude](https://zenn.dev/omohikane/articles/endeavour-antigravity-cli)
- **重要度**: 5/10
- **タグ**: opus, cowork, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-07 | 自動生成 |
