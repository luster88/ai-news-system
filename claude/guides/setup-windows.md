---
title: Setup Windows
category: guides
subcategory: setup-windows
tags:
- claude-code
- cowork
- setup
- windows
date: '2026-06-20'
updated: '2026-07-11'
sources:
- url: https://qiita.com/soldierboy/items/beb47801a1c81c5b4e35
  title: Claudeにyosysとopenroad環境構築をお願いした
  date: '2026-06-20'
- url: https://zenn.dev/imaginarygate/articles/46e2514135bc01
  title: Claude Cowork導入前に確認した、Windows側のClaude関連フォルダの棚卸しメモ
  date: '2026-06-30'
- url: https://qiita.com/lumichy/items/4bfde6829df08ee60930
  title: Claude Code完了時に音声通知！Stop Hookを使ったWindows環境での自動化設定ガイド
  date: '2026-07-11'
---



# Setup Windows

---

## 2026-07-11

### Claude Code完了時に音声通知！Stop Hookを使ったWindows環境での自動化設定ガイド

Claude Codeの回答完了時にWindows環境で音声通知を自動再生する方法を解説。Stop Hookを使い、~/.claude/settings.jsonに音声再生コマンドを設定することで、バックグラウンド処理の完了を見逃さずに通知できる。tts-edgeスキルで日本語音声も生成可能で、Claude Code自身に設定を任せるプロンプト例も紹介。

- **ソース**: [Qiita claude](https://qiita.com/lumichy/items/4bfde6829df08ee60930)
- **重要度**: 6/10
- **タグ**: claude-code, setup, windows

---

## 2026-06-30

### Claude Cowork導入前に確認した、Windows側のClaude関連フォルダの棚卸しメモ

Windows環境でClaude Cowork導入前に、既存のClaude Desktop関連フォルダを確認・整理した記録。WSL/Ubuntu側でCodex CLIとClaude Codeを比較検証していたが、Claude CoworkとDesignの試用期限が迫ったため、Windows側の検証に着手。検証用フォルダを作成し、SECURITY_POLICY.mdで触らせない場所を明文化した上で、既存のClaude Desktop設定やキャッシュの存在を確認し、クリーンな状態から始めるために一度アンインストールを実施。

- **ソース**: [Zenn claude](https://zenn.dev/imaginarygate/articles/46e2514135bc01)
- **重要度**: 4/10
- **タグ**: windows, setup, cowork

---

## 2026-06-20

### Claudeにyosysとopenroad環境構築をお願いした

Claudeを使ってWSL/Ubuntu環境にyosys（論理合成）とOpenROAD（配置配線）の環境構築を実施した記事。WindowsノートPC上でWSLのメモリ割り当て調整、ビルド手順、OpenROAD GUIでのレイアウト確認方法まで、実際の構築プロセスを詳細に記録している。

- **ソース**: [Qiita claude](https://qiita.com/soldierboy/items/beb47801a1c81c5b4e35)
- **重要度**: 4/10
- **タグ**: setup, windows, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-20 | 自動生成 |
