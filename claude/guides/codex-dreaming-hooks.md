---
title: Codex Dreaming Hooks
category: guides
subcategory: codex-dreaming-hooks
tags:
- claude-code
- prompt
- 新機能
date: '2026-06-18'
updated: '2026-06-18'
sources:
- url: https://zenn.dev/kakecake/articles/20260618-codex-hooks-dreaming
  title: Anthropic の Dreaming を Codex で再現する：hooks でコンテキストを増やさず精度を上げる
  date: '2026-06-18'
---

# Codex Dreaming Hooks

---

## 2026-06-18

### Anthropic の Dreaming を Codex で再現する：hooks でコンテキストを増やさず精度を上げる

Anthropic の Dreaming を OpenAI Codex で再現する実装記事。hooks を活用し、コンテキスト量を増やさずに精度を上げる設計が特徴。記憶の索引は最小限にし、汎用的な補正処理（UTF-8エンコーディングなど）を hook で自動化することで、プロンプト注入に頼らず決定的に問題を解決する。夜間バッチで記憶を整理・統合し、全自動運用を実現している。

- **ソース**: [Zenn claude](https://zenn.dev/kakecake/articles/20260618-codex-hooks-dreaming)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-18 | 自動生成 |
