---
title: Api Security Bug
category: troubleshooting
subcategory: api-security-bug
tags:
- bugfix
- claude-code
- release
date: '2026-07-08'
updated: '2026-07-08'
sources:
- url: https://qiita.com/picnic/items/90b07be747c7966124a1
  title: Claude Code v2.1.203/204で判明したAPIキー誤送信バグとバックグラウンド機能の大型修正
  date: '2026-07-08'
---

# Api Security Bug

---

## 2026-07-08

### Claude Code v2.1.203/204で判明したAPIキー誤送信バグとバックグラウンド機能の大型修正

Claude Code v2.1.203/204で、ANTHROPIC_BASE_URLを無視してAPIキーがデフォルトエンドポイントに誤送信されるセキュリティバグが修正されました。社内プロキシやLLMゲートウェイ経由で利用している組織では、意図しない宛先への認証情報送信が発生していた可能性があります。加えて、バックグラウンドセッション機能の安定性向上として約40件の修正が実施され、ヘッドレスセッションのSessionStartフック配信不良も解消されました。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/90b07be747c7966124a1)
- **重要度**: 8/10
- **タグ**: claude-code, bugfix, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-08 | 自動生成 |
