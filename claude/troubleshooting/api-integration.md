---
title: Api Integration
category: troubleshooting
subcategory: api-integration
tags:
- bugfix
- claude-api
- claude-code
- cowork
- haiku
- setup
date: '2026-05-27'
updated: '2026-10-16'
sources:
- url: https://zenn.dev/tsuzudev05/articles/github-actions-pr-review-api-journey
  title: GitHub Actions で AI 自動レビューを作るまでに全 API でハマった記録
  date: '2026-05-27'
- url: https://qiita.com/charge0315/items/4a6107cf8ac70156e405
  title: 「契約済み」は思い込みだった 〜データの軸を足す前に実際のAPIを叩く（Claude Code開発記）〜
  date: '2026-10-16'
---


# Api Integration

---

## 2026-10-16

### 「契約済み」は思い込みだった 〜データの軸を足す前に実際のAPIを叩く（Claude Code開発記）〜

Claude Code を使った株式分析システム開発で、信用取引データの取得に失敗した事例。開発者の記憶違いで API プランが不足しており、実際に API を叩いて初めて判明。無料の代替手段（PDF 解析）も検討したが保守コストを考慮してプラン変更を決定。データソース追加前に実際の API を検証する重要性を示す。

- **ソース**: [Qiita claudecode](https://qiita.com/charge0315/items/4a6107cf8ac70156e405)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, cowork

---

## 2026-05-27

### GitHub Actions で AI 自動レビューを作るまでに全 API でハマった記録

GitHub ActionsでAI自動コードレビューを実装する際に遭遇した全APIのトラブルシューティング記録。Claude、Gemini、Groqの3つのAPIを試行し、APIキーのヘッダーエラー、Geminiの課金アカウント必須問題、Groqのトークン上限超過など10回以上のエラーを解決。最終的にGroqが個人開発には最適と結論。各APIの料金体系の違いや、「無料枠あり」と「クレカ不要」が別物であることなど実践的な知見を共有。

- **ソース**: [Zenn claude](https://zenn.dev/tsuzudev05/articles/github-actions-pr-review-api-journey)
- **重要度**: 6/10
- **タグ**: claude-api, haiku, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-27 | 自動生成 |
