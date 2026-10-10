---
title: Ai Agent Workflow
category: guides
subcategory: ai-agent-workflow
tags:
- claude-api
- claude-code
- cowork
- mcp
- prompt
- setup
- 新機能
date: '2026-06-15'
updated: '2026-10-10'
sources:
- url: https://zenn.dev/gto_cto/articles/48fbf279efc43f
  title: Claude CodeとCodexを並列稼働したら競合祭りになったので、AI専用ロックファイルを作った
  date: '2026-06-15'
- url: https://www.reddit.com/r/ClaudeAI/comments/1v3o7fe/a_small_trick_to_guide_an_llm_agent_while_its
  title: A small trick to guide an LLM Agent while it’s coding
  date: '2026-07-22'
- url: https://qiita.com/akihidem/items/f746e5613ec988469062
  title: 複数サブエージェントの並列実行を本番で回す：ワークフロー設計と運用の勘所
  date: '2026-09-03'
- url: https://zenn.dev/ryu7865/articles/2026-09-23-ai-agent-side-business-03
  title: 「4体のAIで月100Kドル」系の投稿を、実際にAIで副業を回している立場で検証した(第3回)
  date: '2026-09-23'
- url: https://zenn.dev/norishio22/articles/20260731-ai-coding-agent-practice
  title: AIエージェントに作業を任せるときのについて考えてみた
  date: '2026-09-27'
- url: https://qiita.com/ishizakahiroshi/items/a552bb339bab8b08eb8b
  title: AIエージェントへの依頼をどう回すか 受け箱とMCPを考えている途中です
  date: '2026-10-06'
- url: https://qiita.com/sescore/items/1f5faa0bc45f4cbf5069
  title: OpenClaw×Claude Code連携実践|記憶と実行を分離するAI開発フロー
  date: '2026-10-10'
---







# Ai Agent Workflow

---

## 2026-10-10

### OpenClaw×Claude Code連携実践|記憶と実行を分離するAI開発フロー

OpenClawとClaude Codeを連携させた実践例を紹介。記憶・判断層（OpenClaw）と実行層（Claude Code）を分離し、CLAUDE.md形式でルールを蓄積することで、AIエージェントの事故リスクを構造的に防ぐ手法を解説。cron連携、セキュリティレビュー、allowedTools制約など、実務で使える具体的なコマンドと構成を共有している。

- **ソース**: [Qiita claude](https://qiita.com/sescore/items/1f5faa0bc45f4cbf5069)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 2026-10-06

### AIエージェントへの依頼をどう回すか 受け箱とMCPを考えている途中です

AIエージェント（dots等）への依頼管理システムの設計記録。many-ai-cliで複数AIを並列実行し、Desklyで進捗管理する構想。受け箱とMCPによる連絡経路、GitHub ProjectsとIssueを正本とする6層アーキテクチャを整理中だが、受け箱やMCP受付は未実装。案件番号の統一運用と、5分ごとのポーリングから通知型への移行を検討している。

- **ソース**: [Qiita claudecode](https://qiita.com/ishizakahiroshi/items/a552bb339bab8b08eb8b)
- **重要度**: 5/10
- **タグ**: mcp, cowork, setup

---

## 2026-09-27

### AIエージェントに作業を任せるときのについて考えてみた

Claude Code や Codex などの AI コーディングエージェントを個人リポジトリで使う際の運用ルールをまとめた実践記事。未コミット差分の確認、Git/GitHub 設定の分離、複数アカウント環境での local 設定推奨、リポジトリ内に AGENTS.md などの入口ファイルを置く設計、Issue の判断権限の線引き、公開ディレクトリや GitHub Actions 設定の扱いなど、実運用で気をつけるべきポイントを具体的に解説している。

- **ソース**: [Zenn claude](https://zenn.dev/norishio22/articles/20260731-ai-coding-agent-practice)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-09-23

### 「4体のAIで月100Kドル」系の投稿を、実際にAIで副業を回している立場で検証した(第3回)

「4体のAIで月100Kドル」という投稿を実際にClaude Codeで副業を運営する立場から検証。100Kドルや追加費用0ドルという主張には根拠が示されていない点、334人の集客根拠が不明な点を指摘。一方で役割分担と引き継ぎ設計の考え方は有用と評価し、GumroadやZennでの実装確認の重要性を強調。数字の誇張に惑わされず、自分の環境で検証してから採用することを推奨。

- **ソース**: [Zenn claude](https://zenn.dev/ryu7865/articles/2026-09-23-ai-agent-side-business-03)
- **重要度**: 4/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-09-03

### 複数サブエージェントの並列実行を本番で回す：ワークフロー設計と運用の勘所

Claude Agent SDK で複数のサブエージェントを並列実行する際の設計と運用のポイントを解説。並列化が効く条件（サブタスクの独立性・コンテキストの独立性）、SDK の上限設定（ネスト深さ3層・同時実行20・予算上限）、そして実際に3つのファイルを並列レビューするワークフローの実装例を示す。TypeScript SDK v0.3.219 / Python SDK v0.2.127 以降が対象で、agents.json によるエージェント定義と run_in_background によるバックグラウンド実行がデフォルト動作となる。

- **ソース**: [Qiita claudecode](https://qiita.com/akihidem/items/f746e5613ec988469062)
- **重要度**: 7/10
- **タグ**: claude-code, claude-api, 新機能

---

## 2026-07-22

### A small trick to guide an LLM Agent while it’s coding

LLMエージェントがコーディング中に誤ったコードを書いている時、割り込むとコンテキストを失い、待つとミスが蓄積する問題への対処法。コード内に意図的に構文エラーとなる平文のメモを書き込むことで、エージェントがファイルを開いてメモを読み、修正すべき点を理解できる。これにより実行を中断せずにライブコードレビューのような形でガイドできる。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v3o7fe/a_small_trick_to_guide_an_llm_agent_while_its)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-06-15

### Claude CodeとCodexを並列稼働したら競合祭りになったので、AI専用ロックファイルを作った

Claude CodeとCodexを並列稼働させた際に発生したファイル競合問題について、AI専用ロックファイルを作成して解決した事例を紹介。複数のAIエージェントを別ブランチ・別worktreeで同時運用する際のベストプラクティスを模索している。

- **ソース**: [Zenn claude](https://zenn.dev/gto_cto/articles/48fbf279efc43f)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-15 | 自動生成 |
