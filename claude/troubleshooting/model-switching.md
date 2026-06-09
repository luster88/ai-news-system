---
title: Model Switching
category: troubleshooting
subcategory: model-switching
tags:
- claude-code
- opus
date: '2026-06-09'
updated: '2026-06-09'
sources:
- url: https://qiita.com/yurukusa/items/68c10b6026835b78c0b5
  title: Claude Codeで固定したはずのモデルが勝手に切り替わる——自分のログで本当に何が動いたか確かめる
  date: '2026-06-09'
---

# Model Switching

---

## 2026-06-09

### Claude Codeで固定したはずのモデルが勝手に切り替わる——自分のログで本当に何が動いたか確かめる

Claude Codeでモデルが勝手に切り替わる問題について、ローカルのJSONログ（~/.claude-code/sessions/*.jsonl）から実際の応答モデルを確認する方法を解説。jqやPython3を使った集計コマンド、ブラウザベースの可視化ツールを提供し、「Opusに固定したはずがSonnetに降格していた」などの事実を時刻付きで証明できるようにする。Anthropicへの報告に必要な具体的証拠の集め方を示す。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/68c10b6026835b78c0b5)
- **重要度**: 7/10
- **タグ**: claude-code, opus

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-09 | 自動生成 |
