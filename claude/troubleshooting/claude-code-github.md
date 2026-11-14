---
title: Claude Code Github
category: troubleshooting
subcategory: claude-code-github
tags:
- bugfix
- claude-code
- cowork
- setup
date: '2026-10-11'
updated: '2026-11-14'
sources:
- url: https://qiita.com/homhom44/items/d866772fde1183485dd9
  title: GitHub連携が認証切れする時の最短チェック手順！Claude Code でつまずいたときの切り分けメモ（2026-10-11）
  date: '2026-10-11'
- url: https://zenn.dev/arx8/articles/97259b103f22d0
  title: Claude Code の cloud session の commit を「誰の依頼か」わかるようにする
  date: '2026-11-14'
---


# Claude Code Github

---

## 2026-11-14

### Claude Code の cloud session の commit を「誰の依頼か」わかるようにする

Claude Code の cloud session で作成されるコミットは、デフォルトで author と committer が両方 Claude になり、チームでの利用時に誰の依頼か追跡できない問題がある。公式の機能リクエストは not planned で却下されたが、SessionStart hook を使って author のみをセッション所有者に設定し、committer は Claude のままにすることで解決できる。これにより GitHub 上で「依頼者 authored and claude committed」と表示され、両者の関与が明確になる。

- **ソース**: [Zenn claude](https://zenn.dev/arx8/articles/97259b103f22d0)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 2026-10-11

### GitHub連携が認証切れする時の最短チェック手順！Claude Code でつまずいたときの切り分けメモ（2026-10-11）

Claude Code を使用中に発生する GitHub 連携の認証切れやツール呼び出しエラーの切り分け手順をまとめた troubleshooting 記事。GitHub Issues で複数報告されている実際の症状に基づき、手元で検証したコマンド実行結果を元に、認証確認と再試行失敗時の状況把握ポイントを整理している。

- **ソース**: [Qiita claudecode](https://qiita.com/homhom44/items/d866772fde1183485dd9)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-11 | 自動生成 |
