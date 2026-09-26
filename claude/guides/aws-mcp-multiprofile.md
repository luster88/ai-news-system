---
title: Aws Mcp Multiprofile
category: guides
subcategory: aws-mcp-multiprofile
tags:
- claude-code
- mcp
- setup
date: '2026-09-26'
updated: '2026-09-26'
sources:
- url: https://qiita.com/kio-ku/items/5b426ffca0eda550e042
  title: AWS_MCP_PROXY_PROFILES で、AWS MCP のアカウントごとの面倒な設定を 1 つにまとめた
  date: '2026-09-26'
---

# Aws Mcp Multiprofile

---

## 2026-09-26

### AWS_MCP_PROXY_PROFILES で、AWS MCP のアカウントごとの面倒な設定を 1 つにまとめた

AWS MCP Serverをマルチアカウント環境で使用する際、従来は各アカウントごとに.mcp.jsonに設定ブロックを記述する必要があったが、2025年6月5日のアップデートで導入されたAWS_MCP_PROXY_PROFILES環境変数により、複数のAWSプロファイルを1つの設定ブロックにまとめられるようになった。mcp-proxy-for-aws v1.6.0以降で利用可能で、~/.aws/configや~/.aws/credentialsに各プロファイルが存在し、最小権限が設定されていることが前提条件となる。

- **ソース**: [Qiita claudecode](https://qiita.com/kio-ku/items/5b426ffca0eda550e042)
- **重要度**: 7/10
- **タグ**: mcp, setup, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-26 | 自動生成 |
