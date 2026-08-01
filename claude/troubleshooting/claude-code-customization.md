---
title: Claude Code Customization
category: troubleshooting
subcategory: claude-code-customization
tags:
- claude-code
- setup
- 新機能
date: '2026-08-01'
updated: '2026-08-01'
sources:
- url: https://qiita.com/devex12/items/6d5dab6ec0613afa0c43
  title: 公式ドキュメントゼロ。Claude Codeの秘密テーマ機能を、grep -a十数回・10分のバイナリ解析だけで解明した話
  date: '2026-08-01'
---

# Claude Code Customization

---

## 2026-08-01

### 公式ドキュメントゼロ。Claude Codeの秘密テーマ機能を、grep -a十数回・10分のバイナリ解析だけで解明した話

Claude Code CLIに存在する非公開のカスタムテーマ機能を、grep -aによるバイナリ解析で10分で解明。ドキュメント未公開の機能でも、保存関数・ロード処理・値検証ロジックを芋づる式に追うことで仕様を再現できることを実証した。~/.claude/themes/配下にcustom:プレフィックス付きテーマファイルを作成し、baseテーマのキーをoverridesで上書きする仕組みが判明。

- **ソース**: [Qiita claudecode](https://qiita.com/devex12/items/6d5dab6ec0613afa0c43)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-01 | 自動生成 |
