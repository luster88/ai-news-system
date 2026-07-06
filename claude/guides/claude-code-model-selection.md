---
title: Claude Code Model Selection
category: guides
subcategory: claude-code-model-selection
tags:
- claude-code
- opus
- sonnet
date: '2026-07-06'
updated: '2026-07-06'
sources:
- url: https://zenn.dev/stockdev_sho/articles/8a9df3a1cb6001
  title: Claude Code のモデル選択──Opus / Sonnet / Haiku をタスクとコストで使い分ける
  date: '2026-07-06'
---

# Claude Code Model Selection

---

## 2026-07-06

### Claude Code のモデル選択──Opus / Sonnet / Haiku をタスクとコストで使い分ける

Claude Code でのモデル選択方法を解説。指定方法は4つあり、優先順位は `/model` > `--model` / `ANTHROPIC_MODEL` > `settings.json` > デフォルト。Opus は難易度高いタスク、Sonnet は日常開発、Haiku は定型処理に向く。`opusplan` は計画をOpus、実装をSonnetで自動切替する。`/fast` はOpus専用の高速化で別モデル切替ではない。サブエージェントは `model: inherit` で親と同じモデルを使うが、単純作業は明示的にHaikuに振るとコスト削減になる。

- **ソース**: [Zenn claude](https://zenn.dev/stockdev_sho/articles/8a9df3a1cb6001)
- **重要度**: 7/10
- **タグ**: claude-code, opus, sonnet

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-06 | 自動生成 |
