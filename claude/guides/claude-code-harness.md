---
title: Claude Code Harness
category: guides
subcategory: claude-code-harness
tags:
- claude-code
- cowork
- mcp
- setup
- windows
- 新機能
date: '2026-04-04'
updated: '2026-08-24'
sources:
- url: https://zenn.dev/kosk_t/articles/claude-code-harness-audit-skill
  title: Claude Codeの設定、何から手をつける？ ハーネスエンジニアリングを体系化するスキルを作った
  date: '2026-04-04'
- url: https://qiita.com/daisuke-nagata/items/8f82bb7e2d51343657fd
  title: Claude Codeのハーネスは下から積め——MCPから入って壊した3ヶ月で学んだ積み上げ順
  date: '2026-05-22'
- url: https://www.reddit.com/r/ClaudeAI/comments/1vrjryf/week_3_of_making_my_fishing_game_entirely_with_ai
  title: Week 3 of making my fishing game entirely with AI
  date: '2026-08-18'
- url: https://zenn.dev/itdo/articles/8c62b571b7ec6e
  title: ChatGPT／CodexとClaude／Claude Codeを整理する――製品名ではなく4つの軸で見る
  date: '2026-08-24'
---




# Claude Code Harness

---

## 2026-08-24

### ChatGPT／CodexとClaude／Claude Codeを整理する――製品名ではなく4つの軸で見る

ChatGPT/CodexとClaude/Claude Codeの違いを製品名ではなく4つの軸（業務/開発、操作IF、実行環境、Windows/WSL2）で整理。デスクトップアプリ利用でも実行場所はLocal/Cloud/Remoteで異なり、製品選択には作業目的・必要資源・継続条件・OS環境を先に決めることが重要と解説。

- **ソース**: [Zenn claude](https://zenn.dev/itdo/articles/8c62b571b7ec6e)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 2026-08-18

### Week 3 of making my fishing game entirely with AI

ユーザーがClaude AIを使って釣りゲームを開発する3週目の進捗報告。Claude Artifactsでの開発からMCPを使用したBlenderとGodot連携へとワークフローを進化させ、ほぼすべての開発をClaudeで実施（画像生成のみChatGPT使用）。Godot 4.7.1エンジンとClaude Code MCPを活用し、コンセプトアート生成から3Dモデリング、実装まで一貫したAI支援開発の実例を紹介。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vrjryf/week_3_of_making_my_fishing_game_entirely_with_ai)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-05-22

### Claude Codeのハーネスは下から積め——MCPから入って壊した3ヶ月で学んだ積み上げ順

Claude Codeの自律性を高めるには、MCPから始めるのではなく、CLAUDE.md/AGENTS.md → hooks → skills → sub-agents → MCPの順に「下から積む」ことが重要。筆者は当初4本のMCPサーバーを同時接続し、ツール選択ミスが31%に達したが、ハーネスを正しい順序で再構築することで問題を解決した。CLAUDE.mdはルートを薄く保ち、hooksで確実な制御を行い、MCPは最後に追加する設計パターンが推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/daisuke-nagata/items/8f82bb7e2d51343657fd)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, setup

---

## 2026-04-04

### Claude Codeの設定、何から手をつける？ ハーネスエンジニアリングを体系化するスキルを作った

Claude Codeのハーネスエンジニアリング（CLAUDE.md、hooks、permissions、memory等の設定体系）を実践するための診断スキル「harness-audit」を紹介。プロンプトによる「助言」ではなく、環境設計でエージェントの品質を担保する手法を、7つの原則（Instruction Budget、Silent Success等）とともに解説。設定の抜け漏れ確認や優先順位付けを自動化し、Claude Code環境の最適化を支援する。

- **ソース**: [Zenn claude](https://zenn.dev/kosk_t/articles/claude-code-harness-audit-skill)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-04 | 自動生成 |
