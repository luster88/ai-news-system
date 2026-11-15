---
title: Security Config
category: troubleshooting
subcategory: security-config
tags:
- claude-code
- mcp
- setup
date: '2026-11-15'
updated: '2026-11-15'
sources:
- url: https://qiita.com/Hideki_Tamae/items/880fb8afa49cfa65e9a2
  title: 0。Claude Enterpriseに『推奨設定と比較するセキュリティセンター』が追加されたと報じられた週、自分のクラウド環境の許可ホストを数えたら、この数字だった
  date: '2026-11-15'
---

# Security Config

---

## 2026-11-15

### 0。Claude Enterpriseに『推奨設定と比較するセキュリティセンター』が追加されたと報じられた週、自分のクラウド環境の許可ホストを数えたら、この数字だった

Claude Code Remoteのデフォルト環境で`get_environment`を実行し、許可ホストが0件であることを確認。パッケージ管理ツールとMCPサーバーのみ接続可能で、外部ニュースサイトへのWebFetchは失敗。認証情報はGitHub Actionsのリポジトリシークレットに分離されており、最小権限の原則に基づく設計が実証された。Claude Enterpriseのセキュリティセンター追加報道を契機に、エージェント環境の権限設定を定量的に検証した事例。

- **ソース**: [Qiita claudecode](https://qiita.com/Hideki_Tamae/items/880fb8afa49cfa65e9a2)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-15 | 自動生成 |
