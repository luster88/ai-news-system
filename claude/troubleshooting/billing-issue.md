---
title: Billing Issue
category: troubleshooting
subcategory: billing-issue
tags:
- bugfix
- claude-api
- claude-code
- pricing
date: '2026-05-12'
updated: '2026-07-03'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1tbaq2d/psa_if_your_project_has_an_anthropic_api_key_in
  title: 'PSA: If your project has an ANTHROPIC_API_KEY in any .env file, Claude Code
    will silently bill your API account instead of your Max plan — Anthropic calls
    it "intentional functionality"'
  date: '2026-05-12'
- url: https://www.reddit.com/r/ClaudeAI/comments/1um9j1u/fable_5_max_hit_limit_i_topped_up_250_then_one
  title: Fable 5 Max hit limit, I topped up $250, then one “hey” cost me ~$20?
  date: '2026-07-03'
---


# Billing Issue

---

## 2026-07-03

### Fable 5 Max hit limit, I topped up $250, then one “hey” cost me ~$20?

Reddit ユーザーが Claude の有料プラン（Max $200）で使用上限に達し、$250 をトップアップ後、「hey」という1単語のメッセージ送信で約$20 が消費されるという異常な課金が発生。画面表示では数トークンしか使用していないにも関わらず、実際には 847k トークンが消費されたと表示される。その後のメッセージでは正常な課金に戻ったが、初回の課金が異常に高額だった事例の報告と、同様の経験をした人への問いかけ。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1um9j1u/fable_5_max_hit_limit_i_topped_up_250_then_one)
- **重要度**: 6/10
- **タグ**: pricing, bugfix, claude-api

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
