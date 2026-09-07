---
title: Claude Code Analytics
category: guides
subcategory: claude-code-analytics
tags:
- claude-api
- claude-code
- cowork
- performance
- setup
date: '2026-07-15'
updated: '2026-09-07'
sources:
- url: https://zenn.dev/mskbhd/articles/lab-102-claude
  title: Claudeのプロジェクト履歴を解析して、自分の作業パターンを可視化してみた
  date: '2026-07-15'
- url: https://qiita.com/chiisanasoft/items/de047ac451a8b49c740c
  title: Claude Code のログでブランチ運用を数えたら、git_branch の "HEAD" が2つの意味を持っていた
  date: '2026-08-24'
- url: https://zenn.dev/web_benriya/articles/claude-code-ga4-event-tracking-gap-detection
  title: Claude CodeでGA4のイベント計測漏れを自動検知・修正提案する仕組み
  date: '2026-09-07'
---



# Claude Code Analytics

---

## 2026-09-07

### Claude CodeでGA4のイベント計測漏れを自動検知・修正提案する仕組み

Claude CodeとGA4のBigQueryエクスポートデータを組み合わせて、イベント計測の漏れを自動検知し修正提案する実装方法を解説。日次のイベント発火件数集計SQLや流入元別の計測状況比較、PythonでのBigQueryデータ取得とClaude API連携、Slack通知による自動アラート化までを含む。GTMのタグ・トリガー修正提案も可能で、非エンジニアでも計測異常を早期発見できる体制を構築できる。

- **ソース**: [Zenn claude](https://zenn.dev/web_benriya/articles/claude-code-ga4-event-tracking-gap-detection)
- **重要度**: 6/10
- **タグ**: claude-code, claude-api, cowork

---

## 2026-08-24

### Claude Code のログでブランチ運用を数えたら、git_branch の "HEAD" が2つの意味を持っていた

Claude Codeの4ヶ月分436セッションのログを分析した結果、名前付きブランチでの作業は12セッション(2.8%)のみだった。git_branchに記録される「HEAD」には、detached HEADとリポジトリ外の2つの意味があり、198件のうち66件が前者、132件が後者だった。集計では、ターンが0件のセッション除外、cwdの多数決による.git判定、母数の定義などに注意が必要。

- **ソース**: [Qiita claude](https://qiita.com/chiisanasoft/items/de047ac451a8b49c740c)
- **重要度**: 5/10
- **タグ**: claude-code

---

## 2026-07-15

### Claudeのプロジェクト履歴を解析して、自分の作業パターンを可視化してみた

Claudeのプロジェクト履歴（~/.claude/projects/）を解析し、自分の作業パターンを可視化する手法を紹介。68セッションの分析から、Bash実行が59.5%を占めるなど「書くより実行している」傾向が判明。Read呼び出し過多やユーザー往復過多などの非効率パターンを特定し、改善の余地を発見。元ツイートの「全履歴をLLMに丸投げ」主張は誇張だが、ツール使用パターンの可視化による自己改善は有用。200行のPython解析スクリプト付き。

- **ソース**: [Zenn claude](https://zenn.dev/mskbhd/articles/lab-102-claude)
- **重要度**: 6/10
- **タグ**: claude-code, setup, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
