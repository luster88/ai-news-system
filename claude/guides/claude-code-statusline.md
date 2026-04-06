---
title: Claude Code Statusline
category: guides
subcategory: claude-code-statusline
tags:
- claude-code
- prompt
- setup
date: '2026-04-06'
updated: '2026-04-06'
sources:
- url: https://qiita.com/kiyotaman/items/d2a277b00acad4e1a3c5
  title: Claude Code の statusLine を自作する ― モデル / コンテキスト / レート制限を 2〜3 行で全部見せる
  date: '2026-04-06'
---

# Claude Code Statusline

---

## 2026-04-06

### Claude Code の statusLine を自作する ― モデル / コンテキスト / レート制限を 2〜3 行で全部見せる

Claude Code の statusLine 機能を活用し、bash + jq で現在のモデル名、コンテキスト使用量、レート制限情報を2〜3行で常時表示する方法を解説。settings.json に任意のコマンドを登録し、stdin 経由で受け取る JSON を整形することで、長時間作業中のコンテキスト枯渇やレート制限到達を視覚的に防げる。デバッグ用の環境変数設定、jq の効率的な呼び出し方、macOS/Linux 両対応の日時処理など、実装上の細かいノウハウが詰まった実践的ガイド。

- **ソース**: [Qiita claude](https://qiita.com/kiyotaman/items/d2a277b00acad4e1a3c5)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-06 | 自動生成 |
