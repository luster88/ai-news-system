---
title: Ai Cowork Tips
category: guides
subcategory: ai-cowork-tips
tags:
- claude-code
- cowork
date: '2026-05-19'
updated: '2026-05-19'
sources:
- url: https://zenn.dev/yosiki/articles/chrome-extension-ai-agent-bug-loop
  title: AIと二人三脚でChrome拡張を作ったら、同じバグを何度も直す羽目になった
  date: '2026-05-19'
---

# Ai Cowork Tips

---

## 2026-05-19

### AIと二人三脚でChrome拡張を作ったら、同じバグを何度も直す羽目になった

Chrome拡張開発でClaude Sonnet 4とCodexを併用した際、AIに「完了の定義」を明文化しなかったため同じバグを繰り返し修正する事態に。JestとChromeの動作差異、Manifest V3のService Worker制約、DOMツリーの違いなど、テストでは検出できない問題が多発。最終的にagent-handoff.mdとAI.mdに完了条件を具体的に記述することで解決した実践例。

- **ソース**: [Zenn claude](https://zenn.dev/yosiki/articles/chrome-extension-ai-agent-bug-loop)
- **重要度**: 6/10
- **タグ**: claude-code, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-19 | 自動生成 |
