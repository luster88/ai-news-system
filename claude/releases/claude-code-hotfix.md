---
title: Claude Code Hotfix
category: releases
subcategory: claude-code-hotfix
tags:
- bugfix
- claude-code
- opus
- release
date: '2026-04-16'
updated: '2026-05-16'
sources:
- url: https://qiita.com/moha0918_/items/6a21a6b76828fc7529af
  title: 今日のClaude Code v2.1.112 リリース｜毎日Changelog解説
  date: '2026-04-16'
- url: https://qiita.com/moha0918_/items/6a21a6b76828fc7529af
  title: 今日のClaude Code v2.1.112 リリース｜毎日Changelog解説
  date: '2026-04-16'
- url: https://qiita.com/moha0918_/items/4a177eb40bcf7fb66fba
  title: Claude Code v2.1.142〜v2.1.143 リリース｜毎日Changelog解説
  date: '2026-05-16'
---


# Claude Code Hotfix

---

## 2026-05-16

### Claude Code v2.1.142〜v2.1.143 リリース｜毎日Changelog解説

Claude Code v2.1.142～v2.1.143がリリース。Fast modeのデフォルトモデルがOpus 4.6から4.7に昇格し、既存の挙動に影響する可能性あり。plugin disable/enableが依存関係を強制チェックするようになり、誤った無効化を防止。worktree.bgIsolation: "none"設定で背景セッションが本体ディレクトリを直接編集可能に。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/4a177eb40bcf7fb66fba)
- **重要度**: 7/10
- **タグ**: claude-code, release, opus

---

### Claude Code v2.1.142〜v2.1.143 リリース｜毎日Changelog解説

Claude Code v2.1.142〜v2.1.143のリリース情報。Fast modeのデフォルトモデルがOpus 4.6から4.7に昇格し、環境変数で旧モデルにピン留め可能。プラグインの有効化・無効化時に依存関係を自動チェックする機能が追加され、依存元がある場合は無効化を拒否。worktree.bgIsolation: "none"設定で背景セッションが本体ディレクトリを直接編集可能に。MCP_TOOL_TIMEOUTがリモートMCPサーバにも反映されるようになった。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/4a177eb40bcf7fb66fba)
- **重要度**: 7/10
- **タグ**: claude-code, release, opus

---

## 2026-04-16

### 今日のClaude Code v2.1.112 リリース｜毎日Changelog解説

Claude Code v2.1.112がリリースされ、約4時間前にリリースされたv2.1.111で導入されたAuto mode + Opus 4.7の組み合わせにおける可用性の不具合を修正。v2.1.111ではMaxサブスクライバー向けにAuto modeでOpus 4.7が使えるようになり、xhighというeffort levelも追加されていたが、この新機能に不具合が混入していた。Maxプラン契約者でAuto modeを常用しているユーザーが対象のホットフィックス。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/6a21a6b76828fc7529af)
- **重要度**: 6/10
- **タグ**: claude-code, release, bugfix

---

### 今日のClaude Code v2.1.112 リリース｜毎日Changelog解説

Claude Code v2.1.112 がリリースされました。v2.1.111 で導入された Auto mode と Opus 4.7 の組み合わせに発生した可用性の不具合を、リリースから約4時間で修正する緊急ホットフィックスです。Max プラン契約者で Auto mode を使用しているユーザーが対象で、アップデートを適用すれば問題なく Opus 4.7 が利用できるようになります。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/6a21a6b76828fc7529af)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-16 | 自動生成 |
