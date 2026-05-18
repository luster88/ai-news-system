---
title: Aws Integration
category: guides
subcategory: aws-integration
tags:
- claude-api
- claude-code
- setup
- 新機能
date: '2026-05-12'
updated: '2026-05-18'
sources:
- url: https://qiita.com/j-dai/items/d228234f043972e80103
  title: Claude Platform on AWS 実装ガイド(継続改訂中)
  date: '2026-05-12'
- url: https://qiita.com/daitak/items/daf289a8e75e0bd4044d
  title: Agent Toolkit for AWS を使ってClaude CodeからEKSクラスタを作成してみる!
  date: '2026-05-18'
---


# Aws Integration

---

## 2026-05-18

### Agent Toolkit for AWS を使ってClaude CodeからEKSクラスタを作成してみる!

2026年5月6日にリリースされたAgent Toolkit for AWSを使って、Claude CodeからEKSクラスタを作成する実践ガイド。VS Code環境でaws-coreプラグインをインストールし、対話形式でS3バケットやEKSクラスタ、ノードグループを作成。Claude Codeがバケット名の命名規則を理解して修正提案したり、既存のCloudFormationテンプレートを活用するなど、スムーズなAWSリソース構築が実現できた。

- **ソース**: [Qiita claude](https://qiita.com/daitak/items/daf289a8e75e0bd4044d)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-12

### Claude Platform on AWS 実装ガイド(継続改訂中)

Claude Platform on AWSの実装ガイド。AWS IAMを入口としてAnthropicのClaude APIを利用する統合方式について、セットアップ手順、IAM権限設定、Outbound Web Identity Federation（OWIF）の有効化、データレジデンシーの考慮点などを運用・セキュリティ視点で解説。Bedrockとの違いやエンタープライズ契約時の注意点も含む。

- **ソース**: [Qiita claude](https://qiita.com/j-dai/items/d228234f043972e80103)
- **重要度**: 6/10
- **タグ**: claude-api, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-12 | 自動生成 |
