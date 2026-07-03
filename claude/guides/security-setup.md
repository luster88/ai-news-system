---
title: Security Setup
category: guides
subcategory: security-setup
tags:
- claude-api
- claude-code
- linux
- prompt
- setup
- 新機能
date: '2026-05-04'
updated: '2026-07-03'
sources:
- url: https://qiita.com/honey-0326-honey/items/c16d628aee898e3f9f72
  title: 【初心者向け】社内PCでClaude Codeを使う前に。絶対に知っておきたいセキュリティの罠と対策
  date: '2026-05-04'
- url: https://zenn.dev/shun0326/articles/1a144d73f0f2f0
  title: 【初心者向け】社内PCでClaude Codeを使う前に。絶対に知っておきたいセキュリティの罠と対策
  date: '2026-05-04'
- url: https://zenn.dev/avot/articles/a802d403c02340
  title: direnvを使って、AssumeRoleで安全なロールに上書きしよう
  date: '2026-05-15'
- url: https://qiita.com/ujunja/items/2b5cceaf5a1a39f43033
  title: Claude Codeのサンドボックスだけでは秘密情報を守れない — 権限ルール・巻き戻しまで含めた安全設定
  date: '2026-07-03'
---



# Security Setup

---

## 2026-07-03

### Claude Codeのサンドボックスだけでは秘密情報を守れない — 権限ルール・巻き戻しまで含めた安全設定

Claude Codeのサンドボックス機能だけでは秘密情報（AWSクレデンシャルやSSH鍵など）の読み取りを防げないことを解説。権限ルール（deny/ask/allow）、サンドボックス、巻き戻し機能を組み合わせた多層防御の設定方法を初心者向けに説明。特に「deny」ルールは「allow」より優先され、スコープをまたいで適用される点が重要。

- **ソース**: [Qiita claude](https://qiita.com/ujunja/items/2b5cceaf5a1a39f43033)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-15

### direnvを使って、AssumeRoleで安全なロールに上書きしよう

direnvを使ってClaude利用時にAWS IAMロールをAssumeRoleで自動的に読み取り専用ロールに切り替える方法を解説。.envrcファイルで環境変数を上書きし、デフォルトで安全な権限に制限することでClaudeによる誤操作を防ぐセットアップガイド。

- **ソース**: [Zenn claude](https://zenn.dev/avot/articles/a802d403c02340)
- **重要度**: 5/10
- **タグ**: setup, claude-api, linux

---

## 2026-05-04

### 【初心者向け】社内PCでClaude Codeを使う前に。絶対に知っておきたいセキュリティの罠と対策

社内PCでClaude Codeを使用する際の必須セキュリティ対策を初心者向けに解説。APIキーを環境変数で管理する方法、コマンド実行の自動承認制限、アクセス可能ディレクトリの制限など、具体的な設定手順を紹介。設定ミスによる情報漏洩や誤操作のリスクを防ぐための実践的ガイド。

- **ソース**: [Qiita claude](https://qiita.com/honey-0326-honey/items/c16d628aee898e3f9f72)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

### 【初心者向け】社内PCでClaude Codeを使う前に。絶対に知っておきたいセキュリティの罠と対策

社内PCでClaude Codeを安全に使うための初心者向けセキュリティガイド。APIキーを環境変数で管理する方法、コマンド実行の自動承認を制限する設定、アクセス可能なディレクトリを制限する方法を具体的に解説。.claude/settings.jsonの設定例や、誤って機密情報を送信してしまうリスクについて警告している。

- **ソース**: [Zenn claude](https://zenn.dev/shun0326/articles/1a144d73f0f2f0)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-04 | 自動生成 |
