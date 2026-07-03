---
title: Model Management
category: guides
subcategory: model-management
tags:
- setup
- sonnet
- 新機能
date: '2026-07-03'
updated: '2026-07-03'
sources:
- url: https://zenn.dev/masafumi_heijo/articles/claude-model-update-detect-not-apply
  title: Claude（Sonnet 5）モデル更新の検知だけを自動化する——notify-only設計の実装ノート
  date: '2026-07-03'
---

# Model Management

---

## 2026-07-03

### Claude（Sonnet 5）モデル更新の検知だけを自動化する——notify-only設計の実装ノート

Claude Sonnet 5のリリースをきっかけに、モデル更新の自動検知と手動適用を分離する設計を実装。全自動適用は破壊的変更（Extended thinking非対応、トークナイザー変更による30%コスト増）やコスト暴発のリスクがあるため、検知のみを自動化し、実際の切り替えは人間の判断に委ねる「notify-only設計」を採用。Pythonスクリプトで公式ドキュメントを定期的にチェックし、プロンプトインジェクションを回避する。

- **ソース**: [Zenn claude](https://zenn.dev/masafumi_heijo/articles/claude-model-update-detect-not-apply)
- **重要度**: 6/10
- **タグ**: sonnet, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-03 | 自動生成 |
