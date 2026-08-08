---
title: Setup Linux
category: guides
subcategory: setup-linux
tags:
- claude-code
- linux
- setup
date: '2026-03-30'
updated: '2026-08-08'
sources:
- url: https://qiita.com/supertask/items/ab017f78d75fb9a1f61b
  title: Raspberry PiでClaude Codeを起動時に自動実行してDiscordボットとして常駐させる
  date: '2026-03-30'
- url: https://zenn.dev/gsy0911/articles/a4dc76f0639576
  title: Raspberry Pi 5でClaude Codeを動かす
  date: '2026-08-08'
---


# Setup Linux

---

## 2026-08-08

### Raspberry Pi 5でClaude Codeを動かす

Raspberry Pi 5上にNixOSを導入し、Claude Codeをremote-controlモードで常時起動させる手順を解説。MacBook Proのスリープ問題を回避し、低消費電力で24時間稼働可能な専用Agentサーバーを構築。SD イメージのビルドからSSH接続、Claude Codeの常駐設定までをカバーし、構成管理をNixOSで宣言的に行う。

- **ソース**: [Zenn claude](https://zenn.dev/gsy0911/articles/a4dc76f0639576)
- **重要度**: 6/10
- **タグ**: claude-code, setup, linux

---

## 2026-03-30

### Raspberry PiでClaude Codeを起動時に自動実行してDiscordボットとして常駐させる

Raspberry Pi上でClaude Codeを起動時に自動実行し、Discordボットとして常駐させる方法を解説。systemdユーザーサービスとシェルスクリプトを使い、デスクトップ環境でターミナルウィンドウを表示させながらClaude Codeを動作させる。CLAUBBIT環境変数でワークスペース信頼ダイアログをスキップし、非対話環境での実行を可能にする。

- **ソース**: [Qiita claude](https://qiita.com/supertask/items/ab017f78d75fb9a1f61b)
- **重要度**: 6/10
- **タグ**: claude-code, setup, linux

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-30 | 自動生成 |
