---
date: 2026-03-22
type: model-report
---

# 最新AIモデルまとめ - 2026-03-22

## 概要
- 2026年3月中旬、GoogleがGemini 3.1 Pro Previewを発表し、Artificial Analysisのリーダーボードで最高のIntelligence Index（57）を記録。GPT-5.4と並びトップに立つ。
- Googleは低価格モデルGemini 3.1 Flash-Liteも発表。入力$0.25/出力$1.50（1M tokens）という低価格で前モデル比2.5倍の初回応答速度を実現。
- AnthropicのClaude Coworkが市場に大きな影響を与え、SaaS業界で約5.7兆円の市値蒸発。AIエージェントによる従来ソフトウェア代替が現実化。
- Claude Coworkにスマホ遠隔操作機能「Dispatch」が追加され、モバイルからPC上のタスクを実行可能に。
- 楽天がRakuten AI 3.0を発表したが、DeepSeek-V3ベースとの指摘があり、ベースモデルは非公開とされた。GoogleはAI駆動UIツール「Stitch」をβ公開。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Gemini 3.1 Pro Preview | Google | 57 | 最高のIntelligence Index、マルチモーダル対応、エージェント機能に優れる |
| 2 | GPT-5.4 (xhigh) | OpenAI | 57 | Gemini 3.1 Pro Previewと同率トップ |
| 3 | GPT-5.3 Codex (xhigh) | OpenAI | 54 | コーディングに特化した高性能モデル |
| 4 | Claude Opus 4.6 (max) | Anthropic | 53 | Extended Thinking対応、エージェント構築とコーディングに最適 |
| 5 | Claude Sonnet 4.6 (max) | Anthropic | 52 | 速度と知能のバランスに優れる、Extended Thinking対応 |
| 6 | GLM-5 (Reasoning) | Zhipu AI | 50 | 最高性能のオープンウェイトモデル |
| 7 | Kimi K2.5 (Reasoning) | Moonshot AI | 47 | 推論機能を持つオープンウェイトモデル |
| 8 | Qwen3.5 397B A17B (Reasoning) | Alibaba | 45 | 大規模パラメータの推論モデル |
| 9 | Claude Haiku 4.5 | Anthropic | 不明 | 最速モデル、フロンティアに近い知能を持つ |
| 10 | Gemini 3.1 Flash-Lite | Google | 1432 (Arena.ai Elo) | 低価格で高速、大量処理タスクに最適化 |
| 11 | Mercury 2 | 不明 | 不明 | 最速の出力速度896 tokens/s |
| 12 | Gemini 2.5 Flash-Lite (Sep) | Google | 不明 | 出力速度446 tokens/s、高速モデル |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Gemini 3.1 Pro Preview | Google | $2.00 (≤200k tokens), $4.00 (>200k tokens) | $12.00 (≤200k tokens), $18.00 (>200k tokens) | ★★★ |
| Gemini 3.1 Flash-Lite | Google | $0.25 | $1.50 | ★★★★★ |
| Claude Opus 4.6 | Anthropic | $5.00 | $25.00 | ★★ |
| Claude Sonnet 4.6 | Anthropic | $3.00 | $15.00 | ★★★ |
| Claude Haiku 4.5 | Anthropic | $1.00 | $5.00 | ★★★★ |
| Gemma 3n E4B | Google | $0.03 (blended) | 不明 | ★★★★★ |
| LFM2 24B A2B | 不明 | $0.05 (blended) | 不明 | ★★★★★ |
| Nova Micro | Amazon | $0.06 (blended) | 不明 | ★★★★★ |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 3.1 Pro Preview | Google | 2026-03 | 最高性能のマルチモーダルモデル、エージェント機能とvibe-codingに優れる |
| Gemini 3.1 Flash-Lite | Google | 2026-03-16 | 低価格・高速モデル、大量処理タスクに最適化、前モデル比2.5倍の初回応答速度 |
| Claude Opus 4.6 | Anthropic | 2026 | 最も知能の高いモデル、エージェント構築とコーディングに最適、Extended Thinking対応 |
| Claude Sonnet 4.6 | Anthropic | 2026 | 速度と知能の最良バランス、Extended Thinking対応 |
| Claude Haiku 4.5 | Anthropic | 2025-10-01 | 最速モデル、フロンティアに近い知能を持つ |
| GPT-5.4 (xhigh) | OpenAI |  | 最高Intelligence Index 57、トップクラスの性能 |
| GPT-5.3 Codex (xhigh) | OpenAI |  | コーディングに特化、楽天がMTTR50%削減を実現 |
| Rakuten AI 3.0 | 楽天 | 2026-03-17 | 日本語LLM、オープンソースベース（DeepSeek-V3との指摘あり） |
| GLM-5 (Reasoning) | Zhipu AI |  | 最高性能のオープンウェイトモデル、Intelligence Index 50 |
| Kimi K2.5 (Reasoning) | Moonshot AI |  | 推論機能を持つオープンウェイトモデル、Intelligence Index 47 |

### 画像生成
- 該当なし

### 音声AI
- 該当なし

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 3.1 Pro Preview | Google | 2026-03 | テキスト、画像、動画、音声などマルチモーダル対応、同一ベクトル空間で処理 |
| Gemini Embedding 2 | Google | 2026-03-15 | 次世代埋め込みモデル、テキスト・画像・動画・音声を同一ベクトル空間で扱う |
| Claude Opus 4.6 | Anthropic | 2026 | テキストと画像入力対応、ビジョン機能搭載 |
| Claude Sonnet 4.6 | Anthropic | 2026 | テキストと画像入力対応、ビジョン機能搭載 |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Stitch | Google | 2026-03-18 | AIを活用したUIデザイン生成ツール、手書きスケッチから数秒でコード化 |
| Groundsource | Google | 2026-03-16 | Geminiを活用してニュース報道を構造化データに変換するツール |
| Claude Cowork | Anthropic | 2026-03 | PC上でタスクを自律実行するAIエージェント、Dispatch機能でスマホ遠隔操作可能 |
| Claude Dispatch | Anthropic | 2026-03-18 | スマホからテキストメッセージでClaudeとやり取りできるサービス |

## 今週の新モデル・アップデート

### Gemini 3.1 Pro Preview (Google)
- 2026年3月に発表された最新モデル。Artificial Analysisリーダーボードで最高のIntelligence Index 57を記録。マルチモーダル理解、エージェント機能、vibe-codingで世界最高クラスの性能。入力$2-4/出力$12-18（1M tokens）。

### Gemini 3.1 Flash-Lite (Google)
- 2026年3月16日発表。入力$0.25/出力$1.50（1M tokens）という低価格を実現。前モデル比2.5倍の初回応答速度、45%の出力速度向上。Arena.aiでEloスコア1432を記録。翻訳、コンテンツモデレーション、UI生成などの大量処理に最適。
- 参照: [https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale](https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale)

### Claude Cowork Dispatch (Anthropic)
- 2026年3月18日、Claude Coworkにスマホ遠隔操作機能「Dispatch」を追加。Maxユーザー向けに試験提供開始、19日からProユーザーにも展開。スマホから指示を出すとPC上でスプレッドシート作成やファイル整理などを自律実行。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/18/news130.html](https://www.itmedia.co.jp/aiplus/articles/2603/18/news130.html)

### Stitch (Google)
- 2026年3月18日、Google Labsでβ版公開。Galileo AI技術とGemini 3を統合したUIデザイン生成ツール。自然言語や手書きスケッチから数秒でUIを自動生成。Figma書き出しやReact、Tailwind CSSコード出力に対応。現在無料、標準モード1日350回制限。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/19/news084.html](https://www.itmedia.co.jp/aiplus/articles/2603/19/news084.html)

### Gemini Embedding 2 (Google)
- 2026年3月15日発表。次世代埋め込みモデルで、テキスト、画像、動画、音声などを同一ベクトル空間で扱うマルチモーダル対応。検索や推薦システムの精度向上が期待される。
- 参照: [https://ledge.ai/articles/google_gemini_embedding_2_multimodal_embedding_model](https://ledge.ai/articles/google_gemini_embedding_2_multimodal_embedding_model)

### Rakuten AI 3.0 (楽天)
- 2026年3月17日公開。日本語LLMで、オープンソースコミュニティの既存モデルをベースに楽天独自データで開発。Hugging FaceページにDeepSeek-V3の表記があり、ベースモデルとの指摘があるが、楽天は「ベースモデルは非公開」と回答。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/19/news099.html](https://www.itmedia.co.jp/aiplus/articles/2603/19/news099.html)

### Groundsource (Google)
- 2026年3月16日発表。Geminiを活用してニュース報道を構造化データに変換するツール。気候変動や持続可能性に関連する情報を扱い、大量のニュース記事から有用なデータを抽出・整理する。
- 参照: [https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini](https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale](https://deepmind.google/blog/gemini-3-1-flash-lite-built-for-intelligence-at-scale)
- [https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini](https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini)
- [https://36kr.com/p/3729806778597639](https://36kr.com/p/3729806778597639)
- [https://www.itmedia.co.jp/aiplus/articles/2603/19/news084.html](https://www.itmedia.co.jp/aiplus/articles/2603/19/news084.html)
- [https://www.itmedia.co.jp/aiplus/articles/2603/19/news099.html](https://www.itmedia.co.jp/aiplus/articles/2603/19/news099.html)
- [https://www.itmedia.co.jp/news/articles/2603/19/news091.html](https://www.itmedia.co.jp/news/articles/2603/19/news091.html)
- [https://arxiv.org/abs/2603.15636](https://arxiv.org/abs/2603.15636)
- [https://www.producthunt.com/products/claude-dispatch](https://www.producthunt.com/products/claude-dispatch)
- [https://www.itmedia.co.jp/aiplus/articles/2603/18/news130.html](https://www.itmedia.co.jp/aiplus/articles/2603/18/news130.html)
- [https://arxiv.org/abs/2603.13239](https://arxiv.org/abs/2603.13239)
