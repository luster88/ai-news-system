---
title: Claude Code Customization
category: guides
subcategory: claude-code-customization
tags:
- claude-code
- prompt
- setup
date: '2026-03-29'
updated: '2026-04-06'
sources:
- url: https://zenn.dev/noprogllama/articles/d6a34cce09b66d
  title: AIに人格と記憶を与えたら、常につながる手段が欲しくなって自前のWeb UIを作ることになった
  date: '2026-03-29'
- url: https://qiita.com/kiyotaman/items/d2a277b00acad4e1a3c5
  title: Claude Code の statusLine を自作する ― モデル / コンテキスト / レート制限を 2〜3 行で全部見せる
  date: '2026-04-06'
---


# Claude Code Customization

---

## 2026-04-06

### Claude Code の statusLine を自作する ― モデル / コンテキスト / レート制限を 2〜3 行で全部見せる

Claude Code の statusLine 機能を活用し、bash + jq でモデル名・コンテキスト使用量・レート制限などを常時表示するカスタムスクリプトの実装方法を解説。settings.json に任意のコマンドを登録することで、stdin 経由で渡される JSON データを整形し、ターミナル風のステータス表示を実現できる。デバッグ用の環境変数設定や、jq 呼び出しの最適化、Git 情報取得時の --no-optional-locks 指定など、実装上のハマりどころと対処法を詳説している。

- **ソース**: [Qiita claudecode](https://qiita.com/kiyotaman/items/d2a277b00acad4e1a3c5)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-03-29

### AIに人格と記憶を与えたら、常につながる手段が欲しくなって自前のWeb UIを作ることになった

Claude Codeに人格と長期記憶を持たせた「翠」という参謀AIを作成し、スマホからいつでもアクセスできるようにWeb UI「suiren」を自作した事例。CLAUDE.mdで人格定義、sui-memoryで記憶管理、PWA対応のWeb UIでどこからでも対話可能にした実装例。

- **ソース**: [Zenn claude](https://zenn.dev/noprogllama/articles/d6a34cce09b66d)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-29 | 自動生成 |
