---
title: Agent Tool Generation
category: guides
subcategory: agent-tool-generation
tags:
- claude-api
- mcp
- prompt
date: '2026-07-21'
updated: '2026-07-21'
sources:
- url: https://zenn.dev/mk0bayashi/articles/2a6ee4123e671f
  title: オントロジー定義から AI エージェントのツールを機械的に生成する
  date: '2026-07-21'
---

# Agent Tool Generation

---

## 2026-07-21

### オントロジー定義から AI エージェントのツールを機械的に生成する

オントロジー定義（業務モデルのYAML）からClaude Agent SDKのツールを機械的に生成する実装手法の報告。Palantir Foundryのオペレーショナル・オントロジーパターンを縮小実装した「ミハシラ」を開発し、オブジェクトは検索・取得ツールに、アクションは実行ツールに自動変換される。zodスキーマも型情報から導出され、設計判断の余地がほぼない構造的な写像関係が実証された。

- **ソース**: [Zenn claude](https://zenn.dev/mk0bayashi/articles/2a6ee4123e671f)
- **重要度**: 7/10
- **タグ**: claude-api, mcp, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-21 | 自動生成 |
