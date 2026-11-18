---
title: Agent Memory Design
category: guides
subcategory: agent-memory-design
tags:
- claude-api
- claude-code
- cowork
- prompt
- 新機能
date: '2026-10-27'
updated: '2026-11-18'
sources:
- url: https://qiita.com/joinclass/items/c45c6bcf0f62cfed8bf4
  title: エージェントのメモリ設計 — 短期・中期・長期の3層とベクトルDBを入れる判断基準
  date: '2026-10-27'
- url: https://qiita.com/Simon_Zhang/items/c112590a80a1129daeaa
  title: 【徹底解説】Anthropic「The components of agent memory」を読む ― AIエージェントの記憶は"4層"と"dreaming"で設計する
  date: '2026-11-18'
---


# Agent Memory Design

---

## 2026-11-18

### 【徹底解説】Anthropic「The components of agent memory」を読む ― AIエージェントの記憶は"4層"と"dreaming"で設計する

Anthropicの公式記事「The components of agent memory」を詳しく解説。AIエージェントの記憶設計を「トランスクリプト→メモリノート→メモリ表現→注入コンテキスト」の4層構造で整理し、セッション間で記憶を見直す「dreaming」プロセスの重要性を説明。CL-Benchでの世代別評価結果も紹介し、強力なモデルほど記憶の活用が上達していることを示している。

- **ソース**: [Qiita claude](https://qiita.com/Simon_Zhang/items/c112590a80a1129daeaa)
- **重要度**: 8/10
- **タグ**: claude-api, prompt, 新機能

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
