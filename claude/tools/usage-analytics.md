---
title: Usage Analytics
category: tools
subcategory: usage-analytics
tags:
- claude-code
- performance
- pricing
- 新機能
date: '2026-05-11'
updated: '2026-08-20'
sources:
- url: https://zenn.dev/kojihq/articles/2c211edbf84727
  title: Claude Code 1 日で $874 使った日のログを koji-lens で見たら、subagent経由Bashが68%だった
  date: '2026-05-11'
- url: https://qiita.com/chiisanasoft/items/9c9512b08507515f3c59
  title: Claude Code の利用ログを SQLite に取り込んで API 換算したら302万円だった
  date: '2026-08-20'
---


# Usage Analytics

---

## 2026-08-20

### Claude Code の利用ログを SQLite に取り込んで API 換算したら302万円だった

Claude Codeの4ヶ月間の利用ログをSQLiteで分析し、API換算で302万円相当の利用実績を可視化。73,548ターンの集計で、金額の67%がキャッシュ読み出し、ユーザー入力は0.2%のみと判明。集計ツールの単価計算に落とし穴があり、新モデルが0円扱いされ総額の33%を見落とす実害が発生。未知のモデルを0円でなくn/aで表示する対策の重要性を指摘。

- **ソース**: [Qiita claude](https://qiita.com/chiisanasoft/items/9c9512b08507515f3c59)
- **重要度**: 6/10
- **タグ**: claude-code, pricing, performance

---

## 2026-05-11

### Claude Code 1 日で $874 使った日のログを koji-lens で見たら、subagent経由Bashが68%だった

Claude Code の1日あたりのコスト分析ツール koji-lens を紹介。24時間で$874相当（API換算）を消費し、その68%がsubagent経由のBash呼び出しだったことが判明。/usageコマンドやAnthropic Consoleでは見えないツール別・subagent別の内訳を可視化できる。ローカルJSONLから集計し、ccusageと並行運用可能。

- **ソース**: [Zenn claude](https://zenn.dev/kojihq/articles/2c211edbf84727)
- **重要度**: 6/10
- **タグ**: claude-code, performance, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-11 | 自動生成 |
