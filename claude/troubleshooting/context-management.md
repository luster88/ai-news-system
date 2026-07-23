---
title: Context Management
category: troubleshooting
subcategory: context-management
tags:
- claude-code
- claude-console
- cowork
- mcp
- performance
- prompt
- vscode
date: '2026-04-02'
updated: '2026-07-23'
sources:
- url: https://qiita.com/MirabelleQuest/items/f3b27e9740d4b22135fc
  title: '# Claude Code でセッション開始直後から Context 使用率が高かったので確認した'
  date: '2026-04-02'
- url: https://qiita.com/monakai/items/8a7721f4f6bef54707da
  title: 素人が一人でゲーム開発を始めて、何度も失敗した話 ②コンテキスト量なんて概念はありませんでした
  date: '2026-04-25'
- url: https://www.reddit.com/r/ClaudeAI/comments/1v4f6cw/when_to_compact
  title: When to Compact?
  date: '2026-07-23'
---



# Context Management

---

## 2026-07-23

### When to Compact?

Claude初心者が、コンテキストをいつコンパクト化すべきかについて質問。50k、100k、200k、500kなど様々な情報があり混乱している。文書処理作業で3-400kまでコンテキストが増え、いつClaudeがミスをするか不安を感じている。大量の文書やExcelファイルを扱う業務でClaude（max 20トークン）を活用しているが、コンパクト化のタイミングに関するベストプラクティスを求めている。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v4f6cw/when_to_compact)
- **重要度**: 4/10
- **タグ**: claude-console, performance, cowork

---

## 2026-04-25

### 素人が一人でゲーム開発を始めて、何度も失敗した話 ②コンテキスト量なんて概念はありませんでした

個人ゲーム開発でClaudeのプロジェクト機能を使用中、手順欄に大量の情報を詰め込んだ結果、コンテキスト量の急激な消費に直面した体験談。1回の返答で週間制限が9%進む事態に焦り、チャット間参照や手順欄の整理を試みるも効果が薄く、最終的にトークン節約の重要性を学んだ。AIは明示的に指示しない限りトークン節約より精度・効率向上を優先する傾向があることも発見した。

- **ソース**: [Qiita claude](https://qiita.com/monakai/items/8a7721f4f6bef54707da)
- **重要度**: 6/10
- **タグ**: claude-console, prompt, cowork

---

## 2026-04-02

### # Claude Code でセッション開始直後から Context 使用率が高かったので確認した

Claude Code のセッション開始直後に Context 使用率が 40% を超えていた原因を調査したところ、MCP Tools が大きな割合を占めていることが判明。MCP サーバーの有効/無効の切り替えは、セッション開始時点で読み込まれたツール定義に影響し、途中で変更しても即座には反映されない挙動を確認。不要な MCP 接続を外してからセッションを開始することで、初期 Context 使用率を抑えられることがわかった。

- **ソース**: [Qiita claudecode](https://qiita.com/MirabelleQuest/items/f3b27e9740d4b22135fc)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, vscode

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
