---
title: Claude Code Safety
category: guides
subcategory: claude-code-safety
tags:
- claude-code
- setup
- 新機能
date: '2026-05-09'
updated: '2026-07-01'
sources:
- url: https://qiita.com/Ngen/items/dd5090c6d05ec9c7994c
  title: Claude Codeのフック5個で「うっかり事故」を本気で潰した話
  date: '2026-05-09'
- url: https://zenn.dev/shun_producer/articles/5ea67d91ed8f5a
  title: 「はい」を押す前に止まれ。Claude Codeでやってはいけないこと7選【Ch6】
  date: '2026-05-28'
- url: https://qiita.com/evesquare/items/c593e35ec53b734b148f
  title: Claude Codeに自動で任せる、でも危険なgit操作だけはルールで縛る
  date: '2026-07-01'
---



# Claude Code Safety

---

## 2026-07-01

### Claude Codeに自動で任せる、でも危険なgit操作だけはルールで縛る

Claude Codeでgit操作を自動化する際、危険なコマンド（push、ブランチ削除、reset --hard等）を設定ファイルで制御する方法を解説。~/.claude/settings.jsonのpermissions機能を使い、確認が必要な操作は「ask」、実行を禁止したい操作は「deny」で宣言的にルール化。CLAUDE.mdへの記述と異なり、仕組みとして強制力を持たせることができる。

- **ソース**: [Qiita claudecode](https://qiita.com/evesquare/items/c593e35ec53b734b148f)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-28

### 「はい」を押す前に止まれ。Claude Codeでやってはいけないこと7選【Ch6】

Claude Codeの初心者が陥りやすい7つの失敗パターンを実例付きで解説。rm コマンドによる誤削除、.env ファイルの Git 漏洩、本番 DB への誤操作、git commit 忘れ、エラー無視、大規模作業の一括実行、動作確認の省略など、「はい」を押す前に確認すべきポイントを具体的に紹介している。各失敗に対する対処法も明記されており、Claude Code を安全に使うための実践的なガイドとなっている。

- **ソース**: [Zenn claude](https://zenn.dev/shun_producer/articles/5ea67d91ed8f5a)
- **重要度**: 7/10
- **タグ**: claude-code, setup

---

## 2026-05-09

### Claude Codeのフック5個で「うっかり事故」を本気で潰した話

Claude Codeが危険なコマンド（rm -rf /等）を実行しかける事故を防ぐため、5種類のフック（PreToolUse/PostToolUse/PreEdit/PostEdit/Stop）を実装した実践ログ。プロンプトでの「お願い」は5回に1回突破されるため、物理的なガードとしてフックで危険コマンド検知・秘密ファイル保護・通知を行う。stdin からのJSON読み取り、exit 0 でのblock返却、reasonの明示が重要なポイント。

- **ソース**: [Qiita claude](https://qiita.com/Ngen/items/dd5090c6d05ec9c7994c)
- **重要度**: 7/10
- **タグ**: claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-09 | 自動生成 |
