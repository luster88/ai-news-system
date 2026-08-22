---
title: Comfyui Integration
category: troubleshooting
subcategory: comfyui-integration
tags:
- performance
- setup
- windows
date: '2026-08-22'
updated: '2026-08-22'
sources:
- url: https://zenn.dev/kentaro_tak/articles/comfyui-sdxl-8gb-on-demand
  title: VRAM 8GBでSDXLを「必要な時だけ」動かす。ComfyUIの起動をStart-Processで書いたら、呼び出し元が固まった
  date: '2026-08-22'
---

# Comfyui Integration

---

## 2026-08-22

### VRAM 8GBでSDXLを「必要な時だけ」動かす。ComfyUIの起動をStart-Processで書いたら、呼び出し元が固まった

VRAM 8GB環境でComfyUI+SDXLを「呼び出し時だけ起動」する構成を実装した際の技術的な罠を解説。PowerShellのStart-Processがハンドルを継承してハングする問題、HDDへのモデル配置による遅延、--highvramオプションが8GB環境で逆効果になる問題など、実装後に遭遇した3つの具体的な失敗事例と解決策を共有している。

- **ソース**: [Zenn claude](https://zenn.dev/kentaro_tak/articles/comfyui-sdxl-8gb-on-demand)
- **重要度**: 4/10
- **タグ**: setup, windows, performance

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-08-22 | 自動生成 |
