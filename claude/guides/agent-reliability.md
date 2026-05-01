---
title: Agent Reliability
category: guides
subcategory: agent-reliability
tags:
- claude-code
- prompt
date: '2026-05-01'
updated: '2026-05-01'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/1da2d3c108fcc3be10f6
  title: AI Agent の自己診断を信用するな：「証跡必須化」ポリシーで誤報を撲滅した話
  date: '2026-05-01'
---

# Agent Reliability

---

## 2026-05-01

### AI Agent の自己診断を信用するな：「証跡必須化」ポリシーで誤報を撲滅した話

Claude Code等のAI Agentが外部システム障害を誤診断する問題を解決した事例。Agentは実際にコマンドを実行せず推論で「RAGが落ちている」と誤報告していた。対策として、診断時に必ず実コマンド実行とexit code・stderr取得を義務化し、SKILL.mdとEvalで証跡なし報告にペナルティを課す「証跡必須化」ポリシーを導入。結果、誤発動が8割減し障害診断時間も短縮された。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/1da2d3c108fcc3be10f6)
- **重要度**: 7/10
- **タグ**: claude-code, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-01 | 自動生成 |
