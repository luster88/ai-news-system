---
title: Claude Code Cli
category: guides
subcategory: claude-code-cli
tags:
- claude-code
- performance
- prompt
- setup
- 新機能
date: '2026-05-06'
updated: '2026-05-13'
sources:
- url: https://zenn.dev/tbnet/articles/claude-code-headless-text-output
  title: Claude Code の claude -p で純粋テキストだけ返してもらう
  date: '2026-05-06'
- url: https://ai-heartland.com/tool/claude-code-commands-complete-guide
  title: Claude Code 全コマンド完全リファレンス2026年5月版｜スラッシュ・CLI・設定を網羅
  date: '2026-05-07'
- url: https://ai-heartland.com/explain/thariq-non-coding-agents-bash
  title: Thariq「非コーディングエージェントこそbashを使え」｜メール・データ・API全部1ツールで
  date: '2026-05-10'
- url: https://qiita.com/Tadashi_Kudo/items/33d0a9b73b6ce0dee1ad
  title: Claude Code でコンテキストを枯渇させない3つの戦略——working-memory / PreCompact フック / 出力間引き
  date: '2026-05-13'
---




# Claude Code Cli

---

## 2026-05-13

### Claude Code でコンテキストを枯渇させない3つの戦略——working-memory / PreCompact フック / 出力間引き

Claude Code使用時にコンテキストを枯渇させない実践的な3つの戦略を解説。working-memory.mdによる構造化された情報管理、PreCompact/PostCompactフックによる自動状態保存・復元、Agentツール活用による出力間引きで、長時間のコーディングセッションでも重要情報を失わずに作業を継続できる方法を提案している。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/33d0a9b73b6ce0dee1ad)
- **重要度**: 7/10
- **タグ**: claude-code

---

## 2026-05-10

### Thariq「非コーディングエージェントこそbashを使え」｜メール・データ・API全部1ツールで

Claude Code チームの Thariq 氏が、非コーディング系エージェント（メール処理、データ集計など）でも bash ツールを積極活用すべきと提言。専用ツールを増やすとコンテキスト消費が増えエージェント精度が落ちるため、bash を「ユニバーサルアダプター」として CLI ツール群を統一的に扱う設計が推奨される。30 社との対話から得た実践知として 29 万インプレッションを記録。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/thariq-non-coding-agents-bash)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, performance

---

## 2026-05-07

### Claude Code 全コマンド完全リファレンス2026年5月版｜スラッシュ・CLI・設定を網羅

Claude Code v2.1.x系の全スラッシュコマンド・CLIフラグ・主要設定を網羅した完全リファレンスガイド。2026年5月時点で約60種類のスラッシュコマンドと80以上のCLIフラグが存在し、/ultrareview・/security-review・/scheduleなどの新設コマンドと、/vim・/pr-comments削除などの変更点を詳細に解説。ターミナルコマンドとスラッシュコマンドの2階層構造、ビルトインとバンドルスキルの違い、実用例を含めた体系的なコマンド一覧を提供している。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/claude-code-commands-complete-guide)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-06

### Claude Code の claude -p で純粋テキストだけ返してもらう

Claude Code の claude -p コマンドをスクリプトから呼び出す際、デフォルトではエージェントモードで動作し標準出力に要約しか返らない問題への対処法。--tools "" で全ツールを無効化すると純粋なテキスト出力が得られ、--bare と併用することでスクリプト用途に最適化できる。CI/自動化パイプラインでの利用時に有用なTips。

- **ソース**: [Zenn claude](https://zenn.dev/tbnet/articles/claude-code-headless-text-output)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-06 | 自動生成 |
