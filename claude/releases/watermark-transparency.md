---
title: Watermark Transparency
category: releases
subcategory: watermark-transparency
tags:
- claude-api
- release
- 新機能
date: '2026-08-11'
updated: '2026-08-12'
sources:
- url: https://the-decoder.com/anthropic-watermarks-all-claude-outputs-globally-with-marks-that-may-persist-through-some-editing
  title: Anthropic watermarks all Claude outputs globally with marks that "may persist
    through some editing"
  date: '2026-08-11'
- url: https://zenn.dev/jeong/articles/3c5c5431b5109d
  title: Claudeが生成テキストに「見えない透かし」を入れ始めた件を整理する
  date: '2026-08-12'
---


# Watermark Transparency

---

## 2026-08-12

### Claudeが生成テキストに「見えない透かし」を入れ始めた件を整理する

2026年8月11日、AnthropicがClaude生成テキストに人間には知覚できないウォーターマーク（透かし）を埋め込むことを公式発表。EU AI Act対応として8月2日以降のモデルに適用され、日本含む全世界が対象。テキストはモデルレベルでのサンプリング過程に統計的信号を埋め込む方式（Green-list方式など）と推定され、C2PA標準に準拠した画像メタデータ署名も実施。コピー＆ペーストでも透かしは残り、編集後も検出可能な設計。

- **ソース**: [Zenn claude](https://zenn.dev/jeong/articles/3c5c5431b5109d)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, release

---

## 2026-08-11

### Anthropic watermarks all Claude outputs globally with marks that "may persist through some editing"

Anthropic が EU AI Act に署名し、2026年8月から全 Claude モデルに透かし（ウォーターマーク）を実装することを発表。テキストには不可視の透かしが埋め込まれ、画像などのファイルには C2PA 標準の署名付きメタデータが付与される。この要件は EU だけでなく世界中の Claude 製品（API、Claude Code、Claude Cowork など）に適用される。透かしはコピー＆ペーストや一部の編集を経ても残る可能性があるが、大幅な編集やフォーマット変更で除去される場合もある。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-watermarks-all-claude-outputs-globally-with-marks-that-may-persist-through-some-editing)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-11 | 自動生成 |
