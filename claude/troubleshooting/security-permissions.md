---
title: Security Permissions
category: troubleshooting
subcategory: security-permissions
tags:
- bugfix
- claude-code
- setup
date: '2026-04-02'
updated: '2026-04-02'
sources:
- url: https://qiita.com/asuka1975/items/6d13484a6755467cad63
  title: Claude CodeでRead(hoge)をdenyしても必ずしも読まれないとは限らない
  date: '2026-04-02'
---

# Security Permissions

---

## 2026-04-02

### Claude CodeでRead(hoge)をdenyしても必ずしも読まれないとは限らない

Claude Code のヘッドレスモードにおける権限設定の検証記事。Read(sample) を deny に設定しても、Bash(cat *) や Bash(cat s*) などワイルドカードを使った間接的な読み取りによって、秘匿情報が漏洩する可能性があることを実験で証明。ブラックリスト形式の deny 設定は不十分で、ホワイトリスト形式で個別ファイルのみを許可する必要があると結論付けている。100回の試行中、allow 設定次第で2回の情報漏洩が発生した。

- **ソース**: [Qiita claudecode](https://qiita.com/asuka1975/items/6d13484a6755467cad63)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
