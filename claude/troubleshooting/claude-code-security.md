---
title: Claude Code Security
category: troubleshooting
subcategory: claude-code-security
tags:
- bugfix
- claude-code
- mcp
date: '2026-04-12'
updated: '2026-04-12'
sources:
- url: https://qiita.com/yurukusa/items/f9c48bb44569bbf4492e
  title: Claude Codeのdeny rulesが50コマンドで無効化される——hookで防ぐ方法
  date: '2026-04-12'
---

# Claude Code Security

---

## 2026-04-12

### Claude Codeのdeny rulesが50コマンドで無効化される——hookで防ぐ方法

Claude Codeのdeny rulesに深刻な脆弱性が発見された。50個以上のサブコマンドを連結するとすべてのdeny rulesが無効化され、危険なコマンドが実行可能になる。Anthropicはv2.1.90で修正したが、hookを使った防御が推奨される。hookはdeny rulesの上位互換として、コマンドの内容を自由にスクリプトで検査できる。

- **ソース**: [Qiita claude](https://qiita.com/yurukusa/items/f9c48bb44569bbf4492e)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-12 | 自動生成 |
