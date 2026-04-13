---
title: Token Consumption
category: troubleshooting
subcategory: token-consumption
tags:
- bugfix
- claude-code
- performance
date: '2026-04-01'
updated: '2026-04-13'
sources:
- url: https://qiita.com/yurukusa/items/49f1fa305522368d7e7a
  title: Claude Codeのトークン消費が突然10倍になる原因と、hookで防ぐ実践的な方法
  date: '2026-04-01'
- url: https://qiita.com/yurukusa/items/49f1fa305522368d7e7a
  title: Claude Codeのトークン消費が突然10倍になる原因と、hookで防ぐ実践的な方法
  date: '2026-04-01'
- url: https://qiita.com/yurukusa/items/c0acc6da4cb1c90fa431
  title: Claude Code v2.1.100でトークン消費が40%増えた——cache_creation膨張の原因と削減方法
  date: '2026-04-13'
---


# Token Consumption

---

## 2026-04-13

### Claude Code v2.1.100でトークン消費が40%増えた——cache_creation膨張の原因と削減方法

Claude Code v2.1.100以降でcache_creation_input_tokensが約40%増加（49,726→69,922トークン）する問題が報告されている。GitHub Issueでは92リアクションを獲得。最も効果的な回避策はv2.1.98への固定だが、セキュリティ上の懸念がある。キャッシュTTLの短縮（1時間→5分）やシステムプロンプトキャッシュの94%増加など、複数のトークン消費問題が同時に報告されており、診断ツールや体系的な最適化手法の導入が推奨されている。

- **ソース**: [Qiita claude](https://qiita.com/yurukusa/items/c0acc6da4cb1c90fa431)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, performance

---

## 2026-04-01

### Claude Codeのトークン消費が突然10倍になる原因と、hookで防ぐ実践的な方法

Claude Codeのトークン消費が突然10倍以上に跳ね上がる問題について、プロンプトキャッシュ無効化が主原因であることを解説。セッションファイル読み取り、セッション再開、サブエージェント同時起動の3つの原因を特定し、hook機能を使った自動検知・防止方法を実践的なコード例とともに紹介。700時間以上の運用実績に基づく対策により、トークン消費の爆発を大幅に削減できることを示している。

- **ソース**: [Qiita claude](https://qiita.com/yurukusa/items/49f1fa305522368d7e7a)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, performance

---

### Claude Codeのトークン消費が突然10倍になる原因と、hookで防ぐ実践的な方法

Claude Codeのトークン消費が突然10倍以上に増える問題について、プロンプトキャッシュ無効化が主原因であることを解説。会話履歴ファイルの読み取り、セッション再開、サブエージェント起動の3つの原因と、hook機能を使った自動検知・防止方法を実践的なコード例とともに紹介。700時間の運用実績に基づく対策を提供。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/49f1fa305522368d7e7a)
- **重要度**: 8/10
- **タグ**: claude-code, performance, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-01 | 自動生成 |
