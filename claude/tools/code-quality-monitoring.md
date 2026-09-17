---
title: Code Quality Monitoring
category: tools
subcategory: code-quality-monitoring
tags:
- claude-code
- cursor
- mcp
- prompt
- 新機能
date: '2026-06-26'
updated: '2026-09-17'
sources:
- url: https://zenn.dev/k0chi/articles/76a4d1d72d2bdb
  title: AI が書いたコードの設計劣化を検知する sentrux をまとめてみる
  date: '2026-06-26'
- url: https://zenn.dev/robot/articles/434ebacac356bd
  title: AIのゴミコメントを改善するためのSkillを作った話
  date: '2026-09-17'
---


# Code Quality Monitoring

---

## 2026-09-17

### AIのゴミコメントを改善するためのSkillを作った話

AI が生成する過剰なコメントを改善するための OSS Skill「hush」を作成。Claude Code や Codex に対応し、5つの原則（命名改善によるコメント削除、公開 API への完全なドキュメント、誤解を招くコードへの説明、条件分岐での why の記述、それ以外はコメント不要）に基づいてコメントを整理する。skills CLI 経由で自動適用可能。

- **ソース**: [Zenn claude](https://zenn.dev/robot/articles/434ebacac356bd)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 2026-06-26

### AI が書いたコードの設計劣化を検知する sentrux をまとめてみる

AI コーディングエージェント（Claude Code、Cursor など）を使用する際のコードベース設計劣化を検知するOSSツール「sentrux」の紹介記事。quality_signal という0-10000のスコアで、依存関係、ファイルサイズの偏り、循環依存などからコードベース全体の健康状態を数値化する。MCP連携により、AIエージェント自身がsentruxを呼び出して変更前後の品質差分を確認できる。テストや型チェックの代替ではなく、コードベースが持続的に変更可能な形を保っているかを見るためのツール。

- **ソース**: [Zenn claude](https://zenn.dev/k0chi/articles/76a4d1d72d2bdb)
- **重要度**: 6/10
- **タグ**: claude-code, cursor, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-26 | 自動生成 |
