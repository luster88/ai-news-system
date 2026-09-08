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
updated: '2026-09-08'
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
---



# Claude Code Security

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
