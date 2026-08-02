---
title: Claude Code Skill
category: tools
subcategory: claude-code-skill
tags:
- claude-code
- cowork
- prompt
- vscode
- 新機能
date: '2026-03-28'
updated: '2026-08-02'
sources:
- url: https://qiita.com/nishiken1118/items/bac44a98ce05b09b78f6
  title: AI レビューの「仕分け疲れ」を解消する Claude Code skill を作った話
  date: '2026-03-28'
- url: https://zenn.dev/tell_y/articles/e21d348284c5a5
  title: Claude Code で最小再現環境の構築を自動化する — minimal-repro スキルの紹介
  date: '2026-04-06'
- url: https://zenn.dev/hibinoue/articles/2071643334a25f
  title: みんなのClaudeスキルが見たい！発信の手間を削減する「Zenn記事の全自動生成」スキル
  date: '2026-06-17'
- url: https://www.reddit.com/r/ClaudeAI/comments/1v55he0/i_made_a_claude_code_skill_that_turns_a_photo_of
  title: I made a Claude Code skill that turns a photo of your handwriting into an
    installable font
  date: '2026-07-24'
- url: https://ai-heartland.com/ai/claude/google-ads-builder
  title: Google Ads Builderとは｜URL1本で検索広告の下書きを作るClaude Codeスキル
  date: '2026-08-02'
---





# Claude Code Skill

---

## 2026-08-02

### Google Ads Builderとは｜URL1本で検索広告の下書きを作るClaude Codeスキル

Google Ads BuilderはWebサイトのURLを1つ入力するだけで、Google検索広告のキーワード設計・広告文・除外キーワード・入稿用CSVまでを自動生成するClaude Codeスキル。広告アカウントには一切接続せず、264行の標準ライブラリのみで構成された軽量なツール。処理の大半はSKILL.mdの指示に基づきClaude側が判断し、Pythonスクリプトは最終的なCSVとHTMLの変換のみを担当する。誇張を抑える注意書きが必須化されており、実際の配信前の検証を促す設計となっている。

- **ソース**: [AI Heartland](https://ai-heartland.com/ai/claude/google-ads-builder)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, prompt

---

## 2026-07-24

### I made a Claude Code skill that turns a photo of your handwriting into an installable font

Claude Code の skill として手書き文字の写真からインストール可能なフォント（TTF）を生成するツールが公開されました。ノートに書いたアルファベットの写真をドラッグし「make my font」と指示するだけで、potrace と font assembly を使った CLI を Claude が制御し、文字認識・大小文字判別・ノイズ除去・プレビュー確認を行います。完全にローカル動作で MIT ライセンス、npx skills add コマンドで簡単にインストール可能です。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v55he0/i_made_a_claude_code_skill_that_turns_a_photo_of)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-06-17

### みんなのClaudeスキルが見たい！発信の手間を削減する「Zenn記事の全自動生成」スキル

Claude Code のカスタムスキルを Zenn や Qiita 向けの記事として全自動で生成するスキル「claude-skills-article」の紹介。SKILL.md を読み込むだけで、想定読者の推定、パス・APIキーのマスキング、プラットフォーム別の記法対応、7セクション構成の記事生成を行い、発信のハードルを大幅に下げることを目的としている。

- **ソース**: [Zenn claude](https://zenn.dev/hibinoue/articles/2071643334a25f)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-04-06

### Claude Code で最小再現環境の構築を自動化する — minimal-repro スキルの紹介

Claude Code で最小再現環境を自動生成する「minimal-repro」スキルの紹介。/minimal-repro コマンドで複数パターンの再現環境を一括生成し、依存インストール、動作確認、レポート出力までを自動化。Vite 8 アップグレード時の実問題で有効性を実証した。内部用と外部用の2種類のレポートを生成し、Issue報告や再現リポジトリの公開にも対応している。

- **ソース**: [Zenn claude](https://zenn.dev/tell_y/articles/e21d348284c5a5)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, vscode

---

## 2026-03-28

### AI レビューの「仕分け疲れ」を解消する Claude Code skill を作った話

Claude Code の /pr-review-toolkit:review-pr が出力するAIレビューコメントを「すぐ対応」「issue化」「棄却」に自動仕分けする skill を開発した記事。フローチャートと判断基準（既存変更との関連度、メリット・デメリット、変更コスト、放置コスト）を用いて、「AIレビューのレビュー疲れ」という新たな課題を解決する実践的なアプローチを紹介している。

- **ソース**: [Qiita claudecode](https://qiita.com/nishiken1118/items/bac44a98ce05b09b78f6)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-28 | 自動生成 |
