---
title: Claude Code Cloud Plugins
category: troubleshooting
subcategory: claude-code-cloud-plugins
tags:
- bugfix
- claude-code
- setup
date: '2026-10-21'
updated: '2026-10-21'
sources:
- url: https://zenn.dev/i_shinya/articles/claude-code-cloud-plugins-pitfalls
  title: Claude Codeのクラウド（Projects）にプラグインを持ち込むときのハマりどころメモ
  date: '2026-10-21'
---

# Claude Code Cloud Plugins

---

## 2026-10-21

### Claude Codeのクラウド（Projects）にプラグインを持ち込むときのハマりどころメモ

Claude Code の Projects（ベータ版）でクラウド上の thread にカスタムプラグインを持ち込む際のハマりどころをまとめた記事。リポジトリの .claude/settings.json で有効化したプラグインはクラウドでは読み込まれず、claude.ai のアカウント側でブラウザから追加する必要がある。デスクトップアプリから追加するとローカルのみに反映され、クラウドでは使えない点も注意が必要。

- **ソース**: [Zenn claude](https://zenn.dev/i_shinya/articles/claude-code-cloud-plugins-pitfalls)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-21 | 自動生成 |
