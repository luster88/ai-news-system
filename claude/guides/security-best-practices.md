---
title: Security Best Practices
category: guides
subcategory: security-best-practices
tags:
- claude-code
- prompt
- setup
date: '2026-07-21'
updated: '2026-09-11'
sources:
- url: https://qiita.com/suzuyoshi/items/49710258b7cf11e17ae7
  title: AIに全自動でサービスを作らせたら、セキュリティはどうなる? — Claude Codeに組んだ「多層防御スタック」
  date: '2026-07-21'
- url: https://zenn.dev/stkaji/articles/1dff8ba2f4ef04
  title: AI駆動開発時代のセキュリティと開発速度の天秤
  date: '2026-09-11'
---


# Security Best Practices

---

## 2026-09-11

### AI駆動開発時代のセキュリティと開発速度の天秤

Claude Codeを用いたAI駆動開発において、開発速度の向上と引き換えにセキュリティリスクが顕在化した経験を基に、IPA『安全なウェブサイトの作り方』とOWASP ASVSを参照しながらLaravelでの具体的なセキュリティ実装を整理。AIが生成したコードの信頼性、権限管理、速度と安全性のトレードオフについて、実務者の視点で考察している。

- **ソース**: [Zenn claude](https://zenn.dev/stkaji/articles/1dff8ba2f4ef04)
- **重要度**: 6/10
- **タグ**: claude-code

---

## 2026-07-21

### AIに全自動でサービスを作らせたら、セキュリティはどうなる? — Claude Codeに組んだ「多層防御スタック」

Claude Codeで全自動開発したWebサービスのセキュリティ対策を解説。Anthropic公式のsecurity-guidanceプラグイン、Semgrep静的解析、Git Secretsなど5層の防御スタックを構築し、LLMレビューと機械的チェックを組み合わせた多層防御アプローチを実装。AIが生成するコードだからこそ、機械的なチェックを何層も挟める点を強調している。

- **ソース**: [Qiita claudecode](https://qiita.com/suzuyoshi/items/49710258b7cf11e17ae7)
- **重要度**: 7/10
- **タグ**: claude-code, setup, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-21 | 自動生成 |
