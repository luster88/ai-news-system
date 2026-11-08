---
date: 2026-11-08
type: model-report
---

# 最新AIモデルまとめ - 2026-11-08

## 概要
- 2026年10月末時点で、Gemini 4 Carbon (high)とClaude Opus 5.5 (max)がArtificial Analysis Intelligence Indexで最高スコア（60/59）を記録し、フロンティアモデルの性能競争が激化している。
- OpenAIはGPT-6シリーズ（Astra/Sol/Terra/Luna）で用途別の最適化を進め、特にGPT-6.1 Terraは低コスト・高速処理で注目を集めている。Anthropicは単一エージェント構成を推奨する方針転換を発表。
- AIコーディングツール（Claude Code、Codex）の企業導入が加速し、Goldman SachsやHeimstadenなど大手企業での活用事例が報告される一方、セキュリティリスク（AGENTS.md攻撃、settings.local.json漏洩）も顕在化。
- 中国勢ではKimi K3.1 ProがGPT-6 Astra相当の性能を達成し11月4日に無償公開予定。DeepSeek V4.1 FlashやQwen3.8シリーズも高コスパで存在感を示す。
- 料金面では、Gemini Omni 1.2 Flashが30%値下げ、Anthropicは月額200ドルUltraプランで5時間制限を撤廃するなど、競争激化に伴う価格改定が相次いでいる。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Gemini 4 Carbon (high) | Google | 60 | 最高スコア。サイバーセキュリティと長期タスク処理に特化 |
| 2 | Claude Opus 5.5 (max) | Anthropic | 59 | 長時間エージェント作業・知識作業向け最上位モデル |
| 3 | Gemini 4 Carbon (medium) | Google | 58 | Carbon高速版。コスト効率とのバランス重視 |
| 4 | Claude Opus 5.5 (xhigh) | Anthropic | 57 | 高推論設定。maxより高速でコスト効率良好 |
| 5 | GPT-6 Astra (max) | OpenAI | 57 | OpenAI最上位。高度な推論タスク向け |
| 6 | GPT-6 Astra (xhigh) | OpenAI | 55 | Astra高速版。推論品質とスピードのバランス |
| 7 | GPT-6 Astra (high) | OpenAI | 55 | 標準的な高推論設定 |
| 8 | GPT-6.1 Sol (max) | OpenAI | 55 | バランス型。Astraの約1/5のコストで同等精度 |
| 9 | Claude Sonnet 5.5 (max) | Anthropic | 55 | 速度と知性の最良バランス。最大推論設定 |
| 10 | Gemini 4 Carbon (low) | Google | 54 | Carbon低推論版。レイテンシ8.51秒と高速 |
| 11 | GPT-6.1 Sol (xhigh) | OpenAI | 52 | Sol高推論版。コスパ良好 |
| 12 | Claude Opus 5.5 (high) | Anthropic | 52 | 標準推論設定。実用的な性能とコストバランス |
| 13 | GPT-6 Astra (medium) | OpenAI | 52 | 中推論設定。レイテンシ7.31秒と高速 |
| 14 | GPT-6.1 Terra (max) | OpenAI | 51 | 定型業務向け。低コスト重視 |
| 15 | Gemini 4 Argon (high) | Google | 50 | 前世代フロンティアモデル。Carbon登場前の主力 |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Claude Fable 5.1 | Anthropic | $10 | $50 | ★★ |
| Claude Opus 5.5 | Anthropic | $4 | $20 | ★★★ |
| Claude Sonnet 5.5 | Anthropic | $2 | $10 | ★★★★ |
| Claude Haiku 5.5 | Anthropic | $0.10 | $0.50 | ★★★★★ |
| Gemini 4 Carbon | Google | $2 | $10 | ★★★★ |
| Gemini 4 Argon | Google | $2 | $10 | ★★★★ |
| Gemini Omni 1.2 Flash (720p) | Google | 不明 | $0.07/秒 | ★★★★ |
| GPT-6 Astra | OpenAI | 不明 | 不明 | ★★★ |
| GPT-6.1 Sol | OpenAI | 不明 | 不明 | ★★★★ |
| GPT-6.1 Terra | OpenAI | 不明 | 不明 | ★★★★★ |
| GPT-6 Luna | OpenAI | 不明 | 不明 | ★★★★★ |
| Kimi K3.1 Pro | Moonshot AI | $2 | $10 | ★★★★ |
| DeepSeek V4.1 Flash 1017 | DeepSeek | $0.48 | $1.92 | ★★★★★ |
| Qwen3.8 27B | Alibaba | 不明 | 不明 | ★★★★ |
| Mistral Large 4 | Mistral AI | $0.70 | $2.10 | ★★★★★ |
| GLM-5.3 | Z AI | 不明 | 不明 | ★★★ |
| Grok 4.7 | SpaceXAI | 不明 | 不明 | ★★★ |
| Muse Wonder | Meta | 不明 | 不明 | ★★★ |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 4 Carbon | Google | 2026-10-29 | サイバーセキュリティ特化。SEC-bench Pro 88.2%、ExploitGym 54.8%で最高水準 |
| Claude Opus 5.5 | Anthropic | 2026-09 | 長時間エージェント作業向け最上位。適応的思考機能搭載 |
| Claude Fable 5.1 | Anthropic | 2026 | 高度推論・長期エージェント作業向け。128Kトークン出力対応 |
| GPT-6 Astra | OpenAI | 2026 | OpenAI最上位モデル。高度タスク向け |
| GPT-6.1 Sol | OpenAI | 2026 | バランス型。Astraの約1/5コストで同等精度 |
| GPT-6.1 Terra | OpenAI | 2026 | 定型業務向け。低コスト・高速処理 |
| GPT-6 Luna | OpenAI | 2026 | 最低コスト。大量API呼び出し・サブエージェント向け |
| Kimi K3.1 Pro | Moonshot AI | 2026-10-24 | 2.8兆パラメータMoE。GPT-6 Astra相当性能。11月4日無償公開予定 |
| DeepSeek V4.1 Flash 1017 | DeepSeek | 2026-10 | 高コスパ。284Bパラメータを64GB RAMで動作可能（llama-modchip） |
| Qwen3.8 27B | Alibaba | 2026 | 中国製高性能モデル。複数推論レベル対応 |
| Mistral Large 4 (Le Chonk) | Mistral AI | 2026-10-30 | 1兆パラメータMoE（実稼働520億）。GLM-5.3匹敵、トークン使用47%減 |
| Claude Sonnet 4.6 | Anthropic | 2026-02-17 | コーディング・エージェント・長文推論で大幅向上。Opusクラスタスクを処理可能 |
| ERNIE-5.0-0110 | Baidu | 2026-01 | LMArena中国モデル1位、世界8位。数学分野世界2位 |

### 画像生成

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini Omni 1.2 Flash | Google | 2026-11-05 | 最大15秒動画生成。30%値下げ（720p 0.07ドル/秒）。マルチターン編集対応 |

### 音声AI
- 該当なし

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 4 Argon | Google | 2026 | マルチモーダル対応フロンティアモデル |
| GPT-6 Cyber | OpenAI | 2026-11-05 | サイバーセキュリティ特化。ExploitGym 48.5%、Firefox未知脆弱性81件発見 |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemma 4 | Google | 2026 | 宇宙空間でTPU上で実行成功（Project Suncatcher衛星） |
| CodeMender | Google | 2026-11-07 | 脆弱性修正AI。Gemini 4 Argon含む複数モデル活用。サンドボックス検証環境追加 |
| BioBasicsBench | OpenAI | 2026-11-06 | ウェットラボ作業評価ベンチマーク。GPT-6 Astra高推論で66.7%達成 |

## 今週の新モデル・アップデート

### Gemini 4 Carbon (Google)
- 2026年10月29日発表。サイバーセキュリティと長期タスク処理に特化した最新フロンティアモデル。SEC-bench Pro 88.2%、ExploitGym 54.8%で最高水準を達成。Gemini 4 Argonに続く迅速なリリースでフロンティア進化ペースを示す。入力100万トークン2ドル、出力10ドル。
- 参照: [https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model)

### Claude Ultra (旧Max 20x) (Anthropic)
- 2026年10月30日、月額200ドルプランを「Ultra」に改称し、認証済みアカウントの5時間制限を撤廃。週間上限は維持。月額100ドルの「Max 5x」も「Max」に改称。料金据え置きで既存契約者は自動移行。
- 参照: [https://japan.cnet.com/article/35254252](https://japan.cnet.com/article/35254252)

### Kimi K3.1 Pro (Moonshot AI)
- 2026年10月24日発表。総パラメータ2.8兆、アクティブ1040億のMoEモデル。100万トークンコンテキスト。複数ベンチマークでGPT-6 Astra、Claude Fable 5.1を上回る。2026年11月4日にモデル無償公開予定。API入力2ドル/出力10ドル（100万トークン）。
- 参照: [https://gigazine.net/news/20261024-kimi-k3-1-pro](https://gigazine.net/news/20261024-kimi-k3-1-pro)

### Mistral Large 4 (Le Chonk) (Mistral AI)
- 2026年10月30日、1兆パラメータMoEモデル（実稼働約520億）の重みをHugging Faceで公開。GLM-5.3匹敵のコーディング性能、トークン使用47%減。160以上言語対応、商用利用可。API入力0.70ドル/出力2.10ドル（100万トークン）。
- 参照: [https://www.itmedia.co.jp/aiplus/article/2610/30/2000002762](https://www.itmedia.co.jp/aiplus/article/2610/30/2000002762)

### Gemini Omni 1.2 Flash (Google)
- 2026年11月5日一般提供開始。最大15秒動画生成対応、前バージョンから30%値下げ（720p動画1秒0.07ドル）。マルチターン会話編集機能搭載。360p/720pドラフト→1080p/4Kアップスケールワークフロー対応。2026年12月3日から1.1 Flashリクエストは自動的に1.2へルーティング。
- 参照: [https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips)

### GPT-6 Cyber (OpenAI)
- 2026年11月5日発表。サイバーセキュリティ特化モデル。ExploitGymベンチマークで前世代GPT-5.6 Cyberの32.1%から48.5%へ51%相対改善。Linuxで948件の権限昇格エクスプロイト開発、Firefoxで81件の未知高深刻度脆弱性発見。スコープ外攻撃回避率99.93%。
- 参照: [https://openai.com/index/introducing-gpt-6-cyber](https://openai.com/index/introducing-gpt-6-cyber)

### OpenAI Astral買収 (OpenAI)
- 2026年3月22日発表。PythonツールチェーンRuff、uvで知られるAstralを買収。Codexの成長加速と次世代Python開発者ツール強化が狙い。Pythonエコシステムへの投資拡大。
- 参照: [https://openai.com/index/openai-to-acquire-astral](https://openai.com/index/openai-to-acquire-astral)

### Claude Cowork Projects + Dispatch (Anthropic)
- 2026年3月20日追加。Projectsはプロジェクトごとにファイル・指示・履歴をローカル保存しコンテキスト継続。Dispatchは外出先からデスクトップAIエージェント操作可能。38以上のMCPコネクター（Gmail、Slack、Notion等）と組み合わせ可能。
- 参照: [https://qiita.com/AI-SKILL-LAB/items/a39ca150b3a784a967fd](https://qiita.com/AI-SKILL-LAB/items/a39ca150b3a784a967fd)

### Anthropic単一エージェント推奨 (Anthropic)
- 2026年10月25日、最新モデル（Opus 4.5、Opus 5.5、Fable 5.1以降）が複雑タスクを単独処理可能になったため、複数サブエージェントを単一エージェントに統合すべきと推奨。実証では単一構成がマルチ構成の約2倍高速で品質・コスト・レイテンシで優位。移行キットGitHub公開。
- 参照: [https://the-decoder.com/anthropic-says-one-ai-agent-beats-many-subagents-now-that-models-can-handle-complexity-alone](https://the-decoder.com/anthropic-says-one-ai-agent-beats-many-subagents-now-that-models-can-handle-complexity-alone)

### Gemini API CLI (gemini-api) (Google)
- 2025年10月27日ベータ版公開。ステートレス・依存ゼロ設計でCI/CD、シェルスクリプト、AIエージェントから利用可能。Interactions APIベース。テキスト生成、ファイル分析、マネージドエージェント実行を単一コマンドで実行。
- 参照: [https://qiita.com/picnic/items/515e3eb615af6e782664](https://qiita.com/picnic/items/515e3eb615af6e782664)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://github.com/synchopate/llama-modchip](https://github.com/synchopate/llama-modchip)
- [https://the-decoder.com/andrej-karpathy-built-a-curated-video-platform-in-a-weekend-using-claude-and-20-years-of-hacker-news](https://the-decoder.com/andrej-karpathy-built-a-curated-video-platform-in-a-weekend-using-claude-and-20-years-of-hacker-news)
- [https://japan.cnet.com/article/35254548](https://japan.cnet.com/article/35254548)
- [https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers)
- [https://zenn.dev/torudev/articles/dd45de860fc7c3](https://zenn.dev/torudev/articles/dd45de860fc7c3)
- [https://www.reddit.com/r/LocalLLaMA/comments/1xr09nq/does_censorship_exist_in_country_according_to](https://www.reddit.com/r/LocalLLaMA/comments/1xr09nq/does_censorship_exist_in_country_according_to)
- [https://www.reddit.com/r/LocalLLaMA/comments/1xr3ymf/gpt55_dataset_across_my_used_25_billion_tokens](https://www.reddit.com/r/LocalLLaMA/comments/1xr3ymf/gpt55_dataset_across_my_used_25_billion_tokens)
- [https://www.reddit.com/r/LocalLLaMA/comments/1xr01bj/users_have_started_buying_rtx_5060_ti_16gb](https://www.reddit.com/r/LocalLLaMA/comments/1xr01bj/users_have_started_buying_rtx_5060_ti_16gb)
- [https://the-decoder.com/ai-auditors-catch-most-agent-misbehavior-but-flood-reviewers-with-false-alarms-new-study-finds](https://the-decoder.com/ai-auditors-catch-most-agent-misbehavior-but-flood-reviewers-with-false-alarms-new-study-finds)
- [https://www.ithome.com/1/023/824.htm](https://www.ithome.com/1/023/824.htm)
