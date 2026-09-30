---
title: Claude Api Streaming
category: guides
subcategory: claude-api-streaming
tags:
- claude-api
- prompt
- setup
- 新機能
date: '2026-06-28'
updated: '2026-09-30'
sources:
- url: https://zenn.dev/yamamoshu/articles/claude-api-streaming-ros2
  title: Claude APIのストリーミング応答をROS2で使う【リアルタイム音声合成・UI更新】
  date: '2026-06-28'
- url: https://qiita.com/yureki_lab/items/7c0307bb84b46d6f61b1
  title: Claude API のストリーミング(SSE)を Python で実装する手順 — input_json_delta を都度パースして落ちる・HTTP
    200 の後に error イベント・usage の取り違え、3つのハマりどころ【2026】
  date: '2026-09-30'
---


# Claude Api Streaming

---

## 2026-09-30

### Claude API のストリーミング(SSE)を Python で実装する手順 — input_json_delta を都度パースして落ちる・HTTP 200 の後に error イベント・usage の取り違え、3つのハマりどころ【2026】

Claude API のストリーミング実装時に遭遇する3つの落とし穴を解説。tool use 使用時の input_json_delta は断片文字列で届くため都度パースすると失敗する、HTTP 200 返却後に error イベントで失敗するケースがある、usage が message_start と message_delta の2箇所に分散して届く、という実装上の注意点を Python コード例とともに説明している。

- **ソース**: [Qiita claude](https://qiita.com/yureki_lab/items/7c0307bb84b46d6f61b1)
- **重要度**: 6/10
- **タグ**: claude-api, prompt

---

## 2026-06-28

### Claude APIのストリーミング応答をROS2で使う【リアルタイム音声合成・UI更新】

Claude API のストリーミング応答を ROS2 と組み合わせてロボット制御に活用する方法を解説。client.messages.stream() を使い、生成された文字を /llm_stream トピックにリアルタイムで流す実装例を紹介。ROS2 spin をブロックしないよう別スレッドで処理する点が重要。

- **ソース**: [Zenn claude](https://zenn.dev/yamamoshu/articles/claude-api-streaming-ros2)
- **重要度**: 6/10
- **タグ**: claude-api, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-28 | 自動生成 |
