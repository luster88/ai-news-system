---
title: Web Scraping
category: tools
subcategory: web-scraping
tags:
- claude-api
- performance
- sonnet
date: '2026-09-12'
updated: '2026-09-12'
sources:
- url: https://zenn.dev/orange_k/articles/366cd9db8be68b
  title: AIエージェントにGoogleマップをスクレイピングさせたら何が起きたか
  date: '2026-09-12'
---

# Web Scraping

---

## 2026-09-12

### AIエージェントにGoogleマップをスクレイピングさせたら何が起きたか

Claudeエージェントにブラウザ操作ツールのみを与え、Googleマップから60件のコーヒーショップ情報をスクレイピングさせた実験。エージェントは全フィールドを正確に取得したが、1件あたり19万〜54万処理トークン、23〜35秒かかった。一方、素のPlaywrightスクリプトは1件6〜14秒、モデルトークンゼロ。エージェントの戦略変更により1件あたりのコスト削減が可能だったが、依然として従来スクリプトと比較して大きなコスト差がある。

- **ソース**: [Zenn claude](https://zenn.dev/orange_k/articles/366cd9db8be68b)
- **重要度**: 6/10
- **タグ**: claude-api, sonnet, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-12 | 自動生成 |
