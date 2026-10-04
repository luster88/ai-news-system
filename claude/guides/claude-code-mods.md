---
title: Claude Code Mods
category: guides
subcategory: claude-code-mods
tags:
- claude-code
- mcp
- prompt
- setup
- 新機能
date: '2026-09-19'
updated: '2026-10-04'
sources:
- url: https://ai-heartland.com/explain/claude-code-mods
  title: Claude Code modsとは｜AGENTS.md対応のagents-md modをソースで読み、4つのモードを実測
  date: '2026-09-19'
- url: https://zenn.dev/oishiigohan/books/claude-code-mods-jissen
  title: Claude Code Mods 実践ガイド ― 関数フックで本体を改造する、動く Mod 7本
  date: '2026-09-20'
- url: https://qiita.com/suwa_nobu/items/981419874758372f65eb
  title: Claude Code の mod を1本書いて測った。公式が言う対応版は、実際には1つ前から動く
  date: '2026-10-02'
- url: https://qiita.com/faruryo/items/c075c8c3d664c38f2384
  title: Claude Code Modsは一番深く拡張できて、一番持ち運べない — 直近のアップデート13個を★で評価（2026/10/3時点）
  date: '2026-10-04'
---




# Claude Code Mods

---

## 2026-10-04

### Claude Code Modsは一番深く拡張できて、一番持ち運べない — 直近のアップデート13個を★で評価（2026/10/3時点）

Claude Code v2.1.283〜2.1.288の13個の変更を実務観点で評価。Claude Modsは最も深い拡張が可能だがClaude Code専用で、Nodeが使えず、hookが10秒を超えると権限判断が素通りになる制約が判明。verifyスキルは検証の結果、実運用では不要と判断。claude --resumeコマンドは端末や権限モードの違いで届かない制約がある。

- **ソース**: [Qiita claude](https://qiita.com/faruryo/items/c075c8c3d664c38f2384)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, setup

---

## 2026-10-02

### Claude Code の mod を1本書いて測った。公式が言う対応版は、実際には1つ前から動く

Claude Code 2.1.287で正式リリースされたmod機能について、実際には2.1.286から動作していたことを実証。modはプラグイン内で動くJavaScript関数で、ツール呼び出しやプロンプト送信に割り込める強力な機能だが、サンドボックス化されず自分の権限で動作するため、他人のmodを入れる際は注意が必要。--safe-modeで無効化可能。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/981419874758372f65eb)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-09-20

### Claude Code Mods 実践ガイド ― 関数フックで本体を改造する、動く Mod 7本

Claude Code の Mod システムを実践的に解説する技術書。関数フックを使った本体改造の手法を、usage-watch（使用量監視）、secret-scrub（秘密情報除去）、intent-guard（危険コマンド判定）など7つの動作する Mod 実装例とともに詳しく紹介。バリデータの型定義、テスト手法、配布手順まで網羅し、イベント・API の全一覧も付録として収録。

- **ソース**: [Zenn claude](https://zenn.dev/oishiigohan/books/claude-code-mods-jissen)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

## 2026-09-19

### Claude Code modsとは｜AGENTS.md対応のagents-md modをソースで読み、4つのモードを実測

Claude Code mods は2026年9月に公開された新しい拡張層で、TypeScript関数でエンジンのイベントを直接フックできる。hooksがシェルコマンドでイベントの前後に反応するのに対し、modsはイベントそのものを包む。AGENTS.md対応のagents-md modが同梱され、4つのinstructionFilesモード全てが実測検証された。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-mods)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-19 | 自動生成 |
