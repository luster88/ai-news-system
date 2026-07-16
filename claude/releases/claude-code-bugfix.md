---
title: Claude Code Bugfix
category: releases
subcategory: claude-code-bugfix
tags:
- bugfix
- claude-code
- pricing
date: '2026-07-16'
updated: '2026-07-16'
sources:
- url: https://qiita.com/moha0918_/items/c8b144e3ba36744b964b
  title: Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説
  date: '2026-07-16'
---

# Claude Code Bugfix

---

## 2026-07-16

### Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説

Claude Code v2.1.211がリリースされ、Bedrock/Vertex/Mantle/Foundryでプロンプトキャッシュが機能せず、システムコンテキストの末尾が毎回新規トークンとして課金されていた重大なバグが修正されました。この不具合により、ゲートウェイ経由での会話が重なるほど無駄な入力トークン課金が積み上がっていました。新機能は--forward-subagent-textフラグの追加のみで、その他は権限とキャッシュ周りの挙動修正が中心となっています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/c8b144e3ba36744b964b)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-16 | 自動生成 |
