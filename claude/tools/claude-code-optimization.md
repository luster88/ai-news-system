---
title: Claude Code Optimization
category: tools
subcategory: claude-code-optimization
tags:
- claude-code
- mcp
- performance
- prompt
date: '2026-03-30'
updated: '2026-06-23'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s7qu07/i_built_a_universal_claudemd_that_cuts_claude
  title: I built a universal CLAUDE.md that cuts Claude output tokens by 63% - validated
    with benchmarks, fully open source
  date: '2026-03-30'
- url: https://qiita.com/Anuj7411/items/e4138b830bde92e85115
  title: 自分の「Claude Code」ツールが、無駄になったトークンの数を83倍も過小評価していたことに気づいた経緯
  date: '2026-06-23'
---


# Claude Code Optimization

---

## 2026-06-23

### 自分の「Claude Code」ツールが、無駄になったトークンの数を83倍も過小評価していたことに気づいた経緯

Claude Codeの長時間セッションで動作が遅くなる原因は、同じファイルの重複読み込みと詳細なツール出力の蓄積によるコンテキストウィンドウの肥大化。著者は重複排除とツール出力制限を行うオープンソースCLI「Sipcode」を開発し、ベンチマークで62%のツール出力削減を達成。開発過程で自ツールが83倍も過小評価していたバグを発見し、トランスクリプト走査による遡及的キャッシュ構築で修正。トークン節約よりもクリーンなコンテキストによる品質向上が真の目的。

- **ソース**: [Qiita claudecode](https://qiita.com/Anuj7411/items/e4138b830bde92e85115)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, performance

---

## 2026-03-30

### I built a universal CLAUDE.md that cuts Claude output tokens by 63% - validated with benchmarks, fully open source

コミュニティメンバーがClaude Codeの冗長な出力を削減するユニバーサルCLAUDE.mdファイルを開発。プロジェクトルートに配置するだけで、「You're absolutely right!」などの定型文、絵文字、不要な提案を排除し、トークン数を平均63%削減することに成功。ベンチマークで検証済みで完全オープンソース。Claude自身を使って開発されたツールという点でもユニーク。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s7qu07/i_built_a_universal_claudemd_that_cuts_claude)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-30 | 自動生成 |
