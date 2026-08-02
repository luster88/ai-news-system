---
title: Long Context Tips
category: guides
subcategory: long-context-tips
tags:
- claude-api
- performance
- prompt
date: '2026-08-02'
updated: '2026-08-02'
sources:
- url: https://zenn.dev/every_ai_recipe/articles/long-context-changes-ai-ranking
  title: 提案書骨子の生成、参考資料が4000字を超えるとAIの順位が入れ替わる理由を検証した
  date: '2026-08-02'
---

# Long Context Tips

---

## 2026-08-02

### 提案書骨子の生成、参考資料が4000字を超えるとAIの順位が入れ替わる理由を検証した

提案書骨子生成タスクで、200字の短い参考資料では ChatGPT・Claude・Gemini がほぼ同スコアだったが、4000字の長い資料では Claude が最高点（14点）、ChatGPT が最低点（10点）となり順位が逆転した。Claude の100万トークンという大規模コンテキストウィンドウと実効的な参照能力の高さが、長文入力時の抜け漏れの少なさに直結した。ただし構成の論理性は章立てテンプレートの明示が別途必要で、長文対応力と構造化出力は独立した変数である。

- **ソース**: [Zenn claude](https://zenn.dev/every_ai_recipe/articles/long-context-changes-ai-ranking)
- **重要度**: 6/10
- **タグ**: claude-api, performance, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-02 | 自動生成 |
