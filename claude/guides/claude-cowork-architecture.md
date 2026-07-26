---
title: Claude Cowork Architecture
category: guides
subcategory: claude-cowork-architecture
tags:
- claude-code
- cowork
- setup
date: '2026-05-21'
updated: '2026-07-26'
sources:
- url: https://qiita.com/Ngen/items/a407f8c04b9bebf82cce
  title: Skills/CLAUDE.md/Hook を90日使い分けた4つの選定基準
  date: '2026-05-21'
- url: https://zenn.dev/toroby/articles/1c06c287096878
  title: NVD × Red Hat Security Data APIで"本当に刺さる"脆弱性だけDiscordに流す仕組みを作った
  date: '2026-07-26'
---


# Claude Cowork Architecture

---

## 2026-07-26

### NVD × Red Hat Security Data APIで"本当に刺さる"脆弱性だけDiscordに流す仕組みを作った

AWS未経験者がClaude CodeとClaude Desktopを役割分担させ、RHELの脆弱性情報をDiscordに自動通知するシステムをAWS Lambda上に構築した体験記。Claude Codeは実装の高速反復に、Claude Desktopは段階的なAWS設定の説明・ガイドに活用し、両者の引き継ぎに「HANDOFF文書」を作成することで一貫性を保った。AWS無料枠内での実装を重視し、Secrets ManagerではなくSSM Parameter Storeを採用。

- **ソース**: [Zenn claude](https://zenn.dev/toroby/articles/1c06c287096878)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 2026-05-21

### Skills/CLAUDE.md/Hook を90日使い分けた4つの選定基準

Claude Cowork における Skills、CLAUDE.md、Hook の3機能を90日間使い分けた実践知見。「タスク種類ならSkills」「プロジェクト前提ならCLAUDE.md」「イベント制御ならHook」というトリガー別の選定基準を提示。CLAUDE.mdの肥大化防止（200行上限）、Hookの応答速度（100ms以内）、Skillsの誤発火対策など、7つの失敗パターンと具体的な回避策を解説している。

- **ソース**: [Qiita claude](https://qiita.com/Ngen/items/a407f8c04b9bebf82cce)
- **重要度**: 6/10
- **タグ**: cowork, claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-21 | 自動生成 |
