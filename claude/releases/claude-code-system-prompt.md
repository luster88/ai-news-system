---
title: Claude Code System Prompt
category: releases
subcategory: claude-code-system-prompt
tags:
- claude-code
- prompt
- release
- setup
- 新機能
date: '2026-07-24'
updated: '2026-11-22'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1v5mhhl/anthropic_cut_80_of_claude_codes_system_prompt
  title: Anthropic cut 80% of Claude Code's system prompt for the Claude 5 models
    and published what should still go in your CLAUDE.md and skills
  date: '2026-07-24'
- url: https://qiita.com/NaokiIshimura/items/a75af610ec8c0d2ff699
  title: Claude Code 開発者が注目している5つのアップデート（v2.1.326 - v2.1.330）
  date: '2026-11-21'
- url: https://qiita.com/NaokiIshimura/items/0b054c35b3c8b8aa5796
  title: Claude Code v2.1.326 - v2.1.330 リリースノートまとめ
  date: '2026-11-21'
- url: https://ai-heartland.com/tool/claude-code-code-mode
  title: Claude Code Code Mode とは｜JavaScriptでツールを一括実行する仕組みと権限・Hooksの注意点
  date: '2026-11-22'
---



# Claude Code System Prompt

---

## 2026-11-22

### Claude Code Code Mode とは｜JavaScriptでツールを一括実行する仕組みと権限・Hooksの注意点

Claude Codeに実験機能としてCode Modeが追加された。複数のツール呼び出しをJavaScript 1本にまとめて並列実行・結果の絞り込みを行い、速度と文脈の節約を実現する。環境変数で有効化する必要があり、権限チェックやフックの動作がコード単位での判断に変わる点に注意が必要。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/claude-code-code-mode)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-11-21

### Claude Code 開発者が注目している5つのアップデート（v2.1.326 - v2.1.330）

Claude Code v2.1.326～v2.1.330の重要なアップデートを解説。Bashサンドボックスのセキュリティ強化により一部コマンドに確認が必要になり、CI環境では注意が必要。サードパーティプロバイダー経由のOpus/Sonnet 4.6でauto modeが利用可能になり、既定動作が変更。/code-reviewコマンドが刷新され、バグとCLAUDE.md違反に特化し、ラベル付けで優先度が明確化。

- **ソース**: [Qiita claude](https://qiita.com/NaokiIshimura/items/a75af610ec8c0d2ff699)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.326 - v2.1.330 リリースノートまとめ

Claude Code v2.1.326〜v2.1.330の更新内容。Bashサンドボックス・パーミッションチェック強化、Opus 4.6/Sonnet 4.6のauto modeをサードパーティプロバイダーで解禁、/code-reviewの出力形式刷新、Enterprise Admin Console管理組織へのサインイン対応、チャート描画mod「easel」追加。/loopとスケジュールタスクの実行期限が7日から30日に延長され、Code Mode周辺の大量の修正も含まれる。

- **ソース**: [Qiita claude](https://qiita.com/NaokiIshimura/items/0b054c35b3c8b8aa5796)
- **重要度**: 8/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code 開発者が注目している5つのアップデート（v2.1.326 - v2.1.330）

Claude Code v2.1.326～v2.1.330の5つの重要アップデートを解説。Bashサンドボックスのパーミッション強化により、CI環境での自動実行時に確認プロンプトが拒否になる可能性がある。サードパーティプロバイダー経由のOpus/Sonnet 4.6でauto modeが利用可能になり、既定動作が変更。/code-reviewコマンドが刷新され、バグとCLAUDE.md違反に特化し、PR番号指定時の挙動も改善された。

- **ソース**: [Qiita claudecode](https://qiita.com/NaokiIshimura/items/a75af610ec8c0d2ff699)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-24

### Anthropic cut 80% of Claude Code's system prompt for the Claude 5 models and published what should still go in your CLAUDE.md and skills

Anthropic が Claude 5 モデル向けに Claude Code のシステムプロンプトを 80% 削減し、CLAUDE.md とスキルに記載すべき内容を公開。「コメントを書くな」などのハードルールを廃止し、モデルの判断に委ねる方針に転換。ツール説明の例も新モデルでは制約となるため削減。単一の CLAUDE.md ではなく、必要時に読み込むファイルツリー構造を推奨。また、古いモデル向けルールを検出する /doctor コマンドを追加。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v5mhhl/anthropic_cut_80_of_claude_codes_system_prompt)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-24 | 自動生成 |
