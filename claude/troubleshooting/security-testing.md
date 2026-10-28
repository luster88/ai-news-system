---
title: Security Testing
category: troubleshooting
subcategory: security-testing
tags:
- bugfix
- claude-code
- sonnet
date: '2026-10-28'
updated: '2026-10-28'
sources:
- url: https://zenn.dev/utsumi/articles/079faa1ab9e564
  title: テスト315本・カバレッジ98.85%のCLIに、AIの攻撃役が見つけたHIGH 4件
  date: '2026-10-28'
---

# Security Testing

---

## 2026-10-28

### テスト315本・カバレッジ98.85%のCLIに、AIの攻撃役が見つけたHIGH 4件

Claude Codeで構築したWordPressエクスポートCLI（テスト315本・カバレッジ98.85%）を、AI攻撃役エージェントで診断した結果、HIGH 4件・MEDIUM 20件・LOW 8件の脆弱性が発見された。空白文字のパスワード判定ミス、競合状態でのパストラバーサル（3000回中399回成功）、ハードリンク経由のファイル漏洩など、通常のテストでは見逃される問題が明らかになった。各脆弱性はSonnetエージェントが攻撃・修正・回帰テスト追加を自動実行し、指揮役エージェントが再現確認することで対処された。

- **ソース**: [Zenn claude](https://zenn.dev/utsumi/articles/079faa1ab9e564)
- **重要度**: 7/10
- **タグ**: claude-code, sonnet, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-28 | 自動生成 |
