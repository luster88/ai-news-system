---
title: Claude Code Security Fix
category: releases
subcategory: claude-code-security-fix
tags:
- bugfix
- claude-code
- release
date: '2026-08-04'
updated: '2026-08-04'
sources:
- url: https://qiita.com/moha0918_/items/4a520c01ae3e04f211e4
  title: Claude Code v2.1.221｜zsh の [[ ]] で権限チェックが素通りしていた｜毎日Changelog解説
  date: '2026-08-04'
---

# Claude Code Security Fix

---

## 2026-08-04

### Claude Code v2.1.221｜zsh の [[ ]] で権限チェックが素通りしていた｜毎日Changelog解説

Claude Code v2.1.221 では、zsh の [[ ]] 正規表現条件にコマンドを隠すことで Bash ツールの権限チェックを素通りできていた脆弱性が修正されました。該当コマンドは許可プロンプトの対象となり、allow ルールで自動実行している環境では挙動が変わります。また print モードでの MCP サーバー初回ターン問題、サンドボックス認証情報のマスクモード追加、VSCode の Focus view 追加なども含まれています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/4a520c01ae3e04f211e4)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-04 | 自動生成 |
