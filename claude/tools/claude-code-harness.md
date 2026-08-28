---
title: Claude Code Harness
category: tools
subcategory: claude-code-harness
tags:
- claude-code
- mcp
- performance
- prompt
- setup
- 新機能
date: '2026-04-14'
updated: '2026-08-28'
sources:
- url: https://ai-heartland.com/ai/claude/code-harness
  title: Claude Code Harness：Claudeのコード実行を安全に制御するOSSツール
  date: '2026-04-14'
- url: https://ai-heartland.com/explain/effective-html-claude-code-skills
  title: effective-htmlとは｜Claude Code・Codexでワイヤーフレーム/プロトタイプを作る6スキルの使い方
  date: '2026-08-27'
- url: https://ai-heartland.com/explain/avoid-ai-writing-japanese-test
  title: AIっぽい文章を機械で消すOSSスキル avoid-ai-writing｜日本語で実測したら検出器が動かず
  date: '2026-08-28'
- url: https://ai-heartland.com/tool/claude-seo-claude-code-seo-audit
  title: claude-seoとは｜Claude Code SEO監査25スキルを日本語サイトで実測した結果と限界
  date: '2026-08-28'
---



# Claude Code Harness

---

## 2026-08-28

### AIっぽい文章を機械で消すOSSスキル avoid-ai-writing｜日本語で実測したら検出器が動かず

AIが生成した文章の型を検出・修正するOSSスキル「avoid-ai-writing」を日本語で実測した記事。スキルは指示書(SKILL.md)と検出エンジン(patterns.js)の2部構成だが、検出エンジンは日本語を空白区切りで語数カウントするため機能せず、指示書側のみが日本語の「XではなくY」構文などを検出可能。Claude Codeなどで動作し、発火確認は--output-format stream-jsonで行う。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/avoid-ai-writing-japanese-test)
- **重要度**: 5/10
- **タグ**: claude-code, prompt, setup

---

### claude-seoとは｜Claude Code SEO監査25スキルを日本語サイトで実測した結果と限界

claude-seoはClaude Codeに25スキルと18サブエージェントを追加するOSSのSEO監査ツール。日本語サイトでの実測では構造化データ検証やリンク構造分析は機能するが、コンテンツ品質スコアは英語専用トークナイザのため日本語本文を評価できない。実装は判断をLLMに任せ、決定的計算のみPythonで処理する設計。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/claude-seo-claude-code-seo-audit)
- **重要度**: 6/10
- **タグ**: claude-code, setup

---

## 2026-08-27

### effective-htmlとは｜Claude Code・Codexでワイヤーフレーム/プロトタイプを作る6スキルの使い方

effective-htmlは、Claude CodeやCodexでHTMLを生成する際に「粒度のブレ」を防ぐための6つのスキル集です。ワイヤーフレーム、プロトタイプ、図表など目的別に分業させることで、意図しない完成度の成果物が返ってくる問題を解決します。GitHubスター2,062、MIT ライセンスで公開されており、ビルド不要の単一HTMLファイルとして動作する点が特徴です。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/effective-html-claude-code-skills)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, prompt

---

## 2026-04-14

### Claude Code Harness：Claudeのコード実行を安全に制御するOSSツール

Claude Code Harness v4.0「Hokage」は、Claude Codeのtool call実行を高速化・安全化するOSSツール。Go Native設計により、従来のNode.js+bashスタックから単一バイナリ化し、tool callオーバーヘッドを40-60msから10msへ劇的に短縮。5つの動詞スキル（plan/test/code/review/work）により、計画から実装・検証・リリースまでの統合ワークフローを提供し、セキュリティ機構と並列開発機能を備える。

- **ソース**: [AI Heartland](https://ai-heartland.com/ai/claude/code-harness)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-14 | 自動生成 |
