---
title: Claude Code Plugins
category: guides
subcategory: claude-code-plugins
tags:
- claude-api
- claude-code
- cowork
- prompt
- setup
- 新機能
date: '2026-04-07'
updated: '2026-07-01'
sources:
- url: https://qiita.com/moha0918_/items/b3011c218210ab2695b7
  title: プラグイン作成の3つの方法、結局どれを選ぶべき？
  date: '2026-04-07'
- url: https://www.reddit.com/r/ClaudeAI/comments/1sfsz67/i_gave_claude_my_dead_games_30yearold_files_and
  title: I gave Claude my dead game's 30-year-old files and asked it to bring the
    game back to life
  date: '2026-04-08'
- url: https://zenn.dev/edhiblemeer/articles/ai-persona-memory-separation
  title: AIに人格をロードする ── 記憶と人格を分離する設計思想
  date: '2026-05-19'
- url: https://qiita.com/shokan/items/fae1e00d089aea9cd041
  title: Claude Code とは何かをわかりやすく解説する
  date: '2026-05-20'
- url: https://zenn.dev/gudezou/articles/d3b954f51bca04
  title: Claude Code の slash command と custom skill は何が違うのか
  date: '2026-05-27'
- url: https://qiita.com/YujiNaramoto/items/27516f3c3126875a8557
  title: なぜ SKILL.md を「仕様書から書く」より「Claude に書かせる」ほうが正しいのか
  date: '2026-06-09'
- url: https://zenn.dev/hobomokha/articles/e4225ad7811e4b
  title: AIに自分を覚えさせたら、毎日どう育てる？
  date: '2026-06-14'
- url: https://qiita.com/shu15511551/items/4b5c95976adb2d7d2efd
  title: （後編）Sheets も、フォルダも使わない ── 20年もののファイル探しツールが、Googleドライブで「G-クイック」になるまでの話
  date: '2026-06-14'
- url: https://qiita.com/mnoguchi/items/65af2c1e7440226b3cac
  title: Claude Codeで歴史的リーダー診断アプリを30分で作った【Next.js + Anthropic API】
  date: '2026-06-21'
- url: https://qiita.com/Rapls/items/ac05434441e57348d5ed
  title: 正直に言います。初心者のClaude Codeは、9割「頼み方」で損してます【コピペで直せる10個】
  date: '2026-06-29'
- url: https://zenn.dev/tatsuqumo/articles/b4f6b05461065c
  title: Claude Code の「ループ」総整理 — /goal・/loop・/schedule・Routines をいつ使うか
  date: '2026-07-01'
---










# Claude Code Plugins

---

## 2026-07-01

### Claude Code の「ループ」総整理 — /goal・/loop・/schedule・Routines をいつ使うか

Claude Code の繰り返し実行機能（/goal、/loop、/schedule、Routines）を「トリガー」と「停止条件」の観点から体系的に整理した解説記事。ターンベース、目標ベース、時間ベースの3分類と、それぞれの向き不向きを比較。/loop はローカルで定期実行、/schedule はクラウドで永続実行、/goal は条件達成まで自律実行する仕組みを明確化。

- **ソース**: [Zenn claude](https://zenn.dev/tatsuqumo/articles/b4f6b05461065c)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-06-29

### 正直に言います。初心者のClaude Codeは、9割「頼み方」で損してます【コピペで直せる10個】

Claude Code初心者が陥りがちな失敗パターンと、効率的な使い方の10個の型を紹介。「直して」だけで投げない、1依頼1タスクに分割、短い前提を書く、diffを必ず確認、contextを測って減らすなど、コピペで使える実践的なプロンプト改善方法を解説。

- **ソース**: [Qiita claude](https://qiita.com/Rapls/items/ac05434441e57348d5ed)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, 新機能

---

## 2026-06-21

### Claude Codeで歴史的リーダー診断アプリを30分で作った【Next.js + Anthropic API】

Claude Code を使い Next.js + Anthropic API（Claude Haiku）で30分でマネージャータイプ診断アプリを構築した実践記事。10問の質問から歴史上の人物を診断する仕組みで、JSON形式指定・候補の幅明示・文字数指定などプロンプトエンジニアリングのコツを紹介。Claude Haiku を使用し1回約700トークンで動作する。

- **ソース**: [Qiita claudecode](https://qiita.com/mnoguchi/items/65af2c1e7440226b3cac)
- **重要度**: 6/10
- **タグ**: claude-code, claude-api, prompt

---

## 2026-06-14

### AIに自分を覚えさせたら、毎日どう育てる？

Claude Code を使った「秘書リポジトリ」の運用方法を解説。日常会話の中で「覚えておいて」と指示するだけで、AIが情報を整理しファイルに記録。1週間使うとmaster_profileやdomains配下にファイルが増え、過去の自分のパターンを覚えたAIが文脈を踏まえた対話をしてくれる。ただし使い続けると情報が重複・散在し、古い記述と新しい記述が混在する「散らかり問題」が必ず発生する。

- **ソース**: [Zenn claude](https://zenn.dev/hobomokha/articles/e4225ad7811e4b)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

### （後編）Sheets も、フォルダも使わない ── 20年もののファイル探しツールが、Googleドライブで「G-クイック」になるまでの話

20年前にExcelで作ったファイル検索ツールをGoogleドライブに移植した「G-クイック」開発の経緯。当初はGeminiとスプレッドシートで開発したが速度に不満があり、GAS単独WebアプリとしてClaudeと共に再設計。機能を絞り込み、マイドライブのみ対象とすることで安定動作を実現した話。

- **ソース**: [Qiita claudecode](https://qiita.com/shu15511551/items/4b5c95976adb2d7d2efd)
- **重要度**: 5/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-06-09

### なぜ SKILL.md を「仕様書から書く」より「Claude に書かせる」ほうが正しいのか

Claude Code の SKILL.md は仕様書を読んでから書くより、実際の作業を Claude に書かせてから調整する方が効率的。name と description の最小構成で十分動作し、起動精度は description の調整で改善できる。具体的な問題に対処する方が何を直すべきか明確になる。

- **ソース**: [Qiita claudecode](https://qiita.com/YujiNaramoto/items/27516f3c3126875a8557)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

## 2026-05-27

### Claude Code の slash command と custom skill は何が違うのか

Claude Code における slash command と custom skill の違いを解説。commands 形式は skills に統合され、既存ファイルはそのまま動作する。skill 形式は補助ファイル用ディレクトリ、自動読み込み制御（disable-model-invocation、user-invocable）、paths による起動条件の絞り込みといった追加機能を持つ。description フィールドが自動読み込みの手がかりとなり、1536字制限に注意が必要。

- **ソース**: [Zenn claude](https://zenn.dev/gudezou/articles/d3b954f51bca04)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-05-20

### Claude Code とは何かをわかりやすく解説する

Claude Code はコマンドラインから起動する対話型AIツールで、最大の特徴はローカルファイルに直接アクセスできること。従来の ChatGPT などブラウザベースの対話型 AI と異なり、コピペの手間なくファイルを読み書きできる。数十〜数百ファイルからなるプロジェクトの改修など、大規模な作業を現実的に実行可能にする。コマンドベースの操作により、開発者向けのワークフローに自然に統合できる点が強み。

- **ソース**: [Qiita claudecode](https://qiita.com/shokan/items/fae1e00d089aea9cd041)
- **重要度**: 6/10
- **タグ**: claude-code, setup, cowork

---

## 2026-05-19

### AIに人格をロードする ── 記憶と人格を分離する設計思想

Claude Codeを複数セッション立ち上げて事業運営する中で、AIが「忘れる」問題に直面。業界主流のRAG/DB検索型メモリーではなく、判断基準を常にコンテキスト内にロードする「人格」アプローチを提唱。ベテランのように検索せず即座に判断できる仕組みを目指す設計思想の実践記録。

- **ソース**: [Zenn claude](https://zenn.dev/edhiblemeer/articles/ai-persona-memory-separation)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-08

### I gave Claude my dead game's 30-year-old files and asked it to bring the game back to life

開発者が1992年に作成したオンラインゲーム「Legends of Future Past」の30年前のスクリプトファイルとマニュアルをClaude Codeに与え、ゲームの再構築を依頼。Claudeは訓練データに存在しない独自スクリプト言語の文法を逆解析し、2,273の部屋、1,990のアイテム、297種類のモンスターを含むゲーム全体を週末で再構築。元々数ヶ月かかった作業を数時間で完了し、リバースエンジニアリング能力の高さを実証。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1sfsz67/i_gave_claude_my_dead_games_30yearold_files_and)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-04-07

### プラグイン作成の3つの方法、結局どれを選ぶべき？

Claude Code のカスタマイズ作成において、スタンドアロン設定・ローカルプラグイン・マーケットプレイスプラグインの3つのアプローチを比較。スタンドアロンはプロジェクト固有の簡単なカスタマイズに最適で、複数プロジェクトで使いたくなったらローカルプラグイン化し、さらに公開したい場合はマーケットプレイスプラグインにする段階的な進め方を推奨。プラグイン化の際は .claude-plugin/plugin.json の配置やネームスペースの理解が重要。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/b3011c218210ab2695b7)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-07 | 自動生成 |
