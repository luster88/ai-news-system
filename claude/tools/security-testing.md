---
title: Security Testing
category: tools
subcategory: security-testing
tags:
- claude-code
date: '2026-11-09'
updated: '2026-11-09'
sources:
- url: https://ai-heartland.com/security/pentestgpt
  title: PentestGPTとは｜論文の対話型とClaude Codeを動かす自律型、2つの中身と注意点
  date: '2026-11-09'
---

# Security Testing

---

## 2026-11-09

### PentestGPTとは｜論文の対話型とClaude Codeを動かす自律型、2つの中身と注意点

PentestGPTは、論文ベースの対話型（legacy）とClaude Code/Codex CLI を使う自律型（agent）の2種類が存在する。対話型は人がコマンドを実行し、LLMが提案を行う。自律型はFULL_ACCESS権限でCLIが自律動作するため、隔離された使い捨て環境での実行が必須。README記載の成功率86.5%は過去データで、起動コマンドの定義も不明瞭。ペネトレーションテスト支援OSSとして、使用前に動作モード・権限範囲・データ送信先を確認する必要がある。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/pentestgpt)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-09 | 自動生成 |
