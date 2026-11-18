---
title: Memory Management
category: guides
subcategory: memory-management
tags:
- claude-code
- prompt
- setup
- 新機能
date: '2026-04-27'
updated: '2026-11-18'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/e717659f10192f32e7b1
  title: 67kスター「claude-mem」は本当に必要か？Claude Code自前メモリ管理の3層構造で代替する
  date: '2026-04-27'
- url: https://qiita.com/Tadashi_Kudo/items/50e8770b61fdc6c66383
  title: Anthropic "Dreaming"をscheduled-taskで再現する——週次cross-agent記憶整理の実装
  date: '2026-05-24'
- url: https://qiita.com/KYoshiyama/items/623e13ced9c119b614aa
  title: AI も「一晩寝かせる」と考えがまとまる🥱 寝ている間に記憶を整理する Dreaming の仕組み
  date: '2026-11-18'
---



# Memory Management

---

## 2026-11-18

### AI も「一晩寝かせる」と考えがまとまる🥱 寝ている間に記憶を整理する Dreaming の仕組み

AnthropicがAIエージェントの記憶整理機能「Dreaming」を発表。人間の睡眠中の記憶整理と同様に、AIが夜間に作業ログを見返してメモを修正しWikiを更新する仕組み。Claude Codeでの追実装例を含む詳細な解説記事で、ポケモンを使った実験ではメモを絞った方が効率的に進められることが示された。

- **ソース**: [Qiita claude](https://qiita.com/KYoshiyama/items/623e13ced9c119b614aa)
- **重要度**: 7/10
- **タグ**: 新機能, claude-code, prompt

---

## 2026-05-24

### Anthropic "Dreaming"をscheduled-taskで再現する——週次cross-agent記憶整理の実装

Anthropic の Dreaming（セッション外記憶整理）を Claude Code の scheduled-task で再現する実装を解説。週次で複数セッションを跨ぐパターンを抽出し、working-memory.md への concurrent write を OCC（楽観的同時実行制御）で防ぎながら、長期記憶の品質を維持する仕組みを紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/50e8770b61fdc6c66383)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-04-27

### 67kスター「claude-mem」は本当に必要か？Claude Code自前メモリ管理の3層構造で代替する

人気のclaud-mem（67kスター）の代替として、Claude Code純正機能による3層メモリ管理構造を提案。グローバルCLAUDE.md（160-180行）、プロジェクトルール（中立正本+adapter分離）、自動メモリ（MEMORY.mdをインデックス化し200行制限で分散）の組み合わせで、外部依存なしにセッション跨ぎの記憶管理を実現。hooksによる自動学習機能も実装可能で、個人開発〜中規模ならMarkdownとgrepで十分対応できると主張。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/e717659f10192f32e7b1)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-27 | 自動生成 |
