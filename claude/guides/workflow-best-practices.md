---
title: Workflow Best Practices
category: guides
subcategory: workflow-best-practices
tags:
- claude-code
- cowork
- cursor
- prompt
- setup
date: '2026-05-24'
updated: '2026-08-21'
sources:
- url: https://qiita.com/y_tsubasa/items/a0213eaad3402d00ed0a
  title: AI と毎日開発していて定着した、地味だけど効く工夫の棚卸し
  date: '2026-05-24'
- url: https://qiita.com/nrEngineer/items/b1abd81ca2a9f74f30b6
  title: AI時代の開発ワークフロー実践ロードマップ ― 78バグから10本の記事を書いて見えたこと
  date: '2026-05-31'
- url: https://qiita.com/rikiza1989/items/9948daf97fb221da78c2
  title: AIエージェントを"暴走"させない仕組み ― ドキュメントを憲法にしたら、コードより先にルールが育った話
  date: '2026-07-11'
- url: https://zenn.dev/u_taaaaan/articles/ai-skills-in-dev-process
  title: AI を「コードを書かせる道具」にしないために開発プロセスにスキルを組み込んだ話
  date: '2026-08-12'
- url: https://qiita.com/Rai_050902/items/442d1d6b03c9a0e0150f
  title: AIと3つのシステムを作って、全部捨てた。既に社内にあった「良いファイル」に乗り換えた話
  date: '2026-08-21'
---





# Workflow Best Practices

---

## 2026-08-21

### AIと3つのシステムを作って、全部捨てた。既に社内にあった「良いファイル」に乗り換えた話

Claude Codeで成績処理システムを3バージョン作成したが、最終的に既存の社内Excelファイルの方が優れていたため全て破棄した事例。AIによる開発コスト低下により「作る前に既存を調べる」手順が省略されやすくなる副作用と、作らない判断の重要性を示す。業務の入口から出口まで設計された既存ファイルには、実運用で培われた汎用性があり、自作では「最後の一手間」が残っていた。

- **ソース**: [Qiita claudecode](https://qiita.com/Rai_050902/items/442d1d6b03c9a0e0150f)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 2026-08-12

### AI を「コードを書かせる道具」にしないために開発プロセスにスキルを組み込んだ話

Claude Code を使った開発プロセスにおいて、コードを書く速度だけでなく、設計レビュー段階とセルフレビュー段階にスキルを配置することで品質を向上させた実践例。受入条件の確認、設計の鮮度チェック、レビュー観点の統一、汎用手順のプラグイン化により、AI を単なるコーディングツールではなく開発プロセス全体に組み込んだ取り組みを紹介している。

- **ソース**: [Zenn claude](https://zenn.dev/u_taaaaan/articles/ai-skills-in-dev-process)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, setup

---

## 2026-07-11

### AIエージェントを"暴走"させない仕組み ― ドキュメントを憲法にしたら、コードより先にルールが育った話

Claude Code等のAIエージェントに長期開発を任せる際、「ドキュメントがコードより上位」という憲法(CLAUDE.md)で制御する個人プロジェクトapp_generatorの紹介。自然言語の指示ではなく、機械的な検証スクリプト(doc_lint.ps1/check_trace.ps1)とゲート機構でドキュメント更新を強制し、タスクライフサイクル管理(REQ/ADR/TASK-ID体系)と権限分離したエージェント設計で「暴走」を防ぐ。言語非依存の設計思想で、コードより先にルールを育てるアプローチを実践している。

- **ソース**: [Qiita claudecode](https://qiita.com/rikiza1989/items/9948daf97fb221da78c2)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-05-31

### AI時代の開発ワークフロー実践ロードマップ ― 78バグから10本の記事を書いて見えたこと

78件のバグ分析から生まれた実践的なAI開発ワークフロー「SFAD（Spec-First AI Development）」の完全ガイド。lint strictで45%のバグが防止可能だったことを発見し、Example MappingとDouble-Loop TDDを組み合わせた6つのClaude Codeコマンド（init, cycle, spec, test, impl, reverse）として体系化。初心者向けの3段階実践ロードマップ付き。

- **ソース**: [Qiita claudecode](https://qiita.com/nrEngineer/items/b1abd81ca2a9f74f30b6)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 2026-05-24

### AI と毎日開発していて定着した、地味だけど効く工夫の棚卸し

Claude CodeやCursor等のAI開発ツールを日常的に使う中で効果的だった実践的な工夫を棚卸しした記事。「AIとの認識ズレを減らす」「繰り返しを仕組み化」「文脈を外部保存」の3つが軸。プランモードの活用、grill-meスキルによる質問攻めで設計段階の曖昧さを潰す、スコープと入出力を事前明示するなど、地味だが確実に手戻りを減らす運用Tips集。

- **ソース**: [Qiita claude](https://qiita.com/y_tsubasa/items/a0213eaad3402d00ed0a)
- **重要度**: 6/10
- **タグ**: claude-code, cursor, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-24 | 自動生成 |
