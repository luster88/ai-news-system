---
title: Claude Code Orchestration
category: tools
subcategory: claude-code-orchestration
tags:
- claude-code
- cowork
- mac
- setup
- 新機能
date: '2026-09-08'
updated: '2026-11-16'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1wazam9/i_built_an_app_where_each_of_my_claude_code
  title: I built an app where each of my Claude Code agents looks after one thing
  date: '2026-09-08'
- url: https://ai-heartland.com/agent/database-architect
  title: database-architect｜Claude CodeのDB設計サブエージェントを旧版と比べて検証、RLSの落とし穴
  date: '2026-11-16'
---


# Claude Code Orchestration

---

## 2026-11-16

### database-architect｜Claude CodeのDB設計サブエージェントを旧版と比べて検証、RLSの落とし穴

Claude Codeのデータベース設計サブエージェント「database-architect」の新版（2026年11月12日リリース）について解説。旧版682行から203行に書き直され、「試していないSQLを渡さない」という方針を採用。特にマルチテナント環境でのRLS（行レベルセキュリティ）の実装において、旧版では全テナントが見えてしまう問題があったが、新版ではこれを防ぐルールを明記。PostgreSQL 16での検証結果とともに、両バージョンの違いを詳細に比較している。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/database-architect)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-09-08

### I built an app where each of my Claude Code agents looks after one thing

開発者が Claude Code エージェントを複数起動し、それぞれが独立したタスク（フィードバック管理、Web サイト管理、成長分析など）を担当する Mac/iPhone アプリ「Omni」を構築。各エージェントは独自の会話履歴を保持し、複数のエージェント間で協調してリリース作業などを実行できる。ユーザー自身の Claude アカウントで動作し、アプリ自体に AI 機能はなく無料で利用可能。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wazam9/i_built_an_app_where_each_of_my_claude_code)
- **重要度**: 6/10
- **タグ**: claude-code, mac, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-08 | 自動生成 |
