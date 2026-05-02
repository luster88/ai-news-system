---
title: Plugin Installation
category: troubleshooting
subcategory: plugin-installation
tags:
- bugfix
- claude-code
- setup
date: '2026-05-02'
updated: '2026-05-02'
sources:
- url: https://qiita.com/t-tonton/items/7dbee3180f34a72e12b6
  title: マルチエージェント対応のスキル配布、symlink で外出ししようとしたら踏んだ罠
  date: '2026-05-02'
---

# Plugin Installation

---

## 2026-05-02

### マルチエージェント対応のスキル配布、symlink で外出ししようとしたら踏んだ罠

Claude CodeとCodex CLIでスキルを共有するためsymlinkで外部ディレクトリを参照したところ、Claude Codeのキャッシュ機構がsymlinkを辿らず、プラグインが認識されない問題が発生。Claude Codeは~/.claude/plugins/cache/にコピー展開する際、プラグインディレクトリ外のファイルを無視する仕様のため、symlink先が空になる。解決策として、スキル本体をpluginディレクトリ内に実体配置し、Codex側からsymlinkで参照する構成に変更した。

- **ソース**: [Qiita claudecode](https://qiita.com/t-tonton/items/7dbee3180f34a72e12b6)
- **重要度**: 6/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-02 | 自動生成 |
