---
title: Claude Code Performance
category: troubleshooting
subcategory: claude-code-performance
tags:
- bugfix
- claude-code
- performance
- pricing
date: '2026-04-11'
updated: '2026-10-07'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1sifepi/amd_ai_directors_analysis_confirms_lobotomization
  title: AMD AI directors analysis confirms lobotomization of Claude
  date: '2026-04-11'
- url: https://www.reddit.com/r/ClaudeAI/comments/1wzhbfc/56_of_my_claude_code_usage_was_claude_rereading
  title: 56% of my Claude Code usage was Claude re-reading the conversation
  date: '2026-10-07'
---


# Claude Code Performance

---

## 2026-10-07

### 56% of my Claude Code usage was Claude re-reading the conversation

Claude Code の6ヶ月間の利用分析により、API料金の56%が会話の再読み込みに費やされ、実際の有用な作業は20%のみだったことが判明。ユーザーは `/clear` コマンドの活用と自動コンパクト化の設定変更（`CLAUDE_CODE_AUTO_COMPACT_WINDOW: 200000`）を試行中。毎回のコンテキスト再送信により、約半数の呼び出しで20万トークン以上が消費されている点が課題。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wzhbfc/56_of_my_claude_code_usage_was_claude_rereading)
- **重要度**: 7/10
- **タグ**: claude-code, performance, pricing

---

## 2026-04-11

### AMD AI directors analysis confirms lobotomization of Claude

AMDのAI部門ディレクターStella Laurenzoが、Claude Codeのパフォーマンス劣化を詳細に分析したGitHub issueを公開。約7,000セッションの分析により、3月以降コード読み込みが3分の1に減少し、ファイル全体の書き換えが2倍に増加、タスク放棄率も上昇したことが判明。Anthropicが3月に実施した思考プロセスの非表示化（100%→0%）が原因とされ、AMDチームは既に競合ツールへ移行済み。Laurenzoは思考プロセスの可視化復元とプレミアム階層の導入を提案している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1sifepi/amd_ai_directors_analysis_confirms_lobotomization)
- **重要度**: 8/10
- **タグ**: claude-code, performance, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-11 | 自動生成 |
