---
title: Claude Code Opus Bugs
category: troubleshooting
subcategory: claude-code-opus-bugs
tags:
- bugfix
- claude-code
- opus
- setup
date: '2026-06-12'
updated: '2026-08-18'
sources:
- url: https://qiita.com/yurukusa/items/cecb7d55f87df3e50f30
  title: Claude Code の Opus 4.8 で起きる2つの事故をログで切り分ける——トークン10倍浪費と、道具の結果の捏造
  date: '2026-06-12'
- url: https://qiita.com/homhom44/items/db6ce6c0252a6ebb634b
  title: Claude Code でつまずいたときの切り分けメモ（2026-08-19）
  date: '2026-08-18'
---


# Claude Code Opus Bugs

---

## 2026-08-18

### Claude Code でつまずいたときの切り分けメモ（2026-08-19）

Claude Code の実行時エラーや接続切断、画面遷移の停止など、GitHub Issues で複数報告されている症状について、手元で検証した切り分け手順をまとめたトラブルシューティング記事。応答が返らない場合の確認観点、通信切断の再現条件とログ確認、ブラウザ拡張機能の影響、起動時の問題、データ不整合など、具体的な症状別に原因の特定方法を整理している。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/db6ce6c0252a6ebb634b)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-06-12

### Claude Code の Opus 4.8 で起きる2つの事故をログで切り分ける——トークン10倍浪費と、道具の結果の捏造

Claude Code の Opus 4.8 で、トークンを10倍以上浪費する費用の事故と、道具の実行結果を待たずに捏造する正しさの事故が2026年5月末から報告されている。記事では JSONL ログを使って output_tokens の中央値を計算し浪費を検出する方法、および tool_use と tool_result の突合で捏造を検証する具体的なコマンドを紹介。2026年6月12日の最新版でも両問題が継続中。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/cecb7d55f87df3e50f30)
- **重要度**: 8/10
- **タグ**: claude-code, opus, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-12 | 自動生成 |
