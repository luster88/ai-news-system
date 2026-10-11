---
title: Ollama Integration
category: guides
subcategory: ollama-integration
tags:
- claude-code
- setup
- vscode
date: '2026-03-23'
updated: '2026-10-11'
sources:
- url: https://qiita.com/AI-SKILL-LAB/items/6589c5124c391f923320
  title: Ollama 0.18 × Claude Code 完全移行ガイド ── 「/v1ハック」を卒業してネイティブAPIでローカルLLMを本物のエージェントにする【2026年3月最新】
  date: '2026-03-23'
- url: https://zenn.dev/uhu/articles/01e681749f90fe
  title: Ollama Cloud をいろいろなハーネスで使う方法
  date: '2026-10-11'
---


# Ollama Integration

---

## 2026-10-11

### Ollama Cloud をいろいろなハーネスで使う方法

Ollama Cloud を claude、codex、dsh、opencodeなどの各種ハーネスで使用する方法を解説。:cloud指定でクラウドモデルを呼び出し、APIキーまたはローカルOllama経由で接続可能。[1m]トークン指定の罠やautoモード時の分類器の問題、各ハーネスでの設定手順を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/uhu/articles/01e681749f90fe)
- **重要度**: 5/10
- **タグ**: claude-code, setup, vscode

---

## 2026-03-23

### Ollama 0.18 × Claude Code 完全移行ガイド ── 「/v1ハック」を卒業してネイティブAPIでローカルLLMを本物のエージェントにする【2026年3月最新】

Ollama 0.18で、Claude CodeのネイティブAPIサポートが実装され、従来の/v1互換モード経由での接続時に発生していたツール呼び出しの不具合が解消されました。/api/chatエンドポイントによる正式統合により、ファイル操作やWeb検索などのエージェント機能が正常に動作するようになり、ollama launchコマンドで設定も簡略化されました。プライバシー重視ならローカルモデル、リアルタイム応答重視ならクラウドモデルの使い分けが推奨されています。

- **ソース**: [Qiita claude](https://qiita.com/AI-SKILL-LAB/items/6589c5124c391f923320)
- **重要度**: 7/10
- **タグ**: claude-code, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-23 | 自動生成 |
