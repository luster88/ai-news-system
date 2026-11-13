---
title: Workflow Management
category: guides
subcategory: workflow-management
tags:
- claude-code
- claude-console
- copilot
- cowork
- prompt
- setup
- windows
date: '2026-06-17'
updated: '2026-11-13'
sources:
- url: https://qiita.com/shinjpn1/items/f194dc84928c6598477e
  title: 「Claude Code 使ってます?」— テキストファイルで AI を管理していた私が、結局システムを作るまで
  date: '2026-06-17'
- url: https://qiita.com/haruki_nakayama/items/65cc8517912ca5ceb670
  title: AI 駆動開発に変更管理を組み込んだ話
  date: '2026-09-17'
- url: https://qiita.com/Rai_050902/items/a156d3a867af23375931
  title: 生命保険の見直しをAIと進めたら、2つのClaude（チャットとCode）を「Markdown1枚」でバトンリレーさせる運用に落ち着いた話
  date: '2026-09-20'
- url: https://zenn.dev/atsushi_apps/articles/claude-code-sessions-busho
  title: Claude Codeのセッションを「部署」に分けて、個人開発を回す
  date: '2026-10-17'
- url: https://zenn.dev/sato_ken/articles/46f7f1f7a1e856
  title: AIを10窓並行で回してたら頭がパンクしたので「進行板」を作った
  date: '2026-11-01'
- url: https://qiita.com/umezu_y/items/a5a86c005f8c66cecbad
  title: Claude Code を「時間割」で回す ― 1日10件以上を並行しても、目の前の1件に集中できる
  date: '2026-11-13'
---






# Workflow Management

---

## 2026-11-13

### Claude Code を「時間割」で回す ― 1日10件以上を並行しても、目の前の1件に集中できる

Claude Code のデスクトップアプリで、複数の作業を並行管理する「時間割」手法を紹介。ネストセッションを活用し、1日10件以上の案件を並行しても、目の前の1件に集中できる運用方法を解説。サイドバーでの視覚的な進捗管理と、時間割セッションでの優先順位付けがポイント。

- **ソース**: [Qiita claudecode](https://qiita.com/umezu_y/items/a5a86c005f8c66cecbad)
- **重要度**: 6/10
- **タグ**: claude-code, windows

---

## 2026-11-01

### AIを10窓並行で回してたら頭がパンクしたので「進行板」を作った

複数のAIチャットを並行稼働させる際の進捗管理の課題を解決するため、案件単位でカードを管理する「進行板」を開発。チャット単位ではなく案件単位で管理し、AIが自動で進捗を更新。さらに板自体にAIを配置して更新漏れを監視する仕組みを実装。人間は判断のみに集中できる体制を構築した事例。

- **ソース**: [Zenn claude](https://zenn.dev/sato_ken/articles/46f7f1f7a1e856)
- **重要度**: 6/10
- **タグ**: prompt, cowork

---

## 2026-10-17

### Claude Codeのセッションを「部署」に分けて、個人開発を回す

個人開発者が複数のiPhoneアプリをClaude Codeで管理する際、セッションを「部署」として分割し、アプリ担当・紹介サイト担当・コンサル担当などに役割分担する手法を紹介。セッション間でメッセージをやり取りし、共通ルールをCLAUDE.mdで管理することで、トークン節約と作業効率化を実現。PreToolUseフックで誤操作を防止する仕組みも解説。

- **ソース**: [Zenn claude](https://zenn.dev/atsushi_apps/articles/claude-code-sessions-busho)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 2026-09-20

### 生命保険の見直しをAIと進めたら、2つのClaude（チャットとCode）を「Markdown1枚」でバトンリレーさせる運用に落ち着いた話

生命保険の見直しを数ヶ月かけて進める中で、Claude チャット版（相談用）と Claude Code（計算・ファイル操作用）を Markdown ファイル1枚で連携させる運用を確立。会話履歴を AI に頼らず外部ファイルに記録することで、長期的なテーマでも文脈を維持しながら効率的に作業できるようになった事例。非エンジニアでも実践できる複数 AI の役割分担と記憶の橋渡し方法を紹介。

- **ソース**: [Qiita claude](https://qiita.com/Rai_050902/items/a156d3a867af23375931)
- **重要度**: 6/10
- **タグ**: claude-code, claude-console, cowork

---

## 2026-09-17

### AI 駆動開発に変更管理を組み込んだ話

Claude Codeを用いたAI駆動開発において、チケット単位で影響マップ（impact.md）・判断記録（decisions.md）・クロージャチェック（closure.md）の3ファイルを用いた変更管理の仕組みを導入した実践報告。Amazon Kiroの仕様駆動開発（SDD）をベースに、変更追跡と決着確認を独自に拡張し、実装理由や判断基準の可視化、レビュー効率化、チーム内の知見共有を実現した。

- **ソース**: [Qiita claudecode](https://qiita.com/haruki_nakayama/items/65cc8517912ca5ceb670)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 2026-06-17

### 「Claude Code 使ってます?」— テキストファイルで AI を管理していた私が、結局システムを作るまで

Claude Code導入をきっかけに、3年間停滞していたポーカーゲーム開発を再開した開発者の体験記。テキストファイルでのAI管理から始まり、Claude Pro + GitHub Copilot Pro+の併用、インデックス管理システムの構築、そして最終的にFlowGateという独自の証跡管理システムを開発するまでの過程を詳述。AIの一貫性のなさやフロントエンドバグへの対処法、作業履歴の重要性について実体験をもとに語っている。

- **ソース**: [Qiita claudecode](https://qiita.com/shinjpn1/items/f194dc84928c6598477e)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, copilot

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-17 | 自動生成 |
