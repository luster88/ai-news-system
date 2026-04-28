---
title: Csv Analysis Automation
category: guides
subcategory: csv-analysis-automation
tags:
- claude-api
- cowork
- 新機能
date: '2026-04-28'
updated: '2026-04-28'
sources:
- url: https://zenn.dev/enaga7561/articles/3bd55b1def1e48
  title: Next.js + Claude APIでCSVを日本語で分析するツールを作った話——大容量ファイルへの向き合い方
  date: '2026-04-28'
---

# Csv Analysis Automation

---

## 2026-04-28

### Next.js + Claude APIでCSVを日本語で分析するツールを作った話——大容量ファイルへの向き合い方

Next.jsとClaude APIを使い、10万行超の大容量CSVを日本語で分析するツールを開発した事例。Claudeには生データを渡さず、ヘッダーとサンプル3行のみ送信して集計仕様をJSON形式で取得し、実際の集計処理はNode.js側で実行する役割分担を採用。製造業向けにShift-JIS対応やExcelファイル読み込み機能も実装し、「キクデータ」として公開している。

- **ソース**: [Zenn claude](https://zenn.dev/enaga7561/articles/3bd55b1def1e48)
- **重要度**: 6/10
- **タグ**: claude-api, 新機能, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-28 | 自動生成 |
