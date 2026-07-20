---
title: Architecture Design
category: guides
subcategory: architecture-design
tags:
- claude-api
- claude-code
- cowork
- prompt
date: '2026-04-07'
updated: '2026-07-20'
sources:
- url: https://qiita.com/mellowlaunch/items/a4d7f66bcea582429936
  title: スペック駆動開発入門 ～SaaSを「交換可能な部品」にする設計
  date: '2026-04-07'
- url: https://zenn.dev/ryosuke_tanabe/articles/3f9296e2c672ba
  title: GeminiをやめてClaudeにしたら、コードが190行になった
  date: '2026-07-20'
---


# Architecture Design

---

## 2026-07-20

### GeminiをやめてClaudeにしたら、コードが190行になった

半年かけて構築したGemini + Google Drive APIベースの外部脳システムを、Claudeによるローカルファイル書き込み + OS同期に置き換えたところ、コードが190行に収束した事例。公式APIへの依存が設計を複雑化させる「公式性の罠」と、核心（SSOT）と周辺（インフラ）の分離による移植性の重要性を論じている。

- **ソース**: [Zenn claude](https://zenn.dev/ryosuke_tanabe/articles/3f9296e2c672ba)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 2026-04-07

### スペック駆動開発入門 ～SaaSを「交換可能な部品」にする設計

SaaSを「交換可能な部品」にするスペック駆動開発の設計思想を解説。Behaviorスペックで業務ロジックを定義し、アダプターパターンで実装層を分離することで、Salesforceなどの特定SaaSに依存しない柔軟なシステム設計を実現する方法を、注文承認のユースケースとPythonコードで具体化している。

- **ソース**: [Qiita claudecode](https://qiita.com/mellowlaunch/items/a4d7f66bcea582429936)
- **重要度**: 5/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-07 | 自動生成 |
