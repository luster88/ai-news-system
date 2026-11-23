---
title: Code Mode Performance
category: troubleshooting
subcategory: code-mode-performance
tags:
- claude-code
- performance
- 新機能
date: '2026-11-23'
updated: '2026-11-23'
sources:
- url: https://qiita.com/hatyibei/items/3b7fdc74936f98913451
  title: Claude CodeのCode Modeを18回比べた：API往復は減らず、入力トークンは約4割減
  date: '2026-11-23'
---

# Code Mode Performance

---

## 2026-11-23

### Claude CodeのCode Modeを18回比べた：API往復は減らず、入力トークンは約4割減

Claude CodeのCode Modeのオン/オフで18セッションを比較検証した結果、API往復回数は減らず、入力トークンは約4割減（0.62-0.64倍）となった。これは主にツール定義が15個から2個に削減されたことが原因。ただしAPI料金換算では0.91-0.93倍程度で、短い作業での測定値のため長い会話では効果は小さくなる見込み。claude -pモードでは機能しないことも判明。

- **ソース**: [Qiita claudecode](https://qiita.com/hatyibei/items/3b7fdc74936f98913451)
- **重要度**: 6/10
- **タグ**: claude-code, performance, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-23 | 自動生成 |
