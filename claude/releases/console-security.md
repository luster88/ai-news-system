---
title: Console Security
category: releases
subcategory: console-security
tags:
- claude-api
- claude-console
- 新機能
date: '2026-10-23'
updated: '2026-10-23'
sources:
- url: https://qiita.com/picnic/items/2e6773bdaa4cc420a11a
  title: Claude Consoleで組織単位のweb fetch無効化とドメイン制限が可能に|400エラー対策
  date: '2026-10-23'
---

# Console Security

---

## 2026-10-23

### Claude Consoleで組織単位のweb fetch無効化とドメイン制限が可能に|400エラー対策

Claude Consoleに組織単位でweb fetch機能を無効化し、ドメインの許可・ブロックリストを設定できる機能が追加されました。web fetchをオフにすると、該当ツールを含むMessages APIリクエストが400エラーになる破壊的変更が含まれるため、既存アプリへの影響に注意が必要です。Managed Agentsのweb_fetchとweb_searchも組織のドメイン制限に従うようになり、エージェント側とConsole側の両方の設定を満たす必要があります。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/2e6773bdaa4cc420a11a)
- **重要度**: 8/10
- **タグ**: claude-console, claude-api, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-23 | 自動生成 |
