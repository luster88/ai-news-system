---
title: Setup Windows
category: troubleshooting
subcategory: setup-windows
tags:
- cowork
- setup
- windows
date: '2026-03-29'
updated: '2026-03-29'
sources:
- url: https://qiita.com/kan2530/items/fbac7254b3375a9fe690
  title: 【実体験】Claude Cowork（Windows）セットアップ時に仮想化が有効にできなかった話とBIOS設定での解決方法
  date: '2026-03-29'
---

# Setup Windows

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
