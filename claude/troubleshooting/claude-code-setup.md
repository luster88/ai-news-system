---
title: Claude Code Setup
category: troubleshooting
subcategory: claude-code-setup
tags:
- bugfix
- claude-code
- mac
- setup
date: '2026-03-23'
updated: '2026-04-26'
sources:
- url: https://qiita.com/juliuse/items/981cee0228c394ffc28f
  title: Claude Codeさいしょのつまずき【claudeコマンドが使えない】
  date: '2026-03-23'
- url: https://zenn.dev/nabecoach/articles/6a4d2a9709424a
  title: Claude Code setup トラブルシューティング API連携になっていたので、サブスクリプションに切り替えた
  date: '2026-04-26'
---


# Claude Code Setup

---

## 2026-04-26

### Claude Code setup トラブルシューティング API連携になっていたので、サブスクリプションに切り替えた

Claude Codeのセットアップで「command not found」やAPI課金問題に遭遇した事例の解決方法を解説。2026年現在の公式推奨手順として、npmではなくネイティブインストーラーを使用し、PATHを~/.local/binに通す方法を紹介。さらに、API認証からClaude Proサブスクリプション認証への切り替え手順（/logoutして再ログイン）と、トラブル時のclaude doctorコマンドの活用方法を詳述している。

- **ソース**: [Zenn claude](https://zenn.dev/nabecoach/articles/6a4d2a9709424a)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 2026-03-23

### Claude Codeさいしょのつまずき【claudeコマンドが使えない】

Claude Code のインストール後に `claude` コマンドが使えない問題について解説。公式インストールスクリプト実行後もパスが通っていないため、手動でパスを通す必要がある。初回実行時にセットアップが開始され、`quit` コマンドで終了できる。

- **ソース**: [Qiita claudecode](https://qiita.com/juliuse/items/981cee0228c394ffc28f)
- **重要度**: 5/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-23 | 自動生成 |
