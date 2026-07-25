---
title: Benchmark Evaluation
category: ecosystem
subcategory: benchmark-evaluation
tags:
- claude-code
- cowork
- cursor
- opus
- performance
- 新機能
date: '2026-04-26'
updated: '2026-07-25'
sources:
- url: https://the-decoder.com/500-investment-bankers-review-ai-outputs-and-find-none-ready-for-client-delivery
  title: 500 investment bankers review AI outputs and find none ready for client delivery
  date: '2026-04-26'
- url: https://the-decoder.com/an-ai-model-programmed-nonstop-for-19-days-on-a-single-mirrorcode-task-that-cost-2600-to-run
  title: An AI model programmed nonstop for 19 days on a single MirrorCode task that
    cost $2,600 to run
  date: '2026-06-26'
- url: https://zenn.dev/okssusucha/articles/20260707-swe-together-interactive-coding-agent-ben
  title: AIに何回ダメ出ししたかを測る、対話型ベンチSWE-Together
  date: '2026-07-25'
---



# Benchmark Evaluation

---

## 2026-07-25

### AIに何回ダメ出ししたかを測る、対話型ベンチSWE-Together

SWE-Togetherは、AIコーディングエージェントを「何回修正指示が必要だったか」で評価する新しい対話型ベンチマークです。従来のSWE-benchが最終結果のみを評価するのに対し、実際のCursorやClaude Code使用時の「途中で何度も指示を出す」体験に近い評価を実現しています。11,260件のセッション記録から109タスクを厳選し、User Correction指標で介入コストを数値化。Opus 4.8が最も手がかからず（1.38回）、pass@1との相関は-0.92と強い逆相関を示しました。

- **ソース**: [Zenn claude](https://zenn.dev/okssusucha/articles/20260707-swe-together-interactive-coding-agent-ben)
- **重要度**: 7/10
- **タグ**: claude-code, performance, cursor

---

## 2026-06-26

### An AI model programmed nonstop for 19 days on a single MirrorCode task that cost $2,600 to run

Epoch AI と METR が開発した新ベンチマーク「MirrorCode」では、AI モデルがソースコードなしで完全なプログラムを再実装する能力をテストします。Claude Opus 4.7 が 56% の解決率で首位となり、16,000 行のバイオインフォマティクスツールキットをわずか 14 時間で再実装しました。最大のタスクでは AI が 19 日間連続で作業し、実行コストは 2,600 ドルに達しましたが、最も複雑なタスクはまだ解決されていません。

- **ソース**: [The Decoder Claude](https://the-decoder.com/an-ai-model-programmed-nonstop-for-19-days-on-a-single-mirrorcode-task-that-cost-2600-to-run)
- **重要度**: 7/10
- **タグ**: opus, performance, 新機能

---

## 2026-04-26

### 500 investment bankers review AI outputs and find none ready for client delivery

投資銀行員500名がAI出力を評価した結果、GPT-5.4やClaude Opus 4.6を含むトップモデルでも、クライアント納品可能な成果物は皆無だった。BankerToolBenchという新ベンチマークで、Excel財務モデルやPowerPoint資料など実務タスクを評価。ただし半数以上の銀行員が「たたき台としては使える」と回答。

- **ソース**: [The Decoder Claude](https://the-decoder.com/500-investment-bankers-review-ai-outputs-and-find-none-ready-for-client-delivery)
- **重要度**: 6/10
- **タグ**: opus, performance, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-26 | 自動生成 |
