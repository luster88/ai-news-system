---
title: Claude Code Permissions
category: troubleshooting
subcategory: claude-code-permissions
tags:
- bugfix
- claude-code
- performance
- setup
- windows
date: '2026-05-09'
updated: '2026-08-29'
sources:
- url: https://qiita.com/enomoso_pm/items/623bd77ce2bb89569e3d
  title: 「設定したのになぜ？」Claude Codeのパーミッションが効かない理由と、今すぐできる対策
  date: '2026-05-09'
- url: https://qiita.com/Tadahiro_Yamamura/items/400de8ecd549db2df7a3
  title: Claude Codeのパーミッションパターン、パスを含むと全滅しちゃう・・・
  date: '2026-05-11'
- url: https://zenn.dev/tsutomusaito/articles/permission-rules-decay-ja
  title: 許可ルールを152件ためこんでいた。完全一致で書かれた92件は、10万9762回の実行で一度も効かなかった
  date: '2026-08-29'
---



# Claude Code Permissions

---

## 2026-08-29

### 許可ルールを152件ためこんでいた。完全一致で書かれた92件は、10万9762回の実行で一度も効かなかった

Claude Code の permissions.allow に自動保存される完全一致の許可ルールは、実際には再利用されない形で蓄積されることが判明。10万9762回のコマンド実行に対して、完全一致形式の92件のルールは0回しか一致しなかった。一方、手動で追加した接頭辞ルール（:*形式）20件は47,559回一致し、実際に機能していた。完全一致ルールは定期的に削除し、必要なものは接頭辞形式で書き直すべきと結論。

- **ソース**: [Zenn claude](https://zenn.dev/tsutomusaito/articles/permission-rules-decay-ja)
- **重要度**: 7/10
- **タグ**: claude-code, setup, performance

---

## 2026-05-11

### Claude Codeのパーミッションパターン、パスを含むと全滅しちゃう・・・

Claude Codeのパーミッション自動承認機能において、ファイルパスを含むパターンが一切機能しないバグが報告されている。Windows環境で様々なパターン（引用符、スラッシュ、起動方法）を検証した結果、パスを含まない場合のみ動作することが判明。GitHub issue #30519で「2025年中頃から壊れている」と報告されており、修正待ちの状態。非インタラクティブモードとTUIで実行環境が異なる点も判明し、検証には手動確認が必要。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadahiro_Yamamura/items/400de8ecd549db2df7a3)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, windows

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
