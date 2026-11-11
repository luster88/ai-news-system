---
title: Mcp Server Design
category: guides
subcategory: mcp-server-design
tags:
- claude-api
- cowork
- mcp
- setup
date: '2026-08-05'
updated: '2026-11-11'
sources:
- url: https://zenn.dev/knottle/articles/34f45544848d3e
  title: AIエージェントに「取り消せる操作」と「取り消せない操作」を区別させる設計 ― 電子帳簿保存法対応から考えるMCPツール設計
  date: '2026-08-05'
- url: https://zenn.dev/gear_aiteam/articles/logics-ui-and-mcp-from-one-table
  title: 画面とMCPを「操作の表」1つから作る：個人アプリにAIの手足を付ける方法
  date: '2026-11-11'
---


# Mcp Server Design

---

## 2026-11-11

### 画面とMCPを「操作の表」1つから作る：個人アプリにAIの手足を付ける方法

個人開発のWebアプリで、画面UIとMCPツールを「操作の表」1つから自動生成する設計パターンを紹介。domain.jsに操作を1つ書くだけで、REST APIとMCPツールが同時に生成され、ずれが起きない仕組み。Supabase + Vercelで動作し、テストで一貫性を保証。

- **ソース**: [Zenn claude](https://zenn.dev/gear_aiteam/articles/logics-ui-and-mcp-from-one-table)
- **重要度**: 7/10
- **タグ**: mcp, claude-api, setup

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
