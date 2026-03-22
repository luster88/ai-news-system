---
title: "Claude エコシステム情報"
category: index
tags: [claude, ecosystem, index]
date: 2026-03-23
updated: 2026-03-23
---

# Claude エコシステム情報

Claude / Claude Code / Claude Console および関連ツールの最新情報を収集・整理するセクションです。

---

## カテゴリ一覧

| カテゴリ | 内容 |
|----------|------|
| [releases/](releases/) | リリースノート・アップデート情報（モデル・Claude Code・Console・API） |
| [guides/](guides/) | セットアップ手順・ワークフロー・ベストプラクティス |
| [tools/](tools/) | 関連ツール比較・MCP サーバー・連携情報 |
| [prompts/](prompts/) | プロンプトテンプレート・エンジニアリング技法 |
| [troubleshooting/](troubleshooting/) | よくあるエラーと対処法・環境別の問題 |
| [ecosystem/](ecosystem/) | 料金・プラン・コミュニティ動向・競合比較 |

---

## 方針

- **日本語でまとめる**（ソースは英語/日本語混在）
- **重複排除**: 同じトピックは1箇所に集約し、日付付きで追記
- **蓄積型**: 過去の情報は削除せず、最新情報を上に追記
- **ソース明記**: 各情報に出典 URL と日付を記載
- **カテゴリ横断の相互リンク**: 関連する記事同士をリンクで接続

---

## 更新ルール

- 新しい情報を追加したら `updated` フィールドを更新する
- 大きなリリース情報は `releases/` に、使い方は `guides/` に分離する
- 既存ファイルのトピックに該当する情報は新規ファイルを作らず追記する
- ソースの URL は `sources` frontmatter に記録する

---

## Frontmatter 仕様

```yaml
---
title: "記事タイトル"
category: releases          # releases / guides / tools / prompts / troubleshooting / ecosystem
subcategory: claude-code    # カテゴリ内のサブ分類
tags: [claude-code, release]
date: 2026-03-23            # 作成日
updated: 2026-03-23         # 最終更新日
sources:
  - url: "https://..."
    title: "ソースのタイトル"
    date: 2026-03-22
---
```
