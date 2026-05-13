---
title: Claude Code Codex Cowork
category: guides
subcategory: claude-code-codex-cowork
tags:
- claude-code
- cowork
- setup
date: '2026-05-13'
updated: '2026-05-13'
sources:
- url: https://qiita.com/kirozero/items/aec53be56a5427475969
  title: Claude Code × Codex 共存セットアップ — ルール・Skills・hooks を一元管理する
  date: '2026-05-13'
---

# Claude Code Codex Cowork

---

## 2026-05-13

### Claude Code × Codex 共存セットアップ — ルール・Skills・hooks を一元管理する

Claude CodeとCodexを同一プロジェクトで併用する際の設定・ルール・Skills・hooksの二重管理を避けるため、共通正本（AGENTS.md、shared/hooks/）とツール固有のアダプタ層を分ける設計手法を解説。Memoryはローカル補助として扱い、確定情報はAGENTS.mdに集約する運用ルールを提案している。Codex AppのImport機能による自動変換時の注意点や、symlinkを用いたskills管理の具体的な配置例も示す。

- **ソース**: [Qiita claudecode](https://qiita.com/kirozero/items/aec53be56a5427475969)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-13 | 自動生成 |
