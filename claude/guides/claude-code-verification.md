---
title: Claude Code Verification
category: guides
subcategory: claude-code-verification
tags:
- claude-code
- cowork
- setup
date: '2026-10-22'
updated: '2026-10-22'
sources:
- url: https://qiita.com/tsukurugawa/items/9d01a0e9b89af4c0c91c
  title: Claude Codeの「完了しました」を証拠で確かめる：API→画面→schedulerの起動確認スクリプト（FastAPI + Vite）
  date: '2026-10-22'
---

# Claude Code Verification

---

## 2026-10-22

### Claude Codeの「完了しました」を証拠で確かめる：API→画面→schedulerの起動確認スクリプト（FastAPI + Vite）

Claude Codeの「完了しました」報告を鵜呑みにせず、API・画面・schedulerの3つを自動確認するPythonスクリプトを紹介。FastAPI + Viteプロジェクトで、古いビルド配信やlifespan内タスクの異常終了など、ステータス200でも実際には壊れているケースを検出する実践的な手法。作業前と完了後に必ず実行し、証拠として出力を記録することで、AIの報告を検証可能にする。

- **ソース**: [Qiita claudecode](https://qiita.com/tsukurugawa/items/9d01a0e9b89af4c0c91c)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-22 | 自動生成 |
