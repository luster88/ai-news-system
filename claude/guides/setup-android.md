---
title: Setup Android
category: guides
subcategory: setup-android
tags:
- claude-code
- linux
- setup
date: '2026-08-29'
updated: '2026-08-29'
sources:
- url: https://qiita.com/Khronos31/items/9d640434f405a7a43367
  title: Termux(Android)でClaude Codeの最新版をフル機能で動かす
  date: '2026-08-29'
---

# Setup Android

---

## 2026-08-29

### Termux(Android)でClaude Codeの最新版をフル機能で動かす

Termux（Android）上で最新版のClaude Codeをフル機能で動作させる方法を解説。proot-distroでUbuntuを用意せず、muslビルドのバイナリをpatchelfで書き換え、DNS解決のみprootで補う最小構成を提案。2.1.113以降のバージョンでAndroid向けバイナリ配布が終了したため、Alpine LinuxからmuslランタイムとlibgccをパッケージングしてLD_PRELOADを回避する詳細な手順を提供。同様の方法でCodex CLIも動作確認済み。

- **ソース**: [Qiita claudecode](https://qiita.com/Khronos31/items/9d640434f405a7a43367)
- **重要度**: 6/10
- **タグ**: claude-code, setup, linux

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-29 | 自動生成 |
