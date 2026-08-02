---
title: Multi Agent Harness
category: tools
subcategory: multi-agent-harness
tags:
- claude-code
- cowork
- cursor
- setup
date: '2026-07-13'
updated: '2026-08-02'
sources:
- url: https://ai-heartland.com/explain/loopkit-cross-tool-harness
  title: loopkit解説｜Claude Code・Cursor・Codexを横断する最小ハーネスと49スキル
  date: '2026-07-13'
- url: https://ai-heartland.com/agent/omnigent-meta-harness
  title: Omnigentとは｜Claude CodeやCodexを差し替えるメタハーネスをポリシーとサンドボックスで解説
  date: '2026-08-02'
---


# Multi Agent Harness

---

## 2026-08-02

### Omnigentとは｜Claude CodeやCodexを差し替えるメタハーネスをポリシーとサンドボックスで解説

Omnigentは複数のAIコーディングエージェント（Claude Code、Codex、Cursorなど24種）を統一的に扱うメタハーネスフレームワーク。YAML設定でハーネスを差し替え可能にし、ポリシー（ALLOW/DENY/ASK）による行動制御とOSサンドボックス（macOS=seatbelt、Linux=bwrap、Windows=Job Object）による隔離機能を提供する。2026年6月公開のアルファ版で、GitHub Star8,007だが公開issue812件と成熟度には注意が必要。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/omnigent-meta-harness)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 2026-07-13

### loopkit解説｜Claude Code・Cursor・Codexを横断する最小ハーネスと49スキル

loopkitは、Claude Code、Cursor、Codexなど複数のAIコーディングエージェントを横断して同じスキルセットを使い回せる最小構成のハーネスです。Plan→Act→Verifyの3段規律と49の専門スキルを提供し、各ツールに散らばった設定を一元管理できます。ランタイムを持たず、ディスク上のファイルのみで構成されるため、既存プロジェクトへの後付けが容易で、ロックインしない設計になっています。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/loopkit-cross-tool-harness)
- **重要度**: 6/10
- **タグ**: claude-code, cursor, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-13 | 自動生成 |
