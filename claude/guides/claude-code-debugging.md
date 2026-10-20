---
title: Claude Code Debugging
category: guides
subcategory: claude-code-debugging
tags:
- bugfix
- claude-code
- mac
- prompt
- setup
date: '2026-03-22'
updated: '2026-10-20'
sources:
- url: https://qiita.com/Akkami/items/5580361e3426198ff54a
  title: Claude Codeでデバッグするなら「ベテランの感覚」をCLAUDE.mdとSkillsに埋め込め
  date: '2026-03-22'
- url: https://zenn.dev/leegrey/articles/4f3cf300dd8aac
  title: 【完全版】Claude Code コマンド・ショートカット全集：次世代AIエージェントを使いこなす
  date: '2026-03-25'
- url: https://www.reddit.com/r/ClaudeAI/comments/1x9smgq/claude_caught_a_cryptominer_on_my_mac_whilst
  title: Claude caught a cryptominer on my Mac whilst building me a temperature monitor
    app
  date: '2026-10-20'
---



# Claude Code Debugging

---

## 2026-10-20

### Claude caught a cryptominer on my Mac whilst building me a temperature monitor app

ユーザーが Claude Code に Mac の温度モニターアプリを作成させたところ、センサーの値が異常に高かったため、Claude が CPU 使用率をチェック。その結果、12 コア分（約 1175% CPU）を消費するクリプトマイナー（xmrig）が動作していることを発見した。Claude の問題解決能力とデバッグスキルを示す興味深い事例。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1x9smgq/claude_caught_a_cryptominer_on_my_mac_whilst)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, mac

---

## 2026-03-25

### 【完全版】Claude Code コマンド・ショートカット全集：次世代AIエージェントを使いこなす

Claude Code（CLIエージェントツール）の全コマンド・ショートカットを網羅したリファレンス記事。基本操作から初期設定、コスト管理まで、実務で使うための完全ガイド。/init、/ls、/add、/drop などのコマンドを活用したワークフロー構築により、ターミナル上でAIと協働しながら設計からデプロイまで完結できる開発体験を実現する。

- **ソース**: [Zenn claude](https://zenn.dev/leegrey/articles/4f3cf300dd8aac)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 2026-03-22

### Claude Codeでデバッグするなら「ベテランの感覚」をCLAUDE.mdとSkillsに埋め込め

Claude Codeでのデバッグ精度を高めるため、ベテランエンジニアの知見をCLAUDE.mdとSkillsに体系的に埋め込む方法を解説。CLAUDE.mdには過去の実障害や地雷情報を200行以内で記載し、Skillsには再利用可能なデバッグワークフローを定義することで、毎回プロンプトを書かずに現場特有の知識を自動適用できる。Claude Codeの強みであるファイル直接読み取り機能を活かし、ログやコードのパスを指定する「材料を教える」アプローチが効果的。

- **ソース**: [Qiita claude](https://qiita.com/Akkami/items/5580361e3426198ff54a)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-22 | 自動生成 |
