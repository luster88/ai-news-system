---
title: Security Leaks
category: troubleshooting
subcategory: security-leaks
tags:
- bugfix
- claude-code
- setup
date: '2026-07-20'
updated: '2026-07-20'
sources:
- url: https://qiita.com/yurukusa/items/cfa9b8ef2b37ce063473
  title: Claude Codeにgitを任せると.envやAPIキーが公開リポに上がるのか——無料フックがどこまで止めるかを終了コードで検証した
  date: '2026-07-20'
---

# Security Leaks

---

## 2026-07-20

### Claude Codeにgitを任せると.envやAPIキーが公開リポに上がるのか——無料フックがどこまで止めるかを終了コードで検証した

Claude Codeで git コミット・プッシュを任せる際、.envファイルやAPIキーが公開リポジトリに漏洩するリスクを検証。無料の安全フック cc-safe-setup (secret-guard) の npm公開版29.8.0を実測した結果、直接的な `git add .env` や `git add .` は終了コード2で停止するが、コマンドの連結形式や `git commit`/`git push` は素通り（終了コード0）することを確認。フックは字面の先頭一致で判定するため構造的な限界があり、真の予防は .gitignore への登録と追跡状態の確認が本丸であることを強調。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/cfa9b8ef2b37ce063473)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-20 | 自動生成 |
