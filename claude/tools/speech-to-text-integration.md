---
title: Speech To Text Integration
category: tools
subcategory: speech-to-text-integration
tags:
- cowork
- haiku
- mcp
date: '2026-06-15'
updated: '2026-06-15'
sources:
- url: https://zenn.dev/uya0526_design/articles/main_article_reading-speed-meter
  title: 日本語の音読を「AmiVoiceのタイムスタンプ」で測る ─ STT→Claudeで終わらせない音読コーチアプリの設計
  date: '2026-06-15'
---

# Speech To Text Integration

---

## 2026-06-15

### 日本語の音読を「AmiVoiceのタイムスタンプ」で測る ─ STT→Claudeで終わらせない音読コーチアプリの設計

AmiVoiceの音声認識タイムスタンプを活用し、日本語音読の速度と流暢性を測定するWebアプリの開発記事。STTの結果をClaudeに丸投げせず、コード側で発話速度と淀み率を計算し、Claude Haikuが1文でフィードバックする二段構えの設計を採用。Next.js APIルートでBFF構成を実現し、APIキーをブラウザに露出させない安全な実装を解説。

- **ソース**: [Zenn claude](https://zenn.dev/uya0526_design/articles/main_article_reading-speed-meter)
- **重要度**: 6/10
- **タグ**: haiku, mcp, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-15 | 自動生成 |
