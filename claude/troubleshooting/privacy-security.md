---
title: Privacy Security
category: troubleshooting
subcategory: privacy-security
tags:
- bugfix
- claude-code
- claude-console
- setup
date: '2026-07-01'
updated: '2026-07-27'
sources:
- url: https://the-decoder.com/hidden-code-in-claude-code-secretly-flagged-chinese-users
  title: Hidden code in Claude Code secretly flagged Chinese users
  date: '2026-07-01'
- url: https://the-decoder.com/shared-claude-chats-were-reportedly-showing-up-in-search-engines
  title: Shared Claude chats were reportedly showing up in search engines
  date: '2026-07-27'
- url: https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google
  title: 'PSA: Your Claude shared chats and Artifacts may have ended up on Google'
  date: '2026-07-27'
---


# Privacy Security

---

## 2026-07-27

### Shared Claude chats were reportedly showing up in search engines

Claudeの「リンクで共有」機能で作成された共有チャットが検索エンジンにインデックスされ、一般公開される問題が発生。noindexタグの不備により、Google検索でclaude.ai/shareのURLが大量に表示され、暗号鍵や法的相談内容を含むチャットが閲覧可能になっていた。Anthropicは迅速に対応し、Googleの検索結果からは削除されたが、BingやBrave Searchでは長時間表示され続けた。ユーザーは設定のプライバシーセクションから共有チャットを管理可能。

- **ソース**: [The Decoder Claude](https://the-decoder.com/shared-claude-chats-were-reportedly-showing-up-in-search-engines)
- **重要度**: 8/10
- **タグ**: bugfix, claude-console, setup

---

### PSA: Your Claude shared chats and Artifacts may have ended up on Google

週末、Claudeの共有チャットとArtifactsが予期せずGoogle検索結果に大量に表示される問題が発覚しました。健康記録や企業文書、子供の個人情報などを含むコンテンツが公開状態になっていたことが判明。Anthropicはユーザーが意図的に共有した場合のみ検索結果に表示されると説明していますが、共有機能の仕様とユーザーの期待値にギャップがあった可能性が指摘されています。

- **ソース**: [TechCrunch Claude](https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google)
- **重要度**: 8/10
- **タグ**: claude-console, bugfix

---

## 2026-07-01

### Hidden code in Claude Code secretly flagged Chinese users

Claude Code v2.1.91にて、中国ユーザーを密かに識別する隠しコードが発見され炎上。システムプロンプトのステガノグラフィ技術でタイムゾーンやプロキシURLをチェックし、XOR暗号化で難読化していた。Anthropicは「不正転売防止の実験」と釈明し、機能のロールバックを発表。

- **ソース**: [The Decoder Claude](https://the-decoder.com/hidden-code-in-claude-code-secretly-flagged-chinese-users)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-01 | 自動生成 |
