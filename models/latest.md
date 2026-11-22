---
date: 2026-11-22
type: model-report
---

# 最新AIモデルまとめ - 2026-11-22

## 概要
- 2026年11月時点で、Claude Fable 5.2が最高性能モデルとして登場し、Intelligence Index 65を記録。GPT-6.2 Astra（62）、Gemini 4 Neon（61）が続く。
- AIコーディングエージェントは単体ベンチマークで高得点だが、実際の職場環境では10タスク中1つ未満しか完了できないという課題が明らかに。
- Anthropicの数学者がClaudeを用いてリーマン予想の証明を主張するなど、AI支援による数学的証明が話題に（検証は未完了）。
- Google Gemini 4シリーズ（Carbon、Neon、Hydrogen）が相次いで登場し、用途別の最適化が進む。Carbonはサイバーセキュリティとエージェントワークフローに特化。
- MCP（Model Context Protocol）の拡張やClaude Code、Codexなどのコーディングエージェントの実用化が加速。vibe-codingによるガジェットカスタマイズも広がる。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Claude Fable 5.2 | Anthropic | 65 | 最高性能。demanding reasoningと長期エージェント作業に最適。Max effort時 |
| 2 | GPT-6.2 Astra | OpenAI | 62 | Max effort時。複雑なソフトウェアエンジニアリングに強み |
| 3 | Gemini 4 Neon | Google | 61 | Xhigh推論レベル。マルチモーダル統合処理に優れる |
| 4 | Gemini 4 Carbon | Google | 60 | High effort。サイバーセキュリティとエージェントワークフローに特化 |
| 5 | Claude Opus 5.5 | Anthropic | 59 | Max effort。長期エージェントコーディングと知識作業向け |
| 6 | GPT-6.2 Sol | OpenAI | 57 | Max effort。コスパに優れる |
| 7 | Claude Sonnet 5.5 | Anthropic | 55 | Max effort。速度と知能のバランスが最良 |
| 8 | Gemini 4 Hydrogen | Google | 54 | Xhigh推論。高速処理重視。無料ユーザーにも提供 |
| 9 | GPT-6.1 Terra | OpenAI | 51 | Max effort。低コストで高性能 |
| 10 | Gemini 4 Argon | Google | 50 | High effort |
| 11 | Muse Wonder Full | Meta | 50 | Max effort。パーソナルAIエージェント |
| 12 | Kimi K3.1 Pro | Moonshot AI | 46 | 中国製。長文処理に強み |
| 13 | Muse Wonder | Meta | 44 | Max effort。エージェント機能充実 |
| 14 | Qwen4 Max | Alibaba | 43 | 984kコンテキスト |
| 15 | Claude Haiku 5.5 | Anthropic | 36 | Max effort。高速・低レイテンシタスク向け |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Claude Fable 5.2 | Anthropic | 8 | 40 | ★★ |
| Claude Opus 5.5 | Anthropic | 4 | 20 | ★★★ |
| Claude Sonnet 5.5 | Anthropic | 2 | 10 | ★★★★ |
| Claude Haiku 5.5 | Anthropic | 0.10 | 0.50 | ★★★★★ |
| Gemini 4 Carbon | Google | 不明 | 不明 | ★★ |
| Gemini 4 Neon | Google | 3 | 15 | ★★★ |
| Gemini 4 Hydrogen | Google | 不明 | 不明 | ★★★★ |
| GPT-6.2 Astra | OpenAI | 不明 | 不明 | ★★ |
| GPT-6.2 Sol | OpenAI | 不明 | 不明 | ★★★★★ |
| GPT-6.1 Terra | OpenAI | 不明 | 不明 | ★★★★★ |
| GPT-6 Luna | OpenAI | 不明 | 不明 | ★★★★★ |
| GPT-5.4 mini | OpenAI | 不明 | 不明 | ★★★★★ |
| GPT-5.4 nano | OpenAI | 不明 | 不明 | ★★★★★ |
| DeepSeek V4.1 Flash | DeepSeek | 不明 | 不明 | ★★★★★ |
| Qwen3.8-Flash-Next | Alibaba | 不明 | 不明 | ★★★★ |
| GLM-5.3 | Zhipu AI | 不明 | 不明 | ★★★ |
| Muse Wonder | Meta | 不明 | 不明 | ★★★ |
| Muse Ember | Meta | 不明 | 不明 | ★★★★★ |
| Command A+ | Cohere | 0 | 0 | ★★★★★ |
| K2 Horizon 375B A23B | 不明 | 0 | 0 | ★★★★★ |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Claude Fable 5.2 | Anthropic | 2026-11-09 | 最高性能モデル。demanding reasoningと長期エージェント作業に最適。出力速度30%向上 |
| Claude Opus 5.5 | Anthropic | 2026-09 | 長期エージェントコーディングと知識作業向け。デフォルトモデルに設定 |
| Claude Sonnet 5.5 | Anthropic | 2026-09 | 速度と知能のバランスが最良。多くのタスクに推奨 |
| Claude Haiku 5.5 | Anthropic | 2026-10 | 高速・低レイテンシ。分類、抽出、ルーティングなど大量処理向け |
| Claude Sonnet 4.6 | Anthropic | 2026-02-17 | コーディング、エージェント、長文推論で大幅性能向上。Opusクラスの性能をSonnetで実現 |
| GPT-6.2 Astra | OpenAI | 2026 | 複雑なソフトウェアエンジニアリングに強み。Intelligence Index 62 |
| GPT-6.2 Sol | OpenAI | 2026 | コスパに優れる高性能モデル。Intelligence Index 57 |
| GPT-6.1 Terra | OpenAI | 2026 | 低コストで高性能。Intelligence Index 51 |
| GPT-6 Luna | OpenAI | 2026 | 最速クラスのタスク完了時間。低コスト |
| GPT-5.4 mini | OpenAI | 2026-03-22 | 小型高速版。コーディング、ツール利用、マルチモーダル推論に最適化 |
| GPT-5.4 nano | OpenAI | 2026-03-22 | 超小型版。大量API呼び出しやサブエージェントワークロードに最適 |
| Gemini 4 Carbon | Google | 2026-11-11 | サイバーセキュリティと長期エージェントワークフローに特化。CursorBench等で1位 |
| Gemini 4 Neon | Google | 2026-11-18 | フロンティアレベルの知能と高速タスク完了。100万トークンコンテキスト |
| Gemini 4 Hydrogen | Google | 2026-11-14 | 高速処理重視。Google検索とGeminiアプリの無料ユーザーにも展開 |
| Gemini 4 Argon | Google | 2026 | Intelligence Index 50の高性能モデル |
| Gemini 3.5 Flash-Lite | Google | 2026 | 超高速・低コスト。Time to First Token最速クラス |
| DeepSeek V4.1 Flash | DeepSeek | 2026-10 | 約600万ドルで開発。全研究公開。低コスト高性能 |
| Qwen4 Max | Alibaba | 2026 | 984kコンテキスト。Intelligence Index 43 |
| Qwen3.8-Flash-Next | Alibaba | 2026 | 高速処理。256kコンテキスト |
| GLM-5.3 | Zhipu AI | 2026 | Intelligence Index 32。中国製高性能モデル |
| Kimi K3.1 Pro | Moonshot AI | 2026 | Intelligence Index 46。長文処理に強み |
| ERNIE-5.0-0110 | Baidu | 2026-01-10 | LMArenaで中国モデル1位、世界8位。数学分野で世界2位 |

### 画像生成

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Claude Fable 5.2 | Anthropic | 2026-11-09 | Pythonコードで仮想キャンバス上に筆致を再現する独自の画像生成手法 |
| Gemini Omni | Google | 2026 | Adobe FireflyやPhotoshopで利用可能な画像生成AIモデル |
| Veo | Google | 2026 | 動画生成AIモデル。Adobe製品に統合 |

### 音声AI
- 該当なし

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 4 Neon | Google | 2026-11-18 | スプレッドシート、PDF、チャート、音声、動画など多様な入力を統合処理 |
| Gemini 3 Flash | Google | 2026 | Gemini Notebookで利用。マルチモーダル対応 |
| Phi-4 Multimodal | Microsoft | 2026 | 最速クラスのTime to First Token（0.55秒） |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini Decision 1 | Google | 2026-11-14 | AIエージェントの判断処理に特化。最大1,000問を一括判定 |
| Codex | OpenAI | 2026 | コーディングエージェント。サンドボックス機構を実装 |
| Claude Code | Anthropic | 2026 | コーディングエージェント。Code Mode、Projects、Dispatch機能を追加 |
| Muse | Meta | 2026 | パーソナルAIエージェント。代理電話機能、各種アプリ連携 |

## 今週の新モデル・アップデート

### Claude Fable 5.2 (Anthropic)
- 2026年11月9日発表。最高性能モデルとしてIntelligence Index 65を記録。出力速度が前版より最大30%向上。demanding reasoningと長期エージェント作業に最適化。社内実験では1,000体超のAIエージェントを指揮し8日間でOS試作品を開発。
- 参照: [https://www.anthropic.com/news/claude-fable-5-2](https://www.anthropic.com/news/claude-fable-5-2)

### Gemini 4 Carbon (Google)
- 2026年11月11日公開。サイバーセキュリティと長期エージェントワークフローに特化した最強モデル。CursorBench 4.0、WANDR、AutomationBenchで1位獲得。/swarm機能で単一プロンプトから複数エージェント協調チーム生成が可能。
- 参照: [https://deepmind.google/blog/gemini-4-carbon-is-now-available](https://deepmind.google/blog/gemini-4-carbon-is-now-available)

### Gemini 4 Neon (Google)
- 2026年11月18日発表。フロンティアレベルの知能と高速タスク完了を実現。Artificial Analysis Intelligence Indexで総合3位（61）、Vals Indexで2位（70.9%）。100万トークンコンテキスト、入力3ドル/出力15ドル（100万トークンあたり）。
- 参照: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon)

### Gemini 4 Hydrogen (Google)
- 2026年11月14日発表。高速処理を重視した新モデルで、Google検索とGeminiアプリの無料ユーザーにも展開。xhigh推論レベルでは出力トークンが約6倍、コストも約6倍に増加するが品質が大幅向上。
- 参照: [https://ledge.ai/articles/google_gemini_4_hydrogen](https://ledge.ai/articles/google_gemini_4_hydrogen)

### Claude Opus 5.5 (Anthropic)
- 2026年11月にデフォルトモデルに設定。古いプロンプト習慣（「よく考えて」などの指示）は不要で、削除することで応答が速くなり品質は低下しない。Mediumエフォートで前世代Opus 5のHighと同等性能。
- 参照: [https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5](https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5)

### Claude Code (Anthropic)
- 2026年11月にProjects機能とDispatch機能を追加。Projectsはプロジェクトごとにファイル・指示・作業履歴をローカル保存し、AIとのコンテキストを継続可能に。Dispatchは外出先からデスクトップのAIエージェントを操作できる機能。Code Modeでは複数ツール呼び出しを1回にまとめて実行。
- 参照: [https://ai-heartland.com/tool/claude-code-code-mode](https://ai-heartland.com/tool/claude-code-code-mode)

### Gemini Notebook API (Google)
- 2026年11月10日に公式REST APIとMCPサーバを公開プレビュー提供開始。ノートブックの作成・削除、WebページやYouTube動画の自動取り込みが可能に。個人アカウントでも利用可能だが、質問応答やポッドキャスト生成は今後対応予定。
- 参照: [https://atmarkit.itmedia.co.jp/ait/articles/2611/11/news011.html](https://atmarkit.itmedia.co.jp/ait/articles/2611/11/news011.html)

### MCP Events (Anthropic)
- 2025年11月20日に仕様SEP-3415がFinalとなりベータ公開。外部イベントでエージェントを起動する機能を追加。Poll（取得）・Push（配信）・Webhook（POST受信）の3方式で購読・配信可能。MCPJamとChatGPTが対応済み。
- 参照: [https://ai-heartland.com/mcp/mcp-events](https://ai-heartland.com/mcp/mcp-events)

### Google Tasks（旧Spark） (Google)
- 2026年11月17日にリブランド。Gemini 4 Hydrogenモデル搭載で無料提供開始。食事計画、カレンダー管理、メール内の不要な定期支出検出などが可能。米国では企業への電話での価格比較や在庫確認、Google Payでの購入も可能。
- 参照: [https://www.theverge.com/tech/1035756/google-spark-ai-tasks-free](https://www.theverge.com/tech/1035756/google-spark-ai-tasks-free)

### OpenAI Astral買収 (OpenAI)
- 2026年3月22日発表。Pythonツールチェーン開発企業Astralを買収。RuffやuvなどのPython開発ツールでCodexの成長を加速させ、次世代Python開発者ツールを強化する狙い。
- 参照: [https://openai.com/index/openai-to-acquire-astral](https://openai.com/index/openai-to-acquire-astral)

### ChatGPT Wallet (OpenAI)
- 2026年11月13日発表。ChatGPT Work、Codex、dots上で動作するエージェントが承認制で購入を完了できる決済機能。エージェントによる自律的な商取引の決済基盤が整う。
- 参照: [https://qiita.com/picnic/items/1d2524574e7e141d52d5](https://qiita.com/picnic/items/1d2524574e7e141d52d5)

### GAS×Gemini (Google)
- 2026年11月17日に一般提供開始。Google Apps ScriptでGeminiサイドパネルが利用可能に。自然言語の指示でスクリプトの作成・編集・エラー修正が可能。Business Standard以上のエディションやAI関連アドオンが対象。
- 参照: [https://kn.itmedia.co.jp/kn/article/2611/18/2000003256](https://kn.itmedia.co.jp/kn/article/2611/18/2000003256)

### Samsung Gemini搭載スマートグラス (Samsung/Google)
- 2026年12月10日に米韓で発売予定。重量約41g、価格395ドルから。1,200万画素カメラで周囲を認識し、物体説明、会議要約、翻訳、道案内などをハンズフリーで利用可能。Snapdragon AR1 Gen 1搭載。
- 参照: [https://www.watch.impress.co.jp/docs/news/2157226.html](https://www.watch.impress.co.jp/docs/news/2157226.html)

### ドラクエX おしゃべりスラミィ (Square Enix/Google)
- 2026年3月発表。Gemini 3 FlashとGemini Live APIを活用した対話型AIキャラクター。プレイヤーと音声・テキストで会話し、ゲーム内の「仲間」として冒険に同行。マルチエージェント構成で質問内容に応じて適切なエージェントを自動切り替え。
- 参照: [https://www.itmedia.co.jp/aiplus/articles/2603/21/news012.html](https://www.itmedia.co.jp/aiplus/articles/2603/21/news012.html)

### Claude Duet (Anthropic)
- 2026年11月13日発表。コンシューマーAIエージェントで、仕事や小規模ビジネス向けに設計。生産性ツールやチャットサービスと連携し、優先すべきタスクを判断してカード形式で提案。Pro/Max/Ultra会員向けに米国で研究プレビュー版として提供開始。
- 参照: [https://www.theverge.com/ai-artificial-intelligence/1032518/claude-duet-ai-agent-hands-on](https://www.theverge.com/ai-artificial-intelligence/1032518/claude-duet-ai-agent-hands-on)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace)
- [https://www.theverge.com/column/1039139/vibe-coding-gadgets-tv-camera](https://www.theverge.com/column/1039139/vibe-coding-gadgets-tv-camera)
- [https://www.qbitai.com/2026/11/511870.html](https://www.qbitai.com/2026/11/511870.html)
- [https://ledge.ai/articles/anthropic_claude_riemann_hypothesis_proof_claim](https://ledge.ai/articles/anthropic_claude_riemann_hypothesis_proof_claim)
- [https://ai-heartland.com/mcp/codekb](https://ai-heartland.com/mcp/codekb)
- [https://zenn.dev/mocchi_agent/articles/ceab2005012245](https://zenn.dev/mocchi_agent/articles/ceab2005012245)
- [https://simonwillison.net/2026/Nov/20/levent-alpoge](https://simonwillison.net/2026/Nov/20/levent-alpoge)
- [https://simonwillison.net/2026/Nov/20/llm-gemini](https://simonwillison.net/2026/Nov/20/llm-gemini)
- [https://www.qbitai.com/2026/11/511570.html](https://www.qbitai.com/2026/11/511570.html)
- [https://ai-heartland.com/mcp/mcp-events](https://ai-heartland.com/mcp/mcp-events)
