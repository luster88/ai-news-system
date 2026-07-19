---
title: Claude Code Skills
category: guides
subcategory: claude-code-skills
tags:
- claude-code
- cowork
- mcp
- performance
- prompt
- setup
- 新機能
date: '2026-03-22'
updated: '2026-07-19'
sources:
- url: https://qiita.com/souichirou/items/26f3c6fe731e710f62e3
  title: Claude Codeのexample-skillsを全部使いこなすガイド【17種類まとめ】
  date: '2026-03-22'
- url: https://qiita.com/dai_chi/items/0702e3a9f7a487ceaa3e
  title: Claude Codeのスキルが増えすぎた？管理ツールを作る前に知っておきたいフロントマター設定
  date: '2026-03-24'
- url: https://zenn.dev/bentenweb_fumi/articles/twde0igmoklh
  title: Claude Codeのスキルファイル分割パターン──「1スキル=1責務」でAIの精度が劇的に変わる
  date: '2026-04-17'
- url: https://qiita.com/kamome_susume/items/41300417840aa107472e
  title: 【2026年4月更新】Claude Codeの役に立つフロントデザインのskills10選
  date: '2026-04-19'
- url: https://qiita.com/kamome_susume/items/0817c06eb25935216299
  title: 【保存版】Claude Code時代にエンジニアが身につけるべき能力10選
  date: '2026-04-21'
- url: https://qiita.com/asahide/items/53cfdab083905fedeed5
  title: oracle/skills を Claude Skill に登録すると AWR 解析で何が変わるか — Haiku/Sonnet × Skill有無の4パターン比較
  date: '2026-04-29'
- url: https://qiita.com/Tadashi_Kudo/items/e0484a0f800b5dca4665
  title: Claude Skills（SKILL.md）設計「6法則」と自分の環境を照合したら、2点で先を行っていた話
  date: '2026-05-01'
- url: https://qiita.com/hinaworks/items/93ae032d392bdad25655
  title: Claude Code Skills で /briefing コマンドを5分で実装する
  date: '2026-05-09'
- url: https://qiita.com/atsushi11o7/items/5cbef4b10f3ec55c75a1
  title: Claude Code の skill 機能を本格的に試す - 開発フローを丸ごと任せて PR まで完結させた話
  date: '2026-05-09'
- url: https://qiita.com/nrEngineer/items/615ec7a1599d95e004d4
  title: Claude Code Skillの作り方 ― 開発手法をAIに覚えさせる技術（ダイジェスト版）
  date: '2026-05-17'
- url: https://qiita.com/tips4you/items/47d04503c45056712a67
  title: コミットメッセージで悩む時間をゼロにする — Claude Code 用 /commit スキルの設計と全文公開
  date: '2026-05-21'
- url: https://zenn.dev/sngjpw/articles/1385f21aff9308
  title: Claudeのスキル機能とは？自分専用AIを育てる方法【実体験あり】🛠️
  date: '2026-05-22'
- url: https://zenn.dev/shino_i/articles/20c49c73152956
  title: Claude Code の Skill スコープとコンテキスト設計を考える
  date: '2026-06-02'
- url: https://zenn.dev/giana12th/articles/aea54291a56bdf
  title: Claude Code の過去会話を読んでブログを書くスキルを Claude Code で作った話
  date: '2026-06-11'
- url: https://qiita.com/kirozero/items/28a20168ace6f0299763
  title: grill-me がバズった Matt Pocock の Claude Code skills リポジトリを一通り眺めてみた
  date: '2026-07-05'
- url: https://zenn.dev/shun_producer/articles/popular-claude-code-skills
  title: いま使われているClaude Codeスキルとは？ 非エンジニア向け厳選8選
  date: '2026-07-19'
---















# Claude Code Skills

---

## 2026-07-19

### いま使われているClaude Codeスキルとは？ 非エンジニア向け厳選8選

Claude Code のスキル機能について、非エンジニア向けに実用的な8つを厳選して紹介。スキルはClaude に専門知識と実行能力を追加する拡張機能で、書類作成・市場調査・営業メール・SEO診断・広告文生成・コードレビュー・ビジネス分析・カスタムスキル作成など、日常業務を自動化できる。スマホアプリのように必要な機能を追加することで、Claudeを特定業務に特化させられる仕組み。

- **ソース**: [Zenn claude](https://zenn.dev/shun_producer/articles/popular-claude-code-skills)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, prompt

---

## 2026-07-05

### grill-me がバズった Matt Pocock の Claude Code skills リポジトリを一通り眺めてみた

Matt Pocock が公開した Claude Code 用スキル集 mattpocock/skills について、全体構造と設計思想を解説。user-invoked と model-invoked の 2 層構造、grill-me（実装前の尋問スキル）や domain-modeling（共有言語管理）などの主要スキルを紹介。小さく・改造しやすく・組み合わせ可能な設計が特徴で、AI エージェントの典型的な失敗モード（意図の齟齬、冗長な説明）への対処法を示している。

- **ソース**: [Qiita claudecode](https://qiita.com/kirozero/items/28a20168ace6f0299763)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-06-11

### Claude Code の過去会話を読んでブログを書くスキルを Claude Code で作った話

Claude Code の過去セッション会話履歴を自動検索・整形してブログ執筆に活用する `/blog-dev` スキルの開発事例。~/.claude/history.jsonl と ~/.claude/projects/ 配下のセッションデータを収集し、サブエージェント `history-summarizer` で処理してコンテキストに注入する仕組み。dynamic context injection や allowed-tools による権限制御、Git Bash 実行環境など実装の技術的工夫が詳述されている。

- **ソース**: [Zenn claude](https://zenn.dev/giana12th/articles/aea54291a56bdf)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

## 2026-06-02

### Claude Code の Skill スコープとコンテキスト設計を考える

Claude Code の Skills 機能における Progressive Disclosure（段階的開示）の仕組みと、スキルのスコープ設計について解説。スキルが起動するトリガーは説明文と依頼のマッチングであり、スコープの広さは見落としの少なさと消費の重さのトレードオードになる。有限なコンテキストを効率的に配分するための4層モデル（依頼の分割、context fork、結果の外部化など）を提案している。

- **ソース**: [Zenn claude](https://zenn.dev/shino_i/articles/20c49c73152956)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, performance

---

## 2026-05-22

### Claudeのスキル機能とは？自分専用AIを育てる方法【実体験あり】🛠️

Claude Code（CLIツール）のスキル機能について解説。スキルとは自分専用の指示書を.claude/skills/配下のSKILL.mdファイルに保存し、キーワード一つで同じクオリティのアウトプットを得られる機能。毎回プロンプトを書き直す手間が省け、自分専用のAIアシスタントを育てる感覚で使える。

- **ソース**: [Zenn claude](https://zenn.dev/sngjpw/articles/1385f21aff9308)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

## 2026-05-21

### コミットメッセージで悩む時間をゼロにする — Claude Code 用 /commit スキルの設計と全文公開

Claude Code のカスタムスキル機能を活用した /commit コマンドの設計と実装を公開。git add したファイルのみを対象に、Conventional Commits 準拠の日本語コミットメッセージを自動生成し、変更の種類（feat/fix/docs等）に応じて複数のアトミックコミットに自動分割することで、コミットメッセージ作成の負担を大幅に軽減する。

- **ソース**: [Qiita claudecode](https://qiita.com/tips4you/items/47d04503c45056712a67)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-05-17

### Claude Code Skillの作り方 ― 開発手法をAIに覚えさせる技術（ダイジェスト版）

Claude Code Skill の作成方法を解説する記事。開発手法（BDD/TDD等）をMarkdown形式のSkillファイルとして定義することで、AIに手順を実行させる仕組みを紹介。ワークフローの言語化、Phase分割、ゲート設定など7ステップの方法論の概要を説明し、完全版はnoteで公開している。

- **ソース**: [Qiita claudecode](https://qiita.com/nrEngineer/items/615ec7a1599d95e004d4)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 2026-05-09

### Claude Code Skills で /briefing コマンドを5分で実装する

Claude Code の Skills 機能を使って、SNS運用の朝の確認作業を自動化する方法を解説。.claude/skills/ フォルダに Markdown ファイルを置くことで、スラッシュコマンドとして使えるようになる。CLAUDE.md を作成することで、Skills が特定のアカウントとして動作する設定も可能。

- **ソース**: [Qiita claudecode](https://qiita.com/hinaworks/items/93ae032d392bdad25655)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

### Claude Code の skill 機能を本格的に試す - 開発フローを丸ごと任せて PR まで完結させた話

Claude Code の skill 機能を実戦投入し、Dev Container + MCP + GitHub CLI で開発環境を構築。GitHub CLI の gh skill サブコマンド（2026年4月追加）で Anthropic 公式 skill を導入し、frontend-design skill を使ったコンポーネント再設計から PR 作成までのフローを自動化した実践記事。.mcp.json による MCP サーバ設定（Context7、GitHub MCP）と、永続化された Claude 認証情報の管理方法も詳説。

- **ソース**: [Qiita claudecode](https://qiita.com/atsushi11o7/items/5cbef4b10f3ec55c75a1)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, setup

---

## 2026-05-01

### Claude Skills（SKILL.md）設計「6法則」と自分の環境を照合したら、2点で先を行っていた話

Claude Skillsの設計に関する6法則を分析した記事。筆者は自環境でスキル検証制度化（トリガー率90%目標の10パターンメンタルテスト）とローテーション機構（skills-usage.jsonによる実行回数記録、50件上限でアーカイブ退避）を実装済み。外部分析が「設計の質」を論じる一方、自環境は「検証の制度化」と「ライフサイクル管理」まで進んでおり、scaffoldテンプレートにOut of Scope節を組み込むなど、長期運用を見据えたシステム設計を実現している。

- **ソース**: [Qiita claude](https://qiita.com/Tadashi_Kudo/items/e0484a0f800b5dca4665)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

### Claude Skills（SKILL.md）設計「6法則」と自分の環境を照合したら、2点で先を行っていた話

Claude Code の Skills 設計に関する外部分析「6法則」を自環境と照合した結果、検証制度化とライフサイクル管理の2点で先行実装していたことを報告。SKILL_DESIGN_CHECKLIST.md による10パターンのメンタルテスト、skills-usage.json による実行回数管理と50件上限でのローテーション運用（アーカイブ187件）など、「設計の法則」を超えた「整理の仕組み」の必要性を示す。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/e0484a0f800b5dca4665)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-29

### oracle/skills を Claude Skill に登録すると AWR 解析で何が変わるか — Haiku/Sonnet × Skill有無の4パターン比較

Oracle公式のskillsリポジトリをClaude Skillに登録し、AWRレポート解析における効果を検証。Skill未使用ではHaiku・SonnetともにExecute to Parse %を見落としたが、Haiku + Skillは定量化と優先度評価で優れた結果を示した。モデルのアップグレードよりもSkill追加の効果が大きいことが判明。

- **ソース**: [Qiita claude](https://qiita.com/asahide/items/53cfdab083905fedeed5)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-04-21

### 【保存版】Claude Code時代にエンジニアが身につけるべき能力10選

Claude Code時代にエンジニアが身につけるべき10の能力を解説した記事。AIが実装を担う時代において、問題定義力、設計意図の理解、批判的評価、コンテキスト管理、タスク分解、ドメイン知識などのメタスキルが重要になると主張。「手を動かす力」から「頭を使う力」への重心シフトを強調している。

- **ソース**: [Qiita claude](https://qiita.com/kamome_susume/items/0817c06eb25935216299)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-04-19

### 【2026年4月更新】Claude Codeの役に立つフロントデザインのskills10選

Claude CodeでAI生成UIの「平均的すぎる」デザイン問題を解決するSkills（スキル）10選を紹介。Anthropic公式のfrontend-designやbaseline-ui、アクセシビリティ対応のfixing-accessibility、VercelのWeb設計ガイドライン検証ツールなど、フロントエンド開発に特化した再利用可能な指示セットを活用することで、Claude Codeの出力品質を大幅に向上させる方法を解説。

- **ソース**: [Qiita claude](https://qiita.com/kamome_susume/items/41300417840aa107472e)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, prompt

---

## 2026-04-17

### Claude Codeのスキルファイル分割パターン──「1スキル=1責務」でAIの精度が劇的に変わる

Claude CodeのCLAUDE.mdファイルが200行を超えたら分割のサイン。ルーティングテーブルのみ本体に残し、具体的な手順は用途別スキルファイルに分離する「1スキル=1責務」の原則により、LLMの指示遵守率が大幅に向上する。コンテキストウィンドウのSNR（Signal-to-Noise Ratio）を上げることで、複雑な手順の再現性や条件分岐の精度が改善される。

- **ソース**: [Zenn claude](https://zenn.dev/bentenweb_fumi/articles/twde0igmoklh)
- **重要度**: 7/10
- **タグ**: claude-code, prompt

---

## 2026-03-24

### Claude Codeのスキルが増えすぎた？管理ツールを作る前に知っておきたいフロントマター設定

Claude Codeのスキル機能が増えすぎてメニューが散らかる問題に対し、公式のフロントマター設定（disable-model-invocation、user-invocable）を使った整理方法を解説。スキルを「背景知識型」「副作用操作型」「標準型」の3パターンに分類し、設計段階で呼び出し制御とコンテキスト消費を最適化する手法を紹介。管理ツール導入前にまず設計で整理すべきという実践的アドバイス。

- **ソース**: [Qiita claudecode](https://qiita.com/dai_chi/items/0702e3a9f7a487ceaa3e)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, setup

---

## 2026-03-22

### Claude Codeのexample-skillsを全部使いこなすガイド【17種類まとめ】

Claude Codeの公式スキル集「example-skills」全17種類を紹介するガイド。Excel/PowerPoint操作、React+Tailwind UI構築、p5.jsアート生成、Slack向けGIF最適化、Claude API連携、MCP開発、Playwright UIテスト等の具体的な使用例とインストール方法を解説。各スキルは/スキル名でトリガーし、特定タスクに最適化された動作を実行する。

- **ソース**: [Qiita claude](https://qiita.com/souichirou/items/26f3c6fe731e710f62e3)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-22 | 自動生成 |
