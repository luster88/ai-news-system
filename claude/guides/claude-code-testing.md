---
title: Claude Code Testing
category: guides
subcategory: claude-code-testing
tags:
- claude-code
- cowork
- setup
- 新機能
date: '2026-07-19'
updated: '2026-08-27'
sources:
- url: https://qiita.com/peka2/items/9ce150b3b480516fc16e
  title: Claude Code に iOSアプリの E2Eテスト までやらせるようにした（iOSシミュレータ + AXe）
  date: '2026-07-19'
- url: https://zenn.dev/yuninaka/articles/legacy-ai-test-gen
  title: OSSライブラリで検証：仕様書ゼロからClaude Codeでテスト網羅率93%を達成した話
  date: '2026-08-27'
---


# Claude Code Testing

---

## 2026-08-27

### OSSライブラリで検証：仕様書ゼロからClaude Codeでテスト網羅率93%を達成した話

Joda-Timeライブラリを題材に、仕様書とテストを削除した「レガシーコード」をClaude Codeで復元する検証を実施。既存コードを唯一の正として扱い、JaCoCo（93.43%）とPIT（81%）による高いカバレッジ・変異スコアを達成。数回の指示でClaude Codeが自律的にテスト作成・実行・修正を繰り返し、人間の細かい介入なしで実用的なセーフティネットを構築できることを実証した事例。

- **ソース**: [Zenn claude](https://zenn.dev/yuninaka/articles/legacy-ai-test-gen)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-07-19

### Claude Code に iOSアプリの E2Eテスト までやらせるようにした（iOSシミュレータ + AXe）

Claude Code を使って iOS アプリの E2E テストを自動化する手法の紹介。xcrun simctl と AXe CLI を組み合わせることで、ビルド・起動・操作・スクリーンショット確認までを Claude Code が自律的に実行できる。「シミュレータで動作確認して」というプロンプトだけで、操作→スクショ→確認のループを自動で回してくれるため、GPT や Fable と比較しても検査フェーズまで完結できる点が優れている。

- **ソース**: [Qiita claudecode](https://qiita.com/peka2/items/9ce150b3b480516fc16e)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-19 | 自動生成 |
