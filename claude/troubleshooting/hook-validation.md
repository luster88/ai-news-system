---
title: Hook Validation
category: troubleshooting
subcategory: hook-validation
tags:
- bugfix
- claude-code
- setup
date: '2026-08-17'
updated: '2026-08-17'
sources:
- url: https://qiita.com/yurukusa/items/5e4e587f4ed5ea5f6cfc
  title: フックが正しい瞬間に走っているかを測る手順——909本中24本は別の瞬間に走る
  date: '2026-08-17'
---

# Hook Validation

---

## 2026-08-17

### フックが正しい瞬間に走っているかを測る手順——909本中24本は別の瞬間に走る

Claude Codeのフック909本を機械検査し、24本が誤った実行タイミングに登録されていることを発見。構文エラーは出ないが、PreToolUseとPostToolUseの設定ミスでlintが編集前に実行されるなど、意図しない挙動を引き起こしていた。フック内の複数箇所に記載された設定の食い違いから矛盾を検出し、スクリプトの出力内容や公式ドキュメントを参照して正しい設定を判定する手法を実践した記録。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/5e4e587f4ed5ea5f6cfc)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-17 | 自動生成 |
