---
title: Setup Windows
category: troubleshooting
subcategory: setup-windows
tags:
- claude-code
- cowork
- setup
- windows
date: '2026-03-29'
updated: '2026-07-10'
sources:
- url: https://qiita.com/kan2530/items/fbac7254b3375a9fe690
  title: 【実体験】Claude Cowork（Windows）セットアップ時に仮想化が有効にできなかった話とBIOS設定での解決方法
  date: '2026-03-29'
- url: https://qiita.com/yurukusa/items/3fdb95d4eae990615961
  title: AGENTS.mdとCLAUDE.mdをsymlinkで統一したら、Windowsのメンバーだけ指示が消えていた——Git for Windowsの静かな罠
  date: '2026-06-13'
- url: https://qiita.com/kanameShiga/items/9af4d5144dc79fcada54
  title: Claude Code の【Windowsアプリ版】の会話履歴を新PCへ移行したら沼だった話（自作スクリプトで抜け出すまで）
  date: '2026-07-10'
---



# Setup Windows

---

## 2026-07-10

### Claude Code の【Windowsアプリ版】の会話履歴を新PCへ移行したら沼だった話（自作スクリプトで抜け出すまで）

Claude Code の Windows デスクトップアプリ版で、会話履歴を新PCに移行する際の落とし穴と解決法を解説。プロジェクトフォルダをコピーしても履歴は引き継がれず、作業フォルダの絶対パスに紐づく管理方式が原因。CLI版とアプリ版で異なる索引が使われており、PowerShell 5.1の罠も踏んだ。最終的に自作スクリプトを公開して移行を実現。

- **ソース**: [Qiita claude](https://qiita.com/kanameShiga/items/9af4d5144dc79fcada54)
- **重要度**: 6/10
- **タグ**: claude-code, windows, setup

---

## 2026-06-13

### AGENTS.mdとCLAUDE.mdをsymlinkで統一したら、Windowsのメンバーだけ指示が消えていた——Git for Windowsの静かな罠

AGENTS.mdとCLAUDE.mdをsymlinkで統一する際、Git for WindowsのデフォルトではCLAUDE.mdがリンク先のパス文字列のみのテキストファイルとして展開され、指示が消失する問題を解説。core.symlinks=falseが原因で、公式推奨は@AGENTS.mdによる取り込み方式。チーム開発では全員の設定統一が必要で、設定漏れは静かに動作を破壊する。

- **ソース**: [Qiita claudecode](https://qiita.com/yurukusa/items/3fdb95d4eae990615961)
- **重要度**: 7/10
- **タグ**: claude-code, windows, setup

---

## 2026-03-29

### 【実体験】Claude Cowork（Windows）セットアップ時に仮想化が有効にできなかった話とBIOS設定での解決方法

Claude CoworkをWindowsでセットアップする際に仮想化が有効にならない問題と、その解決方法を実体験に基づいて解説。Windowsの機能設定（Hyper-V、ハイパーバイザープラットフォーム）に加え、BIOS設定でAMD製CPUの場合はSVM Mode、Intel製CPUの場合はVT-xを有効化する必要がある。両方の設定を行うことで、Coworkが正常に起動できるようになる。

- **ソース**: [Qiita claude](https://qiita.com/kan2530/items/fbac7254b3375a9fe690)
- **重要度**: 6/10
- **タグ**: cowork, setup, windows

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-03-29 | 自動生成 |
