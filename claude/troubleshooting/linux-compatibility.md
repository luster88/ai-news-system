---
title: Linux Compatibility
category: troubleshooting
subcategory: linux-compatibility
tags:
- bugfix
- claude-code
- linux
date: '2026-08-25'
updated: '2026-08-25'
sources:
- url: https://qiita.com/picnic/items/18a1cc9c54a77605c0ea
  title: 'Claude Code v2.1.245: glibc 2.44環境での起動クラッシュを修正'
  date: '2026-08-25'
---

# Linux Compatibility

---

## 2026-08-25

### Claude Code v2.1.245: glibc 2.44環境での起動クラッシュを修正

Claude Code v2.1.245が、glibc 2.44を採用するArch Linux、CachyOS、Fedora Rawhideなどのローリングリリース系Linuxディストリビューションで発生していた起動時クラッシュの不具合を修正しました。該当環境では以前のバージョンが完全に起動不能だったため、即時アップデートが必要です。CI/Dockerで固定バージョンを使用している場合は、最低バージョンの引き上げが推奨されます。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/18a1cc9c54a77605c0ea)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, linux

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-25 | 自動生成 |
