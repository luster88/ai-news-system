---
title: Ci Cd Automation
category: guides
subcategory: ci-cd-automation
tags:
- claude-code
- cowork
- setup
date: '2026-06-28'
updated: '2026-06-28'
sources:
- url: https://qiita.com/jqit-yukiono/items/61985c6743b89aa6924b
  title: Jenkinsの失敗ログをn8nで回収してClaudeに原因調査させ、Slackへ自動通知する
  date: '2026-06-28'
---

# Ci Cd Automation

---

## 2026-06-28

### Jenkinsの失敗ログをn8nで回収してClaudeに原因調査させ、Slackへ自動通知する

Jenkins の CI 失敗時に n8n がコンソールログを自動回収し、Claude CLI でエラー原因を解析して Slack に通知する自動化システムの実装例。Kubernetes 環境で n8n と Jenkins を連携させ、Shared Library による疎結合設計と、Claude CLI を pod 内で実行する構成が特徴。Jenkins は失敗通知のみを担当し、ログ取得・AI 解析・通知はすべて n8n に集約している。

- **ソース**: [Qiita claude](https://qiita.com/jqit-yukiono/items/61985c6743b89aa6924b)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-28 | 自動生成 |
