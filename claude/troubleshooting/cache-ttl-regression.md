---
title: Cache Ttl Regression
category: troubleshooting
subcategory: cache-ttl-regression
tags:
- bugfix
- claude-code
- pricing
date: '2026-05-04'
updated: '2026-05-04'
sources:
- url: https://qiita.com/yurukusa/items/7a820e0df6090e69e6b5
  title: 'Cache TTL が 1 時間から 5 分に silent flip した話 — Issue #46829 を 1 ヶ月後に postmortem
    として読み直す'
  date: '2026-05-04'
---

# Cache Ttl Regression

---

## 2026-05-04

### Cache TTL が 1 時間から 5 分に silent flip した話 — Issue #46829 を 1 ヶ月後に postmortem として読み直す

2026年3月、Claude Codeのキャッシュ TTL が1時間から5分へ silent に変更され、Max $200/月ユーザーの quota 消費が急増。リクエストごとに ephemeral_5m タグが選択されるようになり、人間のワークフローと不一致が発生。GitHub Issue #46829 で問題が報告され、4月14日リリースの v2.1.108 で ENABLE_PROMPT_CACHING_1H 環境変数が追加された。目に見える障害はないが、コストが2桁の比率で増加する silent regression の典型例として、postmortem 形式で分析されている。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/7a820e0df6090e69e6b5)
- **重要度**: 8/10
- **タグ**: claude-code, pricing, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-04 | 自動生成 |
