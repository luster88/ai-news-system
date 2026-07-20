---
title: Mcp Skill Management
category: tools
subcategory: mcp-skill-management
tags:
- claude-code
- mcp
- 新機能
date: '2026-07-20'
updated: '2026-07-20'
sources:
- url: https://qiita.com/maronsan611/items/2f7e75db76cfee35e646
  title: そのSKILL.md、別のスキルと発火が被ってない？ 衝突と壊れた参照をCIで落とすリンタを作った
  date: '2026-07-20'
---

# Mcp Skill Management

---

## 2026-07-20

### そのSKILL.md、別のスキルと発火が被ってない？ 衝突と壊れた参照をCIで落とすリンタを作った

Claude の SKILL.md を管理する際の「スキル発火の衝突」と「ファイル参照の腐敗」を CI で自動検出する skills-lint を開発。既存ツールは衝突検出か参照整合のいずれかに限定されていたが、本ツールは両方を依存ゼロで実装し、PR ごとに自動チェック可能。文字バイグラムの Jaccard 類似度でトリガ文の重複を検出し、frontmatter の形式チェックやファイル参照の実在確認も行う。同時に llms.txt 用の reflint もリリース。

- **ソース**: [Qiita claude](https://qiita.com/maronsan611/items/2f7e75db76cfee35e646)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-20 | 自動生成 |
