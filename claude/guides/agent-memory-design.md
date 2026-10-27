---
title: Agent Memory Design
category: guides
subcategory: agent-memory-design
tags:
- claude-code
- cowork
- prompt
date: '2026-10-27'
updated: '2026-10-27'
sources:
- url: https://qiita.com/joinclass/items/c45c6bcf0f62cfed8bf4
  title: エージェントのメモリ設計 — 短期・中期・長期の3層とベクトルDBを入れる判断基準
  date: '2026-10-27'
---

# Agent Memory Design

---

## 2026-10-27

### エージェントのメモリ設計 — 短期・中期・長期の3層とベクトルDBを入れる判断基準

エージェントのメモリ設計について、短期・中期・長期の3層構造を実運用経験から解説。ベクトルDBは最後の手段とし、Markdownファイル・TSV・grepの組み合わせで実装する方法を紹介。CLAUDE.mdは200行以内に抑え、コンテキスト使用率を10-15%に維持するルール、launchdによる自動更新、TSVでのイベント記録など具体的な実装例を示す。

- **ソース**: [Qiita claudecode](https://qiita.com/joinclass/items/c45c6bcf0f62cfed8bf4)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-27 | 自動生成 |
