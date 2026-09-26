---
title: Sandbox Bypass
category: troubleshooting
subcategory: sandbox-bypass
tags:
- bugfix
- claude-code
- setup
date: '2026-09-26'
updated: '2026-09-26'
sources:
- url: https://qiita.com/kai_kou/items/fbe14fb0a42c33981fe8
  title: sandbox.enabled を true にしてもクラウドでは bwrap が無く、許可リスト外へ素通りだった
  date: '2026-09-26'
---

# Sandbox Bypass

---

## 2026-09-26

### sandbox.enabled を true にしてもクラウドでは bwrap が無く、許可リスト外へ素通りだった

Claude Codeのsandbox.enabled設定をtrueにしても、クラウド実行環境ではbwrapが存在せず、network.allowedDomainsの許可リスト外へのアクセスが素通りする問題を検証。ローカルとクラウドで動作が異なる設定の実態を、実際の実行結果で確認し、補償統制の3層による代替防御策を整理。claude-code-repository-baseリポジトリの連載第6回として、自律運用における実行環境依存の穴を明らかにした記事。

- **ソース**: [Qiita claudecode](https://qiita.com/kai_kou/items/fbe14fb0a42c33981fe8)
- **重要度**: 7/10
- **タグ**: claude-code, setup, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-09-26 | 自動生成 |
