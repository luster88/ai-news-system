---
title: Cli Comparison
category: tools
subcategory: cli-comparison
tags:
- cowork
- opus
- performance
date: '2026-06-07'
updated: '2026-06-07'
sources:
- url: https://zenn.dev/omohikane/articles/endeavour-antigravity-cli
  title: Antigravity-cliを試してみる
  date: '2026-06-07'
---

# Cli Comparison

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
