---
title: Workflow Optimization
category: guides
subcategory: workflow-optimization
tags:
- claude-code
- cowork
- cursor
- opus
- prompt
- setup
- sonnet
date: '2026-05-05'
updated: '2026-06-19'
sources:
- url: https://zenn.dev/bentenweb_fumi/articles/fxyojdsgcwap
  title: AIで「手を動かす時間」を減らす：技術者のための時間投資戦略
  date: '2026-05-05'
- url: https://zenn.dev/jun_eng/articles/322442e33841e7
  title: Claude Opus 4.7とSonnet 4.6の"二刀流"設計でnote執筆のコストと時間を半減させた話
  date: '2026-05-25'
- url: https://qiita.com/ryokwkm/items/c3100715000591af723f
  title: AIに毎回「現状を教えて」と聞かれていませんか？ Warm Boot Protocol という解決策
  date: '2026-06-04'
- url: https://qiita.com/goki602/items/4a44eceb28c5cbbcbab6
  title: Claude Code × tmux でバックグラウンド実行とエージェント管理を整理する
  date: '2026-06-07'
- url: https://zenn.dev/pekopugu/articles/agent01-b7-progress-driven
  title: 【Claude Code活用】PROGRESS.md駆動開発でセッションをまたいで開発する
  date: '2026-06-19'
---





# Workflow Optimization

---

## 2026-06-19

### 【Claude Code活用】PROGRESS.md駆動開発でセッションをまたいで開発する

Claude Codeはセッション間で記憶を保持しないため、PROGRESS.md駆動開発という手法を考案。完了済みStep、次Stepの作業内容、気づき・躓いた点の3セクションで構成し、CLAUDE.mdに更新ルールを明記することで、セッションをまたいだ開発を効率化。開発ログが記事素材としても活用でき、コミット履歴以上に意思決定の背景を残せる利点がある。

- **ソース**: [Zenn claude](https://zenn.dev/pekopugu/articles/agent01-b7-progress-driven)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-06-07

### Claude Code × tmux でバックグラウンド実行とエージェント管理を整理する

Claude Codeとtmuxのターミナルマルチプレクサを組み合わせることで、長時間AIエージェントタスクの管理を効率化する方法を解説。tmuxのセッション継続性や並列可視化機能により、エージェントを走らせたまま離席したり、複数エージェントを同時監視できる。Claude Codeの--teammate-modeオプションを使うことで、役割分担した複数エージェントをtmuxペインで管理可能。個人開発者向けに、Agent Viewとtmuxの補完的な使い方と導入判断の材料を提供。

- **ソース**: [Qiita claudecode](https://qiita.com/goki602/items/4a44eceb28c5cbbcbab6)
- **重要度**: 6/10
- **タグ**: claude-code, setup

---

## 2026-06-04

### AIに毎回「現状を教えて」と聞かれていませんか？ Warm Boot Protocol という解決策

Claude CodeやCursorなどのAIエージェントが毎回セッションをリセットする「コールドスタート問題」に対処するため、3層構造のドキュメント設計パターン「Warm Boot Protocol」を提案。AI設定ファイル（CLAUDE.md/.cursorrules）は参照先のみ記載し、ai-context.md（資料インデックス）とprogress.md（現在の文脈バッファ）を分離することで、AIが即座にプロジェクト状況を把握できる状態を実現する実践的な手法。

- **ソース**: [Qiita claudecode](https://qiita.com/ryokwkm/items/c3100715000591af723f)
- **重要度**: 7/10
- **タグ**: claude-code, cursor, prompt

---

## 2026-05-25

### Claude Opus 4.7とSonnet 4.6の"二刀流"設計でnote執筆のコストと時間を半減させた話

Claude Opus 4.7とSonnet 4.6を役割分担させる「二刀流」設計により、note執筆を最適化。Sonnetで骨組み生成、Opusで仕上げという工程分離で、執筆時間39%減、API課金41%減、有料購入数325%増を実現。最上位モデルへの一極集中ではなく、各モデルの強みに役割を割り当て、人間は判断に集中する設計が重要という知見。

- **ソース**: [Zenn claude](https://zenn.dev/jun_eng/articles/322442e33841e7)
- **重要度**: 7/10
- **タグ**: opus, sonnet, prompt

---

## 2026-05-05

### AIで「手を動かす時間」を減らす：技術者のための時間投資戦略

AIツールの利用を「消費」から「投資」へ転換する戦略を提案。プロンプトテンプレート化、CI/CD組み込み、再利用回数の計測など、仕組み化による時間削減効果を定量的に測定する手法を紹介。週次で5-10%の手動作業時間削減を目標とし、3年で数百時間の差が生まれると説く。

- **ソース**: [Zenn claude](https://zenn.dev/bentenweb_fumi/articles/fxyojdsgcwap)
- **重要度**: 6/10
- **タグ**: prompt, cowork, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-05 | 自動生成 |
