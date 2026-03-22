---
date: 2026-03-22
type: model-report
---

# 最新AIモデルまとめ - 2026-03-22

## 概要
- 2026年3月、AIモデル市場は大きな転換期を迎えている。GoogleのGemini 3.1 Pro PreviewとOpenAIのGPT-5.4 (xhigh)がIntelligence Indexで最高スコア57を記録し、性能面でトップを争っている。
- Anthropicは2月にClaude Sonnet 4.6を発表し、従来Opusクラスが必要だったタスクをSonnetで処理可能にした。さらに3月にはClaude Coworkに「Projects」と「Dispatch」機能を追加し、デスクトップAIエージェントのスマホ遠隔操作を実現。
- OpenAIはGPT-5.4の小型版「mini」と「nano」を発表し、コーディングやマルチモーダル推論に最適化。また、Pythonツールチェーン企業Astralを買収し、Codexの強化を図る。
- Googleは低価格モデルGemini 3.1 Flash-Lite（入力$0.25/1M tokens）を発表し、初回応答速度2.5倍、出力速度45%向上を実現。また、AIデザインツール「Stitch」（β版）を公開し、手書きスケッチから数秒でUIコード生成が可能に。
- 中国勢では、BaiduのERNIE-5.0-0110がLMArenaで中国モデル1位・世界8位を獲得。楽天はRakuten AI 3.0を発表したが、DeepSeek-V3ベースとの指摘があり、ベースモデルは非公開とされている。AIエージェントの台頭により、SaaS業界では約5.7兆円の市値蒸発が発生し、従来の座席課金型モデルが崩壊の危機に直面している。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Gemini 3.1 Pro Preview | Google | 57 | 最高性能のマルチモーダルモデル、エージェント機能とvibe-codingに優れる |
| 2 | GPT-5.4 (xhigh) | OpenAI | 57 | Gemini 3.1 Pro Previewと同率トップ |
| 3 | GPT-5.3 Codex (xhigh) | OpenAI | 54 | コーディング特化の高性能モデル |
| 4 | Claude Opus 4.6 (Adaptive Reasoning, Max Effort) | Anthropic | 53 | エージェント構築とコーディングに最適な最高知能モデル |
| 5 | Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort) | Anthropic | 52 | 速度と知能の最良バランス、従来Opusクラスのタスクを処理可能 |
| 6 | GLM-5 (Reasoning) | Zhipu AI | 50 | 最高ランクのオープンウェイトモデル |
| 7 | Kimi K2.5 (Reasoning) | Moonshot AI | 47 | 推論特化のオープンウェイトモデル |
| 8 | Qwen3.5 397B A17B (Reasoning) | Alibaba | 45 | 大規模パラメータの推論モデル |
| 9 | ERNIE-5.0-0110 | Baidu | 1460 (LMArena) | 中国モデル1位、世界8位、数学分野で世界2位 |
| 10 | Claude Sonnet 4.6 | Anthropic | 不明 | 100万トークンコンテキスト、前モデルより高評価 |
| 11 | Claude Haiku 4.5 | Anthropic | 不明 | 準フロンティア知能を持つ最速モデル |
| 12 | Gemini 3.1 Flash-Lite | Google | 1432 (Arena.ai Elo) | 初回応答2.5倍高速、出力45%高速化、同クラス最高性能 |
| 13 | GPT-5.4 mini | OpenAI | 不明 | コーディング、ツール利用、マルチモーダル推論に最適化 |
| 14 | GPT-5.4 nano | OpenAI | 不明 | 大量API呼び出しとサブエージェントワークロードに最適 |
| 15 | Rakuten AI 3.0 | 楽天 | 不明 | 日本語LLM、DeepSeek-V3ベースとの指摘あり |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Claude Opus 4.6 | Anthropic | 5.00 | 25.00 | ★★★ |
| Claude Sonnet 4.6 | Anthropic | 3.00 | 15.00 | ★★★★ |
| Claude Haiku 4.5 | Anthropic | 1.00 | 5.00 | ★★★★★ |
| Gemini 3.1 Pro Preview (≤200k tokens) | Google | 2.00 | 12.00 | ★★★★ |
| Gemini 3.1 Pro Preview (>200k tokens) | Google | 4.00 | 18.00 | ★★★ |
| Gemini 3.1 Pro Preview Batch (≤200k tokens) | Google | 1.00 | 6.00 | ★★★★★ |
| Gemini 3.1 Pro Preview Batch (>200k tokens) | Google | 2.00 | 9.00 | ★★★★ |
| Gemini 3.1 Flash-Lite | Google | 0.25 | 1.50 | ★★★★★ |
| Gemma 3n E4B | Google | 0.03 | 不明 | ★★★★★ |
| GPT-5.4 (xhigh) | OpenAI | 不明 | 不明 | ★★ |
| GPT-5.4 mini | OpenAI | 不明 | 不明 | ★★★★ |
| GPT-5.4 nano | OpenAI | 不明 | 不明 | ★★★★★ |
| Mercury 2 | 不明 | 不明 | 不明 | ★★★★ |
| LFM2 24B A2B | 不明 | 0.05 | 不明 | ★★★★★ |
| Nova Micro | Amazon | 0.06 | 不明 | ★★★★★ |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 3.1 Pro Preview | Google | 2026-03 | 最高性能のマルチモーダルモデル、Intelligence Index 57 |
| GPT-5.4 (xhigh) | OpenAI | 2026-03 | 最高性能モデル、Intelligence Index 57 |
| GPT-5.4 mini | OpenAI | 2026-03-22 | コーディング、ツール利用、マルチモーダル推論に最適化された小型高速版 |
| GPT-5.4 nano | OpenAI | 2026-03-22 | 大量API呼び出しとサブエージェントワークロードに最適化 |
| Claude Opus 4.6 | Anthropic | 2026-02 | エージェント構築とコーディングに最適な最高知能モデル |
| Claude Sonnet 4.6 | Anthropic | 2026-02-17 | 速度と知能の最良バランス、100万トークンコンテキスト |
| Claude Haiku 4.5 | Anthropic | 2025-10 | 準フロンティア知能を持つ最速モデル |
| ERNIE-5.0-0110 | Baidu | 2026-01 | LMArenaで中国モデル1位、世界8位、数学分野世界2位 |
| Rakuten AI 3.0 | 楽天 | 2026-03-17 | 日本語LLM、DeepSeek-V3ベースとの指摘あり |
| GLM-5 | Zhipu AI |  | 最高ランクのオープンウェイト推論モデル、Intelligence Index 50 |
| Kimi K2.5 | Moonshot AI |  | 推論特化のオープンウェイトモデル、Intelligence Index 47 |
| Qwen3.5 397B A17B | Alibaba |  | 大規模パラメータの推論モデル、Intelligence Index 45 |

### 画像生成

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Stitch | Google | 2026-03-18 | 手書きスケッチから数秒でUIデザイン生成、Gemini 3とGalileo AI技術統合 |

### 音声AI
- 該当なし

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 3 Flash | Google | 2026-03 | ドラクエXの対話型AIキャラクター「おしゃべりスラミィ」に採用 |
| Gemini 3.1 Flash-Lite | Google | 2026-03-16 | 初回応答2.5倍高速、出力45%高速化、翻訳・モデレーション・UI生成に最適 |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini Embedding 2 | Google | 2026-03-15 | テキスト、画像、動画、音声を同一ベクトル空間で扱うマルチモーダル埋め込みモデル |
| Groundsource | Google | 2026-03-16 | Geminiを活用してニュース報道を構造化データに変換するツール |

## 今週の新モデル・アップデート

### GPT-5.4 mini / nano (OpenAI)
- GPT-5.4の小型版を発表。miniとnanoはコーディング、ツール利用、マルチモーダル推論、大量API呼び出しやサブエージェントワークロードに最適化された高速バージョン。具体的な性能指標や価格は未公開。
- 参照: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano](https://openai.com/index/introducing-gpt-5-4-mini-and-nano)

### Claude Sonnet 4.6 (Anthropic)
- 2月17日発表。コーディング、エージェント機能、長文推論で大幅性能向上。100万トークンコンテキストをベータ提供。価格は従来のSonnet 4.5と同じ（入力$3/出力$15 per 1M tokens）を維持しながら、従来Opusクラスが必要だったタスクを処理可能に。
- 参照: [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)

### Claude Cowork (Projects & Dispatch) (Anthropic)
- 3月20日にProjectsとDispatch機能を追加。Projectsはプロジェクトごとにファイル・指示・作業履歴をローカル保存し、コンテキスト継続を可能に。Dispatchはスマホから外出先でデスクトップのAIエージェントを遠隔操作できる機能。MCPコネクター（Gmail、Slack、Notionなど38以上）と組み合わせ可能。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/18/news130.html](https://www.itmedia.co.jp/aiplus/articles/2603/18/news130.html)

### Gemini 3.1 Flash-Lite (Google)
- 3月16日発表。入力$0.25/出力$1.50 per 1M tokensの低価格を実現。前モデル2.5 Flashと比較して初回応答速度2.5倍、出力速度45%向上。翻訳、コンテンツモデレーション、UI生成などの大量処理タスクに最適化。Arena.aiでEloスコア1432を記録。
- 参照: [https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale](https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale)

### Stitch (β版) (Google)
- 3月18日にGoogle Labsで公開。買収したGalileo AIの技術とGemini 3を統合し、手書きスケッチや自然言語から数秒でUIデザインを自動生成。生成したデザインはFigmaへの書き出しやReact、Tailwind CSSなどのコードとして出力可能。現在無料だが、標準モード1日350回、高精度モード1日50回の制限あり。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/19/news084.html](https://www.itmedia.co.jp/aiplus/articles/2603/19/news084.html)

### ERNIE-5.0-0110 (Baidu)
- LMArenaのテキストリーダーボードで中国モデル1位、世界8位を獲得（1,460点）。GPT-5.1-HighやGemini-2.5-Proを上回り、数学分野では世界2位にランクイン。プレビュー版から正式版への移行後、初のランキング入りで首位獲得。
- 参照: [https://ernie.baidu.com/blog/posts/ernie-5.0-0110-release-on-lmarena](https://ernie.baidu.com/blog/posts/ernie-5.0-0110-release-on-lmarena)

### Rakuten AI 3.0 (楽天)
- 3月17日公開。日本語LLMとして発表されたが、Hugging FaceページにDeepSeek-V3の表記があり、ベースモデルとの指摘が相次ぐ。楽天は「ベースモデルは非公開」と回答し、「オープンソースコミュニティ上の既存モデルを基に独自データ・技術で開発」と説明。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/19/news099.html](https://www.itmedia.co.jp/aiplus/articles/2603/19/news099.html)

### Gemini Embedding 2 (Google)
- 3月15日発表。テキスト、画像、動画、音声などの異なるモダリティのデータを同一ベクトル空間で扱えるマルチモーダル埋め込みモデル。検索や推薦システムの精度向上が期待される。従来の埋め込みモデルより高度な情報検索と類似性判定が可能。
- 参照: [https://ledge.ai/articles/google_gemini_embedding_2_multimodal_embedding_model](https://ledge.ai/articles/google_gemini_embedding_2_multimodal_embedding_model)

### Groundsource (Google)
- 3月16日発表。Geminiを活用してニュース報道を構造化データに変換するツール。気候変動や持続可能性に関連する情報を扱い、大量のニュース記事から有用なデータを抽出・整理することを目的としている。
- 参照: [https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini](https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini)

### OpenAI Astral買収 (OpenAI)
- 3月22日発表。Pythonツールチェーン開発企業Astralを買収。AstralはRuffやuvなど高速なPython開発ツールで知られる。この買収によりCodexの成長を加速させ、次世代のPython開発者ツールを強化する狙い。Pythonエコシステムへの投資を拡大。
- 参照: [https://openai.com/index/openai-to-acquire-astral](https://openai.com/index/openai-to-acquire-astral)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://openai.com/index/openai-to-acquire-astral](https://openai.com/index/openai-to-acquire-astral)
- [https://openai.com/index/introducing-gpt-5-4-mini-and-nano](https://openai.com/index/introducing-gpt-5-4-mini-and-nano)
- [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [https://www.anthropic.com/81k-interviews](https://www.anthropic.com/81k-interviews)
- [https://ernie.baidu.com/blog/posts/ernie-5.0-0110-release-on-lmarena](https://ernie.baidu.com/blog/posts/ernie-5.0-0110-release-on-lmarena)
- [https://www.itmedia.co.jp/aiplus/articles/2603/21/news012.html](https://www.itmedia.co.jp/aiplus/articles/2603/21/news012.html)
- [https://qiita.com/rira__/items/ac037b9471a7cc9d7a44](https://qiita.com/rira__/items/ac037b9471a7cc9d7a44)
- [https://qiita.com/AI-SKILL-LAB/items/a39ca150b3a784a967fd](https://qiita.com/AI-SKILL-LAB/items/a39ca150b3a784a967fd)
- [https://zenn.dev/yuya_0811/articles/d97286991fa8c5](https://zenn.dev/yuya_0811/articles/d97286991fa8c5)
- [https://zenn.dev/yuya_0811/articles/1a2de6056df8dd](https://zenn.dev/yuya_0811/articles/1a2de6056df8dd)
