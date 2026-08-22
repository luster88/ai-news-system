---
title: Claude Code Remote Execution
category: guides
subcategory: claude-code-remote-execution
tags:
- claude-code
- setup
- windows
date: '2026-08-22'
updated: '2026-08-22'
sources:
- url: https://zenn.dev/kentaro_tak/articles/claude-code-headless-slack-relay
  title: スマホのSlackから自宅PCのClaude Codeを動かす。ポート開放は要らなかったが、作っているのは自宅への遠隔実行経路だった
  date: '2026-08-22'
---

# Claude Code Remote Execution

---

## 2026-08-22

### スマホのSlackから自宅PCのClaude Codeを動かす。ポート開放は要らなかったが、作っているのは自宅への遠隔実行経路だった

スマホのSlackから自宅PCのClaude Codeを遠隔実行する仕組みを構築した事例。Slack Socket Modeで外部ポート開放なしに接続し、標準入力経由でプロンプト渡し、スレッドIDとsession_idを紐付けることで会話継続を実現。Windows特有のcmd.exe改行問題も解決した実践的なガイド。

- **ソース**: [Zenn claude](https://zenn.dev/kentaro_tak/articles/claude-code-headless-slack-relay)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-22 | 自動生成 |
