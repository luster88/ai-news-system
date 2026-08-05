---
title: Mcp Server Design
category: guides
subcategory: mcp-server-design
tags:
- cowork
- mcp
- setup
date: '2026-08-05'
updated: '2026-08-05'
sources:
- url: https://zenn.dev/knottle/articles/34f45544848d3e
  title: AIエージェントに「取り消せる操作」と「取り消せない操作」を区別させる設計 ― 電子帳簿保存法対応から考えるMCPツール設計
  date: '2026-08-05'
---

# Mcp Server Design

---

## 2026-08-05

### AIエージェントに「取り消せる操作」と「取り消せない操作」を区別させる設計 ― 電子帳簿保存法対応から考えるMCPツール設計

AIエージェントに業務システムを操作させる際の安全性設計について、電子帳簿保存法の要件を題材に解説。国産CRM「Knottle」のMCP実装を例に、不可逆操作と修正操作をツールレベルで分離し、拒否条件をサーバー側で制御する設計パターンを提示。発行日のバックデート防止のため入力パラメータから除外するなど、プロンプトではなくインターフェース設計で制約を実現する手法を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/knottle/articles/34f45544848d3e)
- **重要度**: 7/10
- **タグ**: mcp, setup, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-05 | 自動生成 |
