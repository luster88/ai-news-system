---
title: Voice Synthesis Quality
category: troubleshooting
subcategory: voice-synthesis-quality
tags:
- setup
date: '2026-11-23'
updated: '2026-11-23'
sources:
- url: https://zenn.dev/tainari/articles/irodori-tts-clone-komori-engi
  title: 【Irodori-TTS】声のクローンの「こもり」、設定では直らなかった。見本のほうを加工したら直った
  date: '2026-11-23'
---

# Voice Synthesis Quality

---

## 2026-11-23

### 【Irodori-TTS】声のクローンの「こもり」、設定では直らなかった。見本のほうを加工したら直った

Irodori-TTS で音声クローンを行った際の「こもり」問題の解決記録。モデルが高周波数帯を4-7dB減衰させることが原因で、設定変更では改善せず、見本音声の高周波数帯を事前に持ち上げる（プリエンファシス）ことで解決。さらに、モデル自身に読ませた音声を見本にすることで演技表現が改善した。GPU GTX 1660で1文9秒の処理速度。

- **ソース**: [Zenn claude](https://zenn.dev/tainari/articles/irodori-tts-clone-komori-engi)
- **重要度**: 4/10
- **タグ**: setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-11-23 | 自動生成 |
