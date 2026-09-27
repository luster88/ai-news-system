---
title: Debugging Workflow
category: guides
subcategory: debugging-workflow
tags:
- claude-code
- prompt
date: '2026-09-27'
updated: '2026-09-27'
sources:
- url: https://zenn.dev/muranyanta/articles/sf-20260907-cb6319
  title: Claude Codeでデバッグログからバグの原因を特定する──AIが見落とす3つの落とし穴
  date: '2026-09-27'
---

# Debugging Workflow

---

## 2026-09-27

### Claude Codeでデバッグログからバグの原因を特定する──AIが見落とす3つの落とし穴

Claude CodeでSalesforce Apexのデバッグログを分析する際の実践的手法を解説。ログをそのまま貼り付けるだけではAIが誤った原因を示すため、前処理（ノイズ除去・関連セクション抽出）、プロンプト（検証条件の明示・判断不能の許容）、検証の3点が重要。ガバナ制限と論理エラーの区別、リリース差分による挙動変化への注意も必要。AIの回答は仮説として扱い、サンドボックスでの検証が不可欠。

- **ソース**: [Zenn claude](https://zenn.dev/muranyanta/articles/sf-20260907-cb6319)
- **重要度**: 6/10
- **タグ**: claude-code, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-27 | 自動生成 |
