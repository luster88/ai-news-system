---
title: Security Privacy
category: tools
subcategory: security-privacy
tags:
- claude-api
- cowork
- mcp
- prompt
date: '2026-04-27'
updated: '2026-10-20'
sources:
- url: https://ai-heartland.com/security/pasteguard-llm-privacy-proxy
  title: PasteGuard｜LLMに送るプロンプトからPIIとAPIキーを自動マスクするプロキシ
  date: '2026-04-27'
- url: https://zenn.dev/mint69/articles/31f72b57a0206e
  title: 【個人開発】AIに社外秘や個人情報を貼る前にブラウザ内で仮名化、AIの回答を1クリックで元の名前に復元するツールを作った（通信ゼロ・無料）
  date: '2026-10-20'
---


# Security Privacy

---

## 2026-10-20

### 【個人開発】AIに社外秘や個人情報を貼る前にブラウザ内で仮名化、AIの回答を1クリックで元の名前に復元するツールを作った（通信ゼロ・無料）

AIにログやメールを貼る際の個人情報漏洩を防ぐため、ブラウザ内で完結する仮名化ツール「MaskFlow AI」が公開された。シャノン・エントロピー解析で秘密鍵を自動検出し、AI回答を1クリックで元の名前に復元できる。通信ゼロで動作し、構文を壊さないダミー値生成やCLI一括処理も提供。Pro版では50種の正規表現ルールとオフラインCLIが利用可能。

- **ソース**: [Zenn claude](https://zenn.dev/mint69/articles/31f72b57a0206e)
- **重要度**: 6/10
- **タグ**: claude-api, prompt, cowork

---

## 2026-04-27

### PasteGuard｜LLMに送るプロンプトからPIIとAPIキーを自動マスクするプロキシ

PasteGuardは、LLMに送信するプロンプトから個人情報（PII）やAPIキーを自動的にマスキングするローカル実行型プロキシツール。Microsoft Presidioを用いて11種類のPIIを24言語で検出し、OpenAI/Anthropic互換のエンドポイントとして動作する。マスクモードとルートモードの2つの動作モードがあり、機密データをクラウドに送信せずにローカルで処理することでプライバシーを保護する。商用APIの学習防止契約を技術的に補強し、無料サービスやログ保持ポリシーへの対策としても有効。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/pasteguard-llm-privacy-proxy)
- **重要度**: 6/10
- **タグ**: claude-api, mcp

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-27 | 自動生成 |
