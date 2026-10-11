---
title: Skill Testing Automation
category: tools
subcategory: skill-testing-automation
tags:
- claude-api
- claude-code
- copilot
- cowork
- performance
- 新機能
date: '2026-05-04'
updated: '2026-10-11'
sources:
- url: https://zenn.dev/rick2200/articles/9db3f4e32f9286
  title: GitHub ActionsでCopilot SDKを使いClaude Skillsの効果検証をしてみる
  date: '2026-05-04'
- url: https://ai-heartland.com/agent/quicke2e-plain-english-e2e
  title: QuickE2Eとは｜E2Eテスト AIの「8.6倍速い」を同梱の生データから計算し直した
  date: '2026-10-11'
---


# Skill Testing Automation

---

## 2026-10-11

### QuickE2Eとは｜E2Eテスト AIの「8.6倍速い」を同梱の生データから計算し直した

QuickE2EはE2Eテスト用AIツールで、Claude Code + Playwrightに比べて8.6倍高速かつコストが234倍安いことを生データで検証可能。モデルは次の操作を決定するだけで、合否判定はコードで行う設計。依存関係はPlaywright 1本のみで、セレクタ不要の自然言語テスト記述が可能。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/quicke2e-plain-english-e2e)
- **重要度**: 6/10
- **タグ**: claude-api, performance, cowork

---

## 2026-05-04

### GitHub ActionsでCopilot SDKを使いClaude Skillsの効果検証をしてみる

Claude Code Skillsの改善・退行を機械的に検証するため、GitHub ActionsとCopilot SDKを使ったCI評価プラグイン「skill-eval」を開発。PRに/skill-evalとコメントすると、新旧バージョンをA/B比較し、改善✅/退行❌/同等➖の判定をPRコメントに返す。4軸スコア（成功条件充足・網羅性・期待挙動・簡潔さ）で定量評価し、レビュアーが数字を根拠にマージ判断できる仕組み。

- **ソース**: [Zenn claude](https://zenn.dev/rick2200/articles/9db3f4e32f9286)
- **重要度**: 7/10
- **タグ**: claude-code, copilot, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-04 | 自動生成 |
