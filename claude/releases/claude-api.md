---
title: Claude Api
category: releases
subcategory: claude-api
tags:
- claude-api
- mcp
- performance
- release
- 新機能
date: '2026-04-08'
updated: '2026-06-27'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1sfzcyk/official_anthropic_introduces_claude_managed
  title: 'Official: Anthropic introduces Claude Managed Agents, everything you need
    to build & deploy agents at scale'
  date: '2026-04-08'
- url: https://www.reddit.com/r/ClaudeAI/comments/1sgy11x/were_bringing_the_advisor_strategy_to_the_claude
  title: We're bringing the advisor strategy to the Claude Platform.
  date: '2026-04-09'
- url: https://qiita.com/kai_kou/items/16b4aa9fe3f235d66205
  title: Claude Managed Agents入門 — セルフホストサンドボックスとMCPトンネル活用ガイド
  date: '2026-05-20'
- url: https://zenn.dev/akasara/articles/ce6287e39a9a52
  title: Anthropic、Opus超えの新ティア「Claude Fable 5」を一般公開 — Mythos級モデルがついに誰でも使える
  date: '2026-06-09'
- url: https://the-decoder.com/anthropic-releases-claude-fable-5-and-mythos-5-with-major-gains-in-coding-and-science
  title: Anthropic releases Claude Fable 5 and Mythos 5 with major gains in coding
    and science
  date: '2026-06-09'
- url: https://qiita.com/picnic/items/ed4312c9a468f9d9e6c7
  title: Claude API 最新動向まとめ：Fable 5登場・モデル廃止・破壊的変更を完全解説
  date: '2026-06-13'
- url: https://qiita.com/picnic/items/68b39fefea726f97284f
  title: Claude API大規模更新まとめ：Fable 5登場・旧モデル廃止・30%トークン増加への対応
  date: '2026-06-26'
- url: https://qiita.com/kinamocchi_tech/items/cba6ddde529b06629bac
  title: 【速報】Anthropic SDK 同時更新！Python v0.112.0 / TypeScript v0.106.0 を3分で解説
  date: '2026-06-27'
- url: https://the-decoder.com/anthropic-gets-us-approval-to-bring-back-claude-mythos-5
  title: Anthropic gets US approval to bring back Claude Mythos 5
  date: '2026-06-27'
---







# Claude Api

---

## 2026-06-27

### 【速報】Anthropic SDK 同時更新！Python v0.112.0 / TypeScript v0.106.0 を3分で解説

2026年6月24日にAnthropic SDKのPython v0.112.0とTypeScript v0.106.0が同時リリースされた。主な変更点は、system.messageストリーミングイベント対応、refusal（拒否）カテゴリの追加、User Profile IDのリクエストヘッダー送信対応の3つ。Python版ではMemoryツールのパーミッション修正、TypeScript版ではx-stainless-helperヘッダーの整理が行われた。

- **ソース**: [Qiita claude](https://qiita.com/kinamocchi_tech/items/cba6ddde529b06629bac)
- **重要度**: 7/10
- **タグ**: claude-api, release, 新機能

---

### Anthropic gets US approval to bring back Claude Mythos 5

米国政府がAnthropicに対してClaude Mythos 5の再展開を承認。これはサイバーセキュリティに特化したAnthropicの最も強力なAIモデルで、重要インフラを運営・保護する米国組織が再び利用可能に。OpenAIのGPT-5.6 Solと同様の承認を受けた形。6月12日以降、Mythos 5とFable 5のアクセス回復に向けて米国政府と協力してきた結果、今回の承認に至った。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-gets-us-approval-to-bring-back-claude-mythos-5)
- **重要度**: 8/10
- **タグ**: release, 新機能

---

## 2026-06-26

### Claude API大規模更新まとめ：Fable 5登場・旧モデル廃止・30%トークン増加への対応

2026年4〜6月にかけてClaude APIに大規模な破壊的変更が実施されました。Sonnet 4/Opus 4/Haiku 3などの旧モデルが廃止され、新フラッグシップのFable 5/Mythos 5が登場。新トークナイザー採用により同じテキストで約30%トークン数が増加し、コスト試算の見直しが必須となります。adaptive thinkingが唯一の思考モードとなり、手動設定が不可能になるなど、APIの動作に重大な変更が含まれています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/68b39fefea726f97284f)
- **重要度**: 10/10
- **タグ**: claude-api, release, 新機能

---

## 2026-06-13

### Claude API 最新動向まとめ：Fable 5登場・モデル廃止・破壊的変更を完全解説

2025年5月から2026年6月にかけてClaude APIに大規模変更が実施。最新モデルFable 5/Mythos 5ではトークン数が約30%増加する破壊的変更があり、コスト計算とコンテキスト管理に影響。adaptive thinkingのみ対応、ZDR環境では利用不可など制約も追加。Sonnet 4/Opus 4は2026年6月15日廃止予定で移行期限が迫る。Opus 4.8が新たにリリースされ、プロンプトキャッシュの最小長が1,024トークンに改善。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/ed4312c9a468f9d9e6c7)
- **重要度**: 9/10
- **タグ**: release, claude-api

---

## 2026-06-09

### Anthropic、Opus超えの新ティア「Claude Fable 5」を一般公開 — Mythos級モデルがついに誰でも使える

Anthropicが第5世代の新ティア「Claude Fable 5」を一般公開。Opusを超える「Mythosクラス」の初の一般提供モデルで、コーディング・推論・エージェント作業でSOTAを達成。6月22日まで追加料金なしで利用可能だが、23日以降はクレジット制に移行予定。安全分類器により全セッションの5%未満でセーフガードが作動する設計。

- **ソース**: [Zenn claude](https://zenn.dev/akasara/articles/ce6287e39a9a52)
- **重要度**: 10/10
- **タグ**: release, 新機能, performance

---

### Anthropic releases Claude Fable 5 and Mythos 5 with major gains in coding and science

Anthropic が第5世代の Claude Fable 5 と Claude Mythos 5 をリリース。Fable 5 は一般利用向けで、コーディング、画像処理、複雑なデータ分析のベンチマークでトップスコアを記録。Mythos 5 は創薬やゲノム研究に特化し、選定パートナーのみに提供。価格は100万入力トークンあたり10ドルで、Claude Opus 4.8 の約2倍のコストとなる。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-releases-claude-fable-5-and-mythos-5-with-major-gains-in-coding-and-science)
- **重要度**: 10/10
- **タグ**: release, 新機能, performance

---

## 2026-05-20

### Claude Managed Agents入門 — セルフホストサンドボックスとMCPトンネル活用ガイド

AnthropicがClaude Managed Agentsに「Self-hosted sandboxes」（Beta）と「MCP tunnels」（Research Preview）を追加。企業がセンシティブなデータを外部に出さずにAIエージェントを活用できる仕組みで、オーケストレーションはクラウド、ツール実行は社内インフラで完結。ゼロトラスト設計のアウトバウンド接続でファイアウォール変更も不要。

- **ソース**: [Qiita claude](https://qiita.com/kai_kou/items/16b4aa9fe3f235d66205)
- **重要度**: 8/10
- **タグ**: 新機能, claude-api, mcp

---

## 2026-04-09

### We're bringing the advisor strategy to the Claude Platform.

Claude Platform に Advisor Strategy が導入されました。Opus をアドバイザー、Sonnet または Haiku を実行役として組み合わせ、難しい判断が必要な時だけ Opus に相談する仕組みです。SWE-bench Multilingual では Sonnet 単体より 2.7 ポイント高いスコアを記録し、タスクあたりのコストは 11.9% 削減されました。現在ベータ版として利用可能で、単一の API リクエスト内で動作します。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1sgy11x/were_bringing_the_advisor_strategy_to_the_claude)
- **重要度**: 9/10
- **タグ**: claude-api, 新機能, performance

---

## 2026-04-08

### Official: Anthropic introduces Claude Managed Agents, everything you need to build & deploy agents at scale

Anthropic が Claude Managed Agents を公式発表。エージェントの構築とデプロイを大規模に行うための包括的なソリューションで、パブリックベータとして Claude Platform で提供開始。インフラ構築に数ヶ月かかっていた作業を数日で完了でき、タスク、ツール、ガードレールを定義するだけで Anthropic のインフラ上で実行可能。Notion などの早期顧客が既にワークスペース内での並行タスク実行などに活用している。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1sfzcyk/official_anthropic_introduces_claude_managed)
- **重要度**: 9/10
- **タグ**: claude-api, 新機能, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-08 | 自動生成 |
