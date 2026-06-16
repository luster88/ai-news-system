---
title: Codex Plugin Integration
category: guides
subcategory: codex-plugin-integration
tags:
- claude-code
- mcp
date: '2026-06-16'
updated: '2026-06-16'
sources:
- url: https://qiita.com/ZSL/items/713466e1443d3d79f8a6
  title: Claude Code から画像生成する — OpenAI 公式 Codex プラグインで Images 2.0 を呼ぶ（4つの罠と委譲設計）
  date: '2026-06-16'
---

# Codex Plugin Integration

---

## 2026-06-16

### Claude Code から画像生成する — OpenAI 公式 Codex プラグインで Images 2.0 を呼ぶ（4つの罠と委譲設計）

Claude Code には画像生成機能がないが、OpenAI 公式の Codex プラグイン（openai/codex-plugin-cc）を導入することで Images 2.0 に委譲して画像生成が可能になる。実装時にはバックグラウンド実行による応答停止、サンドボックスの書き込み制限、CJK文字化け、Skill()経由でのセッションハングという4つの罠がある。正しい実装方法は Agent(subagent_type="codex:codex-rescue") を使い、親エージェント側でサンドボックス越えのファイル操作と検証を担当する責務分離設計を採用することである。

- **ソース**: [Qiita claudecode](https://qiita.com/ZSL/items/713466e1443d3d79f8a6)
- **重要度**: 6/10
- **タグ**: claude-code, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-16 | 自動生成 |
