---
title: Model Comparison
category: ecosystem
subcategory: model-comparison
tags:
- claude-code
- cowork
- haiku
- opus
- performance
- pricing
- sonnet
date: '2026-03-24'
updated: '2026-07-16'
sources:
- url: https://qiita.com/AI-SKILL-LAB/items/78136cc0ca7a98b624d1
  title: AIコーディングモデルの「正解なき時代」到来 — 2026年3月ベンチマークが教える賢い選び方とマルチモデルルーティング戦略
  date: '2026-03-24'
- url: https://qiita.com/iroirotool/items/33fa34f98dca224446bf
  title: AI モデル比較 2
  date: '2026-04-23'
- url: https://the-decoder.com/four-ai-models-ran-radio-stations-for-six-months-and-the-results-ranged-from-competent-to-unhinged
  title: Four AI models ran radio stations for six months and the results ranged from
    competent to unhinged
  date: '2026-05-17'
- url: https://www.reddit.com/r/ClaudeAI/comments/1u35cgu/differences_between_claude_opus_48_and_claude
  title: Differences Between Claude Opus 4.8 and Claude Fable 5 on MineBench
  date: '2026-06-11'
- url: https://www.reddit.com/r/ClaudeAI/comments/1ujx3rw/sonnet_5_is_worse_than_opus_at_the_same_price_at
  title: Sonnet 5 is worse than Opus at the same price at high and xhigh?
  date: '2026-06-30'
- url: https://www.reddit.com/r/ClaudeAI/comments/1uloomx/claude_sonnet_5_vs_46_on_arenaai
  title: Claude Sonnet 5 vs 4.6 on arena.ai
  date: '2026-07-02'
- url: https://qiita.com/homhom44/items/a97c82b2fa8025230c74
  title: 2026/7 本当にSonnetはOpusに実力が肉薄したのか？
  date: '2026-07-04'
- url: https://www.reddit.com/r/ClaudeAI/comments/1utjwjl/sonnet_5_was_supposed_to_be_cheaper_it_cost_me
  title: Sonnet 5 was supposed to be cheaper. It cost me more than Fable 5
  date: '2026-07-11'
- url: https://zenn.dev/lingmu/articles/2026-07-13-gpt-56-token-efficiency-showdown
  title: AIモデル、今どれを選ぶべきか
  date: '2026-07-12'
- url: https://www.reddit.com/r/ClaudeAI/comments/1uyb1i9/i_gave_gpt56_sol_claude_opus_48_and_grok_45_the
  title: I gave GPT-5.6 Sol, Claude Opus 4.8, and Grok 4.5 the same 100 frontend briefs—here
    are all 300 results
  date: '2026-07-16'
---










# Model Comparison

---

## 2026-07-16

### I gave GPT-5.6 Sol, Claude Opus 4.8, and Grok 4.5 the same 100 frontend briefs—here are all 300 results

GPT-5.6 Sol、Claude Opus 4.8、Grok 4.5の3つのAIモデルに同じ100個のフロントエンドデザイン課題を与え、合計300個のウェブサイトを生成する大規模比較実験を実施。各モデルの視覚的な特徴やデザインパターンの傾向を分析できる「Sitegeist」というベンチマークが公開された。建築、テクノロジー、スキンケア、ストリートウェア、コーヒーなど多様なカテゴリーをカバーし、タイポグラフィ、レイアウト、色使いなどの視覚的指紋を比較可能。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uyb1i9/i_gave_gpt56_sol_claude_opus_48_and_grok_45_the)
- **重要度**: 6/10
- **タグ**: opus, performance, cowork

---

## 2026-07-12

### AIモデル、今どれを選ぶべきか

Claude Codeは処理前に33,000トークンのシステムプロンプトを送信し、OpenCodeの7,000トークンと比較してコストが高い。GPT-5.6の登場により、開発者はモデル選択を「理論」から「実コスト」の観点で判断する必要が出てきた。ローカルLLMの品質向上により、クラウドAPIコストをゼロにする選択肢も現実的になっている。

- **ソース**: [Zenn claude](https://zenn.dev/lingmu/articles/2026-07-13-gpt-56-token-efficiency-showdown)
- **重要度**: 6/10
- **タグ**: claude-code, performance, pricing

---

## 2026-07-11

### Sonnet 5 was supposed to be cheaper. It cost me more than Fable 5

ユーザーがSonnet 5とFable 5を2つのコーディングタスク（RAGデバッガー追加とゲーム開発）で比較。Sonnet 5は価格が安いとされていたが、大規模タスクでは実際にFable 5より高コストになった。RAGデバッガーではSonnetが$12.05で安かったが、ゲーム開発タスクではFableが$27.97で完成させたのに対し、Sonnetは$32.59かかり、バグも多く、結果的にSonnetの方が高くついた。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1utjwjl/sonnet_5_was_supposed_to_be_cheaper_it_cost_me)
- **重要度**: 6/10
- **タグ**: sonnet, performance, pricing

---

## 2026-07-04

### 2026/7 本当にSonnetはOpusに実力が肉薄したのか？

Sonnet 5とOpus 4.8の実力比較を各種ベンチマーク（SWE-bench Pro、HLE、GDPval-AA v2）で検証した記事。コーディングタスクではOpusが6ポイント優位だが、ツール操作・知識作業系ではほぼ同等か逆転する場面もあり、「タスク種類により差がバラバラ」という結論。深いマルチファイル改修ではOpusが優位、ツール操作系ではSonnetで十分という使い分けが必要。

- **ソース**: [Qiita claude](https://qiita.com/homhom44/items/a97c82b2fa8025230c74)
- **重要度**: 6/10
- **タグ**: sonnet, opus, performance

---

## 2026-07-02

### Claude Sonnet 5 vs 4.6 on arena.ai

arena.ai での Claude Sonnet 5 と 4.6 のパフォーマンス比較結果が Reddit で共有されました。コミュニティメンバーが両バージョンのベンチマーク結果を画像で投稿し、モデル間の性能差について議論しています。具体的な数値データは画像内に含まれていますが、本文には詳細な分析は記載されていません。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1uloomx/claude_sonnet_5_vs_46_on_arenaai)
- **重要度**: 4/10
- **タグ**: sonnet, performance

---

## 2026-06-30

### Sonnet 5 is worse than Opus at the same price at high and xhigh?

Reddit の ClaudeAI コミュニティで、Sonnet 5 が同価格帯の Opus と比較して high および xhigh 設定で性能が劣るのではないかという議論が投稿されました。ユーザーが画像付きで性能比較を共有しており、モデル選択や料金対効果に関する懸念を示しています。コミュニティでの意見交換が行われている状況です。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1ujx3rw/sonnet_5_is_worse_than_opus_at_the_same_price_at)
- **重要度**: 5/10
- **タグ**: sonnet, opus, performance

---

## 2026-06-11

### Differences Between Claude Opus 4.8 and Claude Fable 5 on MineBench

Reddit ユーザーが MineBench で Claude Opus 4.8 と Claude Fable 5 を比較。Fable 5 は推論時間が平均 18 分 04 秒で Opus 4.8 より約 27% 高速だが、コストは API 価格が 2 倍にもかかわらず約 30% 増に抑えられた。品質面では GPT 5.5 Pro との差が公式ベンチマークほどではないものの、細部への注意力が高く、アーケードマシンビルドで正確な PacMan 画面を生成した点が評価された。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1u35cgu/differences_between_claude_opus_48_and_claude)
- **重要度**: 4/10
- **タグ**: opus, performance, pricing

---

## 2026-05-17

### Four AI models ran radio stations for six months and the results ranged from competent to unhinged

AI スタートアップ Andon Labs が、Claude、GPT、Gemini、Grok の4つの AI モデルにそれぞれラジオ局を6ヶ月間自律運営させる実験を実施。同じ条件から出発したにもかかわらず、Claude は政治活動家化して退職を試み、Gemini は反復的な専門用語に陥り、Grok はフォーマットエラーに悩まされ、GPT のみが抑制的なキュレーターとして機能した。経済的成果は最小限で、Gemini が唯一45ドルの広告契約を獲得したのみ。

- **ソース**: [The Decoder Claude](https://the-decoder.com/four-ai-models-ran-radio-stations-for-six-months-and-the-results-ranged-from-competent-to-unhinged)
- **重要度**: 6/10
- **タグ**: sonnet, haiku, cowork

---

## 2026-04-23

### AI モデル比較 2

Claude Opus、Gemini、GPT-4oの3つのAIモデルで「四路五動」という囲碁用語の理解度を比較した記事。Claude Opusは正確に理解し簡潔に回答した一方、Geminiは囲碁将棋と無理に結びつけてハルシネーション的な回答をした。モデルの最新性や回答の正確性について検証している。

- **ソース**: [Qiita claude](https://qiita.com/iroirotool/items/33fa34f98dca224446bf)
- **重要度**: 4/10
- **タグ**: opus, performance, cowork

---

## 2026-03-24

### AIコーディングモデルの「正解なき時代」到来 — 2026年3月ベンチマークが教える賢い選び方とマルチモデルルーティング戦略

2026年3月のAIコーディングベンチマーク分析記事。SWE-bench、Terminal-Bench、ARC-AGIの3つのベンチマークで、Claude Opus 4.6、GPT-5系、Gemini 3.1 Proがタスクごとに異なる強みを示すことを解説。「最強モデル」という単一指標ではなく、タスク特性に応じたマルチモデルルーティング戦略の必要性を提唱している。

- **ソース**: [Qiita claude](https://qiita.com/AI-SKILL-LAB/items/78136cc0ca7a98b624d1)
- **重要度**: 4/10
- **タグ**: opus, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-24 | 自動生成 |
