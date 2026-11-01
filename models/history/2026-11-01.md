---
date: 2026-11-01
type: model-report
---

# 最新AIモデルまとめ - 2026-11-01

## 概要
- 2026年10月下旬、Google DeepMindがGemini 4 Carbonを発表。サイバーセキュリティと長期タスク処理に特化し、脆弱性発見などで最高水準を達成。
- Anthropicは有料プラン名称を変更（Max 20x→Ultra、Max 5x→Max）し、Ultraプランで5時間制限を撤廃。Claude Duetエージェントも発表。
- OpenAIはGPT-5.6 SolでPHPの重大脆弱性を発見し「Patch the Planet」を推進。Astral買収でPythonツールチェーン強化も発表。
- Artificial Analysisのリーダーボードでは、Gemini 4 Carbon (high)とClaude Opus 5.5 (max)が最高知能スコア（59/58）を記録。
- 中国勢ではKimi K3.1 ProがGPT-6 Astra同等性能を達成し、DeepSeek V4.1 Flash 1017が高速推論で注目を集める。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Gemini 4 Carbon (high) | Google | 59 | 最高知能スコア。サイバーセキュリティ特化、SEC-bench Pro 88.2% |
| 2 | Claude Opus 5.5 (max with fallback) | Anthropic | 58 | 長時間エージェント作業に最適、適応的思考常時ON |
| 3 | Claude Opus 5.5 (xhigh with fallback) | Anthropic | 57 | 高性能と速度のバランス、コスト効率良好 |
| 4 | GPT-6 Astra (max) | OpenAI | 57 | 最大推論能力、複雑な問題解決向け |
| 5 | GPT-6 Astra (xhigh) | OpenAI | 55 | 高性能モード、バランス型 |
| 6 | GPT-6 Astra (high) | OpenAI | 55 | 高速応答、低レイテンシ |
| 7 | GPT-6.1 Sol (max) | OpenAI | 55 | コスパ優秀、脆弱性発見実績あり |
| 8 | Claude Sonnet 5.5 (max with fallback) | Anthropic | 54 | 速度と知能の最良バランス |
| 9 | GPT-6.1 Sol (xhigh) | OpenAI | 52 | 高性能・低コスト |
| 10 | Claude Opus 5.5 (high with fallback) | Anthropic | 52 | 高速応答、実用的性能 |
| 11 | GPT-6 Astra (medium) | OpenAI | 51 | 中性能、超低レイテンシ（5.07s） |
| 12 | GPT-6.1 Terra (max) | OpenAI | 51 | 中価格帯、バランス型 |
| 13 | Gemini 4 Argon (high) | Google | 50 | 複雑なソフトウェアエンジニアリング向け、1Mトークン生成対応 |
| 14 | GPT-6.1 Sol (high) | OpenAI | 50 | 高コスパ、実用性能 |
| 15 | Claude Fable 5.1 (xhigh with fallback) | Anthropic | 50 | 最高難度推論・長期エージェント作業向け |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Claude Fable 5.1 | Anthropic | $10 | $50 | ★★ |
| Claude Opus 5.5 | Anthropic | $4 | $20 | ★★★ |
| Claude Sonnet 5.5 | Anthropic | $2 | $10 | ★★★★ |
| Claude Haiku 5.5 | Anthropic | $0.10 | $0.50 | ★★★★★ |
| Gemini 4 Argon | Google | $2.00（2026/11/30まで）→$4.00 | $10.00（2026/11/30まで）→$20.00 | ★★★ |
| Gemini 4 Carbon | Google | $2 | $10 | ★★★★ |
| GPT-6 Astra (max) | OpenAI | 推定$3-4 | 推定$15-20 | ★★★ |
| GPT-6.1 Sol | OpenAI | 推定$0.5-1 | 推定$2.5-5 | ★★★★★ |
| GPT-6.1 Terra | OpenAI | 推定$0.1-0.3 | 推定$0.5-1.5 | ★★★★★ |
| GPT-6 Luna | OpenAI | 推定$0.05-0.15 | 推定$0.25-0.75 | ★★★★★ |
| Kimi K3.1 Pro | Moonshot AI | $2 | $10 | ★★★★ |
| DeepSeek V4.1 Flash 1017 | DeepSeek | 推定$0.1-0.3 | 推定$0.5-1.5 | ★★★★★ |
| Mistral Large 4 | Mistral AI | $0.70 | $2.10 | ★★★★★ |
| GLM-5.3 | Zhipu AI | 推定$1-2 | 推定$5-10 | ★★★★ |
| Qwen3.8 Max | Alibaba | 推定$2-3 | 推定$10-15 | ★★★ |
| Qwen3.8 27B | Alibaba | 推定$0.5-1 | 推定$2.5-5 | ★★★★ |
| Grok 4.7 | SpaceXAI | 推定$2-3 | 推定$10-15 | ★★★ |
| Command A+ | Cohere | $0.00（無料層あり） | 推定$0.5-1 | ★★★★★ |
| Nemotron 3.5 Super VL | NVIDIA | 推定$0.3-0.5 | 推定$1.5-2.5 | ★★★★ |
| Mistral Small 4 | Mistral AI | 推定$0.02-0.05 | 推定$0.1-0.25 | ★★★★★ |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 4 Carbon | Google | 2026-10-29 | サイバーセキュリティ特化、脆弱性発見・エクスプロイト・パッチングで最高水準 |
| Gemini 4 Argon | Google | 2026-10 | 複雑なソフトウェアエンジニアリング・数学・科学問題解決、1Mトークン長文生成対応 |
| Claude Fable 5.1 | Anthropic | 2026 | 最高難度推論・長期エージェント作業向け、適応的思考常時ON |
| Claude Opus 5.5 | Anthropic | 2026 | 長時間エージェントコーディング・知識作業向け、1Mトークンコンテキスト |
| Claude Sonnet 5.5 | Anthropic | 2026 | 速度と知能の最良バランス、汎用性高い |
| Claude Sonnet 4.6 | Anthropic | 2026-02-17 | コーディング・エージェント・長文推論で大幅性能向上、Opusクラスタスクを処理可能 |
| Claude Haiku 5.5 | Anthropic | 2026 | 高速・低コスト、分類・抽出・ルーティング向け |
| GPT-6 Astra | OpenAI | 2026 | 最高性能推論モデル、複雑な問題解決向け |
| GPT-6.1 Sol | OpenAI | 2026 | 高性能・高コスパ、脆弱性発見実績（PHP脆弱性発見） |
| GPT-6.1 Terra | OpenAI | 2026 | 中価格帯バランス型、開発作業向け |
| GPT-6 Luna | OpenAI | 2026 | 低コスト・高速、軽量タスク向け |
| GPT-5.4 mini/nano | OpenAI | 2026-03-22 | 小型高速版、コーディング・ツール利用・マルチモーダル推論最適化 |
| Kimi K3.1 Pro | Moonshot AI | 2026-10-24 | 2.8兆パラメータMoE、GPT-6 Astra同等性能、100万トークンコンテキスト |
| DeepSeek V4.1 Flash 1017 | DeepSeek | 2026-10-18 | 超高速推論（1,486 tokens/s）、超高コスパ |
| Mistral Large 4 (Le Chonk) | Mistral AI | 2026-10-30 | 1兆パラメータMoE、GLM-5.3匹敵のコーディング性能、160言語対応 |
| GLM-5.3 | Zhipu AI | 2026 | 中国製高性能モデル、1Mトークンコンテキスト |
| Qwen3.8 27B | Alibaba | 2026 | 中型高性能モデル、推論・非推論モード切替可能 |
| Grok 4.7 | SpaceXAI | 2026 | SpaceXAI最新モデル、500kコンテキスト |
| Nanbeige 4.3-33B | Nanbeige | 2026-10-25 | 中国語LLM、Qwen3.8-27B超える性能、小型モデル蒸留基盤 |
| ERNIE-5.0-0110 | Baidu | 2026-03-22 | LMArena中国モデル1位・世界8位、数学分野世界2位 |

### 画像生成

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Canva Craft | Canva | 2026-10-22 | デザインテンプレート学習の画像生成、2K解像度・30種アスペクト比対応 |

### 音声AI

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| ACE-Step 1.5 | 不明 |  | ローカル音楽生成、Apple Silicon対応、30秒曲を約9秒生成 |

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 4 Carbon | Google | 2026-10-29 | テキスト・画像入力対応、サイバーセキュリティ特化 |
| Gemini 4 Argon | Google | 2026-10 | テキスト・画像・音声対応、複雑推論・長文生成 |
| Claude全モデル | Anthropic | 2026 | テキスト・画像入力、ビジョン・ツール使用対応 |
| Nemotron 3.5 Super VL | NVIDIA | 2026 | ビジョン・言語統合、超高速（474 tokens/s） |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Flora | NVIDIA | 2026-10-25 | ロボットビデオラベリング、GPT-6 Astraの1/125コスト、Qwen3.5ベース |
| Gemma 4 | Google | 2026 | 宇宙空間で俳句生成、衛星搭載TPUで実行 |

## 今週の新モデル・アップデート

### Gemini 4 Carbon (Google)
- 2026年10月29日発表。サイバーセキュリティ特化のフロンティアモデル。SEC-bench Pro 88.2%、ExploitGym 54.8%、CWE-bench 71.0%で最高水準達成。まずサイバー防衛担当者に限定提供後、段階的拡大予定。
- 参照: [https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model)

### Claude有料プラン改称・制限撤廃 (Anthropic)
- 2026年10月30日発表。Max 20x→Ultra（月額$200）、Max 5x→Max（月額$100）に改称。Ultraプランで認証済みアカウントの5時間制限撤廃、週間制限内で自由配分可能に。
- 参照: [https://www.anthropic.com/news](https://www.anthropic.com/news)

### Claude Duet (Anthropic)
- 2026年10月21日発表。プロフェッショナル・中小企業向けAIエージェント。Claude Opus 5.5ベース、接続アプリから毎朝ブリーフィング、会議調整・財務予測・Webアプリプロトタイピング等実行。米国Pro/Maxサブスクライバー向けウェイトリスト提供中。
- 参照: [https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent](https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent)

### Claude Cowork Projects + Dispatch (Anthropic)
- 2026年3月20日追加。Projectsはプロジェクトごとにファイル・指示・履歴をローカル保存しコンテキスト継続。Dispatchは外出先からデスクトップAIエージェント操作可能。38以上のMCPコネクター対応。
- 参照: [https://qiita.com/AI-SKILL-LAB/items/a39ca150b3a784a967fd](https://qiita.com/AI-SKILL-LAB/items/a39ca150b3a784a967fd)

### OpenAI Astral買収 (OpenAI)
- 2026年3月22日発表。Pythonツールチェーン開発企業Astral（Ruff、uv等）を買収。Codexの成長加速と次世代Python開発者ツール強化が狙い。
- 参照: [https://openai.com/index/openai-to-acquire-astral](https://openai.com/index/openai-to-acquire-astral)

### GPT-5.6 Sol PHP脆弱性発見 (OpenAI)
- 2026年10月21日発表。GPT-5.6 SolがPHPの重大脆弱性を発見。「Patch the Planet」イニシアチブの一環で、攻撃者発見前にAIが検出し修正・防御策を準備。同様の発見が今後数ヶ月で急増と予測。
- 参照: [https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities)

### Kimi K3.1 Pro (Moonshot AI)
- 2026年10月24日発表。2.8兆パラメータMoE（アクティブ1040億）、100万トークンコンテキスト。GPT-6 Astra・Claude Fable 5.1超える性能。2026年11月4日モデル無償公開予定。API: 入力$2/出力$10 per 1M tokens。
- 参照: [https://gigazine.net/news/20261024-kimi-k3-1-pro](https://gigazine.net/news/20261024-kimi-k3-1-pro)

### DeepSeek V4.1 Flash 1017 (DeepSeek)
- 2026年10月18日発表。超高速推論（非推論モード1,486 tokens/s）、超高コスパ。検索API（Search API）も同時公開。GGUF版もUnslothチームが公開。
- 参照: [https://www.qbitai.com/2026/10/504067.html](https://www.qbitai.com/2026/10/504067.html)

### Mistral Large 4 (Le Chonk) (Mistral AI)
- 2026年10月30日、1兆パラメータMoE（実稼働約520億）の重みをHugging Faceで公開。GLM-5.3匹敵のコーディング性能、トークン使用量47%削減。160言語対応、商用利用可。API: 入力$0.70/出力$2.10 per 1M tokens。
- 参照: [https://www.itmedia.co.jp/aiplus/article/2610/30/2000002762](https://www.itmedia.co.jp/aiplus/article/2610/30/2000002762)

### Claude Sonnet 4.6 (Anthropic)
- 2026年2月17日発表。コーディング・エージェント・長文推論・コンピュータ操作で大幅性能向上。従来Opusクラス必要タスクをSonnetで処理可能に。100万トークンコンテキストベータ提供。価格据え置き（入力$3/出力$15 per 3M tokens）。
- 参照: [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)

### Gemini Notebook教科書アクセス (Google)
- 2026年10月30日発表。米国・インドの出版社提供の数百冊教科書に無料アクセス可能。OpenStax、Open Textbook Library等。日本からも利用可。教科書ベースの質問回答・練習問題・フラッシュカード作成対応。
- 参照: [https://www.itmedia.co.jp/aiplus/article/2610/30/2000002760](https://www.itmedia.co.jp/aiplus/article/2610/30/2000002760)

### Canva Craft (Canva)
- 2026年10月22日発表。独自開発画像生成モデル。人間デザインテンプレート学習、2K解像度・30種アスペクト比対応。生成画像をCanva Magicで編集可能なレイヤー化デザインに変換可能。全ユーザー提供、ChatGPT・Gemini等でも利用可。
- 参照: [https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model](https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model)

### Google衛星AI (Project Suncatcher) (Google)
- 2026年10月30日、宇宙空間のTPU搭載衛星から初応答送信成功。Gemma 4モデルで俳句生成。今後、軌道上での熱ストレス・放射線下TPU性能評価継続。2027年双子衛星打ち上げ予定。
- 参照: [https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission](https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission)

### OpenAI・Google Cloud提携拡大 (OpenAI)
- 2026年10月21日発表。OpenAIモデル・CodexエージェントをGoogle Cloud Model Gardenに統合。GCP Marketplace経由購入可、既存コミットメント利用可。数週間以内一般提供開始。
- 参照: [https://openai.com/index/openai-models-google-cloud](https://openai.com/index/openai-models-google-cloud)

### Anthropic透かし機能拡大 (Anthropic)
- 2026年10月31日、EU AI法対応でClaude 4モデルにテキスト透かし拡大展開。旧モデル（Opus 4.6、Sonnet 4.6）ではサンプリングパラメータ変更で回避可能な抜け穴あり。新モデル（Mythos 5、Opus 4.7）では制限言及なし。
- 参照: [https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models](https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://the-decoder.com/empathetic-prompts-can-turn-ai-chatbots-into-seemingly-traumatized-conversational-partners](https://the-decoder.com/empathetic-prompts-can-turn-ai-chatbots-into-seemingly-traumatized-conversational-partners)
- [https://www.qbitai.com/2026/11/507038.html](https://www.qbitai.com/2026/11/507038.html)
- [https://japan.cnet.com/article/35254252](https://japan.cnet.com/article/35254252)
- [https://gigazine.net/news/20261031-m3e-canvas](https://gigazine.net/news/20261031-m3e-canvas)
- [https://www.reddit.com/r/LocalLLaMA/comments/1xkxt7a/memdoor_a_team_of_5_qwen3827b_models_beats_fable](https://www.reddit.com/r/LocalLLaMA/comments/1xkxt7a/memdoor_a_team_of_5_qwen3827b_models_beats_fable)
- [https://qiita.com/shu15511551/items/a509cef8e698bef329f7](https://qiita.com/shu15511551/items/a509cef8e698bef329f7)
- [https://qiita.com/songchong/items/ac9779bb8e8838b546b9](https://qiita.com/songchong/items/ac9779bb8e8838b546b9)
- [https://zenn.dev/deepai/articles/claude-code-windows-native-or-wsl](https://zenn.dev/deepai/articles/claude-code-windows-native-or-wsl)
- [https://zenn.dev/marvelousu/articles/gpt61-terra-usage-review](https://zenn.dev/marvelousu/articles/gpt61-terra-usage-review)
- [https://qiita.com/CodeTea_Ping999/items/ec2e84db05b27355c82a](https://qiita.com/CodeTea_Ping999/items/ec2e84db05b27355c82a)
