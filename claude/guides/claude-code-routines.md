---
title: Claude Code Routines
category: guides
subcategory: claude-code-routines
tags:
- bugfix
- claude-code
- cowork
- setup
- 新機能
date: '2026-05-07'
updated: '2026-09-01'
sources:
- url: https://ai-heartland.com/tool/claude-code-routines-ci-autofix
  title: Claude Code Routines完全解説｜Claudeが自分でClaude Codeを起動する非同期自動化
  date: '2026-05-07'
- url: https://qiita.com/nabeo_ji/items/0f808c1c2fea1ab328c5
  title: Claude Code にルーティンでニュース投稿をさせた話
  date: '2026-07-20'
- url: https://qiita.com/devex12/items/4ba5b8b076f366010bfa
  title: 個人開発のバッチを4本、Claude Code RemoteのRoutineで無人稼働させて分かったcron設計3パターンと権限設計チェックリスト
  date: '2026-08-14'
- url: https://zenn.dev/atamaplus/articles/6be03483c0110b
  title: PRレビューもエラー調査も定額で自動化する、Claude Codeのroutine活用実例
  date: '2026-09-01'
---




# Claude Code Routines

---

## 2026-09-01

### PRレビューもエラー調査も定額で自動化する、Claude Codeのroutine活用実例

Claude Codeのroutine機能を使った業務自動化の実例を紹介。定額プランで費用を気にせずPRレビューやエラー調査を自動化でき、スケジュール実行・GitHubイベント・APIトリガーに対応。毎朝の利用枠開始、セッション名整理、休暇予定の集計など8個の実運用例を紹介している。

- **ソース**: [Zenn claude](https://zenn.dev/atamaplus/articles/6be03483c0110b)
- **重要度**: 7/10
- **タグ**: claude-code, cowork, 新機能

---

## 2026-08-14

### 個人開発のバッチを4本、Claude Code RemoteのRoutineで無人稼働させて分かったcron設計3パターンと権限設計チェックリスト

Claude Code RemoteのRoutineで4本のバッチを無人稼働させた実践記録。cronはUTC入力必須でJST換算が必要な点、「push・PR作成はOK、mainへの直接コミットと自動マージは禁止」という権限設計をプロンプトの明示的禁止文言で担保した点、ネットワークポリシーでAPIアクセスがブロックされる可能性があるため単一経路設計は避けるべき点を解説。日次・時次・営業時間帯限定の3パターンのcron設計と、allowed_toolsだけでは分離できない権限制御の実装方法を共有。

- **ソース**: [Qiita claudecode](https://qiita.com/devex12/items/4ba5b8b076f366010bfa)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-07-20

### Claude Code にルーティンでニュース投稿をさせた話

Claude Code のルーティン機能を使って、パーソナライズされたニュース収集と Slack 通知の自動化を試みた事例。当初は GitHub への Push を経由する構成を試したが、ルーティンが毎回新しいブランチを作成してしまい main ブランチへの直接 Push ができない問題に遭遇。最終的に GitHub 連携を廃止し、Claude Code ルーティンから直接 Slack へ通知する単純な構成に変更することで解決した。

- **ソース**: [Qiita claudecode](https://qiita.com/nabeo_ji/items/0f808c1c2fea1ab328c5)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, bugfix

---

## 2026-05-07

### Claude Code Routines完全解説｜Claudeが自分でClaude Codeを起動する非同期自動化

Claude Code Routinesは、2026年4月にリリースされた研究プレビュー機能で、「プロンプト+リポジトリ+連携先」を保存し自動実行する仕組み。Boris Chernyが「Claudeが自分でClaude Codeを起動する」という高階プロンプトとして紹介。schedule・API・GitHub eventの3つのトリガータイプを持ち、Anthropicのクラウドインフラ上で非同期実行される。研究プレビュー段階のため、APIサーフェスや挙動は変更される可能性がある。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/claude-code-routines-ci-autofix)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-07 | 自動生成 |
