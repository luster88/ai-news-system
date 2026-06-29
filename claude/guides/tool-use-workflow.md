---
title: Tool Use Workflow
category: guides
subcategory: tool-use-workflow
tags:
- claude-api
- mcp
- prompt
date: '2026-06-29'
updated: '2026-06-29'
sources:
- url: https://zenn.dev/hisa_tech_2973/articles/a7d7d43db6011a
  title: ローカルAI Gateway - Anthropic Tool Use を試してみました
  date: '2026-06-29'
---

# Tool Use Workflow

---

## 2026-06-29

### ローカルAI Gateway - Anthropic Tool Use を試してみました

Anthropic Tool Useの動作確認を行い、ClaudeがツールのAPIを直接実行するのではなく、tool_useという実行要求を返すのみであることを検証。実際のツール実行はアプリ側の責務であり、Policy Engineのようなポリシー制御を挟む余地があることを確認した。Docker環境でダミーのgithub_list_issuesツールを使用した検証サンプルを実装。

- **ソース**: [Zenn claude](https://zenn.dev/hisa_tech_2973/articles/a7d7d43db6011a)
- **重要度**: 6/10
- **タグ**: claude-api, mcp, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-29 | 自動生成 |
