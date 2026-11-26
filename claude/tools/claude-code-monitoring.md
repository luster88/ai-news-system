---
title: Claude Code Monitoring
category: tools
subcategory: claude-code-monitoring
tags:
- claude-code
- cowork
- mac
- prompt
- setup
- vscode
- windows
date: '2026-07-12'
updated: '2026-11-26'
sources:
- url: https://ai-heartland.com/explain/claude-code-monitor
  title: Claude Code Monitor徹底解説｜複数セッションをTUI＋スマホで一括監視【OSS】
  date: '2026-07-12'
- url: https://www.reddit.com/r/ClaudeAI/comments/1x7o895/i_built_a_free_windows_widget_for_claude_usage
  title: I built a free Windows widget for Claude usage limits with Claude Code —
    pixel Clawd reacts to your sessions
  date: '2026-10-17'
- url: https://qiita.com/kataru_kotonoha/items/32c07a5b9b5e8dadef12
  title: Claude Codeを何個並べても迷わない ― フックで全セッションを見張り、離席中はLINEで知らせる自作ツール「cc-monitor」の仕組み
  date: '2026-11-26'
---



# Claude Code Monitoring

---

## 2026-11-26

### Claude Codeを何個並べても迷わない ― フックで全セッションを見張り、離席中はLINEで知らせる自作ツール「cc-monitor」の仕組み

Claude Codeの複数セッションを監視し、ユーザー待ちや完了状態をLINEで通知する自作ツール「cc-monitor」の実装解説。フックを使って全イベントを収集し、background_tasksの扱いや質問判定の工夫、非同期処理の設計などの技術的課題と解決策を詳述。

- **ソース**: [Qiita claudecode](https://qiita.com/kataru_kotonoha/items/32c07a5b9b5e8dadef12)
- **重要度**: 6/10
- **タグ**: claude-code, vscode, prompt

---

## 2026-10-17

### I built a free Windows widget for Claude usage limits with Claude Code — pixel Clawd reacts to your sessions

コミュニティメンバーがClaude Codeを使用して、Claudeの使用制限を監視するWindows用の無料ウィジェットを開発しました。このツールは現在のセッション、週間制限、Fableの制限を1分ごとに更新表示し、実行中のClaude Codeセッションの状態、Anthropicのサービスステータス、アップデート情報を提供します。PowerShell 5.1とWPFで構築され、トークンを消費せずに`claude -p "/usage"`コマンドでサーバー側のデータを取得します。ピクセルアートのキャラクター「Clawd」がセッション状態に応じてアニメーションで反応する機能も実装されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1x7o895/i_built_a_free_windows_widget_for_claude_usage)
- **重要度**: 6/10
- **タグ**: claude-code, windows, cowork

---

## 2026-07-12

### Claude Code Monitor徹底解説｜複数セッションをTUI＋スマホで一括監視【OSS】

Claude Code Monitorは、複数のClaude Codeセッションを1つのターミナルUIとスマホブラウザから一括監視・操作できるmacOS向けOSSツール。実行中・許可待ち・完了を色分け表示し、1〜9キーで対象端末へ即座にフォーカス可能。サーバレス設計でAppleScriptによる端末制御を実現し、Tailscale経由でのリモート監視にも対応。npx claude-code-monitorで即座に試用でき、並行作業時の「見えない待ち時間」問題を解決する。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-monitor)
- **重要度**: 7/10
- **タグ**: claude-code, setup, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-12 | 自動生成 |
