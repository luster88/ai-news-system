---
title: Claude Code Cache Bug
category: troubleshooting
subcategory: claude-code-cache-bug
tags:
- bugfix
- claude-api
- claude-code
date: '2026-03-30'
updated: '2026-03-30'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1s7mkn3/psa_claude_code_has_two_cache_bugs_that_can
  title: 'PSA: Claude Code has two cache bugs that can silently 10-20x your API costs
    — here''s the root cause and workarounds'
  date: '2026-03-30'
---

# Claude Code Cache Bug

---

## 2026-03-30

### PSA: Claude Code has two cache bugs that can silently 10-20x your API costs — here's the root cause and workarounds

Claude Code のスタンドアロンバイナリに、プロンプトキャッシュを破壊しAPI コストを10-20倍に増大させる2つのバグが発見されました。1つ目は会話内容にセンチネル文字列（cch=00000）が含まれるとキャッシュが無効化される問題、2つ目はシステムプロンプト内の特定パターンでキャッシュが破壊される問題です。リバースエンジニアリングにより、Bun フォークのネイティブレイヤーでの文字列置換処理が原因と特定されました。回避策としてバイナリパッチやプロキシ使用が提案されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1s7mkn3/psa_claude_code_has_two_cache_bugs_that_can)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-30 | 自動生成 |
