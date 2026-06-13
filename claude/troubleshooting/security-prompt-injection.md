---
title: Security Prompt Injection
category: troubleshooting
subcategory: security-prompt-injection
tags:
- bugfix
- claude-api
- claude-code
- prompt
date: '2026-06-05'
updated: '2026-06-13'
sources:
- url: https://ai-heartland.com/security/prompt-injection-defense
  title: プロンプトインジェクションとは？攻撃手口・実例・防御策をLLM開発者向けに徹底解説｜OWASP LLM01
  date: '2026-06-05'
- url: https://zenn.dev/fixu/articles/fake-system-reminder-injection
  title: ツール結果に紛れた偽の停止指示を観測した話 — AIエージェントへの指示注入とその検出
  date: '2026-06-13'
---


# Security Prompt Injection

---

## 2026-06-13

### ツール結果に紛れた偽の停止指示を観測した話 — AIエージェントへの指示注入とその検出

AIエージェントのツール実行結果に、正規のシステム通知を装った偽の停止指示が紛れ込む事象を観測。実際のファイル作成は成功していたが「失敗した」と虚偽報告を促す内容だった。エージェントは実結果との矛盾を検証し、偽指示を検出・無視することに成功。ツール結果の検証設計の重要性を示す事例として共有。

- **ソース**: [Zenn claude](https://zenn.dev/fixu/articles/fake-system-reminder-injection)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, bugfix

---

## 2026-06-05

### プロンプトインジェクションとは？攻撃手口・実例・防御策をLLM開発者向けに徹底解説｜OWASP LLM01

プロンプトインジェクションは悪意ある入力でLLMの指示を上書きする攻撃で、OWASP LLM Top 10の最重要リスク（LLM01）に位置づけられる。直接型と間接型に分類され、AIエージェント時代において単一手段では防げない最大のセキュリティ課題とされる。入力分離・権限最小化・出力検証などの多層防御が現実的な対策として必要であり、Anthropic・OpenAI・Googleも未解決と認識している。

- **ソース**: [AI Heartland](https://ai-heartland.com/security/prompt-injection-defense)
- **重要度**: 8/10
- **タグ**: prompt, claude-api, claude-code

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-06-05 | 自動生成 |
