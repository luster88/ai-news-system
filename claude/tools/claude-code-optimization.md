---
title: Claude Code Optimization
category: tools
subcategory: claude-code-optimization
tags:
- claude-code
- mcp
- performance
- prompt
- 新機能
date: '2026-03-30'
updated: '2026-08-25'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s7qu07/i_built_a_universal_claudemd_that_cuts_claude
  title: I built a universal CLAUDE.md that cuts Claude output tokens by 63% - validated
    with benchmarks, fully open source
  date: '2026-03-30'
- url: https://qiita.com/Anuj7411/items/e4138b830bde92e85115
  title: 自分の「Claude Code」ツールが、無駄になったトークンの数を83倍も過小評価していたことに気づいた経緯
  date: '2026-06-23'
- url: https://qiita.com/tomada/items/46e675f6ced44dcd10ad
  title: トークン浪費と性能低下を防ぐ、Claude Code の自動引き継ぎ hook を作った
  date: '2026-08-07'
- url: https://qiita.com/inoyu-qiita/items/5b36829f86d1d85a1ab7
  title: 丁寧すぎるClaude Codeを原始人にしたら、トークン使用量が3割減った
  date: '2026-08-25'
---




# Claude Code Optimization

---

## 2026-08-25

### 丁寧すぎるClaude Codeを原始人にしたら、トークン使用量が3割減った

Claude Codeの丁寧すぎる返答を簡潔化するプラグイン「genshijin」の紹介記事。敬語や前置きを削減することで、トークン使用量を約3割削減できた実験結果を報告。日本語特有の冗長表現（承知いたしました、〜させていただきますなど）を削りつつ、技術的内容は保持する設計。3段階のモード切り替えが可能で、公式プラグインディレクトリから簡単にインストールできる。

- **ソース**: [Qiita claude](https://qiita.com/inoyu-qiita/items/5b36829f86d1d85a1ab7)
- **重要度**: 6/10
- **タグ**: claude-code, performance, prompt

---

## 2026-08-07

### トークン浪費と性能低下を防ぐ、Claude Code の自動引き継ぎ hook を作った

Claude Code のコンテキスト使用率が25%を超えると自動で引き継ぎノートを生成する hook スクリプトの実装例。長いセッションでの性能低下とトークン浪費を防ぐため、Stop hook と statusLine を組み合わせて使用率を監視し、Claude 自身に区切りを判断させる仕組みを構築。手動での /compact や区切り操作に頼らず、自動化により料金コストと性能劣化の両方に対処する。

- **ソース**: [Qiita claude](https://qiita.com/tomada/items/46e675f6ced44dcd10ad)
- **重要度**: 7/10
- **タグ**: claude-code, performance, 新機能

---

### トークン浪費と性能低下を防ぐ、Claude Code の自動引き継ぎ hook を作った

Claude Codeで長時間セッション時にコンテキスト使用率が膨らみ性能が低下する問題に対し、hookとstatusLineを使って自動的に引き継ぎを判断・実行させる仕組みを実装。使用率25%で発動し、Claude自身に継続か引き継ぎかを判断させてノートを生成させることで、トークン消費と性能低下を防ぐ。

- **ソース**: [Qiita claudecode](https://qiita.com/tomada/items/46e675f6ced44dcd10ad)
- **重要度**: 7/10
- **タグ**: claude-code, performance, 新機能

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
