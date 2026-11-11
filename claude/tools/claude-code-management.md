---
title: Claude Code Management
category: tools
subcategory: claude-code-management
tags:
- claude-code
- mac
- opus
- prompt
- setup
- vscode
- 新機能
date: '2026-10-08'
updated: '2026-11-11'
sources:
- url: https://zenn.dev/massan3477/articles/woodlot-intro
  title: ターミナルで Claude Code を何本も走らせるのやめませんか？
  date: '2026-10-08'
- url: https://zenn.dev/nhinata/articles/tallyline-claude-code-statusline
  title: usage を何度も開くのが面倒で、Claude Code のステータスラインを自作してみた
  date: '2026-11-01'
- url: https://qiita.com/290oss/items/d175ab396601e144d5d5
  title: Claude Codeが/clearで全部忘れる問題。claude-memで記憶を持たせる前に知っておきたい4つのこと
  date: '2026-11-04'
- url: https://zenn.dev/yando/articles/bb54e3351c9512
  title: Claude の推奨にそのまま乗る前に、反対意見入りの返事を書いてくれるボタンを作った【三人寄れば文殊の知恵】
  date: '2026-11-10'
- url: https://ai-heartland.com/tool/unslop
  title: unslopとは｜AIっぽいUIをデザイナーの目で直すClaude Codeスキルを実際に動かした
  date: '2026-11-11'
---





# Claude Code Management

---

## 2026-11-11

### unslopとは｜AIっぽいUIをデザイナーの目で直すClaude Codeスキルを実際に動かした

unslopは、AI生成UIの「AIっぽさ」（紫のグラデーション、光るボタン、絵文字など）を64項目の兆候リストで洗い出し、デザイン原則に沿って修正するClaude Code向けスキル。デザイナーDamir Sokolovsky氏が開発し、GitHubで1.34万スターを獲得。実測では付属の見本画面に対し8分類74行の具体的な指摘を行番号付きで出力した。

- **ソース**: [AI Heartland](https://ai-heartland.com/tool/unslop)
- **重要度**: 6/10
- **タグ**: claude-code, vscode, 新機能

---

## 2026-11-10

### Claude の推奨にそのまま乗る前に、反対意見入りの返事を書いてくれるボタンを作った【三人寄れば文殊の知恵】

Claude Code の入力欄に「monju」ボタンを追加する mod を開発。押すと Opus 5.5 が会話履歴を第三者視点で分析し、最も強い反対意見を軸にした返答の下書きを生成する。Claude の推奨をそのまま受け入れる前に、別視点からの意見を得ることで、より慎重な意思決定を支援するツール。打ちかけの文章への意見取得や、機能追加を抑制する視点の獲得など、多様な使い方ができる。

- **ソース**: [Zenn claude](https://zenn.dev/yando/articles/bb54e3351c9512)
- **重要度**: 6/10
- **タグ**: claude-code, opus, prompt

---

## 2026-11-04

### Claude Codeが/clearで全部忘れる問題。claude-memで記憶を持たせる前に知っておきたい4つのこと

Claude Codeで/clearを実行すると会話履歴が消える問題に対し、記憶プラグインclaude-memが解決策となる。このプラグインは作業記録を自動で保存し次回の会話に要点を差し込むが、導入前に注意すべき点がある。APIキーが記録される可能性、正しいインストール方法（npx claude-mem install）の使用、記憶作成にもAI使用量がかかること、そしてフックシステムによる自動記録の仕組みを理解する必要がある。

- **ソース**: [Qiita claude](https://qiita.com/290oss/items/d175ab396601e144d5d5)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能, setup

---

## 2026-11-01

### usage を何度も開くのが面倒で、Claude Code のステータスラインを自作してみた

Claude Code のステータスラインを自作したツール tallyline の紹介記事。利用上限の使用率、コンテキストサイズ、月間累計トークン数を常時表示可能。/usage や /context を頻繁に開く手間を削減し、月単位の使用量推移を可視化できる点が特徴。Python標準ライブラリのみで実装され、依存パッケージなしで動作する。

- **ソース**: [Zenn claude](https://zenn.dev/nhinata/articles/tallyline-claude-code-statusline)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-10-08

### ターミナルで Claude Code を何本も走らせるのやめませんか？

Claude Code をターミナルで複数セッション管理する際の課題（視認性の悪さ、セッション混乱、理解負債）を解決する Mac アプリ Woodlot の紹介記事。worktree による作業分離、カード型 UI による状態可視化、AI による要約機能でセッション管理を効率化。Bedrock/API キー利用者に特に有用。

- **ソース**: [Zenn claude](https://zenn.dev/massan3477/articles/woodlot-intro)
- **重要度**: 6/10
- **タグ**: claude-code, setup, mac

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-08 | 自動生成 |
