---
date: 2026-11-15
type: model-report
---

# 最新AIモデルまとめ - 2026-11-15

## 概要
- 2026年11月時点で、Claude Fable 5.2がArtificial Analysis Intelligence Indexで65点を獲得し最高性能を記録。Gemini 4 Carbon（60点）、Claude Opus 5.5（59点）が続く。
- OpenAIはGPT-6シリーズ（Astra/Sol/Terra/Luna）を展開し、用途別の最適化を推進。GPT-6.1 Solは性能とコストのバランスで評価が高い。
- Google Gemini 4世代（Carbon/Hydrogen/Argon）が登場し、Carbonは数学特化、Hydrogenは高速処理、Argonはセキュリティ・コーディングに特化。
- DeepSeek V4.1 Flashが低コスト（入力$0.048/1M tokens）で高性能を維持し、中国製オープンモデルの競争力が顕著に。
- AIコーディングツール（Claude Code、Codex）の実用化が進み、非プログラマーによるアプリ開発事例や企業導入（Goldman Sachs制限、Holiday Extras活用）が報告されている。

## 性能ランキング

| 順位 | モデル名 | 提供元 | スコア | 備考 |
|---:|---|---|---:|---|
| 1 | Claude Fable 5.2 | Anthropic | 65 | 最高性能。長期エージェントワーク・高度推論に特化。出力速度30%向上 |
| 2 | Gemini 4 Carbon | Google | 60 | 数学特化。MathArenaで首位。サイバーセキュリティ機能強化 |
| 3 | Claude Opus 5.5 | Anthropic | 59 | 長時間エージェントコーディング・知識作業向け。バランス型最上位 |
| 4 | GPT-6 Astra | OpenAI | 57 | 高度タスク向け。BioBasicsBenchで66.7%達成 |
| 5 | GPT-6.1 Sol | OpenAI | 55 | バランス型。Astraの約1/5のコストで同等精度 |
| 6 | Claude Sonnet 5.5 | Anthropic | 55 | 速度と知性の最適バランス。バグ修正などに推奨 |
| 7 | Gemini 4 Hydrogen | Google | 54 | 高速処理重視。無料ユーザーにも展開予定 |
| 8 | GPT-6.1 Terra | OpenAI | 51 | GUI操作・コード修正高速。出力トークン少なめ（約159/応答） |
| 9 | Gemini 4 Argon | Google | 50 | セキュリティ・コーディング特化。CodeMender強化に使用 |
| 10 | Muse Wonder Full | Meta | 50 | マルチモーダル対応。代理電話機能を提供 |
| 11 | Kimi K3.1 Pro | Moonshot AI | 46 | 中国製。Blackwellチップ使用の痕跡が報告される |
| 12 | Muse Wonder | Meta | 44 | 最大262Kコンテキスト対応 |
| 13 | Claude Haiku 5.5 | Anthropic | 36 | 高速・低コスト。分類・抽出・ルーティング向け |
| 14 | Muse Ember | Meta | 36 | 低コスト（$0.14/タスク）。高速応答（3.3分/タスク） |
| 15 | DeepSeek V4.1 Flash 1017 | DeepSeek | 33 | 超低コスト（$0.60/タスク）。約600万ドルで開発 |

## コスト比較

| モデル名 | 提供元 | 入力 ($/1M tokens) | 出力 ($/1M tokens) | コスパ評価 |
|---|---|---:|---:|---|
| Claude Fable 5.2 | Anthropic | $8 | $40 | ★★ |
| Claude Opus 5.5 | Anthropic | $4 | $20 | ★★★ |
| Claude Sonnet 5.5 | Anthropic | $2 | $10 | ★★★★ |
| Claude Haiku 5.5 | Anthropic | $0.10 | $0.50 | ★★★★★ |
| Gemini 4 Carbon | Google | 不明 | 不明 | ★★（GPT-6.1 Solの約15倍と報道） |
| Gemini 4 Hydrogen | Google | 不明 | 不明 | ★★★★（無料ユーザー向け展開予定） |
| Gemini 4 Argon | Google | 不明 | 不明 | ★★★ |
| Gemini Omni 1.2 Flash | Google | $12/1M tokens（動画出力） | 30%値下げ実施 | ★★★★ |
| GPT-6 Astra | OpenAI | 不明 | 不明 | ★★★ |
| GPT-6.1 Sol | OpenAI | 不明 | 不明 | ★★★★★（Astraの約1/5のコスト） |
| GPT-6.1 Terra | OpenAI | 不明 | 不明（約159トークン/応答） | ★★★★（Solの半額） |
| GPT-6 Luna | OpenAI | 不明 | 不明 | ★★★★★（定型業務向け低コスト） |
| DeepSeek V4.1 Flash 1017 | DeepSeek | $0.048 | $0.192 | ★★★★★ |
| Qwen 3.8 27B | Alibaba | 不明 | 不明（Basalt 0.4.0で最大776 tok/s） | ★★★★ |
| GLM-5.3 | Zhipu AI | 不明 | 不明 | ★★★ |
| Kimi K3.1 Pro | Moonshot AI | 不明 | 不明 | ★★★ |
| MiniMax-M3.1-Flash | MiniMax | 不明 | 不明 | ★★★★ |
| Muse Wonder | Meta | 不明 | 不明 | ★★★ |
| Muse Ember | Meta | 不明 | 不明 | ★★★★★（$0.14/タスク） |
| ERNIE-5.0 | Baidu | 不明 | 不明 | ★★★（LMArena中国モデル1位） |

## カテゴリ別モデル一覧

### LLM（テキスト生成）

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Claude Fable 5.2 | Anthropic | 2026-11-09 | 最高性能。長期エージェントワーク・高度推論特化。出力30%高速化 |
| Claude Opus 5.5 | Anthropic | 2026-09 | 長時間エージェントコーディング・知識作業向けバランス型最上位 |
| Claude Sonnet 5.5 | Anthropic | 2026-09 | 速度と知性の最適バランス。バグ修正などに推奨 |
| Claude Haiku 5.5 | Anthropic | 2026-10 | 高速・低コスト。分類・抽出・ルーティング向け |
| Gemini 4 Carbon | Google | 2026-11-11 | 数学・サイバーセキュリティ特化。MathArena首位 |
| Gemini 4 Hydrogen | Google | 2026-11-14 | 高速処理重視。無料ユーザー向け展開予定 |
| Gemini 4 Argon | Google | 2026-11 | セキュリティ・コーディング特化。CodeMender強化 |
| Gemini Decision 1 | Google | 2026-11-14 | AIエージェント判断処理特化。最大1,000問一括判定 |
| GPT-6 Astra | OpenAI | 2026 | 高度タスク向け。BioBasicsBenchで66.7% |
| GPT-6.1 Sol | OpenAI | 2026 | バランス型。Astraの約1/5のコストで同等精度 |
| GPT-6.1 Terra | OpenAI | 2026 | GUI操作・コード修正高速。出力トークン少なめ |
| GPT-6 Luna | OpenAI | 2026 | 定型業務向け低コスト。最速タスク処理 |
| GPT-6 Cyber | OpenAI | 2026-11-05 | サイバーセキュリティ特化。脆弱性発見・検証能力51%向上 |
| DeepSeek V4.1 Flash 1017 | DeepSeek | 2026-10 | 超低コスト（入力$0.048/1M）。約600万ドルで開発 |
| Qwen 3.8 27B | Alibaba | 2026 | Basalt 0.4.0で最大776 tok/s。BF16比較でtop-1精度92.8% |
| Kimi K3.1 Pro | Moonshot AI | 2026 | 中国製。Blackwellチップ使用痕跡報告 |
| GLM-5.3 | Zhipu AI | 2026 | 中国製。Blackwellチップ使用痕跡報告 |
| ERNIE-5.0 | Baidu | 2026-01 | LMArenaテキストリーダーボード中国モデル1位、世界8位 |
| Muse Wonder | Meta | 2026 | 最大262Kコンテキスト。代理電話機能提供 |

### 画像生成

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Claude Fable 5.2（画像生成） | Anthropic | 2026-11-15 | Pythonコードで仮想キャンバス上に筆致再現。約70万回の筆致使用 |
| Gemini Omni 1.2 Flash | Google | 2026-11-05 | 最大15秒動画生成。30%値下げ（720p 0.07ドル/秒） |
| Seedance 2.0 | ByteDance | 2026 | 写真1枚から7秒動画生成。Bicep Hearts開発に使用 |

### 音声AI

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini Live API | Google | 2026 | 音声・テキスト対話。ドラクエXの「おしゃべりスラミィ」に採用 |

### マルチモーダル

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| Gemini 3 Flash | Google | 2026 | マルチモーダル対応。ドラクエXでGemini 3 Flash活用 |
| Gemma 4 | Google | 2026 | 軌道上で動作。宇宙TPUで俳句生成成功 |
| Phi-4 Multimodal | Microsoft | 2026 | 最速First Answer Token（0.39秒） |

### その他

| モデル名 | 提供元 | リリース日 | 特徴 |
|---|---|---|---|
| ggml 1.0 | コミュニティ | 2025-11-13 | llama.cpp基盤ライブラリ。非推奨関数13個削除の整理版 |
| Basalt 0.4.0 | コミュニティ | 2026-11-15 | Qwen 27B最大776 tok/s。構造化出力高速化 |
| Together Compiler (TKCC) | Together AI | 2026-11-13 | AI推論継続最適化。Llama 1Bで1.7倍、フロンティアモデルで2.6倍TPS向上 |
| llama-modchip | コミュニティ | 2026-11-08 | 284B DeepSeekをGPUなし64GB RAMで動作。44.36 tok/s達成 |

## 今週の新モデル・アップデート

### Claude Fable 5.2 (Anthropic)
- 2026年11月9日発表。出力速度30%向上、API料金入力$8/出力$40（100万トークンあたり）。社内実験で1,000体超AIエージェントを指揮し8日間でOS試作品開発。画像生成はPythonコードで仮想キャンバス上に筆致再現する独自手法を採用。
- 参照: [https://the-decoder.com/anthropics-claude-fable-5-2-doesnt-generate-images-it-paints-them](https://the-decoder.com/anthropics-claude-fable-5-2-doesnt-generate-images-it-paints-them)

### Gemini 4 Carbon (Google)
- 2026年11月11日一般提供開始。MathArenaベンチマークで首位獲得。サイバーセキュリティ機能と長期エージェントワークフローに特化。CursorBench 4.0、WANDR、AutomationBenchで1位。コストは次点モデルの半分以下。
- 参照: [https://deepmind.google/blog/gemini-4-carbon-is-now-available](https://deepmind.google/blog/gemini-4-carbon-is-now-available)

### Gemini 4 Hydrogen (Google)
- 2026年11月14日発表。高速処理を重視した新モデル。Google検索とGeminiアプリの無料ユーザーにも展開予定。詳細な性能指標は未公開だが、高速性能を特徴とする。
- 参照: [https://ledge.ai/articles/google_gemini_4_hydrogen](https://ledge.ai/articles/google_gemini_4_hydrogen)

### Gemini Decision 1 (Google)
- 2026年11月14日発表。AIエージェントの判断処理に特化。画像や音声などマルチモーダル入力をもとに、最大1,000問の判定を一括処理可能。AIエージェントの複雑な意思決定支援に特化した設計。
- 参照: [https://ledge.ai/articles/gemini_decision_1](https://ledge.ai/articles/gemini_decision_1)

### Gemini Omni 1.2 Flash (Google)
- 2026年11月5日一般提供。最大15秒動画生成対応、動画出力料金30%値下げ（720p 0.07ドル/秒）。マルチターン会話による編集機能搭載。360p/720pドラフト作成後1080p/4Kアップスケール可能。
- 参照: [https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips)

### Claude Opus 5.5 (Anthropic)
- 2026年11月14日、有料プラン全体でデフォルトモデルに設定。古いプロンプト習慣（「よく考えて」など）は不要で自動推論を行うため削除推奨。努力レベルはMediumから開始推奨（前世代Opus 5のHighと同等性能）。
- 参照: [https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5](https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5)

### GPT-6 Cyber (OpenAI)
- 2026年11月5日発表。サイバーセキュリティ特化モデル。ExploitGymベンチマークで前世代GPT-5.6 Cyberの32.1%から48.5%へ51%相対改善。Linuxで948件の権限昇格エクスプロイト開発、Firefoxで81件の未知高深刻度脆弱性発見。
- 参照: [https://openai.com/index/introducing-gpt-6-cyber](https://openai.com/index/introducing-gpt-6-cyber)

### Claude Code (Anthropic)
- 非プログラマーが13日間でiPhoneアプリ開発・App Store公開に成功した事例が報告（2026年11月15日）。一方、Goldman Sachsは10月に非エンジニアの利用を制限。「Don't ask again」機能で秘密情報が平文保存される問題も指摘される。
- 参照: [https://japan.cnet.com/article/35254571](https://japan.cnet.com/article/35254571)

### Codex (OpenAI)
- Holiday Extrasがモバイルアプリ再構築に活用し、従来6ヶ月以上の開発を2週間で完了。予約転換率向上、アプリエラー率19%→9%に半減（2026年11月12日報告）。OpenAIはPierre Computer Company買収を発表（11月5日）。
- 参照: [https://openai.com/business/customer-stories/holidays-extras-codex](https://openai.com/business/customer-stories/holidays-extras-codex)

### Muse (Meta)
- 2026年11月14日、代理電話機能開始。月額19.99ドル最上位プラン加入者は保険会社や飲食店への予約などをAI合成音声で代行可能。一部商家はAIと判明すると電話切断するケースも。
- 参照: [https://www.ithome.com/1/027/238.htm](https://www.ithome.com/1/027/238.htm)

### NotebookLM（Gemini Notebook） (Google)
- 2026年11月10日、公式REST APIとMCPサーバを公開プレビュー提供開始。個人アカウントでも利用可能。ノートブック作成・削除、Webページ・YouTube動画・テキスト追加を自動化可能。質問応答やポッドキャスト生成は今後対応予定。
- 参照: [https://atmarkit.itmedia.co.jp/ait/articles/2611/11/news011.html](https://atmarkit.itmedia.co.jp/ait/articles/2611/11/news011.html)

### Claude Duet (Anthropic)
- 2026年11月13日発表。コンシューマーAIエージェント。仕事・小規模ビジネス向けに設計され、生産性ツールやチャットサービスと連携。優先タスクをカード形式で提案。Pro/Max/Ultra会員向け研究プレビュー版として米国で提供開始。
- 参照: [https://www.theverge.com/ai-artificial-intelligence/1032518/claude-duet-ai-agent-hands-on](https://www.theverge.com/ai-artificial-intelligence/1032518/claude-duet-ai-agent-hands-on)

### ChatGPT Wallet (OpenAI)
- 2026年11月13日発表。ChatGPT Work、Codex、dots上で動作するエージェントが購入を完了できる決済機能。購入はユーザー承認時のみ実行。エージェントによる自律的商取引の決済基盤を整備。
- 参照: [https://qiita.com/picnic/items/1d2524574e7e141d52d5](https://qiita.com/picnic/items/1d2524574e7e141d52d5)

### Gemini for Google (GfG) (Google)
- Google社内専用コーディングAI。Geminiに社内データ1兆トークン学習。社内開発者2万9000人対象A/BテストでGemini 2.5 Pro比較でAIとのやり取り回数23.1%減、応答時間8.9%短縮、コード生存率16.8%向上（2026年11月13日論文発表）。
- 参照: [https://www.itmedia.co.jp/news/article/2611/13/2000003110](https://www.itmedia.co.jp/news/article/2611/13/2000003110)

### ERNIE-5.0 (Baidu)
- 2026年1月版がLMArenaテキストリーダーボードで中国モデル1位、世界8位獲得（1,460点）。GPT-5.1-High、Gemini-2.5-Proを上回る。数学分野で世界2位（GPT-5.2-Highに次ぐ）。
- 参照: [https://ernie.baidu.com/blog/posts/ernie-5.0-0110-release-on-lmarena](https://ernie.baidu.com/blog/posts/ernie-5.0-0110-release-on-lmarena)

## 情報源
- [https://docs.anthropic.com/en/docs/about-claude/models](https://docs.anthropic.com/en/docs/about-claude/models)
- [https://ai.google.dev/pricing](https://ai.google.dev/pricing)
- [https://artificialanalysis.ai/leaderboards/models](https://artificialanalysis.ai/leaderboards/models)
- [https://the-decoder.com/anthropics-claude-fable-5-2-doesnt-generate-images-it-paints-them](https://the-decoder.com/anthropics-claude-fable-5-2-doesnt-generate-images-it-paints-them)
- [https://japan.cnet.com/article/35254571](https://japan.cnet.com/article/35254571)
- [https://ai-heartland.com/llm/ggml](https://ai-heartland.com/llm/ggml)
- [https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up)
- [https://qiita.com/Matsda_K/items/6a29faa0431c388d83bd](https://qiita.com/Matsda_K/items/6a29faa0431c388d83bd)
- [https://www.reddit.com/r/LocalLLaMA/comments/1xwttcw/latest_version_of_strata_made_my_qwen38flashnext](https://www.reddit.com/r/LocalLLaMA/comments/1xwttcw/latest_version_of_strata_made_my_qwen38flashnext)
- [https://the-decoder.com/gemini-4-carbon-takes-the-matharena-crown-but-costs-15-times-more-than-gpt-6-1-sol](https://the-decoder.com/gemini-4-carbon-takes-the-matharena-crown-but-costs-15-times-more-than-gpt-6-1-sol)
- [https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5](https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5)
- [https://www.ithome.com/1/027/238.htm](https://www.ithome.com/1/027/238.htm)
- [https://www.ithome.com/1/027/243.htm](https://www.ithome.com/1/027/243.htm)
