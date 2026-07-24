---
title: Claude Code Bugfix
category: releases
subcategory: claude-code-bugfix
tags:
- bugfix
- claude-code
- opus
- pricing
- release
- 新機能
date: '2026-07-16'
updated: '2026-07-24'
sources:
- url: https://qiita.com/moha0918_/items/c8b144e3ba36744b964b
  title: Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説
  date: '2026-07-16'
- url: https://qiita.com/moha0918_/items/e534c1c6270347af0a5c
  title: Claude Code v2.1.219｜Opus 5 が新デフォルトに｜毎日Changelog解説
  date: '2026-07-24'
- url: https://qiita.com/picnic/items/fd81f1614b95cafdc830
  title: 'Claude Code v2.1.219: Opus 5追加とサブエージェント3階層化を解説'
  date: '2026-07-24'
---


# Claude Code Bugfix

---

## 2026-07-24

### Claude Code v2.1.219｜Opus 5 が新デフォルトに｜毎日Changelog解説

Claude Code v2.1.219では、Opus 5が新しいデフォルトモデルとなり、1M contextとfast modeに対応しました。fast modeの対象モデルがOpus 4.7からOpus 5とOpus 4.8に変更され、サブエージェントのネスト深さがデフォルトで3階層まで可能になりました。Dynamic workflowの既定サイズがmedium（15エージェント未満）に変更され、sandboxのネットワーク制限機能も追加されています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/e534c1c6270347af0a5c)
- **重要度**: 8/10
- **タグ**: claude-code, opus, release

---

### Claude Code v2.1.219: Opus 5追加とサブエージェント3階層化を解説

Claude Code v2.1.219がリリースされ、新モデルClaude Opus 5（1Mトークンコンテキスト対応、fast mode料金は入力$10/出力$50 per Mtok）が追加されOpus選択時のデフォルトに。サブエージェントのネスト生成が深さ3まで拡大され、多段オーケストレーションの自律性が向上。managed MCPの許可/拒否リストにおける変数解決ロジックが変更され、環境変数とmanaged-settingsのenvのみから解決されるようBreaking Changeが導入された。Opus 4.7はfast mode対象外となり、利用チームは移行が必要。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/fd81f1614b95cafdc830)
- **重要度**: 8/10
- **タグ**: claude-code, opus, release

---

### Claude Code v2.1.219｜Opus 5 が新デフォルトに｜毎日Changelog解説

Claude Code v2.1.219 では Opus 5 が新しいデフォルトの Opus モデルとなり、1M context と fast mode に対応しました。/fast の対象モデルが Opus 5 と Opus 4.8 に変更され、Opus 4.7 が外れました。サブエージェントのネスト深さがデフォルトで 3 階層まで可能になり、Dynamic workflow の既定サイズが medium（15エージェント未満）に変更されました。sandbox.network.strictAllowlist の追加により、許可リスト外のホストへの通信を即座に拒否できるようになりました。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/e534c1c6270347af0a5c)
- **重要度**: 8/10
- **タグ**: claude-code, opus, release

---

### Claude Code v2.1.219: Opus 5追加とサブエージェント3階層化を解説

Claude Code v2.1.219がリリースされ、新モデルClaude Opus 5（1Mトークン対応、fast mode料金$10/$50）が追加されOpus選択時のデフォルトに。サブエージェントのネスト生成が深さ3まで拡大され、多段オーケストレーションが可能に。managed MCPの許可リストで環境変数解決ロジックが変更され、既存の構成に影響する可能性あり。Opus 4.7はfast mode対象外となり移行が必要。

- **ソース**: [Qiita claudecode](https://qiita.com/picnic/items/fd81f1614b95cafdc830)
- **重要度**: 8/10
- **タグ**: claude-code, opus, 新機能

---

## 2026-07-16

### Claude Code v2.1.211｜Bedrock/Vertexのキャッシュ課金バグが直る｜毎日Changelog解説

Claude Code v2.1.211がリリースされ、Bedrock/Vertex/Mantle/Foundryでプロンプトキャッシュが機能せず、システムコンテキストの末尾が毎回新規トークンとして課金されていた重大なバグが修正されました。この不具合により、ゲートウェイ経由での会話が重なるほど無駄な入力トークン課金が積み上がっていました。新機能は--forward-subagent-textフラグの追加のみで、その他は権限とキャッシュ周りの挙動修正が中心となっています。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/c8b144e3ba36744b964b)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, pricing

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-16 | 自動生成 |
