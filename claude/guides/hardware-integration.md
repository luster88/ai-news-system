---
title: Hardware Integration
category: guides
subcategory: hardware-integration
tags:
- claude-code
- cowork
- setup
- 新機能
date: '2026-05-05'
updated: '2026-11-11'
sources:
- url: https://qiita.com/moritalous/items/cd53aec76db1dec20862
  title: ハードウェアバディでClaudeとおともだち
  date: '2026-05-05'
- url: https://www.reddit.com/r/ClaudeAI/comments/1xsk5k9/instead_of_collecting_dust_claude_makes_your_old
  title: Instead of collecting dust, Claude makes your old Kindle useful again
  date: '2026-11-11'
---


# Hardware Integration

---

## 2026-11-11

### Instead of collecting dust, Claude makes your old Kindle useful again

古い Kindle（第7世代）を Claude を使って再活用するプロジェクト。Kindle を手動で jailbreak した後、Claude にコンセプト画像を与えてアプリケーションを設計・構築させた。WiFi 経由でデータを取得し、1時間ごとに更新、夜間は更新停止などのバッテリー最適化により週10%の消費に抑えることに成功。KUAL（アプリランチャー）を使用して実装。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1xsk5k9/instead_of_collecting_dust_claude_makes_your_old)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, setup

---

## 2026-05-05

### ハードウェアバディでClaudeとおともだち

Claude Desktopのハードウェアバディ機能をM5Stack Core2 For AWSに移植した実装レポート。公式のM5 StickC Plus向けコードをMicroPythonで書き直し、BLE通信の暗号化/非暗号化対応を実現。esptoolでのファームウェア書き込み、mpremoteでのスクリプト転送、Windowsでのペアリング問題などIoT開発特有の課題を解説。

- **ソース**: [Qiita claude](https://qiita.com/moritalous/items/cd53aec76db1dec20862)
- **重要度**: 6/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-05 | 自動生成 |
