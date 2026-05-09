---
title: Claude Code Permissions
category: troubleshooting
subcategory: claude-code-permissions
tags:
- bugfix
- claude-code
- setup
date: '2026-05-09'
updated: '2026-05-09'
sources:
- url: https://qiita.com/enomoso_pm/items/623bd77ce2bb89569e3d
  title: 「設定したのになぜ？」Claude Codeのパーミッションが効かない理由と、今すぐできる対策
  date: '2026-05-09'
---

# Claude Code Permissions

---

## 2026-05-09

### 「設定したのになぜ？」Claude Codeのパーミッションが効かない理由と、今すぐできる対策

Claude Codeのパーミッション設定が動作しないのは、コマンド全体を文字列マッチしているためで、公式も認識する既知のバグ。GitHub上で30件以上のIssueが報告されている。解決策として、PreToolUse Hooksを使い、PythonスクリプトまたはRust製ライブラリで事前判定する方法が海外コミュニティで定着している。Permissionsは利便性、Hooksは安全確保という使い分けが推奨される。

- **ソース**: [Qiita claude](https://qiita.com/enomoso_pm/items/623bd77ce2bb89569e3d)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-09 | 自動生成 |
