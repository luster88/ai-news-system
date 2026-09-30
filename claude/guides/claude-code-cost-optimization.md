---
title: Claude Code Cost Optimization
category: guides
subcategory: claude-code-cost-optimization
tags:
- claude-code
- cowork
- opus
- performance
- pricing
- prompt
- setup
- sonnet
date: '2026-04-16'
updated: '2026-09-30'
sources:
- url: https://zenn.dev/okamyuji/articles/claude-code-max-x20-token-savings
  title: Claude Codeのトークン消費が$40/日から1週間でも余裕になった全手法
  date: '2026-04-16'
- url: https://www.reddit.com/r/ClaudeAI/comments/1wogab3/made_entirely_with_opus_55_321_of_openrouter_api
  title: Made entirely with Opus 5.5 + $3.21 of OpenRouter API usage
  date: '2026-09-24'
- url: https://qiita.com/caymezon/items/d82d0e2d30d2647293dc
  title: CLAUDE.mdが肥大化してきたら、手順はSKILL.mdに切り出す
  date: '2026-09-25'
- url: https://zenn.dev/goat_eat_any/articles/claude-code-effort-explained
  title: そもそもClaude Codeのエフォートってなに？
  date: '2026-09-28'
- url: https://zenn.dev/goat_eat_any/articles/claude-code-sonnet-opus-advisor
  title: Sonnet 5.5＋Opus 5.5アドバイザーで手軽にコスト削減！
  date: '2026-09-30'
---





# Claude Code Cost Optimization

---

## 2026-09-30

### Sonnet 5.5＋Opus 5.5アドバイザーで手軽にコスト削減！

Claude Code DesktopでSonnet 5.5をメインモデルに設定し、settings.jsonにadvisorModelを追加することで、Opus 5.5をアドバイザーとして活用する方法を紹介。必要時のみOpusが起動するため、コストを抑えつつSonnetと同等の精度を実現できる。設定ファイルに数行追加するだけで導入可能。

- **ソース**: [Zenn claude](https://zenn.dev/goat_eat_any/articles/claude-code-sonnet-opus-advisor)
- **重要度**: 6/10
- **タグ**: claude-code, sonnet, opus

---

## 2026-09-28

### そもそもClaude Codeのエフォートってなに？

Claude Codeのエフォート設定について、公式ドキュメントをもとに解説。エフォートは応答にどれだけトークンを使うかを調整する仕組みで、Opus 5.5では思考の深さとコストを調整する主要な手段となる。実際にlow～maxの5段階でCSV集計課題を解かせた結果、lowでも文字コード確認など基本チェックを行い、エフォートが上がるほど検算や単価整合性確認など検証が丁寧になることが確認された。デフォルト設定のまま使うのではなく、タスクに応じて適切に調整することが推奨される。

- **ソース**: [Zenn claude](https://zenn.dev/goat_eat_any/articles/claude-code-effort-explained)
- **重要度**: 7/10
- **タグ**: claude-code, opus, performance

---

## 2026-09-25

### CLAUDE.mdが肥大化してきたら、手順はSKILL.mdに切り出す

Claude Code/Claude.aiの拡張機能であるClaude Skillsについて、CLAUDE.mdとSKILL.mdの役割の違いと使い分けを解説。SKILL.mdは呼び出し時のみ読み込まれるため詳細な手順書として最適で、descriptionフィールドでの適切な説明、コマンド実行結果の注入、disable-model-invocationによる誤実行防止などの実践的な書き方を紹介している。

- **ソース**: [Qiita claude](https://qiita.com/caymezon/items/d82d0e2d30d2647293dc)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-09-24

### Made entirely with Opus 5.5 + $3.21 of OpenRouter API usage

Claude Opus 5.5を使用して、たった$3.21のOpenRouter API費用で30-60秒のアニメーション動画を完全自動生成した事例。Claude Codeでシングルプロンプトから約1時間20分で、スクリプト・アセット・アニメーション・音声まで全て自律的に制作。8種類のOpenRouter APIを組み合わせ、人間の介入なしでハイクオリティな動画を作成したデモンストレーション。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1wogab3/made_entirely_with_opus_55_321_of_openrouter_api)
- **重要度**: 7/10
- **タグ**: claude-code, opus, cowork

---

## 2026-04-16

### Claude Codeのトークン消費が$40/日から1週間でも余裕になった全手法

Claude Code の Enterprise プランから MAX x20 への切り替えで、1日$40のトークン消費が週間レベルで大幅削減された事例を報告。社内プロキシ設定は同一のままで、課金モデルの構造差（従量課金 vs 定額制）が主因と分析。Enterprise では全トークンが API 単価で従量課金されるのに対し、MAX は月額$200で5時間/週間キャップ内なら追加課金なし。Prompt Caching の効果や、プラン共通で使えるトークン節約手法も紹介。

- **ソース**: [Zenn claude](https://zenn.dev/okamyuji/articles/claude-code-max-x20-token-savings)
- **重要度**: 7/10
- **タグ**: claude-code, pricing, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-16 | 自動生成 |
