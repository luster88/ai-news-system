---
title: Performance Optimization
category: troubleshooting
subcategory: performance-optimization
tags:
- claude-api
- claude-code
- mcp
- performance
- setup
date: '2026-05-15'
updated: '2026-08-19'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/60adfc41690c45d59f15
  title: ハーネスを育てすぎたClaude Codeが素のClaude Codeに負ける「naked codex現象」——自己診断と対処法
  date: '2026-05-15'
- url: https://qiita.com/architectJapan/items/ec7669cb308277a9d4bb
  title: 自宅サーバー1台にAnthropicのbotが1日4万アクセスしてきた、でも全然遅くならなかった話
  date: '2026-05-27'
- url: https://qiita.com/nomurasan/items/c227b092ba30d18aa8a1
  title: Claude Code hookが遅い原因はpydanticだった ― 起動コストを実測してGoに移植したら約8割削減できた話
  date: '2026-08-19'
---



# Performance Optimization

---

## 2026-08-19

### Claude Code hookが遅い原因はpydanticだった ― 起動コストを実測してGoに移植したら約8割削減できた話

Claude Code の hook 実行時、Python + pydantic の起動コストが 108ms と支配的だったため、頻度の高い hook を Go に移植し 23ms に削減。39日間で244万回発火した実測ログから、年間約680 CPU時間が消費されていたことが判明。Go 化自体ではなく「頻度の高い箇所を絞り込んだこと」が効果的だった。pydantic のインポートコストが約84ms を占め、Go/Rust/bash では23〜25ms に収束し、プロセス fork の物理的下限に到達した。

- **ソース**: [Qiita claudecode](https://qiita.com/nomurasan/items/c227b092ba30d18aa8a1)
- **重要度**: 6/10
- **タグ**: claude-code, performance, mcp

---

## 2026-05-27

### 自宅サーバー1台にAnthropicのbotが1日4万アクセスしてきた、でも全然遅くならなかった話

Anthropic の Claude-SearchBot が個人の自宅サーバーに1日4万アクセスしても、DGX Spark 1台とCloudflare Freeの構成で平然と捌けた事例を紹介。Cloudflare の Edge キャッシュと Rate Limit、Next.js の静的レンダリングにより、オリジンサーバーへの負荷が大幅に軽減された。クラウドのオートスケーリング構成と同等の耐性を月額ほぼ0円で実現し、個人開発の上限が上がったことを実感した体験談。

- **ソース**: [Qiita claudecode](https://qiita.com/architectJapan/items/ec7669cb308277a9d4bb)
- **重要度**: 5/10
- **タグ**: claude-api, performance, setup

---

## 2026-05-15

### ハーネスを育てすぎたClaude Codeが素のClaude Codeに負ける「naked codex現象」——自己診断と対処法

Claude Code のカスタマイズを過度に行うと、設定ファイルやスキルが肥大化し、素の Claude Code よりパフォーマンスが低下する「naked codex現象」が発生する。CLAUDE.md が400行超、スキル40件超、hook10件超が警戒ライン。原因はコンテキストウィンドウの圧迫と指示の優先順位の乱れ。対処法として、使われていないルールやスキルの定期的な棚卸し、コマンドファイルへの移行、ネガティブルールの削除が推奨される。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/60adfc41690c45d59f15)
- **重要度**: 7/10
- **タグ**: claude-code, performance, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-15 | 自動生成 |
