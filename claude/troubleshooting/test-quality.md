---
title: Test Quality
category: troubleshooting
subcategory: test-quality
tags:
- claude-code
date: '2026-11-17'
updated: '2026-11-17'
sources:
- url: https://qiita.com/suwa_nobu/items/faf0d787a602cc5ec74c
  title: AI に書かせたテストは、どれだけ穴を見つけるのか。Claude Code・Codex・Gemini CLI のテストを変異テストで48回採点したら、95%以上を見抜き、仕様を渡すと点が下がった
  date: '2026-11-17'
---

# Test Quality

---

## 2026-11-17

### AI に書かせたテストは、どれだけ穴を見つけるのか。Claude Code・Codex・Gemini CLI のテストを変異テストで48回採点したら、95%以上を見抜き、仕様を渡すと点が下がった

Claude Code、Codex、Gemini CLIに同じコードのテストを書かせ、変異テスト（Stryker）で48回採点した結果を報告。AIが書いたテストは95%以上の変異を検出したが、仕様コメントを渡すとClaudeの点数が下がり、仕様外の振る舞い（エラー文言、想定外のクーポン種類）を見逃した。Codexは境界値のテストケースを漏らし、Windows環境では実行できない問題があった。変異テストは行カバレッジでは見えないテストの穴を発見できる有効な手法である。

- **ソース**: [Qiita claudecode](https://qiita.com/suwa_nobu/items/faf0d787a602cc5ec74c)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-17 | 自動生成 |
