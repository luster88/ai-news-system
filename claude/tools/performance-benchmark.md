---
title: Performance Benchmark
category: tools
subcategory: performance-benchmark
tags:
- claude-code
- opus
- performance
date: '2026-10-05'
updated: '2026-10-05'
sources:
- url: https://zenn.dev/oubakiou/articles/fa3b3914e081c8
  title: 【godot-llm-gamebench】Claude Opus 5.5はEffortによってどのように性能が変わるのか
  date: '2026-10-05'
---

# Performance Benchmark

---

## 2026-10-05

### 【godot-llm-gamebench】Claude Opus 5.5はEffortによってどのように性能が変わるのか

Claude Opus 5.5のeffort設定（low/medium/high/xhigh/max）による性能比較ベンチマーク。Godotミニゲーム実装タスクで、highとxhighが平均100点で首位。highは3.3分/$1.09で完了し、gpt-6.1-solのxhigh（28.2分）より1桁速い。一方、maxは35.5分/$7.73と突出して重く、lowは速いが精度が落ちる。medium以上なら満点達成可能で、コスト効率ではhighが最適。

- **ソース**: [Zenn claude](https://zenn.dev/oubakiou/articles/fa3b3914e081c8)
- **重要度**: 6/10
- **タグ**: opus, performance, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-10-05 | 自動生成 |
