---
title: Claude Cowork Automation
category: guides
subcategory: claude-cowork-automation
tags:
- claude-code
- cowork
- mcp
- prompt
- setup
- 新機能
date: '2026-06-04'
updated: '2026-09-01'
sources:
- url: https://zenn.dev/tom1414/articles/87cab2ae7fabff
  title: Claude Cowork × Slack でClaude最新情報を自動収集
  date: '2026-06-04'
- url: https://qiita.com/4q_sano/items/091942f8dfd9145d98ef
  title: ループエンジニアリングを Cowork で実践する ― 毎週のクラッシュ週報を“評価役つき”で全自動 PowerPoint 化
  date: '2026-06-23'
- url: https://zenn.dev/isobeage/articles/morning-briefing-agent-devlog01
  title: 「朝のブリーフィングAI」を作ろうとして、結局スキルを1個捨てた話
  date: '2026-09-01'
---



# Claude Cowork Automation

---

## 2026-09-01

### 「朝のブリーフィングAI」を作ろうとして、結局スキルを1個捨てた話

Claude Coworkを使い、朝のブリーフィングを自動生成する試みを記録した開発ログ。当初はカレンダー・メール・ニュースを集約するHTMLページを自動生成する計画だったが、連携先カレンダーアプリにエクスポート機能がない、PCの起動時刻が不定、などの制約に直面。最終的に「自動生成ページ」から「対話型チェックインスキル」への路線変更を決断し、作りかけのスキルを破棄した経緯を紹介している。

- **ソース**: [Zenn claude](https://zenn.dev/isobeage/articles/morning-briefing-agent-devlog01)
- **重要度**: 5/10
- **タグ**: claude-code, cowork, setup

---

## 2026-06-23

### ループエンジニアリングを Cowork で実践する ― 毎週のクラッシュ週報を“評価役つき”で全自動 PowerPoint 化

Claude Desktop の Cowork を使って、毎週のクラッシュレポートを「データ取得→集計→検証→PowerPoint生成」まで全自動化する「ループエンジニアリング」の実践例。重要なのは生成だけでなく、別の役割（評価役）による検証を組み込むこと。決定論チェックと別モデルによる文章チェックの2段構えで品質を担保し、人間は最後の確認だけを行う。Addy Osmani のループエンジニアリング概念を Cowork の6つのパーツ（スケジュール、スキル、MCP、サブエージェント、フォルダ）に当てはめて実装する具体的な手法を解説。

- **ソース**: [Qiita claude](https://qiita.com/4q_sano/items/091942f8dfd9145d98ef)
- **重要度**: 7/10
- **タグ**: cowork, mcp, prompt

---

## 2026-06-04

### Claude Cowork × Slack でClaude最新情報を自動収集

Claude Coworkのスケジュールタスク機能とSlack連携を使い、Claude公式サイトから最新情報を毎日自動収集してSlackに投稿する仕組みを構築。GUI操作でコネクタを設定し、プログラミング不要で情報収集・保存・通知の自動化を実現。ただしデスクトップアプリを開き続ける必要があり、サーバー混雑時は実行時刻がずれる制約がある。

- **ソース**: [Zenn claude](https://zenn.dev/tom1414/articles/87cab2ae7fabff)
- **重要度**: 6/10
- **タグ**: cowork, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-04 | 自動生成 |
