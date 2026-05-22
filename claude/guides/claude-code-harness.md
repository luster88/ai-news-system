---
title: Claude Code Harness
category: guides
subcategory: claude-code-harness
tags:
- claude-code
- mcp
- setup
- 新機能
date: '2026-04-04'
updated: '2026-05-22'
sources:
- url: https://zenn.dev/kosk_t/articles/claude-code-harness-audit-skill
  title: Claude Codeの設定、何から手をつける？ ハーネスエンジニアリングを体系化するスキルを作った
  date: '2026-04-04'
- url: https://qiita.com/daisuke-nagata/items/8f82bb7e2d51343657fd
  title: Claude Codeのハーネスは下から積め——MCPから入って壊した3ヶ月で学んだ積み上げ順
  date: '2026-05-22'
---


# Claude Code Harness

---

## 2026-05-22

### Claude Codeのハーネスは下から積め——MCPから入って壊した3ヶ月で学んだ積み上げ順

Claude Codeの自律性を高めるには、MCPから始めるのではなく、CLAUDE.md/AGENTS.md → hooks → skills → sub-agents → MCPの順に「下から積む」ことが重要。筆者は当初4本のMCPサーバーを同時接続し、ツール選択ミスが31%に達したが、ハーネスを正しい順序で再構築することで問題を解決した。CLAUDE.mdはルートを薄く保ち、hooksで確実な制御を行い、MCPは最後に追加する設計パターンが推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/daisuke-nagata/items/8f82bb7e2d51343657fd)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, setup

---

## 2026-04-04

### Claude Codeの設定、何から手をつける？ ハーネスエンジニアリングを体系化するスキルを作った

Claude Codeのハーネスエンジニアリング（CLAUDE.md、hooks、permissions、memory等の設定体系）を実践するための診断スキル「harness-audit」を紹介。プロンプトによる「助言」ではなく、環境設計でエージェントの品質を担保する手法を、7つの原則（Instruction Budget、Silent Success等）とともに解説。設定の抜け漏れ確認や優先順位付けを自動化し、Claude Code環境の最適化を支援する。

- **ソース**: [Zenn claude](https://zenn.dev/kosk_t/articles/claude-code-harness-audit-skill)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-04 | 自動生成 |
