---
title: Claude Code Workflow
category: guides
subcategory: claude-code-workflow
tags:
- claude-code
- cowork
- prompt
- setup
- 新機能
date: '2026-03-26'
updated: '2026-04-02'
sources:
- url: https://qiita.com/tatematsu-k/items/ac8a83b09b2aa17416c6
  title: claudecodeを使ってAIドリブン開発をする前に読みたかった
  date: '2026-03-26'
- url: https://zenn.dev/busaiku0084/articles/20260330-dc3vcb5l
  title: 複数案件を掛け持ちするエンジニアのための gh / Claude Code アカウント切り替え術
  date: '2026-03-30'
- url: https://zenn.dev/yrd/articles/bfde3e5b809b79
  title: 非プログラマーのClaude Code実装コントロールのやり方、改善点を教えてください
  date: '2026-04-01'
- url: https://qiita.com/maskedridersystem/items/5e4898bee94fda192f54
  title: 「コーディングの神様」をどう語り継ぐか。AI全盛時代における、ベテランエンジニアの葛藤とログの重要性
  date: '2026-04-01'
- url: https://zenn.dev/sktt_panda/articles/panda-tools-claude-code-dev
  title: Claude Codeでぱんだツールズを作った話。PR 86本・41ツールとトークン代との戦い
  date: '2026-04-02'
- url: https://zenn.dev/penpeen/articles/e5f47b1ed82ad6
  title: Claude Code が速すぎるので「現在地」を可視化したら実装体験が変わった
  date: '2026-04-02'
---




# Claude Code Workflow

---

## 2026-04-02

### Claude Codeでぱんだツールズを作った話。PR 86本・41ツールとトークン代との戦い

個人開発者が Claude Code を使い、1〜2週間で41個のWebツール（ぱんだツールズ）を開発。PR 86本・コミット211件という圧倒的な速度を実現した一方、トークン消費で開発が4日間停止する問題にも直面。CLAUDE.mdやカスタムスキル、worktree分離などの工夫で効率化を図り、特にOGPやSEO設定などの「正確さが必要だが面白くない作業」で大きな効果を発揮した。

- **ソース**: [Zenn claude](https://zenn.dev/sktt_panda/articles/panda-tools-claude-code-dev)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

### Claude Code が速すぎるので「現在地」を可視化したら実装体験が変わった

Claude Code の高速な実装生成に対し、開発者の理解が追いつかない問題を解決するアプローチを紹介。シーケンス図にレイヤーごとの実装状態を色分けして可視化し、AI との認識を合わせながら進捗管理する手法。これにより認知負荷が下がり、効率的な実装が可能になった。計画書から進捗ファイルを生成する Claude Code Skill も作成。

- **ソース**: [Zenn claude](https://zenn.dev/penpeen/articles/e5f47b1ed82ad6)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-01

### 非プログラマーのClaude Code実装コントロールのやり方、改善点を教えてください

非プログラマーのデザイナーが、Claude Code を使った個人アプリ開発の実践的なワークフローを紹介。Claude.ai でプランニング、Claude Code で実装という役割分担、CLAUDE.md による仕様書駆動開発、調査フェーズと実装フェーズの分離、プロトタイプ先行など、試行錯誤から得た具体的なコントロール手法を共有している。

- **ソース**: [Zenn claude](https://zenn.dev/yrd/articles/bfde3e5b809b79)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

### 「コーディングの神様」をどう語り継ぐか。AI全盛時代における、ベテランエンジニアの葛藤とログの重要性

ベテランエンジニアがChatGPTからClaude Codeに移行した際の経験と、AI時代におけるエンジニアの役割変化についての考察。ネイティブアプリの不安定性とログ保存の困難さから、Chrome版に回帰した経緯を説明。AI全盛時代でも「コーディングの神様が降りてくる瞬間」のような手触り感の重要性を次世代にどう伝えるかという葛藤を綴っている。

- **ソース**: [Qiita claudecode](https://qiita.com/maskedridersystem/items/5e4898bee94fda192f54)
- **重要度**: 4/10
- **タグ**: claude-code, cowork, setup

---

## 2026-03-30

### 複数案件を掛け持ちするエンジニアのための gh / Claude Code アカウント切り替え術

複数案件を掛け持ちするエンジニア向けに、GitHub CLI（gh）とClaude Codeのアカウント切り替え方法を解説。gh auth switchでGitHubアカウントを切り替え、claude auth logout/loginでClaude Codeの組織アカウントを切り替える手順を紹介。切り替え忘れによるミスを防ぐため、作業開始前にstatusコマンドで確認する習慣を推奨している。

- **ソース**: [Zenn claude](https://zenn.dev/busaiku0084/articles/20260330-dc3vcb5l)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 2026-03-26

### claudecodeを使ってAIドリブン開発をする前に読みたかった

ClaudeCodeを活用したAI駆動開発における課題と対策を解説。スパゲッティコードの量産やPR肥大化といった問題に対し、SKILL.mdを使った「思考のガードレール」設定によるAIマネージメントの重要性を強調。公式skill creatorの活用により、チーム全体で開発フローを統制する手法を提案している。

- **ソース**: [Qiita claude](https://qiita.com/tatematsu-k/items/ac8a83b09b2aa17416c6)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-26 | 自動生成 |
