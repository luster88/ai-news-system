---
title: Claude Code Internals
category: guides
subcategory: claude-code-internals
tags:
- claude-api
- claude-code
- cowork
- performance
- prompt
date: '2026-07-05'
updated: '2026-07-30'
sources:
- url: https://qiita.com/sukimaengineer/items/33bb83797b920e4524ab
  title: ハーネスの動作を見る ─ Claude Code はPRプロンプトをどう処理するのか
  date: '2026-07-05'
- url: https://qiita.com/megmogmog1965/items/7db66f5a5aa306c68eb8
  title: Claude Code の仕組み — ハーネスの動作と Claude API
  date: '2026-07-30'
---


# Claude Code Internals

---

## 2026-07-30

### Claude Code の仕組み — ハーネスの動作と Claude API

Claude Code の内部動作を3層構造（フロント・ハーネス・API）で体系的に解説した技術記事。Claude API のステートレス性、毎回の全量送信の仕組み、プロンプトキャッシュによるコスト最適化、セッションログからの再構築プロセスについて、実測値と構造を詳細に検証している。cache_control の目印による段階的キャッシュ構築や、1時間 TTL 設定の実態など実装レベルの知見が含まれる。

- **ソース**: [Qiita claude](https://qiita.com/megmogmog1965/items/7db66f5a5aa306c68eb8)
- **重要度**: 7/10
- **タグ**: claude-code, claude-api, performance

---

## 2026-07-05

### ハーネスの動作を見る ─ Claude Code はPRプロンプトをどう処理するのか

Claude Code がプルリクエスト操作を処理する内部動作を詳細に解説。エージェント型コーディングツールのループ構造（思考→コマンド実行→結果観察→次の判断）を5段階に分解し、stop_reason を起点とした制御フローと権限チェックの仕組みを技術的に分析している。

- **ソース**: [Qiita claudecode](https://qiita.com/sukimaengineer/items/33bb83797b920e4524ab)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-05 | 自動生成 |
