---
title: Aws Bedrock Integration
category: guides
subcategory: aws-bedrock-integration
tags:
- claude-api
- prompt
- setup
date: '2026-06-03'
updated: '2026-06-03'
sources:
- url: https://qiita.com/yuta_satake/items/1398f4e0be99801b519d
  title: Claude on Amazon Bedrock で Well-Architected Framework Review アシスタントを作ってみた
  date: '2026-06-03'
---

# Aws Bedrock Integration

---

## 2026-06-03

### Claude on Amazon Bedrock で Well-Architected Framework Review アシスタントを作ってみた

AWS Well-Architected Framework の6本柱に基づいて、システム構成を自動レビューするアシスタントを Claude on Amazon Bedrock で構築した記録。Streamlit でUI を作成し、約80行のコードで実装。Inference Profile ID によるクロスリージョン対応、converse_stream でのリアルタイム表示、Prompt Caching による入力コスト最大90%削減を実現。1回のレビューあたり約6円で運用可能。

- **ソース**: [Qiita claude](https://qiita.com/yuta_satake/items/1398f4e0be99801b519d)
- **重要度**: 6/10
- **タグ**: claude-api, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-03 | 自動生成 |
