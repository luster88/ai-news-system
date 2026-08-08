---
title: Claude Code Internals
category: guides
subcategory: claude-code-internals
tags:
- claude-api
- claude-code
- cowork
- mcp
- performance
- prompt
date: '2026-07-05'
updated: '2026-08-08'
sources:
- url: https://qiita.com/sukimaengineer/items/33bb83797b920e4524ab
  title: ハーネスの動作を見る ─ Claude Code はPRプロンプトをどう処理するのか
  date: '2026-07-05'
- url: https://qiita.com/megmogmog1965/items/7db66f5a5aa306c68eb8
  title: Claude Code の仕組み — ハーネスの動作と Claude API
  date: '2026-07-30'
- url: https://zenn.dev/shoujiki_panman/articles/claude-code-clone-from-scratch
  title: Claude Codeを自作したら、特別なことは何もしていなかった
  date: '2026-08-08'
---



# Claude Code Internals

---

## 2026-08-08

### Claude Codeを自作したら、特別なことは何もしていなかった

Claude Code の仕組みを自作することで、その内部動作を解明した記事。LLMは文章生成のみ可能で、実際の操作は自作コードが行う。エージェントの本質は「判断するLLM」「実行する道具」「両者を繋ぐループ」の3要素で構成される。特別な技術ではなく、確認機構・サンドボックス・権限管理などの作り込みが重要であることを実装を通じて理解した体験記。

- **ソース**: [Zenn claude](https://zenn.dev/shoujiki_panman/articles/claude-code-clone-from-scratch)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, mcp

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
