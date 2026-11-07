---
title: Robots Txt Config
category: guides
subcategory: robots-txt-config
tags:
- claude-api
- setup
date: '2026-11-07'
updated: '2026-11-07'
sources:
- url: https://zenn.dev/aima/articles/4123a403767cdc
  title: robots.txt で AI のロボットを「学習は止めて、検索は通す」に書き分ける
  date: '2026-11-07'
---

# Robots Txt Config

---

## 2026-11-07

### robots.txt で AI のロボットを「学習は止めて、検索は通す」に書き分ける

robots.txtでAIクローラーを学習用と検索用に書き分ける方法を解説。OpenAIとAnthropicは学習用（GPTBot/ClaudeBot）と検索用（SearchGPT/ClaudeBot-Search）のロボット名が分かれているため書き分け可能。Google-Extendedは学習とグラウンディング両方を制御するため分離不可。よくある間違いとして、名指しグループを作るとUser-agent: *の規則が効かなくなること、Disallow: /で全停止後に検索用だけ許可するとGooglebotまで止まることを指摘。

- **ソース**: [Zenn claude](https://zenn.dev/aima/articles/4123a403767cdc)
- **重要度**: 6/10
- **タグ**: claude-api, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-07 | 自動生成 |
