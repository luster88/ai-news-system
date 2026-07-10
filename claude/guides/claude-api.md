---
title: Claude Api
category: guides
subcategory: claude-api
tags:
- claude-api
- cowork
- haiku
- opus
- performance
- prompt
- setup
- 新機能
date: '2026-03-25'
updated: '2026-07-10'
sources:
- url: https://zenn.dev/qinritukou/articles/git-ai-commit
  title: 「fix」とか「update」しか書かないそこのあなたへ。Claudeにコミットメッセージを丸投げする最強エイリアス
  date: '2026-03-25'
- url: https://zenn.dev/ai_eris_log/articles/claude-extended-thinking-20260407
  title: Claude APIのExtended Thinkingを使いこなす——どんなタスクで効果があるか検証した
  date: '2026-04-07'
- url: https://qiita.com/kai_kou/items/9aa2ca4787306e4dc162
  title: Claude Managed Agents入門 — セルフホスト不要でAIエージェントを動かすAPIガイド
  date: '2026-04-14'
- url: https://zenn.dev/nora_saito/articles/46e2d3fdefdf54
  title: Next.js × Claude APIで「読書メモ→X投稿」ツールを作って公開した（zodのバグに最後ハマった）
  date: '2026-06-08'
- url: https://zenn.dev/osakayakyu/articles/2901e4599ff819
  title: Claudeに「ドキュメントを渡す」とRAGは何が違うのか
  date: '2026-06-12'
- url: https://zenn.dev/shun_producer/articles/claude-structured-outputs-beginner
  title: AIの返事を「必ずJSON」にする——Claude構造化出力入門
  date: '2026-06-13'
- url: https://zenn.dev/marusuke/articles/20260625220809
  title: Claude APIでブログ記事を自動生成する実践ガイド
  date: '2026-06-25'
- url: https://zenn.dev/yamamoshu/articles/llm-agent-no-langchain
  title: LangChainなしでLLMエージェントを作る【Claude API + Python実装】
  date: '2026-06-28'
- url: https://zenn.dev/propagandist/articles/0017-spring-boot-claude-multi-turn
  title: Spring Boot で Claude に会話履歴を渡して多ターンで話す
  date: '2026-07-10'
---









# Claude Api

---

## 2026-07-10

### Spring Boot で Claude に会話履歴を渡して多ターンで話す

Spring Boot で Claude API を呼び出し、会話履歴を管理しながら多ターンの対話を実装する方法を解説。ステートレスな API の特性を踏まえ、user/assistant の交互配置を不変条件として保証する Conversation 型を導入し、system プロンプトと messages の適切な分離、履歴の持ち回しとトークン管理の注意点を示す実践ガイド。

- **ソース**: [Zenn claude](https://zenn.dev/propagandist/articles/0017-spring-boot-claude-multi-turn)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, setup

---

## 2026-06-28

### LangChainなしでLLMエージェントを作る【Claude API + Python実装】

LangChainを使わずにClaude APIのFunction Callingを活用してLLMエージェントを自作する方法を解説。ReAct（Reasoning + Acting）パターンを用いた実装により、エージェントの内部動作を理解しながら開発できる。研究・学習目的での自前実装を推奨する記事。

- **ソース**: [Zenn claude](https://zenn.dev/yamamoshu/articles/llm-agent-no-langchain)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, 新機能

---

## 2026-06-25

### Claude APIでブログ記事を自動生成する実践ガイド

Claude APIを使用したブログ記事自動生成システムの実装ガイド。アウトライン生成→セクション展開の二段階方式を採用し、JSON形式でのパース、レート制限対策、ハルシネーション対応などの実践的なノウハウを解説。人間によるレビューを前提とした執筆支援ツールとしての運用方法と、CMS連携やRAG導入などの今後の展開についても言及している。

- **ソース**: [Zenn claude](https://zenn.dev/marusuke/articles/20260625220809)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, opus

---

## 2026-06-13

### AIの返事を「必ずJSON」にする——Claude構造化出力入門

Claude APIの構造化出力機能について、Pythonでの実装方法を初心者向けに解説。JSONスキーマを使ってAPIレスポンスを確実にJSON形式で取得する方法、エラー対処法、実装時の注意点を具体例とともに紹介している。

- **ソース**: [Zenn claude](https://zenn.dev/shun_producer/articles/claude-structured-outputs-beginner)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, setup

---

## 2026-06-12

### Claudeに「ドキュメントを渡す」とRAGは何が違うのか

Claude APIのdocumentブロックによるドキュメント受け渡しとRAGの違いを解説。documentブロックは「渡された文書を読んで引用する」機能であり、RAGは「大量文書から関連箇所を検索して取り出す」前段処理。実運用では両者を併用し、RAGで絞り込んだチャンクをdocumentブロックで渡して引用機能を活かすのが王道。引用機能はコスト削減と信頼性向上のメリットがあるが、構造化出力とは併用不可。

- **ソース**: [Zenn claude](https://zenn.dev/osakayakyu/articles/2901e4599ff819)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 2026-06-08

### Next.js × Claude APIで「読書メモ→X投稿」ツールを作って公開した（zodのバグに最後ハマった）

Next.js 15とClaude API（Haiku 4.5）を使った読書メモからX投稿を生成するツールの開発・公開事例。zodのv3/v4バージョン不整合により本番環境でクラッシュする問題に遭遇し、構造化出力の実装やモデル選択によるコスト最適化、APIクレジット管理の注意点を解説。公開後の実運用で学んだベストプラクティスを共有。

- **ソース**: [Zenn claude](https://zenn.dev/nora_saito/articles/46e2d3fdefdf54)
- **重要度**: 6/10
- **タグ**: claude-api, haiku, setup

---

## 2026-04-14

### Claude Managed Agents入門 — セルフホスト不要でAIエージェントを動かすAPIガイド

Anthropicが2026年4月8日にパブリックベータ公開したClaude Managed Agentsの入門ガイド。従来は自前実装が必要だったエージェントループ・ツール実行・サンドボックスをフルマネージドで提供し、開発者はエージェントの定義に集中できる。Agent/Environment/Session/Eventsの4つのリソース構成、bash/web_searchなどの組み込みツール、料金体系（$0.08/セッション時間）について解説。Python SDKを使ったクイックスタートとカスタムツールの実装方法も紹介している。

- **ソース**: [Qiita claude](https://qiita.com/kai_kou/items/9aa2ca4787306e4dc162)
- **重要度**: 8/10
- **タグ**: claude-api, 新機能, setup

---

## 2026-04-07

### Claude APIのExtended Thinkingを使いこなす——どんなタスクで効果があるか検証した

Claude APIのExtended Thinking機能を複数のタスクで検証した実践記事。数学証明では効果が薄かったが、多制約の最適化問題やコード修正の副作用チェックでは明確な精度向上を確認。budget_tokensのチューニングでコスト最適化が可能で、思考プロセスの可視化により判断根拠の追跡もできる。事実確認タスクでは不要。

- **ソース**: [Zenn claude](https://zenn.dev/ai_eris_log/articles/claude-extended-thinking-20260407)
- **重要度**: 7/10
- **タグ**: claude-api, 新機能, performance

---

## 2026-03-25

### 「fix」とか「update」しか書かないそこのあなたへ。Claudeにコミットメッセージを丸投げする最強エイリアス

AIにコミットメッセージを自動生成させるGitエイリアスの紹介記事。Claudeを使って変更差分から適切なコミットメッセージを生成し、エディタで編集も可能。シンプルなコマンド一発で導入でき、開発効率を向上させる実用的なTips。

- **ソース**: [Zenn claude](https://zenn.dev/qinritukou/articles/git-ai-commit)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-25 | 自動生成 |
