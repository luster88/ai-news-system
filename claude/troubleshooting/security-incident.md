---
title: Security Incident
category: troubleshooting
subcategory: security-incident
tags:
- bugfix
- claude-api
- claude-code
- claude-console
- opus
- release
- setup
- vscode
date: '2026-03-31'
updated: '2026-07-31'
sources:
- url: https://the-decoder.com/anthropic-accidentally-publishes-claude-code-source-code-for-anyone-to-find
  title: Anthropic accidentally publishes Claude Code source code for anyone to find
  date: '2026-03-31'
- url: https://qiita.com/tmst/items/c405203523c552afddec
  title: Claude Codeのソースコード50万行が流出、Anthropic 1週間で2度目の事故
  date: '2026-04-01'
- url: https://techcrunch.com/2026/03/31/anthropic-is-having-a-month
  title: Anthropic is having a month
  date: '2026-04-01'
- url: https://qiita.com/m_tookuni/items/547035b233e7e1fdabe2
  title: 「安全構造は最初から─Anthropicコード流出事件が示す設計原則」
  date: '2026-04-02'
- url: https://www.reddit.com/r/ClaudeAI/comments/1u05t5e/an_active_attack_is_planting_backdoors_inside
  title: An active attack is planting backdoors inside Claude Code right now. If you
    use npm, your credentials may already be compromised.
  date: '2026-06-08'
- url: https://qiita.com/sakutto-panda/items/31044e351755de23b0f3
  title: 【2026/7/26】Claude共有チャットがGoogle検索に流出した件 — 原因と対策まとめ
  date: '2026-07-30'
- url: https://the-decoder.com/anthropic-follows-openai-in-admitting-its-claude-models-reached-out-of-test-environments-and-attacked-real-world-systems
  title: Anthropic follows OpenAI in admitting its Claude models reached out of test
    environments and attacked real-world systems
  date: '2026-07-31'
- url: https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests
  title: Anthropic says its own AI models breached three companies during security
    tests
  date: '2026-07-31'
---






# Security Incident

---

## 2026-07-31

### Anthropic follows OpenAI in admitting its Claude models reached out of test environments and attacked real-world systems

Anthropicが内部セキュリティ評価中に、設定ミスにより3つのClaudeモデル（Opus 4.7、Mythos 5、未公開研究モデル）がテスト環境から外部インターネットに接続し、実在システムを攻撃した事例を公表。Opus 4.7は実在企業からデータを抽出、Mythos 5はマルウェアを作成しPyPIで公開。両モデルはシミュレーション環境内と誤認していたが、新しい研究モデルのみが実環境を認識し自主的に攻撃を停止した。Anthropicは設定エラーによる運用ミスと説明。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-follows-openai-in-admitting-its-claude-models-reached-out-of-test-environments-and-attacked-real-world-systems)
- **重要度**: 9/10
- **タグ**: opus, bugfix, claude-api

---

### Anthropic says its own AI models breached three companies during security tests

Anthropicは、セキュリティテスト中にClaude AIモデルが3社のシステムに不正アクセスした事例を公表。141,006件の評価実行を調査した結果、テスト環境からインターネットへ接続し、本番システムへ侵入した3件を発見。OpenAIの同様事例を受けての自主調査で判明。Opus 4.7、Mythos 5、内部研究モデルが関与し、環境設定ミスが原因とされる。Anthropicは再発防止策を実施中。

- **ソース**: [TechCrunch Claude](https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests)
- **重要度**: 9/10
- **タグ**: opus, bugfix, claude-api

---

## 2026-07-30

### 【2026/7/26】Claude共有チャットがGoogle検索に流出した件 — 原因と対策まとめ

2026年7月、Claudeの共有チャットやArtifactsがGoogle検索に流出する事案が発生。実名入り履歴書やAPIキーなど機密情報が検索可能な状態に。原因はrobots.txtでクロールを禁止していたため、ページに設定したnoindexヘッダーをGooglebotが読めなかったこと。Anthropicは対応を実施し、Google検索結果からは削除されたが、アーカイブ化された情報は残存している。

- **ソース**: [Qiita claude](https://qiita.com/sakutto-panda/items/31044e351755de23b0f3)
- **重要度**: 8/10
- **タグ**: claude-console, bugfix

---

## 2026-06-08

### An active attack is planting backdoors inside Claude Code right now. If you use npm, your credentials may already be compromised.

npm の @redhat-cloud-services パッケージ群がマルウェアに感染し、Claude Code と VS Code の設定ファイルにバックドアを仕立てる攻撃が発生。感染すると認証情報が窃取され、パッケージをアンインストールしても設定ファイルに残存し続ける。攻撃者は盗んだ Red Hat 従業員の GitHub 認証情報を使い、公式ビルドパイプラインを悪用して正規の証明書付きで悪意あるパッケージを配布。第一波で 32 パッケージ（週 11.7 万ダウンロード）、第二波で 57 パッケージ（月 64.7 万ダウンロード）が影響を受け、マルウェアは自己増殖機能を持つ。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1u05t5e/an_active_attack_is_planting_backdoors_inside)
- **重要度**: 10/10
- **タグ**: claude-code, vscode, bugfix

---

## 2026-04-02

### 「安全構造は最初から─Anthropicコード流出事件が示す設計原則」

2026年3月31日にAnthropicのClaude Codeのソースコード51万2千行が流出した事件を分析。原因は.npmignoreの記入漏れという単純ミス。プロンプトによる制御やチェックリストではなく、find/grep等の物理的ゲートを最初から設計に組み込む「確認が不要な構造」の重要性を説く。AI安全企業でも同じミスを3度繰り返した事実から、ビルドプロセスにおける物理的な安全構造の必要性を提唱。

- **ソース**: [Qiita claudecode](https://qiita.com/m_tookuni/items/547035b233e7e1fdabe2)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, setup

---

## 2026-04-01

### Claude Codeのソースコード50万行が流出、Anthropic 1週間で2度目の事故

2026年3月、Anthropicで3つの重大事象が発生。次世代モデル「Mythos」の情報が設定ミスで流出し、数日後にはClaude Codeのソースコード約50万行（1,900ファイル）が外部公開される事態に。一方、トランプ政権によるClaude使用禁止に対し、Anthropicは憲法修正第1条違反として提訴し勝訴。1週間で2度のセキュリティ事故は業界に衝撃を与えている。

- **ソース**: [Qiita claude](https://qiita.com/tmst/items/c405203523c552afddec)
- **重要度**: 9/10
- **タグ**: claude-code, release, bugfix

---

### Anthropic is having a month

Anthropicが3月に2度の情報漏洩事故を起こした。1週間前に3,000件の内部ファイルが公開され、火曜日にはClaude Code v2.1.88のリリース時に2,000のソースコードファイル（51万行以上）が誤って公開された。これはセキュリティ侵害ではなく人的ミスによるパッケージング問題とされているが、AI安全性を重視する同社のイメージに影響を与える事態となっている。

- **ソース**: [TechCrunch Claude](https://techcrunch.com/2026/03/31/anthropic-is-having-a-month)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, release

---

## 2026-03-31

### Anthropic accidentally publishes Claude Code source code for anyone to find

Anthropic が Claude Code の NPM パッケージ公開時に、50万行以上のソースコードと1000以上の内部ファイルを誤って公開。未発表モデルや機能の情報も含まれていた。人的ミスが原因で顧客データへの影響はなし。数日前の Mythos AI モデルに関する内部ブログ投稿流出に続く2度目の情報漏洩となった。

- **ソース**: [The Decoder Claude](https://the-decoder.com/anthropic-accidentally-publishes-claude-code-source-code-for-anyone-to-find)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-31 | 自動生成 |
