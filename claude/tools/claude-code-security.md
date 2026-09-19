---
title: Claude Code Security
category: tools
subcategory: claude-code-security
tags:
- claude-code
- cowork
- setup
- 新機能
date: '2026-07-06'
updated: '2026-09-19'
sources:
- url: https://qiita.com/nogataka/items/4d2a551f89f6b4f94b01
  title: Claude Code の無料セキュリティ監査プラグインで脆弱性を自動検出・修正してみる
  date: '2026-07-06'
- url: https://zenn.dev/gorizawa/articles/claude-code-guard-delete-hook
  title: Claude Code の auto モードで rm -rf 事故を止める PreToolUse hook を書いた
  date: '2026-09-02'
- url: https://www.reddit.com/r/ClaudeAI/comments/1waoo5h/i_ported_toyotas_lean_quality_system_to_claude
  title: I ported Toyota's Lean quality system to Claude Code so the same agent mistakes
    stop coming back (MIT, free)
  date: '2026-09-08'
- url: https://ai-heartland.com/tool/claude-code-security-review-github-action
  title: Claude Code Security Reviewとは｜PRを自動で守るGitHub Actionを実測
  date: '2026-09-17'
- url: https://ai-heartland.com/tool/ai-job-search
  title: ai-job-searchとは｜Claude Code求職OSSは日本語で使えるか、CVのLaTeX日本語化まで実機検証
  date: '2026-09-17'
- url: https://zenn.dev/zutto_nemutai/articles/fafa00f2a1b800
  title: 概念図・ER図・画面を1つのデータから描く「モデルキャンバス」を自作した
  date: '2026-09-19'
---






# Claude Code Security

---

## 2026-09-19

### 概念図・ER図・画面を1つのデータから描く「モデルキャンバス」を自作した

Claude Code を活用して、YAML ベースのモデル定義から概念図・ER図・画面モックを単一キャンバスで表示する「モデルキャンバス」を自作。ビュー間で選択状態が持続し、影響範囲を視覚的に把握できる。Skill 機能で生成フローを標準化し、実案件で 120 テーブルの ER 図を drawio HTML 形式から読み込み、コア 20 ノードに絞り込んで運用。

- **ソース**: [Zenn claude](https://zenn.dev/zutto_nemutai/articles/fafa00f2a1b800)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-09-17

### ai-job-searchとは｜Claude Code求職OSSは日本語で使えるか、CVのLaTeX日本語化まで実機検証

ai-job-searchは、Claude Codeを求職アシスタントに変えるOSSフレームワーク（GitHubスター42.4k）です。求人収集から採点、CV・カバーレター生成、PDF検証、面接準備まで自動化します。日本語での利用は基本的に可能ですが、LaTeXの日本語出力が無言で壊れるため、luatexja-fontspecの追加が必要です。プロンプトとルールの集合として設計され、12個のコマンドと2個のスキルで求職ループを回します。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/ai-job-search)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 2026-09-17

### Claude Code Security Reviewとは｜PRを自動で守るGitHub Actionを実測

Anthropic公式のGitHub Action「Claude Code Security Review」の詳細解説。PRごとに自動でセキュリティ脆弱性を検出し、インジェクション・認証不備・秘密情報のハードコードなど10カテゴリを診断。CLIの/security-reviewコマンドと同機能をCI/CDで実行できる。最終更新は2026年2月で約7ヶ月更新なし、プロンプトインジェクション対策は未実装で信頼できるPRのみが前提。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/claude-code-security-review-github-action)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 2026-09-08

### I ported Toyota's Lean quality system to Claude Code so the same agent mistakes stop coming back (MIT, free)

製造業のリーン生産方式（トヨタのAndonシステム）をClaude Codeに適用したツールの紹介。エージェントが同じミスを繰り返さないよう、失敗をログ化し対策を講じる仕組み。特に「done」「shipped」等の発言時に検証エビデンスをチェックするStopフックが有用。MIT ライセンスでGitHub公開。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1waoo5h/i_ported_toyotas_lean_quality_system_to_claude)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-09-02

### Claude Code の auto モードで rm -rf 事故を止める PreToolUse hook を書いた

Claude Codeのautoモードで危険なrm -rfコマンドを自動実行されるリスクに対処するため、PreToolUse hookを使った削除コマンド監視ツールを実装。allow/ask/denyの3段階判定で、危険な削除は阻止し、判断が必要なものは人間に確認を求める。shlex によるトークン化でコマンド判定の精度を高め、保護ディレクトリの設定や fail-closed 設計で安全性を確保している。

- **ソース**: [Zenn claude](https://zenn.dev/gorizawa/articles/claude-code-guard-delete-hook)
- **重要度**: 7/10
- **タグ**: claude-code, setup

---

## 2026-07-06

### Claude Code の無料セキュリティ監査プラグインで脆弱性を自動検出・修正してみる

Anthropic が Claude Code 向けに公式セキュリティプラグイン security-guidance を公開。ファイル編集時・ターン終了時・コミット時の3層で脆弱性を自動検出し、AI による修正まで可能。社内ベンチマークではセキュリティコメントが 30-40% 減少。AI が大量コード生成する時代に、生成と検査の距離を縮めることで構造的な脆弱性を早期に潰す設計。従来の SAST ツールとの併用や封じ込め設計の考慮が推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/nogataka/items/4d2a551f89f6b4f94b01)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-06 | 自動生成 |
