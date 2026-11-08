---
title: Security Leaks
category: troubleshooting
subcategory: security-leaks
tags:
- bugfix
- claude-code
- setup
date: '2026-07-20'
updated: '2026-11-08'
sources:
- url: https://qiita.com/yurukusa/items/cfa9b8ef2b37ce063473
  title: Claude Codeにgitを任せると.envやAPIキーが公開リポに上がるのか——無料フックがどこまで止めるかを終了コードで検証した
  date: '2026-07-20'
- url: https://ai-heartland.com/security/claude-settings-local-secrets
  title: Claude Codeの「Don’t ask again」で秘密が平文に｜settings.local.jsonの漏えいと確認手順
  date: '2026-11-08'
---


# Security Leaks

---

## 2026-11-08

### Claude Codeの「Don’t ask again」で秘密が平文に｜settings.local.jsonの漏えいと確認手順

Claude Codeの「Don't ask again」機能で承認したコマンドが引数ごと.claude/settings.local.jsonに平文保存され、パスワードやAPIキーを含むコマンドを承認するとそのまま記録される問題。Apiiroの調査で公開GitHubリポジトリ約18万件中1,994件で2,539の秘密情報が見つかった。git履歴の確認とローテーション、.gitignoreへの追加が必要。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/claude-settings-local-secrets)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

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
