---
title: Claude Api Error
category: troubleshooting
subcategory: claude-api-error
tags:
- bugfix
- claude-api
- cowork
- performance
date: '2026-05-11'
updated: '2026-09-12'
sources:
- url: https://zenn.dev/zoetaka38/articles/2328ea1c852dee
  title: AI consultation が突然 400 BadRequest ループに陥る原因と、3層防御で直した話
  date: '2026-05-11'
- url: https://qiita.com/picnic/items/fbe7837c24d64aa0031d
  title: Claudeで複数モデルのエラー率上昇インシデント発生、監視中
  date: '2026-08-03'
- url: https://qiita.com/syun136_616/items/5ed3d24c0b0eadbd5688
  title: Claude Fable 5.1のtool_choice仕様と400エラー対策
  date: '2026-09-06'
- url: https://qiita.com/yureki_lab/items/b2b0a91c77555f4ff020
  title: Claude API の 429(rate_limit_error)を正しく捌く実装手順 — RPMではなくトークンバケツ・retry-after・SDK自動リトライの3つのハマりどころ【2026】
  date: '2026-09-12'
---




# Claude Api Error

---

## 2026-09-12

### Claude API の 429(rate_limit_error)を正しく捌く実装手順 — RPMではなくトークンバケツ・retry-after・SDK自動リトライの3つのハマりどころ【2026】

Claude APIの429エラー(rate_limit_error)の正しい対処法を解説。レート制限はRPM/ITPM/OTPMの3本立てで、トークン数で制限に達することが多い。retry-afterヘッダーに従った待機が正解で、anthropic SDKはデフォルトで2回自動リトライするため自前リトライと重複しないよう注意が必要。max_tokensは必要最小限に指定し、プロンプトキャッシュを活用することで制限を緩和できる。

- **ソース**: [Qiita claude](https://qiita.com/yureki_lab/items/b2b0a91c77555f4ff020)
- **重要度**: 7/10
- **タグ**: claude-api, bugfix, performance

---

## 2026-09-06

### Claude Fable 5.1のtool_choice仕様と400エラー対策

Claude Fable 5.1では、拡張思考（Extended Thinking）を有効にした状態でtool_choiceに「any」や特定ツール名を指定すると400エラーが発生します。対処法として、拡張思考使用時はtool_choiceを「auto」か「none」に限定する必要があります。また、プロンプトキャッシュの読み取りコストが従来の10分の1から4分の1程度に変化したという報告があります。

- **ソース**: [Qiita claudecode](https://qiita.com/syun136_616/items/5ed3d24c0b0eadbd5688)
- **重要度**: 7/10
- **タグ**: claude-api, bugfix

---

## 2026-08-03

### Claudeで複数モデルのエラー率上昇インシデント発生、監視中

2026年8月3日、AnthropicのClaude APIで複数モデルにわたるエラー率上昇インシデントが発生。12:52 UTCに調査開始、13:30 UTCに修正実装されたが現在も監視中でResolved未達。影響を受けた開発者は該当時間帯のログ確認、リトライ処理の動作確認、ステータスページの継続的な監視が推奨される。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/fbe7837c24d64aa0031d)
- **重要度**: 7/10
- **タグ**: claude-api, bugfix, performance

---

## 2026-05-11

### AI consultation が突然 400 BadRequest ループに陥る原因と、3層防御で直した話

Claude API との会話履歴に空の assistant message が混入すると、以降すべてのリクエストが 400 BadRequest でループする障害が発生。原因は Claude API が稀に空 content を返す際、コード側でバリデーションせずに DB 保存していたこと。空文字列の事前チェック、DB 制約追加、履歴送信前フィルタの 3 層防御で解決した実例。

- **ソース**: [Zenn claude](https://zenn.dev/zoetaka38/articles/2328ea1c852dee)
- **重要度**: 6/10
- **タグ**: claude-api, bugfix, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-11 | 自動生成 |
