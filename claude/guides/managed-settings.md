---
title: Managed Settings
category: guides
subcategory: managed-settings
tags:
- claude-code
- cowork
- setup
date: '2026-10-18'
updated: '2026-10-18'
sources:
- url: https://qiita.com/joinclass/items/39af023f21dbf4cb9e53
  title: Claude Codeの managed-settings.d で「消せない組織ルール」をファイル分割して配布する
  date: '2026-10-18'
---

# Managed Settings

---

## 2026-10-18

### Claude Codeの managed-settings.d で「消せない組織ルール」をファイル分割して配布する

Claude Codeの自動化運用でgit force pushによる事故を経験した企業が、CLAUDE.mdではなくmanaged-settings.dを使って「上書き不可能な組織ルール」を実装する方法を解説。複数のJSONファイルに分割して配布することで、チームごとの独立更新が可能になり、permissions.denyで危険なコマンドを強制的にブロックできる。実際の配布スクリプトと検証手順、よくある落とし穴まで網羅。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/39af023f21dbf4cb9e53)
- **重要度**: 7/10
- **タグ**: claude-code, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-18 | 自動生成 |
