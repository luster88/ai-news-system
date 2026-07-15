---
title: Multi Agent Memory
category: guides
subcategory: multi-agent-memory
tags:
- claude-code
- cowork
- prompt
date: '2026-07-15'
updated: '2026-07-15'
sources:
- url: https://zenn.dev/peyangu485/articles/jibun-os-shared-memory
  title: AIエージェントの記憶を揮発させない共有メモリ層を設計した
  date: '2026-07-15'
---

# Multi Agent Memory

---

## 2026-07-15

### AIエージェントの記憶を揮発させない共有メモリ層を設計した

個人開発で複数のAIエージェント（Claude/Gemini/Codex）を役割分担させる際の「記憶の分断」問題に対し、Markdown/JSONLベースの共有メモリ層を設計した事例。DBやベクトルストアではなく、episodes.jsonl（判断ログ）とINDEX.md等のファイルで構成。「3ヶ月後の別セッションが知らないと同じ穴に落ちるか」を記録基準とし、エージェント間・セッション間での暗黙知の揮発を防ぐ運用規約を確立。

- **ソース**: [Zenn claude](https://zenn.dev/peyangu485/articles/jibun-os-shared-memory)
- **重要度**: 6/10
- **タグ**: claude-code, prompt, cowork

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-15 | 自動生成 |
