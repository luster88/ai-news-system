---
title: Claude Code Testing
category: guides
subcategory: claude-code-testing
tags:
- claude-code
- setup
- 新機能
date: '2026-07-19'
updated: '2026-07-19'
sources:
- url: https://qiita.com/peka2/items/9ce150b3b480516fc16e
  title: Claude Code に iOSアプリの E2Eテスト までやらせるようにした（iOSシミュレータ + AXe）
  date: '2026-07-19'
---

# Claude Code Testing

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
