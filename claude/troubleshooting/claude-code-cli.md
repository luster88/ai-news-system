---
title: Claude Code Cli
category: troubleshooting
subcategory: claude-code-cli
tags:
- bugfix
- claude-code
- setup
date: '2026-11-12'
updated: '2026-11-12'
sources:
- url: https://qiita.com/phibi-soon/items/127572cab26cc8a004ec
  title: 【実測あり】claudeで、--effort を打ち間違えても処理は止まらない
  date: '2026-11-12'
---

# Claude Code Cli

---

## 2026-11-12

### 【実測あり】claudeで、--effort を打ち間違えても処理は止まらない

Claude Code の --effort オプションを打ち間違えた場合の挙動を実測した記事。誤った値を指定しても警告が出るだけで処理は継続され、終了コードも 0 となるため、cron などの自動実行時に検知が難しい。事前にスクリプトの値を検証するチェックスクリプトの例も紹介されている。

- **ソース**: [Qiita claudecode](https://qiita.com/phibi-soon/items/127572cab26cc8a004ec)
- **重要度**: 4/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-12 | 自動生成 |
