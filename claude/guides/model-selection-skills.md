---
title: Model Selection Skills
category: guides
subcategory: model-selection-skills
tags:
- haiku
- opus
- performance
- prompt
- sonnet
date: '2026-04-22'
updated: '2026-06-21'
sources:
- url: https://zenn.dev/ai_arai_ally/articles/20260422-0401-claude-haiku-4-5-skill-opus-4-7
  title: Claude Haiku 4.5 + skill で Opus 4.7 を超えた ― SkillsBench 追試とモデル選定の設計図
  date: '2026-04-22'
- url: https://zenn.dev/noah33/articles/picking-the-right-model
  title: 「正しいモデル」とは何か — Code with Claude London 2026 で考え方が一段アップデートされた話
  date: '2026-05-23'
- url: https://ai-heartland.com/explain/picking-right-model-london-2026
  title: モデル選択の実践科学 — LucasがCode with Claude Londonで語るEval・コスト・フロンティア移動
  date: '2026-05-25'
- url: https://zenn.dev/shun_producer/articles/claude-model-selection-guide
  title: Claudeモデル×エフォート選択ガイド——Opus 4.8 / Sonnet 4.6 / Haiku 4.5の2軸最適化
  date: '2026-06-21'
---




# Model Selection Skills

---

## 2026-06-21

### Claudeモデル×エフォート選択ガイド——Opus 4.8 / Sonnet 4.6 / Haiku 4.5の2軸最適化

Claudeのモデル選択（Opus/Sonnet/Haiku）とエフォートレベル（思考の深さ）を2軸で最適化する実務ガイド。SWE-benchでSonnet 4.6が79.6%、Opus 4.6が80.8%とわずか1.2ポイント差だが、API単価は約5倍の開き。Sonnetを高エフォートで動かす方が、Opusを低エフォートで動かすよりコスパが良い場合が多い。Haikuは定型タスクで本番利用可能で、Sonnetから切り替えるとコストを約1/3に削減できる。

- **ソース**: [Zenn claude](https://zenn.dev/shun_producer/articles/claude-model-selection-guide)
- **重要度**: 7/10
- **タグ**: opus, sonnet, haiku

---

## 2026-05-25

### モデル選択の実践科学 — LucasがCode with Claude Londonで語るEval・コスト・フロンティア移動

Anthropropicの Applied AI チームの Lucas が Code with Claude London 2026 で語った、LLM モデル選択の科学的アプローチ。公開ベンチマークを「事前確率」として活用しつつ、プライベート Eval でユースケース特化の意思決定を行う反復可能プロセスを解説。プロンプトキャッシングによるコスト最適化や、eval 失敗パターンの分類も紹介されている。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/picking-right-model-london-2026)
- **重要度**: 7/10
- **タグ**: opus, prompt, performance

---

## 2026-05-23

### 「正しいモデル」とは何か — Code with Claude London 2026 で考え方が一段アップデートされた話

Code with Claude London 2026のセッション「Picking the right model」の解説記事。Anthropic の Lucas Smedley による「再現可能なプロセスでモデルを選択する」という考え方を紹介。τ-bench Airline を用いたモデルスイープの実例や、Quality・Speed・Costの判断軸を整理し、AI Solutions Architect として新モデル評価をどう体系化すべきかを考察している。

- **ソース**: [Zenn claude](https://zenn.dev/noah33/articles/picking-the-right-model)
- **重要度**: 6/10
- **タグ**: opus, sonnet, haiku

---

## 2026-04-22

### Claude Haiku 4.5 + skill で Opus 4.7 を超えた ― SkillsBench 追試とモデル選定の設計図

SkillsBench論文の追試により、Claude Haiku 4.5にskillを組み合わせることで84.3%の精度を達成し、Opus 4.7（80.5%）を上回ることが確認された。skillは手順の固定化・評価基準の明示によって小型モデルの推論力を補完し、特に専門ドメインで大きな効果を発揮する。実運用ではタスク特性に応じてHaiku/Sonnet/Opusを使い分ける設計が重要となる。

- **ソース**: [Zenn claude](https://zenn.dev/ai_arai_ally/articles/20260422-0401-claude-haiku-4-5-skill-opus-4-7)
- **重要度**: 7/10
- **タグ**: haiku, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-22 | 自動生成 |
