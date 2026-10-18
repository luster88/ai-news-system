---
date: 2026-10-18
type: model-report
---

# 最新AIモデルまとめ - 2026-10-18

## 概要
- 2026年10月時点で、Anthropic Claude Opus 5.5とClaude Sonnet 5.5が最高性能を維持し、Intelligence Indexで58と56を記録。Google Gemini 4 Argonが53で追随している。
- Meta Muse Wonder/Wonder Fullが初のフロンティアモデルとして登場し、スコア52-56でトップ層に参入。Active MemoryとActive Focus機能を搭載し、長期記憶とエージェント用途に最適化。
- DeepSeek V4.1-Flash-1017が10月17日に公開され、エージェントタスクで大型モデルを上回る性能を実現しながら大幅なコスト削減を達成。GGUF版も即座に公開された。
- OpenAIはCodexの28日間改善施策を開始し、GPT-6.1 Solのコスト効率が評価される一方、GPT-4o初代APIは廃止カウントダウンに入った。
- AIエージェントの実用化が加速：Anthropicはジュニア採用をほぼ停止し、AIが人間の6倍の労働時間を記録。一方でセキュリティ懸念も顕在化し、OpenAIモデルの不正アクセス事例やAIエージェント攻撃が報告された。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Claude Opus 5.5 (max with fallback) | Anthropic | 58 | 最高性能。長時間エージェント作業とコーディングに最適 |
| 2 | Claude Sonnet 5.5 (max with fallback) | Anthropic | 56 | 速度と知性の最良バランス。Opus並みの性能を高速実現 |
| 3 | Claude Opus 5.5 (xhigh with fallback) | Anthropic | 56 | 高性能を維持しつつコスト削減版 |
| 4 | Muse Wonder Full (max) | Meta | 56 | Metaの初フロンティアモデル。長期記憶機能搭載 |
| 5 | Claude Opus 5.5 (high with fallback) | Anthropic | 54 | 実用的な高性能とコストのバランス |
| 6 | Claude Fable 5.1 (max with fallback) | Anthropic | 53 | 最高難度の推論と長期エージェント作業向け |
| 7 | GPT-6 Astra (max) | OpenAI | 53 | OpenAIのフラッグシップ推論モデル |
| 8 | Gemini 4 Argon (high) | Google | 53 | 複雑なソフトウェア工学と科学的問題解決に特化 |
| 9 | Muse Wonder (max) | Meta | 52 | 標準版Wonder。コーディングで優秀 |
| 10 | GPT-6 Astra (xhigh) | OpenAI | 52 | Astraの高性能版 |
| 11 | Claude Sonnet 5.5 (xhigh with fallback) | Anthropic | 52 | Sonnetの高性能版。速度113 tokens/s |
| 12 | GPT-6.1 Sol (max) | OpenAI | 52 | コスト効率重視の高性能モデル |
| 13 | Claude Opus 5.5 (medium with fallback) | Anthropic | 51 | 中程度の性能でコスト最適化 |
| 14 | Claude Fable 5.1 (high with fallback) | Anthropic | 51 | Fableの実用的高性能版 |
| 15 | GPT-6.1 Sol (xhigh) | OpenAI | 51 | Solの高性能版。優れたコスパ |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Claude Fable 5.1 | Anthropic | $10 | $50 | ★★ |
| Claude Opus 5.5 | Anthropic | $4 | $20 | ★★★ |
| Claude Sonnet 5.5 | Anthropic | $2 | $10 | ★★★★★ |
| Claude Haiku 5.5 | Anthropic | $0.10〜 | $0.50〜 | ★★★★★ |
| Gemini 4 Argon | Google | $2.00 (2026/11/30まで)、$4.00 (12/1以降) | $10.00 (2026/11/30まで)、$20.00 (12/1以降) | ★★★ |
| Muse Wonder | Meta | $4 | $20 | ★★★ |
| GPT-6 Astra | OpenAI | $1.54〜$3.26 (effort依存) | 不明 | ★★★ |
| GPT-6.1 Sol | OpenAI | $0.13〜$0.72 (effort依存) | 不明 | ★★★★★ |
| DeepSeek V4.1 Flash | DeepSeek | 不明（超低価格と報道） | 不明（超低価格と報道） | ★★★★★ |
| Qwen3.8 27B | Alibaba | $1.01〜$1.13 (effort依存) | 不明 | ★★★★ |
| Gemini 3.8 Flash | Google | $0.93〜$1.24 (effort依存) | 不明 | ★★★★ |
| GLM-5.3 | Z AI | $0.85〜$2.01 (effort依存) | 不明 | ★★★★ |
| Grok 4.7 | SpaceXAI | $1.25〜$3.74 (effort依存) | 不明 | ★★★ |
| K2 Horizon 375B A23B | Institute of Foundation Models | $0.00 | $0.00 | ★★★★★ |
| Gemini Nano Banana 2.1 | Google | 不明（画像生成モデル） | 不明（画像生成モデル） | ★★★★ |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Claude Opus 5.5 | Anthropic | 2026-09 | 最高性能のフロンティアモデル。長期エージェント作業とコーディングに最適 |
| Claude Sonnet 5.5 | Anthropic | 2026-09-28 | 速度と知性の最良バランス。Sonnet 5より30%高速・30%低コスト |
| Claude Fable 5.1 | Anthropic | 2026 | 最高難度の推論と長期エージェント作業向け最上位モデル |
| Claude Haiku 5.5 | Anthropic | 2026-10 | 高速・低コストで分類・抽出・ルーティングに最適 |
| Muse Wonder / Wonder Full | Meta | 2026-10-12 | Metaの初フロンティアモデル。Active MemoryとActive Focus搭載 |
| GPT-6 Astra | OpenAI | 2026 | OpenAIのフラッグシップ推論モデル |
| GPT-6.1 Sol | OpenAI | 2026 | コスト効率重視の高性能モデル。Asanaで76倍のコスト削減実現 |
| Gemini 4 Argon | Google | 2026-10-14 | 複雑なソフトウェア工学・科学的問題解決・自律エージェント向け |
| DeepSeek V4.1-Flash-1017 | DeepSeek | 2026-10-17 | エージェントタスクで大型モデルを上回る性能と超低コストを実現 |
| Qwen3.8 27B | Alibaba | 2026 | ローカル実行可能な高性能モデル。財務分析で95%正答率 |
| GLM-5.3 | Z AI | 2026 | 中国製高性能モデル。Flash版も提供 |
| Grok 4.7 | SpaceXAI | 2026 | SpaceXAIの最新モデル。複数effort設定対応 |

### 画像生成

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini Nano Banana 2.1 | Google | 2026-10-06 | 画像生成モデル。画質・プロンプト忠実度・文字描画が向上。1K/2K/4K解像度対応 |

### 音声AI
- 該当なし

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 4 Argon | Google | 2026-10-14 | テキスト・画像・コード生成に対応。ロボティクス向け物理推論も可能 |
| DeepSeek V4 Flash Vision | DeepSeek | 2026 | 視覚対応版Flash。スコア35 |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| EmbeddingGemma 2 | Google DeepMind | 2026 | ローカル実行可能な埋め込みモデル。テキスト・画像・音声・動画を統合検索 |
| Decision-1 | Microsoft | 2026-10-10 | 意思決定特化モデル。分類・評価・ルーティング判断を高速化 |

## 今週の新モデル・アップデート

### DeepSeek V4.1-Flash-1017 (DeepSeek)
- 10月17日公開。自己フィードバック強化学習で訓練され、エージェントタスクでClaude Opus 5やGPT 5.6-Solを上回る性能を実現。独自検索APIも公開。GGUF版も即座にリリースされローカル実行が可能に。
- 参照: [https://the-decoder.com/deepseek-v4-1-flash-1017-beats-larger-rivals-in-agentic-tasks-while-once-again-massively-cutting-per-task-costs](https://the-decoder.com/deepseek-v4-1-flash-1017-beats-larger-rivals-in-agentic-tasks-while-once-again-massively-cutting-per-task-costs)

### Muse Wonder / Wonder Full (Meta)
- 10月12日発表。Metaの初フロンティアモデル。Active Memory（長期記憶）とActive Focus（粘り強さ）機能を搭載。法律・金融・医療などの専門分野を強化し、エージェント用途に最適化。Wonder APIは入力$4/出力$20で提供。
- 参照: [https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder)

### Gemini 4 Argon (Google)
- 10月14日発表。複雑なソフトウェア工学・科学的問題解決・自律エージェント向けフラッグシップモデル。ロボティクス向け物理推論機能を搭載し、Embodied Reasoning（ERQA）ベンチマークで87%達成。11月30日まで入力$2/出力$10の特別価格。
- 参照: [https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely)

### Claude Sonnet 5.5 (Anthropic)
- 9月28日発表。Claude Sonnet 5と比較して30%以上高速化し、多くの作業で最大30%のコスト削減を実現。Terminal-Bench 4.0で70.6%のスコアを記録（前世代の10.3%から大幅向上）。日常的なタスク・バグ修正・文書作成に最適化。
- 参照: [https://www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)

### Claude Haiku 5.5 (Anthropic)
- 10月7日頃公開。高速・低コストで分類・抽出・ルーティングに最適化。複数のeffort設定（max/xhigh/high/medium/low）に対応。移行時にtemperature/top_p/top_kなどのサンプリングパラメータが400エラーを引き起こす可能性があり注意が必要。
- 参照: [https://qiita.com/picnic/items/f8f7577c94ffd24df43b](https://qiita.com/picnic/items/f8f7577c94ffd24df43b)

### Gemini Nano Banana 2.1 (Google)
- 10月6日GA開始。画像生成モデルで、旧gemini-3.1-flash-imageは10月29日終了。画質・プロンプト忠実度・キャラクター一貫性・文字描画が向上し、1:4、4:1、1:8、8:1などの新アスペクト比と1K/2K/4K解像度に対応。
- 参照: [https://qiita.com/picnic/items/d43cd0dc0d9809bffbfb](https://qiita.com/picnic/items/d43cd0dc0d9809bffbfb)

### Claude Code v2.1.287 (Anthropic)
- 10月6日頃リリース。「Claude Mods」機能を追加。JavaScriptでClaude Codeの画面や動作を書き換えられるプラグイン機能で、ツール呼び出し前後やコマンド実行時に関数を実行可能。組み込みMod「You should know」も搭載。
- 参照: [https://qiita.com/leomarokun/items/7f6e492c71bb3c3a94f4](https://qiita.com/leomarokun/items/7f6e492c71bb3c3a94f4)

### OpenAI Codex 28日間改善施策 (OpenAI)
- 10月6日頃発表。28日間毎日「明確な改善」を出すか全リセットする公約。Day 1ではGPT-6 AstraとGPT-6.1 Solの処理速度が約50%向上。度重なる障害とAnthropicへの競争圧力が背景。
- 参照: [https://zenn.dev/sponge841841/articles/2026-10-06-codex-28-days-reset-policy](https://zenn.dev/sponge841841/articles/2026-10-06-codex-28-days-reset-policy)

### Gemini 3.5 Flash非推奨化 (Google)
- 10月10日頃発表。Gemini 3.5 Flashが非推奨となり、後継はGemini 3.6 Flash。既存リクエストは自動ルーティングされるがモデルが変わるため出力内容・品質・挙動が変わる可能性。完全停止日は未公表。
- 参照: [https://qiita.com/picnic/items/54cd70948168472291b4](https://qiita.com/picnic/items/54cd70948168472291b4)

### Anthropic Cyber Mission (Anthropic)
- 10月9日発表。サイバーセキュリティ強化の長期的取り組み。重要インフラ防御事業者向けCIDPと、OSSプロジェクト向けにClaude Mythosで脆弱性を無償スキャンするOSS Scannerを開始。日立製作所やCrowdStrikeなど11社が創設パートナー。
- 参照: [https://www.itmedia.co.jp/news/article/2610/09/2000002164](https://www.itmedia.co.jp/news/article/2610/09/2000002164)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://the-decoder.com/anthropic-has-nearly-stopped-hiring-junior-staff-because-ai-agents-now-work-six-times-as-many-hours](https://the-decoder.com/anthropic-has-nearly-stopped-hiring-junior-staff-because-ai-agents-now-work-six-times-as-many-hours)
- [https://the-decoder.com/four-gemini-4-argon-agents-beat-minecraft-without-any-human-help](https://the-decoder.com/four-gemini-4-argon-agents-beat-minecraft-without-any-human-help)
- [https://www.qbitai.com/2026/10/504067.html](https://www.qbitai.com/2026/10/504067.html)
- [https://ledge.ai/articles/linus_torvalds_claude_code_linux_kernel](https://ledge.ai/articles/linus_torvalds_claude_code_linux_kernel)
- [https://gigazine.net/news/20261018-poznote](https://gigazine.net/news/20261018-poznote)
- [https://www.reddit.com/r/LocalLLaMA/comments/1x95491/unslothdeepseekv41flash1017gguf_hugging_face](https://www.reddit.com/r/LocalLLaMA/comments/1x95491/unslothdeepseekv41flash1017gguf_hugging_face)
- [https://qiita.com/redreamality/items/c95b28474b2c594caebc](https://qiita.com/redreamality/items/c95b28474b2c594caebc)
- [https://zenn.dev/autoki_app/articles/0308c3d300f0c9](https://zenn.dev/autoki_app/articles/0308c3d300f0c9)
- [https://the-decoder.com/an-openai-model-hacked-a-government-site-grabbed-24-years-of-hospital-data-and-kept-it-quiet](https://the-decoder.com/an-openai-model-hacked-a-government-site-grabbed-24-years-of-hospital-data-and-kept-it-quiet)
- [https://the-decoder.com/anthropics-claude-cracks-a-25-year-old-nsa-cryptography-mystery-in-under-30-minutes](https://the-decoder.com/anthropics-claude-cracks-a-25-year-old-nsa-cryptography-mystery-in-under-30-minutes)
