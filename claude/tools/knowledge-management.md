---
title: Knowledge Management
category: tools
subcategory: knowledge-management
tags:
- claude-api
- claude-code
- cowork
- mcp
- prompt
- 新機能
date: '2026-06-15'
updated: '2026-11-01'
sources:
- url: https://ai-heartland.com/explain/claude-memory-compiler-guide
  title: Claude Memory Compilerとは｜会話を知識ベースに自動コンパイルするOSS
  date: '2026-06-15'
- url: https://zenn.dev/n1labo/articles/c29fc8b85f648b
  title: 複数のAIの回答だけを集める「個人ナレッジ庫」という発想（需要テスト中）
  date: '2026-11-01'
---


# Knowledge Management

---

## 2026-11-01

### 複数のAIの回答だけを集める「個人ナレッジ庫」という発想（需要テスト中）

複数のAI（ChatGPT、Claude、Gemini）の回答を一元管理し、後から検索・再利用できる「個人ナレッジ庫」ツールのコンセプト記事。NotionやObsidianのような「置き場」ではなく、AIの画面から直接保存でき、Markdown形式で持ち出せる仕組みを提案。ウェイトリスト50件で開発開始する需要テストを実施中。

- **ソース**: [Zenn claude](https://zenn.dev/n1labo/articles/c29fc8b85f648b)
- **重要度**: 4/10
- **タグ**: cowork, prompt, claude-api

---

## 2026-06-15

### Claude Memory Compilerとは｜会話を知識ベースに自動コンパイルするOSS

Claude Memory Compilerは、Claude Codeとの会話を検索可能な個人知識ベースへ自動コンパイルするOSSです。Andrej Karpathy氏のLLM Knowledge Baseアーキテクチャを会話に適用し、SessionEnd/PreCompactフックで会話を自動キャプチャ、Claude Agent SDKで重要点を抽出してmarkdown記事へ組み上げます。RAGやベクトルDBを使わず、LLMがmarkdownのindex.mdを読んで関連記事を選ぶ方式で、個人規模では高精度を実現。認証はClaude Code組み込みを使用し、APIキー不要でClaudeサブスクの範囲内で利用できます。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-memory-compiler-guide)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-15 | 自動生成 |
