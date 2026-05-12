---
title: Billing Issue
category: troubleshooting
subcategory: billing-issue
tags:
- bugfix
- claude-code
- pricing
date: '2026-05-12'
updated: '2026-05-12'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1tbaq2d/psa_if_your_project_has_an_anthropic_api_key_in
  title: 'PSA: If your project has an ANTHROPIC_API_KEY in any .env file, Claude Code
    will silently bill your API account instead of your Max plan — Anthropic calls
    it "intentional functionality"'
  date: '2026-05-12'
---

# Billing Issue

---

## 2026-05-12

### PSA: If your project has an ANTHROPIC_API_KEY in any .env file, Claude Code will silently bill your API account instead of your Max plan — Anthropic calls it "intentional functionality"

Claude Code がプロジェクトの .env ファイルに ANTHROPIC_API_KEY がある場合、Max プランではなく API アカウントに自動的に請求される問題が報告されました。ユーザーは警告なしに $187 を失い、Anthropic は「意図的な機能」と回答しました。環境変数を起動前に unset することで回避可能ですが、事前警告がないことが批判されています。この挙動は OAuth 認証より環境変数の API キーを優先する仕様によるものです。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1tbaq2d/psa_if_your_project_has_an_anthropic_api_key_in)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-12 | 自動生成 |
