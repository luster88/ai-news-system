---
title: Security Practices
category: guides
subcategory: security-practices
tags:
- claude-code
- setup
date: '2026-04-26'
updated: '2026-04-26'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/5b10c4042a9a382b6554
  title: Claude CodeにAPIキーが丸見え？.claudeignoreで守る実践ガイド
  date: '2026-04-26'
---

# Security Practices

---

## 2026-04-26

### Claude CodeにAPIキーが丸見え？.claudeignoreで守る実践ガイド

Claude Codeでは.gitignoreが効かず、.envなどのシークレットファイルがAIに読まれるリスクがある。対策として、settings.jsonのpermissions.denyで読み取りを拒否し、PreToolUse hookで二重にブロックする「多層防御」を実装。加えて、本番キーは.envに置かず1Password CLIなどから動的注入する設計が推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/5b10c4042a9a382b6554)
- **重要度**: 7/10
- **タグ**: claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-26 | 自動生成 |
