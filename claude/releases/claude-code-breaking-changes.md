---
title: Claude Code Breaking Changes
category: releases
subcategory: claude-code-breaking-changes
tags:
- bugfix
- claude-code
- release
- setup
- 新機能
date: '2026-11-05'
updated: '2026-11-14'
sources:
- url: https://qiita.com/picnic/items/6984d8e59c0e8b52dfab
  title: Claude Code v2.1.318 破壊的変更まとめ：ランナーログ・IDE拡張・deniedMcpServers
  date: '2026-11-05'
- url: https://qiita.com/NaokiIshimura/items/497afd9a11879d369d19
  title: Claude Code 開発者が注目している5つのアップデート（v2.1.321 - v2.1.325）
  date: '2026-11-14'
- url: https://qiita.com/NaokiIshimura/items/59520039c1504a84cf89
  title: Claude Code v2.1.321 - v2.1.325 リリースノートまとめ
  date: '2026-11-14'
---


# Claude Code Breaking Changes

---

## 2026-11-14

### Claude Code 開発者が注目している5つのアップデート（v2.1.321 - v2.1.325）

Claude Code v2.1.321～v2.1.325の5つの重要なアップデートを解説。サンドボックス内Bashコマンドの権限フローが変更され、無人実行には設定の見直しが必要に。未知のモデルIDのコンテキストウィンドウが200Kから1Mに拡大され、サードパーティゲートウェイ利用時は環境変数での調整が推奨される。Claude Fable 5.2がデフォルトモデルとなり、fast modeのレート制限時の挙動が改善された。

- **ソース**: [Qiita claude](https://qiita.com/NaokiIshimura/items/497afd9a11879d369d19)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code 開発者が注目している5つのアップデート（v2.1.321 - v2.1.325）

Claude Code v2.1.321〜v2.1.325の実務影響が大きい5つのアップデートを解説。サンドボックス内Bashの確認動作変更により無人実行が停止する可能性、未知モデルIDのコンテキストウィンドウが200Kから1Mへ変更されサードパーティゲートウェイでエラーが発生しうる問題、Claude Fable 5.2のデフォルト化とfast modeの改善について詳説。

- **ソース**: [Qiita claudecode](https://qiita.com/NaokiIshimura/items/497afd9a11879d369d19)
- **重要度**: 7/10
- **タグ**: claude-code, release, setup

---

### Claude Code v2.1.321 - v2.1.325 リリースノートまとめ

Claude Code v2.1.321-v2.1.325では、新デフォルトモデル Claude Fable 5.2（1Mコンテキスト、入力$8/出力$40）が追加され、実験的なCode Mode（ClaudeがJavaScriptでツールを呼び出す機能）が導入されました。プラグインのengines["claude-code"]によるバージョン範囲指定が可能になり、Bashコマンドの権限フローとセキュリティ修正が大幅に改善されました。MCP関連では、v1クライアントが削除され、v2互換モードへ移行しています。

- **ソース**: [Qiita claudecode](https://qiita.com/NaokiIshimura/items/59520039c1504a84cf89)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

## 2026-11-05

### Claude Code v2.1.318 破壊的変更まとめ：ランナーログ・IDE拡張・deniedMcpServers

Claude Code v2.1.318がリリースされ、3件の破壊的変更が含まれています。セルフホストランナーのログ行フォーマット変更により既存の監視スクリプトが動作しなくなる、IDEターミナルからの拡張自動インストールが廃止される、deniedMcpServersのURL適用範囲が拡大し既存のサーバーがブロックされる可能性があります。また、共有ネットワークホームでの設定消失、セッション継続性の問題、ヘッドレス実行での失敗が成功扱いになる問題など、重要なバグ修正も多数含まれています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/6984d8e59c0e8b52dfab)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-05 | 自動生成 |
