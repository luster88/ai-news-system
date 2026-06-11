---
title: Claude Code Integration
category: guides
subcategory: claude-code-integration
tags:
- claude-code
- cowork
- mcp
- prompt
- setup
- 新機能
date: '2026-04-02'
updated: '2026-06-11'
sources:
- url: https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code
  title: Claude CodeでAI RSSリーダーを作ったら、その日にInoreaderを解約した
  date: '2026-04-02'
- url: https://qiita.com/Tadashi_Kudo/items/c35c0aaed00878d88b05
  title: ObsidianとClaude Codeで作る「第二の脳」——Vault自動管理の全体設計
  date: '2026-04-24'
- url: https://qiita.com/ikkun9595/items/56ae15af2e6dfc106ea1
  title: HTMLで動画を作る HyperFrames をClaude Codeから動かしてみた検証メモ
  date: '2026-05-07'
- url: https://qiita.com/daizou703/items/3e47d8b7ecc0bcf60eb1
  title: Claude Code × Microsoft Fabric (3) － Power BI レポートを AI に作らせる：.pbip を使ったビジュアルページの自動生成
  date: '2026-05-19'
- url: https://qiita.com/sescore/items/3bebfa78a916ca44316f
  title: OpenClaw×Claude Code連携で変わる開発体験——実践コマンドと具体ユースケース完全解説【2026年】
  date: '2026-06-11'
---





# Claude Code Integration

---

## 2026-06-11

### OpenClaw×Claude Code連携で変わる開発体験——実践コマンドと具体ユースケース完全解説【2026年】

OpenClawとClaude Codeを組み合わせた開発フローを解説。OpenClawが「思考・記憶・指示」を担当し、Claude Codeが「開発・実行」を担当する役割分担により、セッションをまたいだ文脈保持が可能になる。実践コマンド、単価相場調査、スキルアップ戦略立案などの具体的ユースケースを紹介し、SESエンジニアのキャリア形成にも言及している。

- **ソース**: [Qiita claude](https://qiita.com/sescore/items/3bebfa78a916ca44316f)
- **重要度**: 4/10
- **タグ**: claude-code, cowork, setup

---

## 2026-05-19

### Claude Code × Microsoft Fabric (3) － Power BI レポートを AI に作らせる：.pbip を使ったビジュアルページの自動生成

Power BI レポートを .pbip 形式で保存すると、レポート定義が JSON に分解され、Claude Code が直接 visual.json を生成できる。Semantic Model が整備されていれば、Entity/Property の指定だけでデータバインディングが完了し、30+ページ・90+ビジュアルを AI 駆動で生成可能。/pbip-visual という Claude Code Skill にパッケージング済みで、Power BI Desktop を開かずにレポートプロジェクトを初期セットアップできる。

- **ソース**: [Qiita claudecode](https://qiita.com/daizou703/items/3e47d8b7ecc0bcf60eb1)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-05-07

### HTMLで動画を作る HyperFrames をClaude Codeから動かしてみた検証メモ

HeyGenがオープンソース公開したHyperFramesを、Claude Codeと組み合わせて動かすまでの検証記録。HyperFramesはHTML/CSS/JavaScriptで書いたコンポジションをヘッドレスChromeでキャプチャし、FFmpegでMP4に変換する動画レンダリングフレームワーク。skills CLIが`.agents/skills/`にスキルを配置する一方、Claude Codeが`.claude/skills/`を参照するパスのズレが原因でスキルが認識されない問題が発生し、シンボリックリンクで解決。GSAPタイムラインを`paused: true`で作成し`window.__timelines`に登録する規約など、実装上の注意点も解説。

- **ソース**: [Qiita claude](https://qiita.com/ikkun9595/items/56ae15af2e6dfc106ea1)
- **重要度**: 6/10
- **タグ**: claude-code, setup

---

### HTMLで動画を作る HyperFrames をClaude Codeから動かしてみた検証メモ

HeyGenがオープンソース公開したHyperFramesをClaude Codeで動作検証した記事。HyperFramesはHTML/CSS/JSで書いたコンポジションをヘッドレスChromeでキャプチャしFFmpegで動画化する決定論的レンダリングフレームワーク。スキルがClaude Codeに認識されない問題は、.agents/skills/と.claude/skills/のパス不一致が原因で、シンボリックリンクで解決。GSAPタイムラインのpaused:true指定など、動画レンダリングの規約とワークフローを詳細に解説している。

- **ソース**: [Qiita claudecode](https://qiita.com/ikkun9595/items/56ae15af2e6dfc106ea1)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 2026-04-24

### ObsidianとClaude Codeで作る「第二の脳」——Vault自動管理の全体設計

ObsidianとClaude Codeを組み合わせ、AIエージェントが自動的にVaultを管理する「第二の脳」システムの設計を紹介。CLAUDE.mdによる行動ルール明文化、MEMORY.mdでの状態永続化、scheduled-tasksによる定期メンテ自動化、ベクトル検索MCPによる概念検索、Gitによる変更履歴管理の5つの要素で構成される。AIに整理・検索・連携を任せることで、ノート作成に集中できる環境を実現する。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/c35c0aaed00878d88b05)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-04-02

### Claude CodeでAI RSSリーダーを作ったら、その日にInoreaderを解約した

Claude Code CLIの-pオプションを活用したパーソナライズRSSリーダー「Feed Curator」の開発事例。APIキー不要でClaude Codeの認証を流用し、既読履歴から嗜好を学習して技術ブリーフィングを自動生成。トークン消費を抑えるため記事全文ではなく先頭500文字+末尾300文字のみ送信し、1日2-4万トークンで運用可能。開発当日にInoreaderを解約した実体験レポート。

- **ソース**: [Zenn claude](https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-02 | 自動生成 |
