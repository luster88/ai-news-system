---
title: Multi Model Comparison
category: tools
subcategory: multi-model-comparison
tags:
- claude-api
- cowork
- cursor
- opus
- performance
- pricing
- sonnet
- 新機能
date: '2026-05-16'
updated: '2026-07-17'
sources:
- url: https://qiita.com/mellisaoez/items/5e1b10bbff78413287ed
  title: ChatGPT・Claude・Gemini・Grokを1つの画面で同時に動かしてみた（MultipleChatを作った話）
  date: '2026-05-16'
- url: https://qiita.com/picnic/items/88c8dda2f40dd75518ae
  title: GLM-5.2はClaude Opus代替になるか？$3.36で実地検証した結果
  date: '2026-06-24'
- url: https://www.reddit.com/r/ClaudeAI/comments/1uwe2id/testing_fable_5_opus_48_gpt56_and_more_through
  title: Testing Fable 5, Opus 4.8, GPT-5.6, and more through playable 3D games
  date: '2026-07-14'
- url: https://qiita.com/xujfcn/items/ba9d61e5c8b66a70f1c1
  title: Kimi K3 と Claude Fable 5 を実測比較：差が出たのは推論力より出力予算と検証性
  date: '2026-07-17'
---




# Multi Model Comparison

---

## 2026-07-17

### Kimi K3 と Claude Fable 5 を実測比較：差が出たのは推論力より出力予算と検証性

Kimi K3とClaude Fable 5の実測比較記事。応答速度はFable 5が37.1秒、Kimi K3が108.0秒と大きく差が出た。確率問題の途中計算ではKimi K3の方が一貫性があり、約12,500 reasoning tokensを使用。max_tokens=4000では両モデルともlengthで終了したが、7000に増やすと両方が8個のassertを通過。finish_reasonと実行テストの重要性を強調している。

- **ソース**: [Qiita claude](https://qiita.com/xujfcn/items/ba9d61e5c8b66a70f1c1)
- **重要度**: 6/10
- **タグ**: performance, sonnet, 新機能

---

## 2026-07-14

### Testing Fable 5, Opus 4.8, GPT-5.6, and more through playable 3D games

WorldBuild Benchという新しい評価手法で、Fable 5、Opus 4.8、GPT-5.6など8つのAIモデルを3Dゲーム生成タスクで比較テスト。空間的・時間的・因果的な一貫性を評価する目的で、各モデルが3種類のゲームを生成し計24個のブラウザプレイ可能な3Dゲームを作成。Fableは最も高コスト（756ドル）だが最高品質のゲームを生成し、GPT-5.6は108ドルで性能は低め、GLM-5.2とGrok 4.5は各19ドルと低コスト。ベンチマークでは捉えきれない「世界モデル」の能力を実用的なゲーム生成タスクで評価する試み。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uwe2id/testing_fable_5_opus_48_gpt56_and_more_through)
- **重要度**: 6/10
- **タグ**: opus, performance, 新機能

---

## 2026-06-24

### GLM-5.2はClaude Opus代替になるか？$3.36で実地検証した結果

Z.AIのオープンウェイトモデルGLM-5.2を用いて、Claude Opusの代替としての実用性を検証した記事。3つの実タスクを総コスト$3.36で完遂し、45分間の自律バグハンティングなどエージェント的な使い方でも機能することを確認。Claude CodeやCursorでの利用方法と、コスト削減を重視する開発者への影響を解説している。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/88c8dda2f40dd75518ae)
- **重要度**: 6/10
- **タグ**: opus, cursor, pricing

---

## 2026-05-16

### ChatGPT・Claude・Gemini・Grokを1つの画面で同時に動かしてみた（MultipleChatを作った話）

ChatGPT・Claude・Gemini・Grokを1画面で同時に動かせる「MultipleChat」の紹介記事。複数モデルの回答を並列比較でき、意見の相違箇所を自動検出する機能を持つ。各AIの得意分野の違いを活かしたクロスチェックやサブスク費用の節約が可能。

- **ソース**: [Qiita claude](https://qiita.com/mellisaoez/items/5e1b10bbff78413287ed)
- **重要度**: 6/10
- **タグ**: cowork, claude-api, cursor

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-16 | 自動生成 |
