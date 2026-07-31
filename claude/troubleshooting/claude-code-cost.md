---
title: Claude Code Cost
category: troubleshooting
subcategory: claude-code-cost
tags:
- claude-code
- performance
- pricing
date: '2026-07-31'
updated: '2026-07-31'
sources:
- url: https://zenn.dev/craftcode/articles/claude-code-token-cost
  title: Claude Codeを1回呼ぶと29,000トークン積まれる。プロンプトを削っても無駄だった
  date: '2026-07-31'
---

# Claude Code Cost

---

## 2026-07-31

### Claude Codeを1回呼ぶと29,000トークン積まれる。プロンプトを削っても無駄だった

Claude Codeを呼び出すと、プロンプトの長さに関わらず約29,000トークンの固定コストが発生する。CLAUDE.mdを削除してもコストはほぼ変わらず、効果的なのは「複数の処理を1回にまとめる」こと（15件まとめで93%削減）と「適切な場面でモデルを下げる」ことの2つ。ただしHaikuへの変更は、要約・判定タスクでは問題ないが、キャラクター性が求められる応答では質が落ちる可能性がある。

- **ソース**: [Zenn claude](https://zenn.dev/craftcode/articles/claude-code-token-cost)
- **重要度**: 7/10
- **タグ**: claude-code, pricing, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-31 | 自動生成 |
