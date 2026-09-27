---
title: Claude Code Config
category: troubleshooting
subcategory: claude-code-config
tags:
- bugfix
- claude-code
- setup
- windows
date: '2026-08-22'
updated: '2026-09-27'
sources:
- url: https://qiita.com/Tsutomu_eng/items/adb531a257c371358d0e
  title: AGENTS.md と CLAUDE.md は解決規則が逆 — symlink する前に確認すること
  date: '2026-08-22'
- url: https://qiita.com/aicoding-guide/items/f5631c2719e10b17804f
  title: Claude Code の --add-dir で追加したディレクトリの CLAUDE.md が読まれないときの設定
  date: '2026-09-10'
- url: https://zenn.dev/arithan/articles/claude-code-silent-pitfalls-windows
  title: Claude Codeの/clearではツールの設定が読み直されない。効かない時に疑う4つのこと
  date: '2026-09-27'
---



# Claude Code Config

---

## 2026-09-27

### Claude Codeの/clearではツールの設定が読み直されない。効かない時に疑う4つのこと

Claude Codeで設定が反映されない問題について解説した記事。/clearコマンドではツール設定が再読み込みされない、親フォルダのコマンドが認識されない、settings.jsonのenv設定が効かないなど、エラーが出ないため気づきにくい6つの不具合事例を紹介。設定が実際に反映されたかを確認する方法や、トラブルシューティングの4つの観点を実例とともに解説している。

- **ソース**: [Zenn claude](https://zenn.dev/arithan/articles/claude-code-silent-pitfalls-windows)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 2026-09-10

### Claude Code の --add-dir で追加したディレクトリの CLAUDE.md が読まれないときの設定

Claude Codeで`--add-dir`により追加した外部ディレクトリのCLAUDE.mdが読み込まれない問題の解決方法を解説。デフォルトでは読み込まれず、環境変数`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD`の設定が必要。共通設定を別リポジトリで管理する際の頻出トラブルシューティング記事。

- **ソース**: [Qiita claudecode](https://qiita.com/aicoding-guide/items/f5631c2719e10b17804f)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 2026-08-22

### AGENTS.md と CLAUDE.md は解決規則が逆 — symlink する前に確認すること

AGENTS.mdとCLAUDE.mdはファイル解決規則が逆であることを解説。AGENTS.mdは最も近い1つが優先される上書きモデルだが、CLAUDE.mdは見つかった全ファイルを連結する累積モデル。モノレポでnestedなAGENTS.mdを使っている場合、symlinkだけではルートの1ファイルしか繋がらず、サブディレクトリの規約がClaude Codeに認識されない実務的な落とし穴がある。

- **ソース**: [Qiita claudecode](https://qiita.com/Tsutomu_eng/items/adb531a257c371358d0e)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-22 | 自動生成 |
