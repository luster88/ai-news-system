---
title: Browser Automation
category: tools
subcategory: browser-automation
tags:
- claude-api
- claude-console
- cowork
- 新機能
date: '2026-06-24'
updated: '2026-08-07'
sources:
- url: https://ai-heartland.com/agent/browser-use-guide-2026
  title: Browser-Useの使い方｜AIに実ブラウザを操作させるOSSの仕組み・導入・他ツール比較【2026】
  date: '2026-06-24'
- url: https://zenn.dev/zeroyenlab/articles/zeroyenlab-claude-in-chrome-note
  title: AIにブラウザ操作を任せている人に聞いた、便利さと「怖さ」の話（Claude in Chrome）
  date: '2026-08-07'
---


# Browser Automation

---

## 2026-08-07

### AIにブラウザ操作を任せている人に聞いた、便利さと「怖さ」の話（Claude in Chrome）

Claude in Chrome（Anthropic公式のChrome拡張機能）の実利用者による体験レポート。ブラウザ操作の自動化により、スクリーンショット不要でUI判断やフォーム入力が可能になる利便性がある一方、プロンプトインジェクション（23.6%→対策後11.2%）などの構造的リスクが存在。API経由の自動化とは安全性の性質が異なるため、警戒を持ちながら使うべきとの実感が共有されている。

- **ソース**: [Zenn claude](https://zenn.dev/zeroyenlab/articles/zeroyenlab-claude-in-chrome-note)
- **重要度**: 7/10
- **タグ**: claude-console, 新機能

---

## 2026-06-24

### Browser-Useの使い方｜AIに実ブラウザを操作させるOSSの仕組み・導入・他ツール比較【2026】

Browser-Useは、LLMに実際のブラウザ操作をさせるMITライセンスのOSS（GitHub 7.8万★、Y Combinator W25採択）。従来のSelenium/Playwrightのように操作手順をコードで書く必要がなく、自然言語でゴールを伝えるだけでエージェントが画面を見て判断・操作する。Claude/GPT/Gemini/Groq/Azure/Ollamaに対応し、pip install＋数行のコードで動作。APIのない業務システムやSaaS管理画面など、ブラウザUI前提の環境を自動化できる点が強み。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/browser-use-guide-2026)
- **重要度**: 6/10
- **タグ**: claude-api, cowork, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-24 | 自動生成 |
