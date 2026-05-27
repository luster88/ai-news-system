---
title: Claude Code Plugins
category: guides
subcategory: claude-code-plugins
tags:
- claude-code
- cowork
- prompt
- setup
- 新機能
date: '2026-04-07'
updated: '2026-05-27'
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
---





# Claude Code Plugins

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
