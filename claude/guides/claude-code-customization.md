---
title: Claude Code Customization
category: guides
subcategory: claude-code-customization
tags:
- claude-code
- mac
- prompt
- setup
- vscode
- 新機能
date: '2026-03-29'
updated: '2026-04-22'
sources:
- url: https://zenn.dev/noprogllama/articles/d6a34cce09b66d
  title: AIに人格と記憶を与えたら、常につながる手段が欲しくなって自前のWeb UIを作ることになった
  date: '2026-03-29'
- url: https://qiita.com/kiyotaman/items/d2a277b00acad4e1a3c5
  title: Claude Code の statusLine を自作する ― モデル / コンテキスト / レート制限を 2〜3 行で全部見せる
  date: '2026-04-06'
- url: https://qiita.com/s_hiroki/items/307e39f9ed763cb28d6f
  title: Claude Codeが付けるCo-Authored-ByとGenerated with Claude Codeを非表示にする
  date: '2026-04-09'
- url: https://zenn.dev/ren21/articles/e5eb47c2789b0a
  title: Claude Code のステータスラインをカスタマイズしてみた
  date: '2026-04-18'
- url: https://qiita.com/hiranuma/items/793b49360d5d814a686f
  title: Claude Codeのセッション使用率をターミナルに常時表示するstatusLineスクリプトの作り方
  date: '2026-04-22'
---





# Claude Code Customization

---

## 2026-04-22

### Claude Codeのセッション使用率をターミナルに常時表示するstatusLineスクリプトの作り方

Claude Codeのstatusline機能を使い、セッション使用率（5時間枠）と週間使用率（7日枠）をターミナル下部にカラー付きプログレスバーで常時表示するスクリプトの実装方法を解説。/statuslineコマンドによる自動生成のほか、macOS標準のPython3を使った手動セットアップ方法も紹介。ANSIカラー対応ターミナルで動作し、APIトークンを消費しない。

- **ソース**: [Qiita claudecode](https://qiita.com/hiranuma/items/793b49360d5d814a686f)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 2026-04-18

### Claude Code のステータスラインをカスタマイズしてみた

Claude Code のステータスラインカスタマイズ方法を解説。Claude と対話するだけで、コンテキスト使用率・レート制限・セッション名などをビジュアル表示できる。jq の代わりに Node.js を使った実装例や、ブロックバーを使った直感的な表示方法を紹介。/statusline スキルで簡単に設定変更可能。

- **ソース**: [Zenn claude](https://zenn.dev/ren21/articles/e5eb47c2789b0a)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-09

### Claude Codeが付けるCo-Authored-ByとGenerated with Claude Codeを非表示にする

Claude Code が自動で付与する Co-Authored-By タグや Generated with Claude Code の表記を非表示にする方法を解説。settings.json に claude.commit.showCoAuthor と claude.pullRequest.showGenerated を false に設定することで、Commit メッセージや PR コメントに Claude の署名が表示されなくなる。公式ドキュメントでは非推奨の記法も紹介されているが、推奨設定により両方を一括で非表示可能。

- **ソース**: [Qiita claudecode](https://qiita.com/s_hiroki/items/307e39f9ed763cb28d6f)
- **重要度**: 5/10
- **タグ**: claude-code, vscode, setup

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
