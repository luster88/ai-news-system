---
title: Api Outage
category: troubleshooting
subcategory: api-outage
tags:
- bugfix
- claude-api
- opus
- sonnet
date: '2026-06-05'
updated: '2026-06-16'
sources:
- url: https://qiita.com/picnic/items/2e22aeba610255b45641
  title: Claude API 障害レポート：複数モデルでエラー率上昇・約3.5時間で完全復旧
  date: '2026-06-05'
- url: https://qiita.com/picnic/items/9f78b0e3dec2aae45dfe
  title: 'Claude APIで複数モデル同時障害: Sonnet/Opusで最大10%エラー率上昇の全容'
  date: '2026-06-16'
---


# Api Outage

---

## 2026-06-16

### Claude APIで複数モデル同時障害: Sonnet/Opusで最大10%エラー率上昇の全容

2026年6月16日にClaude APIで大規模障害が発生し、Sonnet/Opus全モデルで最大10%のエラー率上昇を記録。同日中に解決済みだが、本番運用では公式SDKのリトライ機能（max_retries）活用とステータスページ監視が推奨される。コード変更は不要だが、該当時間帯のエラーログ確認が望ましい。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/9f78b0e3dec2aae45dfe)
- **重要度**: 8/10
- **タグ**: claude-api, bugfix, sonnet

---

## 2026-06-05

### Claude API 障害レポート：複数モデルでエラー率上昇・約3.5時間で完全復旧

2026年6月5日、Claude APIで複数モデル（Opus 4.5-4.8、Sonnet 4.6）のエラー率が上昇する障害が発生し、約3.5時間で完全復旧しました。特にOpus 4.7/4.8は復旧に時間を要しました。本番環境での利用者向けに、ステータスページ監視・フォールバック設計・タイムアウト設定・リトライロジックの実装が推奨されています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/2e22aeba610255b45641)
- **重要度**: 7/10
- **タグ**: claude-api, opus, sonnet

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-05 | 自動生成 |
