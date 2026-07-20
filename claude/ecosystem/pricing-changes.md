---
title: Pricing Changes
category: ecosystem
subcategory: pricing-changes
tags:
- claude-api
- claude-code
- pricing
- sonnet
- 新機能
date: '2026-04-21'
updated: '2026-07-20'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1srzhd7/psa_claude_pro_no_longer_lists_claude_code_as_an
  title: 'PSA: Claude Pro no longer lists Claude Code as an included feature'
  date: '2026-04-21'
- url: https://qiita.com/ballondol/items/471bc13cabe18cc86fd0
  title: 【6/15〜】Claude Code の課金変更、結局「何が対象で何が対象外」なのか公式情報だけで整理した
  date: '2026-06-02'
- url: https://qiita.com/sakutto-panda/items/620152bb67fd47b3c1c3
  title: 【6/15当日撤回】Claude Agent SDK・claude -p のサブスク別枠化は何だったのか
  date: '2026-06-28'
- url: https://www.reddit.com/r/ClaudeAI/comments/1v1qak5/claude_sonnet_5_price_will_be_increased_starting
  title: Claude Sonnet 5 price will be increased starting September 1
  date: '2026-07-20'
---




# Pricing Changes

---

## 2026-07-20

### Claude Sonnet 5 price will be increased starting September 1

2026年9月1日より Claude Sonnet 5 の API 料金が全面的に50%値上げされることが発表されました。入力トークンは $2/MTok から $3/MTok、出力トークンは $10/MTok から $15/MTok に変更されます。これは当初2ヶ月間の割引期間終了によるもので、Sonnet 4.6 と比較してトークナイザーの違いも考慮すると実質30%の価格上昇となります。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v1qak5/claude_sonnet_5_price_will_be_increased_starting)
- **重要度**: 8/10
- **タグ**: pricing, sonnet, claude-api

---

## 2026-06-28

### 【6/15当日撤回】Claude Agent SDK・claude -p のサブスク別枠化は何だったのか

Anthropicは2026年6月15日にClaudeのサブスクリプションを「対話」と「自動化」に分割し、Agent SDKやclaude -pを別課金にする予定だったが、当日に撤回された。特にclaude -pのヘッドレス実行やGitHub Actions経由の自動化利用が影響を受ける予定だったが、現在は変更なし。同じclaudeコマンドでも-pフラグの有無で課金プールが変わる複雑な設計が混乱を招いた。

- **ソース**: [Qiita claude](https://qiita.com/sakutto-panda/items/620152bb67fd47b3c1c3)
- **重要度**: 8/10
- **タグ**: pricing, claude-code, 新機能

---

### 【6/15当日撤回】Claude Agent SDK・claude -p のサブスク別枠化は何だったのか

2026年6月15日、AnthropicはClaudeのサブスクリプションを「対話」と「自動化」に分割し、Agent SDKやclaude -pを別課金枠にする計画を発表したが、施行当日に撤回された。claude -pやGitHub Actions経由の自動化利用を月額クレジット制に移行する予定だったが、「同じコマンドなのに-pフラグで課金枠が変わる」という混乱を招く設計だった。背景には対話と自動化でのモデル消費量の桁違いの差があり、エージェント利用がサブスク枠を圧迫している問題があった。

- **ソース**: [Qiita claudecode](https://qiita.com/sakutto-panda/items/620152bb67fd47b3c1c3)
- **重要度**: 8/10
- **タグ**: pricing, claude-code, 新機能

---

## 2026-06-02

### 【6/15〜】Claude Code の課金変更、結局「何が対象で何が対象外」なのか公式情報だけで整理した

2026年6月15日からClaude ProおよびMaxサブスクリプションにおいて、Agent SDK、claude -p、GitHub Actions経由のプログラム利用が月次クレジット制に移行する。重要なのは、ターミナルやIDEでの対話型Claude Code利用は明示的に対象外である点。デフォルトではクレジット枯渇時にリクエストが停止し、usage creditsを有効化した場合のみ標準APIレートで課金継続される。

- **ソース**: [Qiita claudecode](https://qiita.com/ballondol/items/471bc13cabe18cc86fd0)
- **重要度**: 9/10
- **タグ**: pricing, claude-code, 新機能

---

## 2026-04-21

### PSA: Claude Pro no longer lists Claude Code as an included feature

Claude Pro プランの料金ページから Claude Code が含まれる機能として記載されなくなったことが報告されています。サポート記事のタイトルも「Pro or Max plan」から「Max plan」のみに変更され、記事には「Updated today」と表示されています。公式アナウンスはなく、ユーザーが気づいた変更です。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1srzhd7/psa_claude_pro_no_longer_lists_claude_code_as_an)
- **重要度**: 8/10
- **タグ**: pricing, claude-code, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-21 | 自動生成 |
