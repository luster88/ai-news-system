---
title: Claude Code Security
category: guides
subcategory: claude-code-security
tags:
- claude-code
- cowork
- opus
- prompt
- setup
- 新機能
date: '2026-05-01'
updated: '2026-09-20'
sources:
- url: https://zenn.dev/yuzzzn/articles/45626e1ab08e3c
  title: AIコーディングエージェントをセキュアに使うためのハーネス設計
  date: '2026-05-01'
- url: https://qiita.com/Tadashi_Kudo/items/ffc79c01f54909974075
  title: Claude Codeのpermissions.denyを厚く書いてる人へ：たぶん全部デフォルトで防がれてる
  date: '2026-05-18'
- url: https://zenn.dev/yuzzzn/articles/29b0538948b3d1
  title: 再掲]ClaudeCodeの環境構築,使い方入門
  date: '2026-05-27'
- url: https://zenn.dev/st_27/articles/efb2436a8cd8e0
  title: ハーネスについての備忘録
  date: '2026-08-10'
- url: https://qiita.com/eiri_ai/items/39348da4e1627b72c83d
  title: Claude Code Auto Modeの権限設定をPythonで点検
  date: '2026-08-28'
- url: https://qiita.com/sescore/items/b3ebef2a1f727e3eca28
  title: Claude Code毎日運用で分かった時短術7選【2026年9月版】
  date: '2026-09-11'
- url: https://qiita.com/tkanata-honmono/items/fd7393d490faf0200161
  title: Claude Code の sandbox がわからなかったので図解してみた
  date: '2026-09-13'
- url: https://zenn.dev/tatsu_tanu/articles/d0cb3a659b4a8c
  title: 新卒がClaude Codeを3ヶ月使ってみて感じたこと
  date: '2026-09-15'
- url: https://qiita.com/yureki_lab/items/901489c12338db4d60ad
  title: Claude Code の Agent Skills(SKILL.md)を自作する実装手順 — description で発火しない・allowed-tools・補助ファイル参照の3つのハマりどころ【2026】
  date: '2026-09-16'
- url: https://qiita.com/sescore/items/aff17dc2a577e81f21b8
  title: Claude Code実務Tips7選【2026年最新】年収データ分析とSES比較
  date: '2026-09-17'
- url: https://zenn.dev/t_o_d/articles/fb181bb8a5a023
  title: claude + cve-lite-cliでフロントエンドの脆弱性対応の優先順位づけをAIに任せる
  date: '2026-09-20'
---











# Claude Code Security

---

## 2026-09-20

### claude + cve-lite-cliでフロントエンドの脆弱性対応の優先順位づけをAIに任せる

cve-lite-cliとClaude Codeの Skills 機能を組み合わせて、フロントエンドの脆弱性対応を自動化する手法の解説。CVSSとEPSSによる優先度判断をAIに任せ、セキュリティに詳しくない開発者でも効率的に脆弱性修正ができる仕組みを構築。実際の修正まで自動化し、地味で疲れる作業を軽減する。

- **ソース**: [Zenn claude](https://zenn.dev/t_o_d/articles/fb181bb8a5a023)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 2026-09-17

### Claude Code実務Tips7選【2026年最新】年収データ分析とSES比較

Claude Codeの実務Tips7選を紹介する記事。CLAUDE.mdの使い分け、Plan Modeの活用、サブエージェントによる調査と実装の分離、Hooksによる破壊的操作の防止など、実際の設定ファイルやコマンドを交えた具体的な運用ノウハウが解説されている。また、Claude Code活用スキルがSESエンジニアの年収や働き方に与える影響についても言及。

- **ソース**: [Qiita claude](https://qiita.com/sescore/items/aff17dc2a577e81f21b8)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-09-16

### Claude Code の Agent Skills(SKILL.md)を自作する実装手順 — description で発火しない・allowed-tools・補助ファイル参照の3つのハマりどころ【2026】

Claude Code の Agent Skills(SKILL.md)の自作実装手順を解説。発火トリガーは frontmatter の description のみで本文は参照されない点、allowed-tools でツール制限が可能な点、補助ファイルは SKILL.md に読み込みタイミングを明記しないと参照されない点の3つの落とし穴を実例と共に説明。CLAUDE.md との使い分けは「常時必要か特定タスクのみか」で判断し、Skills は発火まで数十トークンしか消費しないためコンテキスト効率が良い。

- **ソース**: [Qiita claudecode](https://qiita.com/yureki_lab/items/901489c12338db4d60ad)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-09-15

### 新卒がClaude Codeを3ヶ月使ってみて感じたこと

新卒エンジニアがClaude Codeを3ヶ月使用した実践的な知見を紹介。docs配下への情報集約でAIの精度向上、ステップを踏ませる指示出し、サブエージェントによる並列レビューなどの有効活用法と、数字の検証やissue乱立などの注意点を解説。AIレビューでの「やらないこと」の優先判断の重要性を強調。

- **ソース**: [Zenn claude](https://zenn.dev/tatsu_tanu/articles/d0cb3a659b4a8c)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 2026-09-13

### Claude Code の sandbox がわからなかったので図解してみた

Claude Code の sandbox 機能を図解で解説。コマンド実行時にカーネルレベルでファイルアクセスと通信を制限する仕組みを説明。permission ルールとの違い、npm スクリプトなど実際のコマンド実行の流れを詳述。Anthropic 社内では承認プロンプトが84%削減された事例も紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/tkanata-honmono/items/fd7393d490faf0200161)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-09-11

### Claude Code毎日運用で分かった時短術7選【2026年9月版】

Claude Codeの実運用で効果的だった7つの時短術を解説。CLAUDE.mdでの自動コンテキスト設定、スラッシュコマンド化、サブエージェント分業、hookによる安全性確保、Plan Modeでの設計レビューなど、実際に動く設定ファイルとコマンドを公開。無人運用時の注意点やフリーランスエンジニアの単価への影響にも言及。

- **ソース**: [Qiita claudecode](https://qiita.com/sescore/items/b3ebef2a1f727e3eca28)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-08-28

### Claude Code Auto Modeの権限設定をPythonで点検

Claude Code の Auto Mode 導入前に確認すべき settings.local.json の権限設定について解説。Bash(git *) や Bash(python *) などの広すぎる許可は Auto Mode の安全機能とは別に棚卸しが必要。許可ルールは上書きではなく併合されるため、Python スクリプトで監査対象の設定ファイルから危険な許可を抽出し、粒度を小さくする方法を提案。Auto Mode 切り替え時や MCP サーバー追加時の定期点検を推奨している。

- **ソース**: [Qiita claudecode](https://qiita.com/eiri_ai/items/39348da4e1627b72c83d)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-08-10

### ハーネスについての備忘録

Claude Codeにおけるハーネス（ツール呼び出しの制御システム）について解説した技術記事。CLAUDE.md、permissions、hooks、sandboxの4層構造と、それぞれの強制力・役割の違いを整理している。CLAUDE.mdはモデルの意図生成に影響するがハーネスの判定ロジックには介入せず、技術的な制御にはpermissions/hooks/sandboxが必要であることを強調。

- **ソース**: [Zenn claude](https://zenn.dev/st_27/articles/efb2436a8cd8e0)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-05-27

### 再掲]ClaudeCodeの環境構築,使い方入門

Claude Code の安全な環境構築ガイド。settings.json による機械的アクセス制御、PreToolUse hook による二重チェック、Docker コンテナによる隔離の3層防御を解説。200行を超えると無視されるCLAUDE.mdの制限への対処法、Claude Opus 4.7ではSubAgent呼び出しが逆効果になる点、Goal-Driven Executionによる自律実行の最適化など、最新バージョンに対応した実践的な設定方法を紹介。

- **ソース**: [Zenn claude](https://zenn.dev/yuzzzn/articles/29b0538948b3d1)
- **重要度**: 7/10
- **タグ**: claude-code, setup, opus

---

## 2026-05-18

### Claude Codeのpermissions.denyを厚く書いてる人へ：たぶん全部デフォルトで防がれてる

Claude Code の permissions.deny 設定について、デフォルトモードではClaude自身が危険な操作を確認してくるため、denyリストは重複防御になりがち。しかし bypassPermissions モード（自動実行・Agentic実行）では確認プロンプトが出ないため、denyリストが最後の砦となる。rm -rf系の破壊的コマンドやgit操作の誤実行防止には、deny設定とhooksの組み合わせが有効。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/ffc79c01f54909974075)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-01

### AIコーディングエージェントをセキュアに使うためのハーネス設計

Claude Code などの AI コーディングエージェントをセキュアに運用するためのハーネス設計手法を解説。Docker コンテナ隔離・ファイアウォール制御・ファイルアクセス制限・コマンド実行制限・プロンプト設計の 5 層防御アーキテクチャを構築し、プロンプトインジェクション・機密情報漏洩・意図しないコマンド実行のリスクに対処する多層防御を実現。

- **ソース**: [Zenn claude](https://zenn.dev/yuzzzn/articles/45626e1ab08e3c)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-01 | 自動生成 |
