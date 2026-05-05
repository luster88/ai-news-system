---
title: Security Organization
category: guides
subcategory: security-organization
tags:
- claude-code
- setup
- 新機能
date: '2026-05-05'
updated: '2026-05-05'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/6698fa06e3c38265b757
  title: Ultraplan の機密性ベース選別運用：公開リポと機密リポでAI送信先を切り分けた話
  date: '2026-05-05'
---

# Security Organization

---

## 2026-05-05

### Ultraplan の機密性ベース選別運用：公開リポと機密リポでAI送信先を切り分けた話

Claude Code の Ultraplan（Anthropic-managed VM 上の Plan Mode）を組織導入する際に、リポジトリ単位で機密性に基づく選別運用を実施した事例。公開リポと機密リポを明確に区別し、ホワイトリスト・ブラックリストと起動前チェックリストを CLAUDE.md に明文化。環境変数には本番影響のないトークンのみを設定し、CI でのチェック自動化と撤退手順も整備した実践的なセキュリティ運用事例。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/6698fa06e3c38265b757)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-05 | 自動生成 |
