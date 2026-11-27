---
title: Claude Code Automation
category: troubleshooting
subcategory: claude-code-automation
tags:
- bugfix
- claude-code
- cowork
- setup
date: '2026-09-01'
updated: '2026-11-27'
sources:
- url: https://zenn.dev/sivami/articles/e057f47d115721
  title: 健全性チェックが緑なのに、本番は32日間500だった ── 監視が嘘をつく6つの実例
  date: '2026-09-01'
- url: https://zenn.dev/sidejob/articles/a0633f4032b3685c8
  title: Claude Codeの利用上限で夜間自動化が止まる——分割実行・状態保存・再試行で設計し直した記録
  date: '2026-11-27'
---


# Claude Code Automation

---

## 2026-11-27

### Claude Codeの利用上限で夜間自動化が止まる——分割実行・状態保存・再試行で設計し直した記録

Claude Codeを使った夜間自動化システムが利用上限で2日間停止していたが、ログには「正常終了」と記録されていた問題の解決記録。エラー種別の検知と90分待機、状態保存による途中再開、処理の分割実行という3つの対策を実装。fs.renameSync による原子的なフラグ管理で中断時の状態を確実に保存し、利用上限を前提とした堅牢な自動化システムに設計し直した実践例。

- **ソース**: [Zenn claude](https://zenn.dev/sidejob/articles/a0633f4032b3685c8)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-09-01

### 健全性チェックが緑なのに、本番は32日間500だった ── 監視が嘘をつく6つの実例

個人開発で35本以上のプロジェクトをClaude Codeに任せている開発者が、健全性チェックが緑表示でも本番環境が32日間500エラーを返し続けていた事例など、監視システムが機能不全に陥った6つの実例を紹介。「緑」は確認した範囲でしか正しくないこと、監視対象の設計ミス（statusではなくhealthUrlを見るべき、ログの更新ではなく投稿成功を見るべき、など）が問題だったと分析している。

- **ソース**: [Zenn claude](https://zenn.dev/sivami/articles/e057f47d115721)
- **重要度**: 6/10
- **タグ**: claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-01 | 自動生成 |
