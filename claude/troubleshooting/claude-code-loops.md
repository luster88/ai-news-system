---
title: Claude Code Loops
category: troubleshooting
subcategory: claude-code-loops
tags:
- claude-code
- performance
- prompt
date: '2026-06-26'
updated: '2026-06-26'
sources:
- url: https://qiita.com/yurukusa/items/f4f3e9ab0c02fe0b06b8
  title: Claude Codeで翻訳や文章校正をやらせると無限ループしてトークンを溶かす理由と、claude -p での回避策
  date: '2026-06-26'
---

# Claude Code Loops

---

## 2026-06-26

### Claude Codeで翻訳や文章校正をやらせると無限ループしてトークンを溶かす理由と、claude -p での回避策

Claude Codeで翻訳や文章校正を行うと無限ループでトークンを消費する問題について解説。原因はコード編集向けのエージェントループが文章作業に不向きなため。回避策として`claude -p`（非対話モード）で1ターン実行、または全文を一度に返すよう依頼する方法を紹介。コード作業にはエージェントループ、一発変換にはチャットや`-p`オプションが適している。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/f4f3e9ab0c02fe0b06b8)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-26 | 自動生成 |
