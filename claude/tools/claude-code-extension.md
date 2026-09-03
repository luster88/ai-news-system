---
title: Claude Code Extension
category: tools
subcategory: claude-code-extension
tags:
- claude-code
- cowork
- prompt
- setup
- 新機能
date: '2026-05-10'
updated: '2026-09-03'
sources:
- url: https://zenn.dev/jun_eng/articles/71012bb4d0cf51
  title: Claude Code を10倍使いやすくするスラッシュコマンド集を作って公開した
  date: '2026-05-10'
- url: https://ai-heartland.com/explain/claudeclaw-guide
  title: ClaudeClawとは｜Claude Codeを常駐デーモン化しTelegram/Slackから動かすOSS
  date: '2026-06-13'
- url: https://zenn.dev/penpeen/articles/035351eeffcaec
  title: Claude Code の /resume が探しにくいので、会話履歴を全文検索するスキルを作った
  date: '2026-09-03'
---



# Claude Code Extension

---

## 2026-09-03

### Claude Code の /resume が探しにくいので、会話履歴を全文検索するスキルを作った

Claude Code の /resume 機能はタイトルのみ検索対象で会話内容が検索できないため、会話ログ全文を検索できるカスタムスキルが開発された。~/.claude/ 配下の JSONL ファイルを直接検索し、ripgrep で高速に過去セッションを発見できる。GitHub で公開されており、インストール後すぐに利用可能。

- **ソース**: [Zenn claude](https://zenn.dev/penpeen/articles/035351eeffcaec)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-06-13

### ClaudeClawとは｜Claude Codeを常駐デーモン化しTelegram/Slackから動かすOSS

ClaudeClawは、Claude Codeを常駐デーモン化し、24時間稼働させるMITライセンスのOSSツールです。Telegram/Discord/Slackからの操作、cronスケジュール実行、heartbeat監視に対応し、Webダッシュボードで管理できます。Claude Codeのラッパーとして機能し、追加APIキー不要で既存のサブスクリプションをそのまま利用可能です。2026年2月公開、1,100★超のTypeScript製プロジェクトで、14日ごとに約1.5万ダウンロードの規模を持ちます。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claudeclaw-guide)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-05-10

### Claude Code を10倍使いやすくするスラッシュコマンド集を作って公開した

Claude Code のスラッシュコマンド機能を活用した「Claude Code Power Pack」が公開された。コードレビュー、テスト生成、PR説明文生成など、日常的に使うプロンプトを11個のコマンドとして標準化。~/.claude/commands/ にマークダウンファイルを配置することで、再現性の高い固定フォーマットの出力が得られる。GitHub でオープンソースとして公開されており、コミュニティからのフィードバックも受け付けている。

- **ソース**: [Zenn claude](https://zenn.dev/jun_eng/articles/71012bb4d0cf51)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-10 | 自動生成 |
