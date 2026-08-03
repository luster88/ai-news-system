---
title: Claude Memory Architecture
category: guides
subcategory: claude-memory-architecture
tags:
- claude-api
- claude-code
- claude-console
date: '2026-08-03'
updated: '2026-08-03'
sources:
- url: https://zenn.dev/yukihirokimuraj/articles/claude-memory-map
  title: Claudeの「記憶」はどこにある？ チャット・Claude Code・APIの境界を整理する
  date: '2026-08-03'
---

# Claude Memory Architecture

---

## 2026-08-03

### Claudeの「記憶」はどこにある？ チャット・Claude Code・APIの境界を整理する

Claudeの「記憶」機能は、チャット（Web/Desktop/Mobile）、Claude Code、APIの3つの利用場所で完全に分離されており、相互に共有されない。チャット内でもメモリ（継続的に役立つ情報の保持）と過去チャット検索（会話履歴の参照）は別の仕組みで、プロジェクトごとにメモリが分離される。Claude Codeではオートメモリとファイルキャッシュが別々に動作し、APIではMemory Toolを明示的に実装する必要がある。それぞれの保存場所・境界・共有範囲を理解することで、Claudeの「記憶」の仕組みを正しく活用できる。

- **ソース**: [Zenn claude](https://zenn.dev/yukihirokimuraj/articles/claude-memory-map)
- **重要度**: 7/10
- **タグ**: claude-console, claude-code, claude-api

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-03 | 自動生成 |
