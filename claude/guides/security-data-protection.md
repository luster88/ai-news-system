---
title: Security Data Protection
category: guides
subcategory: security-data-protection
tags:
- claude-code
- setup
- 新機能
date: '2026-07-21'
updated: '2026-07-21'
sources:
- url: https://qiita.com/masa_ClaudeCodeLab/items/db2b4a543aa47e94d150
  title: Claude Code/Codexに顧客データを渡す前に止める：Node.jsで作る個人情報プリフライト検査
  date: '2026-07-21'
---

# Security Data Protection

---

## 2026-07-21

### Claude Code/Codexに顧客データを渡す前に止める：Node.jsで作る個人情報プリフライト検査

Claude CodeやCodexに顧客データを渡す前に、Node.jsで個人情報を自動検査する仕組みを解説。氏名、メールアドレス、電話番号などを正規表現でスキャンし、検出時は処理を停止。原本と作業コピーを分離し、AIには匿名化済みデータのみを渡す運用を推奨。package.jsonへの検査コマンド追加や、業務ごとの禁止項目カスタマイズ方法も紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/masa_ClaudeCodeLab/items/db2b4a543aa47e94d150)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-21 | 自動生成 |
