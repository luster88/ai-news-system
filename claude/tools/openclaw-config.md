---
title: Openclaw Config
category: tools
subcategory: openclaw-config
tags:
- claude-code
- setup
- 新機能
date: '2026-04-06'
updated: '2026-04-06'
sources:
- url: https://zenn.dev/dai_mywk/articles/4b354106cf6503
  title: OpenClawのLLM設定の「config」構造（LLMのモデル切り替え作業に知っておくと便利な知識）
  date: '2026-04-06'
---

# Openclaw Config

---

## 2026-04-06

### OpenClawのLLM設定の「config」構造（LLMのモデル切り替え作業に知っておくと便利な知識）

OpenClawはClaude Codeライクなインターフェースで外部LLM（特にZhipu AIのGLMシリーズ）を呼び出せるツール。設定ファイルは「プロバイダ/モデルカタログ定義」と「実際に使うモデルの選択」の2段構造になっており、モデル切り替え時のトラブルシューティングではこの2層の整合性確認が重要。BASE_URLに/v1を含めない、設定変更後の再起動、プラン側のモデル提供状況の確認も必須ポイント。

- **ソース**: [Zenn claude](https://zenn.dev/dai_mywk/articles/4b354106cf6503)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-06 | 自動生成 |
