---
title: Credential Leak
category: troubleshooting
subcategory: credential-leak
tags:
- bugfix
- claude-code
- setup
date: '2026-06-28'
updated: '2026-06-28'
sources:
- url: https://qiita.com/yurukusa/items/c2fdcf5c0be30929b686
  title: AIに「公開して」と頼んだら、認証情報まで一緒に公開されていた——deploy --dir=. の落とし穴と多層防御
  date: '2026-06-28'
---

# Credential Leak

---

## 2026-06-28

### AIに「公開して」と頼んだら、認証情報まで一緒に公開されていた——deploy --dir=. の落とし穴と多層防御

Claude Codeに「Netlifyに公開して」と依頼した際、`netlify deploy --dir=.`により認証情報を含む全ファイルが公開された事故事例。HTML以外のconfig.pyに含まれるGmailパスワードとAPIキーが世界中に公開され、再デプロイでは対処不可。対策として秘密ファイルの配置場所の見直し、.netlifyignore の活用、PreToolUseフックによる事前検証が必要。AIコーディングの事故は「成功の顔をした静かな失敗」として現れることが多い。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/c2fdcf5c0be30929b686)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-28 | 自動生成 |
