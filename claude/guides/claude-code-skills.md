---
title: Claude Code Skills
category: guides
subcategory: claude-code-skills
tags:
- claude-code
- cowork
- prompt
- setup
- 新機能
date: '2026-03-22'
updated: '2026-05-01'
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
---







# Claude Code Skills

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
