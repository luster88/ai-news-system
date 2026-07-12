---
title: Sonnet 5 Release
category: releases
subcategory: sonnet-5-release
tags:
- claude-code
- pricing
- release
- sonnet
- 新機能
date: '2026-04-05'
updated: '2026-07-12'
sources:
- url: https://ai-heartland.com/news/news-claude-sonnet-5-release
  title: Claude Sonnet 5（claude-sonnet-5-20260401）リリース：SWE-bench 92%超えで開発者が知るべき全仕様
  date: '2026-04-05'
- url: https://ai-heartland.com/explain/claude-sonnet-5-guide
  title: Claude Sonnet 5 解説｜Opus級の品質をSonnet価格で使う新モデルの全貌
  date: '2026-07-01'
- url: https://qiita.com/sakutto-panda/items/47a2b51bf6c4f513ec49
  title: 【2026/6/30】Claude Sonnet 5リリース — 1Mコンテキスト標準化・temperature廃止・実質3割の値上げも
  date: '2026-07-12'
---



# Sonnet 5 Release

---

## 2026-07-12

### 【2026/6/30】Claude Sonnet 5リリース — 1Mコンテキスト標準化・temperature廃止・実質3割の値上げも

2026年6月30日、Anthropic が Claude Sonnet 5 をリリース。1Mトークンコンテキストが標準となり、Claude Code のデフォルトモデルに昇格。プロモ価格は $2/$10 per MTok（8月31日まで）だが、新トークナイザが約30%多くトークンを消費するため実質値上げ。API では temperature/top_p/top_k の指定が 400 エラーとなる破壊的変更を含む3つの仕様変更が導入された。

- **ソース**: [Qiita claudecode](https://qiita.com/sakutto-panda/items/47a2b51bf6c4f513ec49)
- **重要度**: 9/10
- **タグ**: sonnet, release, claude-code

---

## 2026-07-01

### Claude Sonnet 5 解説｜Opus級の品質をSonnet価格で使う新モデルの全貌

Anthropicの新モデル Claude Sonnet 5 の解説記事。Opus級の品質をSonnet価格帯で実現し、コーディングやエージェント作業に最適化。1Mコンテキスト・最大128K出力で、価格は入力$3/出力$15（2026年8月まで導入価格$2/$10）。アダプティブ思考が既定でオン、effortによる思考深度制御（xhighがSonnet初）、新トークナイザーで約3割トークン増加、高解像度ビジョン対応などが特徴。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-sonnet-5-guide)
- **重要度**: 9/10
- **タグ**: sonnet, release, pricing

---

## 2026-04-05

### Claude Sonnet 5（claude-sonnet-5-20260401）リリース：SWE-bench 92%超えで開発者が知るべき全仕様

2026年4月1日、AnthropicがClaude Sonnet 5（claude-sonnet-5-20260401）を正式リリース。料金は前モデルと同額の$3/$15（百万トークンあたり）のまま、SWE-bench Verified 92.4%を記録し、上位モデルのOpus 4.6（80.8%）を12ポイント以上上回った。「蒸留推論」アーキテクチャを採用し、コンテキストウィンドウも1Mから2Mトークンに倍増。OSWorld-Verifiedでは88.3%で人間の専門家を約16ポイント上回り、実務レベルのコーディングから推論、PC操作まで全ベンチマークで首位を獲得した。

- **ソース**: [AI Heartland](https://ai-heartland.com/news/news-claude-sonnet-5-release)
- **重要度**: 10/10
- **タグ**: sonnet, release, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-05 | 自動生成 |
