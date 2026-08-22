---
title: Claude Code Config
category: troubleshooting
subcategory: claude-code-config
tags:
- bugfix
- claude-code
- setup
date: '2026-08-22'
updated: '2026-08-22'
sources:
- url: https://qiita.com/Tsutomu_eng/items/adb531a257c371358d0e
  title: AGENTS.md と CLAUDE.md は解決規則が逆 — symlink する前に確認すること
  date: '2026-08-22'
---

# Claude Code Config

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
