---
title: Claude Code Mcp
category: guides
subcategory: claude-code-mcp
tags:
- claude-code
- mcp
- setup
date: '2026-08-24'
updated: '2026-08-24'
sources:
- url: https://qiita.com/hot377/items/4bddfbf69c986714caee
  title: AWS DevOps AgentをTerraformでデプロイしてClaude CodeからMCPで呼び出してみた
  date: '2026-08-24'
---

# Claude Code Mcp

---

## 2026-08-24

### AWS DevOps AgentをTerraformでデプロイしてClaude CodeからMCPで呼び出してみた

AWS DevOps AgentをTerraformでデプロイし、Claude CodeからMCP経由で安全に呼び出す実装例。IAMロールによる権限分離とSigV4認証を用いて、プロンプトではなくツール制限で読み取り専用を担保する設計。Terraform構築時の注意点（タグ形式、IAM伝搬待ち）やMCP認証方式の選定理由も解説。

- **ソース**: [Qiita claudecode](https://qiita.com/hot377/items/4bddfbf69c986714caee)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-24 | 自動生成 |
