---
title: Security Boundary
category: troubleshooting
subcategory: security-boundary
tags:
- claude-code
- setup
- 新機能
date: '2026-10-09'
updated: '2026-10-09'
sources:
- url: https://zenn.dev/mukuro696/articles/d204f2ff1602c0
  title: トークンを見せなくても使えてしまう——AIエージェントに認証情報を使わせない線を点検した
  date: '2026-10-09'
---

# Security Boundary

---

## 2026-10-09

### トークンを見せなくても使えてしまう——AIエージェントに認証情報を使わせない線を点検した

Claude Code エージェントに認証トークンを見せていない状態でも、認証済みコマンド（git push、記事公開など）が実行可能であることが判明。手順書で定めた「見せない線」と「使わせない線」のずれを検証し、公式ドキュメントを基に拒否ルールやauto modeの分類器では使わせない線を技術的に保証できないことを確認。最終的には人間の確認で守る運用が必要と結論。

- **ソース**: [Zenn claude](https://zenn.dev/mukuro696/articles/d204f2ff1602c0)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-09 | 自動生成 |
