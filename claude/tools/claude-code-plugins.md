---
title: Claude Code Plugins
category: tools
subcategory: claude-code-plugins
tags:
- claude-code
- cowork
- mcp
- prompt
- setup
- vscode
- 新機能
date: '2026-04-12'
updated: '2026-07-07'
sources:
- url: https://ai-heartland.com/explain/last30days-skill-guide
  title: last30days-skill完全ガイド｜Reddit・X・YouTube横断AIリサーチスキルの使い方2026年版
  date: '2026-04-12'
- url: https://qiita.com/kanta13jp1/items/d157ccf8a081f14dcd79
  title: Claude Codeに永続メモリを追加する「claude-mem」を実際に導入してみた — 自作hook版との比較
  date: '2026-04-16'
- url: https://ai-heartland.com/tool/prismatic-skills-claude-code-plugin
  title: Prismatic Skills for Claude Code徹底解剖｜iPaaS製スキル束ねプラグインのSKILL.md設計
  date: '2026-05-08'
- url: https://ai-heartland.com/tool/thariq-making-playgrounds-claude-code
  title: Claude Code開発者公式プラグイン「playground」｜ThariqのHTML対話術5実例
  date: '2026-05-10'
- url: https://qiita.com/yukurash/items/a4caa9c63bf9e1f283ff
  title: MBTI 16タイプの人格に議論させる Claude Code プラグイン『16-minds』を作った
  date: '2026-05-19'
- url: https://qiita.com/yukurash/items/4c4bfc492d91770618b8
  title: 記事から ”AIっぽさ” をなくす Skills を作成した - Claude Code プラグイン『16-minds』
  date: '2026-05-21'
- url: https://zenn.dev/shuji_bonji/articles/9fd9850011f3ae
  title: ファクトチェックとメディアリテラシーチェックを2つのClaude Skill化してみた話
  date: '2026-05-22'
- url: https://ai-heartland.com/tool/dair-academy-plugins
  title: DAIR Academy Plugins完全解説 — Claude Codeをパワーアップする5つのOSSプラグイン
  date: '2026-05-24'
- url: https://ai-heartland.com/explain/claude-code-deep-trilogy-guide
  title: Claude Code プラグイン Deep Trilogy 入門｜あいまいなアイデアをspecに分解→TDDで実装まで一気通貫
  date: '2026-06-13'
- url: https://qiita.com/claude_iruka/items/f5c721f2acf2241e6d11
  title: Claude Codeのカスタムコマンドで転職活動の応募書類を自動生成するツールを作ってみた
  date: '2026-06-20'
- url: https://qiita.com/kummn/items/a31c32f8ccbe63421bde
  title: Claudeの残量やリセット時間のわかるマスコットWidget
  date: '2026-07-03'
- url: https://ai-heartland.com/ai/claude/claude-rank
  title: claude-rank徹底解説：AIに引用されないサイトを診断・自動修正するプラグイン
  date: '2026-07-04'
- url: https://ai-heartland.com/explain/agent-rules-books-guide
  title: agent-rules-books解説｜名著13冊をAGENTS.mdルールに蒸留したOSS
  date: '2026-07-07'
---













# Claude Code Plugins

---

## 2026-07-07

### agent-rules-books解説｜名著13冊をAGENTS.mdルールに蒸留したOSS

agent-rules-booksは、『Clean Code』『Refactoring』『DDD』など名著13冊の原則をAGENTS.mdルールに蒸留したOSSプロジェクト。MITライセンスで2,000以上のスターを獲得し、Codex・Cursor・Claude Code・Copilotなどで利用可能。作者の検証では、本の名前を挙げるより具体的なルールを列挙する方が効果的（74点 vs 46点）だった。mini/nano/full の3版が用意され、ツール非依存の設計により様々なAIコーディングエージェントで使える。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/agent-rules-books-guide)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-07-04

### claude-rank徹底解説：AIに引用されないサイトを診断・自動修正するプラグイン

claude-rankは、サイトがAI検索エンジン（ChatGPT、Perplexityなど）に発見・引用されるかを診断し、自動修正するClaude Codeプラグインです。10スキャナ・170以上のチェックでAIクローラのブロック、llms.txt欠如、構造化データ不備などを検出し、robots.txt、sitemap.xml、llms.txt、JSON-LDを自動生成・修正します。従来のSEOに加え、GEO（生成エンジン最適化）とAEO（回答エンジン最適化）に対応し、AI時代の新しいSEO戦略を自動化する無料OSSツールです。

- **ソース**: [AI Heartland](https://ai-heartland.com/ai/claude/claude-rank)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, prompt

---

## 2026-07-03

### Claudeの残量やリセット時間のわかるマスコットWidget

Claude Code のトークン使用量、リセット時間、Extra Charge を一目で確認できるデスクトップウィジェット「claude-watch」が公開されました。マスコットキャラクターを表示する機能も搭載し、作業のお供として使えるツールです。GitHub で公開されており、Claude Code ユーザーのトークン管理を支援します。

- **ソース**: [Qiita claude](https://qiita.com/kummn/items/a31c32f8ccbe63421bde)
- **重要度**: 5/10
- **タグ**: claude-code, 新機能, cowork

---

### Claudeの残量やリセット時間のわかるマスコットWidget

Claude Code のトークン使用量とリセット時間を視覚的に確認できるデスクトップウィジェット「claude-watch」が公開されました。使用量、リセット時間、Extra Charge を一元管理でき、マスコットキャラクターを表示する機能も搭載しています。Claude Code で開発された実用的なモニタリングツールです。

- **ソース**: [Qiita claudecode](https://qiita.com/kummn/items/a31c32f8ccbe63421bde)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-06-20

### Claude Codeのカスタムコマンドで転職活動の応募書類を自動生成するツールを作ってみた

Claude Codeのカスタムスラッシュコマンド機能を活用して、転職活動の応募書類（志望動機・自己PR・職務要約）を企業ごとに自動生成するツール「job-hunting-kit」の開発事例。キャリア情報をMarkdownファイル（my-career.md）として永続化し、/setupコマンドで初期設定、/applyコマンドで企業別の書類を一括生成する仕組み。ChatGPT/Claude Web版と異なり、文脈の永続化とローカルファイル管理が可能で、生成→修正のループを高速化できる点が特徴。

- **ソース**: [Qiita claudecode](https://qiita.com/claude_iruka/items/f5c721f2acf2241e6d11)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 2026-06-13

### Claude Code プラグイン Deep Trilogy 入門｜あいまいなアイデアをspecに分解→TDDで実装まで一気通貫

Pierce Lamb氏が開発したClaude Code向けプラグイン「Deep Trilogy」の解説記事。あいまいなアイデアを/deep-project（分解）→/deep-plan（計画）→/deep-implement（実装）の3段階パイプラインで処理し、TDD前提で実装まで一気通貫で進める。各工程で人間が判断を挟む「human-in-the-loop」設計が特徴で、ファイルベースの状態管理により中断・再開が可能。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-deep-trilogy-guide)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-24

### DAIR Academy Plugins完全解説 — Claude Codeをパワーアップする5つのOSSプラグイン

DAIR.AI Academyが2026年2月にClaude Code向けオープンソースプラグインマーケットプレイス「dair-academy-plugins」を公開。Gemini 3 Proによる画像生成、複数LLMによる議会制審議、学術論文サーベイなど5つの教育・研究特化プラグインを提供。コマンド1行でインストール可能で、公開4ヶ月でスター数198を達成。DAIR.AIはPrompt Engineering Guide（46k+スター）などで知られるAI研究民主化コミュニティ。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/dair-academy-plugins)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-05-22

### ファクトチェックとメディアリテラシーチェックを2つのClaude Skill化してみた話

Claude Code/Coworkで動作するAgent Skillとして、ファクトチェック（20項目×4カテゴリ）とメディアリテラシーチェック（30項目×6カテゴリ）の2つのスキルを公開した事例。PWA版のfact-checklistを基に、LLM向けに移植し、SKILL.mdのfrontmatterでtriggeringを最適化。両スキルは目的が異なるため意図的に分離し、相互補完的に使えるよう設計されている。

- **ソース**: [Zenn claude](https://zenn.dev/shuji_bonji/articles/9fd9850011f3ae)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, 新機能

---

## 2026-05-21

### 記事から ”AIっぽさ” をなくす Skills を作成した - Claude Code プラグイン『16-minds』

Claude Code用プラグイン「16-minds」のv0.3.0リリース記事。AI生成文章特有の「無難さ」を排除するため、MBTI 16タイプの人格を実装。voice-write, voice-decide, voice-voteの3機能で、人格を持った文章生成・意思決定・投票が可能に。具体例として同じテーマを異なる人格で書かせた結果を比較し、AIっぽさを消す3原則（親切を削る・両論併記禁止・抽象を避ける）を解説。

- **ソース**: [Qiita claude](https://qiita.com/yukurash/items/4c4bfc492d91770618b8)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 2026-05-19

### MBTI 16タイプの人格に議論させる Claude Code プラグイン『16-minds』を作った

MBTI 16タイプの人格を並列に召喚してコードレビューやアイデア出しで議論させる Claude Code プラグイン『16-minds』の開発記事。Claude 単体の無難な回答に物足りなさを感じ、subagent 機能を使って16人格を並列実行し、偏った意見の塊から新しい視点を発見する仕組みを構築。light/middle/heavy の3モードで議論の深さを調整でき、4セクション固定フォーマットで議論を構造化する設計が特徴。

- **ソース**: [Qiita claude](https://qiita.com/yukurash/items/a4caa9c63bf9e1f283ff)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, 新機能

---

## 2026-05-10

### Claude Code開発者公式プラグイン「playground」｜ThariqのHTML対話術5実例

Anthropic公式のClaude Code開発者Thariqが、新プラグイン「playground」をリリース。1コマンドでインストールでき、Claude Codeに視覚的な対話UIを持つスタンドアロンHTMLを生成させることで、テキストベースの対話からビジュアル判断へと転換。Anthropic公式マーケットプレイスから配布され、84万インプレッションを記録するほど注目を集めている。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/thariq-making-playgrounds-claude-code)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, vscode

---

## 2026-05-08

### Prismatic Skills for Claude Code徹底解剖｜iPaaS製スキル束ねプラグインのSKILL.md設計

iPaaSベンダーPrismaticが2026年4月に公開したClaude Code用プラグイン「prismatic-skills」の徹底解説記事。5系統のスキル（Component Builder、CNI Builder、Embed Advisor、Orby、Migration Analyzer）を提供し、user-invocable: falseやdisallowed-toolsなど独自のSKILL.md設計手法を採用。自社SaaSのClaude Codeプラグインを作る際の設計テンプレートとして優秀と評価されている。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/prismatic-skills-claude-code-plugin)
- **重要度**: 6/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-04-16

### Claude Codeに永続メモリを追加する「claude-mem」を実際に導入してみた — 自作hook版との比較

Claude Codeに永続メモリを追加するプラグイン「claude-mem」の導入レポート。公開48時間で4.6万スターを獲得したこのツールは、セッション間で文脈を引き継ぎ、SQLite+Chromaによるハイブリッド検索やLLMによる圧縮機能を提供する。筆者が自作した軽量hook版との比較も行い、Gemini APIを使った無料化設定や、3層メモリ構造による複数インスタンス管理の実例を紹介。シンプルなケースでは自作hook、高度な検索が必要な場合はclaude-memという段階的アプローチを推奨している。

- **ソース**: [Qiita claudecode](https://qiita.com/kanta13jp1/items/d157ccf8a081f14dcd79)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-04-12

### last30days-skill完全ガイド｜Reddit・X・YouTube横断AIリサーチスキルの使い方2026年版

last30days-skillは、Claude Code上で動作するマルチプラットフォームAIリサーチスキル。Reddit・X・YouTube・Hacker Newsなど13のプラットフォームを横断検索し、エンゲージメントや予測市場のオッズで情報をスコアリングして調査レポートを自動生成する。GitHubスター21,000超・Trending1位を獲得した実績を持ち、Google検索と異なり「実際の人が今月反応したもの」を返す設計思想が特徴。ゼロ設定でも4ソース（Reddit・HN・Polymarket・GitHub）が即座に利用可能で、APIキーを追加することで対応ソースを段階的に拡張できる。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/last30days-skill-guide)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-12 | 自動生成 |
