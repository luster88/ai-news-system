---
title: Ai Agent Workflow
category: guides
subcategory: ai-agent-workflow
tags:
- claude-code
- cowork
- prompt
date: '2026-06-15'
updated: '2026-07-22'
sources:
- url: https://zenn.dev/gto_cto/articles/48fbf279efc43f
  title: Claude CodeとCodexを並列稼働したら競合祭りになったので、AI専用ロックファイルを作った
  date: '2026-06-15'
- url: https://www.reddit.com/r/ClaudeAI/comments/1v3o7fe/a_small_trick_to_guide_an_llm_agent_while_its
  title: A small trick to guide an LLM Agent while it’s coding
  date: '2026-07-22'
---


# Ai Agent Workflow

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
