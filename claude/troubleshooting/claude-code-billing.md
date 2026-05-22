---
title: Claude Code Billing
category: troubleshooting
subcategory: claude-code-billing
tags:
- bugfix
- claude-code
- pricing
date: '2026-04-25'
updated: '2026-05-22'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1svdm1w/psa_the_string_hermesmd_in_your_git_commit
  title: 'PSA: The string "HERMES.md" in your git commit history silently routes Claude
    Code billing to extra usage — cost me $200'
  date: '2026-04-25'
- url: https://qiita.com/yurukusa/items/6c6a1cae340cc0cfdf1f
  title: Claude Code v2.1.100以降の cache_creation の20K tokens の inflation、6月15日の課金の改定の前に整理すべき構造の事案
  date: '2026-05-22'
---


# Claude Code Billing

---

## 2026-05-22

### Claude Code v2.1.100以降の cache_creation の20K tokens の inflation、6月15日の課金の改定の前に整理すべき構造の事案

Claude Code v2.1.100以降で同一リクエストに対し約20,000トークンのcache_creation_input_tokensが増加する問題を実機で確認。サーバー側の挙動変更によりユーザーは制御不能な課金増加に直面し、コンテキストウィンドウも圧迫される。6月15日の課金改定前に対処が必要な構造的問題として、関連する4件の起票を統合分析。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/6c6a1cae340cc0cfdf1f)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 2026-04-25

### PSA: The string "HERMES.md" in your git commit history silently routes Claude Code billing to extra usage — cost me $200

Claude Code において、git コミット履歴に「HERMES.md」という文字列が含まれていると、Max プランの利用枠を無視して API 料金が課金されるバグが報告されました。ユーザーは $200 の予期しない課金を受け、Anthropic サポートはバグを認めたものの返金を拒否しました。この問題は特定のファイル名パターンが課金ロジックに誤って影響を与えることを示しており、Claude Code ユーザーは git 履歴の確認が推奨されます。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1svdm1w/psa_the_string_hermesmd_in_your_git_commit)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-25 | 自動生成 |
