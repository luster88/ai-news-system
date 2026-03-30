---
title: Mcp Server
category: tools
subcategory: mcp-server
tags:
- claude-code
- cowork
- mcp
- 新機能
date: '2026-03-25'
updated: '2026-03-30'
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
---



# Mcp Server

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
