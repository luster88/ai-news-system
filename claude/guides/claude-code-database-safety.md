---
title: Claude Code Database Safety
category: guides
subcategory: claude-code-database-safety
tags:
- claude-code
- prompt
- setup
date: '2026-11-24'
updated: '2026-11-24'
sources:
- url: https://zenn.dev/h1us3h/articles/85b292cb275c4f
  title: 本番DBしかない個人アプリで、Claude Codeに時刻表データ更新を任せてみた
  date: '2026-11-24'
---

# Claude Code Database Safety

---

## 2026-11-24

### 本番DBしかない個人アプリで、Claude Codeに時刻表データ更新を任せてみた

個人開発の名古屋市営バスアプリで、本番DB環境しかない状況下でClaude Codeに時刻表データ更新を安全に任せる取り組み。CLAUDE.md、settings.json、pre-execute hooksを組み合わせて、本番DBへの誤操作を防ぐ「ハーネスエンジニアリング」を実践。環境変数ファイルの読み取り禁止、本番DBへの書き込みコマンドの遮断、副作用のあるRPC呼び出しの防止などを実装し、約59万行のデータ更新を安全に検証できる環境を構築した事例。

- **ソース**: [Zenn claude](https://zenn.dev/h1us3h/articles/85b292cb275c4f)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-24 | 自動生成 |
