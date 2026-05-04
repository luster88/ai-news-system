---
title: Mcp Server
category: tools
subcategory: mcp-server
tags:
- claude-api
- claude-code
- cowork
- mcp
- performance
- setup
- 新機能
date: '2026-03-25'
updated: '2026-05-04'
sources:
- url: https://zenn.dev/rimon/articles/11a680c4b530ab
  title: 【Claude Codeから画像生成】画像生成MCPを作ってnpmに公開した — Gemini / OpenAI / FLUX対応
  date: '2026-03-25'
- url: https://zenn.dev/nozomi720/articles/705d6d02a82226
  title: ホスティングサービスにUIを作らなかった理由——CLIとMCPを選んだ設計思想
  date: '2026-03-29'
- url: https://zenn.dev/jphfa/articles/markupsidedown-mcp-crawl-events
  title: MCPはオワコンではない。MarkUpsideDownでサイトをクロール（Cloudflare /crawl endpoint）した話。
  date: '2026-03-30'
- url: https://ai-heartland.com/mcp/tradingview-mcp
  title: TradingView MCP：Claude CodeからTradingViewを完全操作する78ツールのMCPサーバー
  date: '2026-04-02'
- url: https://ai-heartland.com/mcp/xmcp
  title: xmcp：X（旧Twitter）APIとClaudeを連携させるMCP実装ツール
  date: '2026-04-07'
- url: https://zenn.dev/claush/articles/6bcd60524fccfe
  title: SQLiteからCockroachDBに移行して、AIの記憶が「本物」になった話 —— iphoneアプリ Claush
  date: '2026-04-09'
- url: https://ai-heartland.com/explain/cognee-ai-memory-guide
  title: cognee完全ガイド：ナレッジグラフ型AIメモリの仕組みとClaude APIローカル連携・MCP設定手順
  date: '2026-04-16'
- url: https://ai-heartland.com/tool/browserbase-skills-claude-code-browser-automation
  title: Browserbase Skills徹底解説｜Claude Codeにブラウザ自動化10機能を授けるスキル集
  date: '2026-04-29'
- url: https://www.reddit.com/r/ClaudeAI/comments/1szvo7t/open_source_we_built_a_local_code_search_mcp_for
  title: Open Source] We built a local code search MCP for Claude Code that uses ~98%
    fewer tokens than grep+read
  date: '2026-04-30'
- url: https://ai-heartland.com/mcp/n8n-mcp
  title: n8n MCP｜Claude Codeから自然言語でn8nワークフローを構築するMCPサーバー
  date: '2026-05-04'
---










# Mcp Server

---

## 2026-05-04

### n8n MCP｜Claude Codeから自然言語でn8nワークフローを構築するMCPサーバー

n8n MCPは、ローコード自動化ツールn8nの1650ノードと2352テンプレートをModel Context Protocol経由でAIに提供するMCPサーバー。Claude CodeやCursorから自然言語でワークフローを構築でき、ノード仕様の詳細取得、テンプレート検索、検証、n8nインスタンスへの直接書き込みが可能。AIが辞書を引きながら設計することで幻覚を防ぎ、GitHub Dailyで19,728スターを獲得している。

- **ソース**: [AI Heartland](https://ai-heartland.com/mcp/n8n-mcp)
- **重要度**: 7/10
- **タグ**: mcp, claude-code

---

## 2026-04-30

### Open Source] We built a local code search MCP for Claude Code that uses ~98% fewer tokens than grep+read

Reddit ユーザーが Claude Code 向けのローカルコードサーチ MCP サーバー「Semble」をオープンソースで公開。grep+read と比較して約98%のトークン削減を実現し、CPU のみで動作。静的埋め込み、BM25、コード最適化された再ランキングスタックを組み合わせ、約250ms でインデックス作成、約1.5ms でクエリ応答が可能。API キーや GPU 不要で、ローカルリポジトリとリモートリポジトリの両方に対応。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1szvo7t/open_source_we_built_a_local_code_search_mcp_for)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, performance

---

## 2026-04-29

### Browserbase Skills徹底解説｜Claude Codeにブラウザ自動化10機能を授けるスキル集

Browserbase SkillsはClaude Codeにブラウザ自動化機能を追加するスキル集。npx一発でインストール可能で、10種類のスキル（browser/browser-trace/ui-test等）を提供。ローカルChromeとBrowserbaseクラウドの両方で動作し、CDPトレース・スクリーンショット・DOMスナップショットによる観測機能を備える。skills.shレジストリに公式登録され、GitHub Stars 595を獲得している。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/browserbase-skills-claude-code-browser-automation)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-04-16

### cognee完全ガイド：ナレッジグラフ型AIメモリの仕組みとClaude APIローカル連携・MCP設定手順

cogneeは「6行でAIエージェントに長期記憶を与える」GitHubスター15,000超のOSSナレッジエンジン。ベクトルRAGと異なり、ナレッジグラフ＋ベクトル検索＋セマンティックルールでエンティティ間の関係性を保持し、複合クエリに強い。ECLパイプライン（Extract-Cognify-Load）で生データを知識構造へ変換し、グラフDB・ベクトルDBの二重インデックスで格納。Claude APIとのローカル連携やMCP設定により、エージェントの永続的メモリ管理を実現する。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/cognee-ai-memory-guide)
- **重要度**: 7/10
- **タグ**: mcp, claude-api, cowork

---

## 2026-04-09

### SQLiteからCockroachDBに移行して、AIの記憶が「本物」になった話 —— iphoneアプリ Claush

Claush（Claude CodeをiPhoneから操作するiOSアプリ）の記憶システムを、SQLiteからCockroachDBに移行した事例。VPS再構築時に記憶が消失する課題を、マネージドDB採用で解決。ベクター検索によるセマンティック記憶検索も実現し、AIの長期記憶が「積み重なる」ものに変化した。

- **ソース**: [Zenn claude](https://zenn.dev/claush/articles/6bcd60524fccfe)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, cowork

---

## 2026-04-07

### xmcp：X（旧Twitter）APIとClaudeを連携させるMCP実装ツール

xmcpは、X（旧Twitter）APIとClaudeなどのLLMを連携させるMCP実装ツール。AnthropicのModel Context Protocol仕様に準拠し、AIエージェントがツイート投稿・分析・トレンド監視などのX API機能をプログラム的に操作できる。Python 3.9以上で動作し、センチメント分析やコンテンツ自動投稿などのユースケースに対応。MCPの実装例として学習教材としても有用。

- **ソース**: [AI Heartland](https://ai-heartland.com/mcp/xmcp)
- **重要度**: 6/10
- **タグ**: mcp, claude-api, 新機能

---

## 2026-04-02

### TradingView MCP：Claude CodeからTradingViewを完全操作する78ツールのMCPサーバー

TradingView MCPは、Claude CodeからTradingView Desktopを直接操作できる78ツール搭載のMCPサーバー。Chrome DevTools Protocolを使いローカル完結でチャート分析、Pine Script開発、アラート管理などを自然言語で実行可能。公開5日で403スターを獲得し、金融×AI×MCPの実用的な実装として注目されている。

- **ソース**: [AI Heartland](https://ai-heartland.com/mcp/tradingview-mcp)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, 新機能

---

## 2026-03-30

### MCPはオワコンではない。MarkUpsideDownでサイトをクロール（Cloudflare /crawl endpoint）した話。

MarkUpsideDownという自作Markdownエディタに内蔵したMCPサーバーを使い、Cloudflare Browser Rendering APIによるWebクロールをClaude Codeから簡単に実行する事例。従来のcurlベースの8ステップ手作業を、MCPツール経由で「please」の1語で自動化。41のツールを公開するRust製MCPサーバーで、extract_jsonツールがJSレンダリング・構造化データ抽出・結果取得を一発で実行する。

- **ソース**: [Zenn claude](https://zenn.dev/jphfa/articles/markupsidedown-mcp-crawl-events)
- **重要度**: 6/10
- **タグ**: mcp, claude-code

---

## 2026-03-29

### ホスティングサービスにUIを作らなかった理由——CLIとMCPを選んだ設計思想

MinToは「AIとの対話でWebサイトを作る」ホスティングサービスで、UIを作らずCLIとMCPのみで完結する設計を採用。ブラウザ操作はスクリーンショットによるトークン消費が数千トークンと大きく、日常利用には非現実的と判断。StreamableHTTPとOAuth 2.1対応のMCPサーバーを実装し、テキストベースで安全かつ低コストな操作を実現している。

- **ソース**: [Zenn claude](https://zenn.dev/nozomi720/articles/705d6d02a82226)
- **重要度**: 6/10
- **タグ**: mcp, claude-code, cowork

---

## 2026-03-25

### 【Claude Codeから画像生成】画像生成MCPを作ってnpmに公開した — Gemini / OpenAI / FLUX対応

Claude CodeやClaude Desktopで直接Gemini、OpenAI、FLUXを使った画像生成ができるMCPサーバーがnpmに公開されました。Claudeとの会話中にコンテキストを保ったまま画像生成が可能で、開発中のプロジェクトに直接画像を保存できます。Skills機能と組み合わせた高度なプロンプトエンジニアリングや、Notion MCPとの連携による絵日記生成など、実用的な活用例が紹介されています。

- **ソース**: [Zenn claude](https://zenn.dev/rimon/articles/11a680c4b530ab)
- **重要度**: 7/10
- **タグ**: mcp, claude-code, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-25 | 自動生成 |
