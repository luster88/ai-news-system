---
title: Plugin Symlink
category: troubleshooting
subcategory: plugin-symlink
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

# Plugin Symlink

---

## 2026-05-02

### マルチエージェント対応のスキル配布、symlink で外出ししようとしたら踏んだ罠

Claude CodeとCodex CLIでスキルを共有するためにsymlinkで外部参照する構成を試みたが、Claude Codeのキャッシュ展開時にsymlinkを辿らないため、プラグインが認識されない問題が発生。解決策として、SKILL.mdの実体をpluginディレクトリ内に配置し、Codex側からsymlinkで参照する構成に変更することで、両エージェントでの動作を実現した。

- **ソース**: [Qiita claude](https://qiita.com/t-tonton/items/7dbee3180f34a72e12b6)
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
