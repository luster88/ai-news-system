---
title: Claude Code Extensions
category: tools
subcategory: claude-code-extensions
tags:
- claude-code
- cursor
- mcp
- vscode
- 新機能
date: '2026-07-22'
updated: '2026-11-05'
sources:
- url: https://ai-heartland.com/explain/hallmark-anti-ai-slop-design-skill
  title: Hallmark デザインスキル解説｜AI slopを拒みClaude Code・Cursorで使う
  date: '2026-07-22'
- url: https://zenn.dev/z_maruhira/articles/claude-code-mod-copy-blocks
  title: Claude Codeの引用・コードブロックにコピーボタンを付けるmod
  date: '2026-10-10'
- url: https://ai-heartland.com/agent/claude-mem
  title: claude-mem完全ガイド｜Claude Codeにセッションを跨ぐ永続記憶を足すOSS
  date: '2026-11-05'
---



# Claude Code Extensions

---

## 2026-11-05

### claude-mem完全ガイド｜Claude Codeにセッションを跨ぐ永続記憶を足すOSS

claude-memはClaude Codeにセッション永続記憶を追加するOSS。ツール使用をフックで自動観測し、AI要約で圧縮してSQLite/Chromaに保存、次回セッション時に関連文脈を注入する。Apache-2.0ライセンスで約11万スター、Claude Code以外にもOpenCode・Codex等に対応。ただし既定設定ではローカル完結でなく、観測モデルやCloud Sync経由で外部送信される可能性があり、プライバシー設定の確認が必要。

- **ソース**: [AI Heartland](https://ai-heartland.com/agent/claude-mem)
- **重要度**: 7/10
- **タグ**: claude-code, mcp, 新機能

---

## 2026-10-10

### Claude Codeの引用・コードブロックにコピーボタンを付けるmod

Claude Codeの引用ブロックやコードブロックに、ワンクリックでコピーできるボタンを追加するmod。Slackへの返信作成時に、行頭の記号や不要な改行を自動除去してコピー可能。modのAssistantMessage機能を使い、回答内に罫線とコピーボタンを配置。設定で表示位置を切り替え可能。

- **ソース**: [Zenn claude](https://zenn.dev/z_maruhira/articles/claude-code-mod-copy-blocks)
- **重要度**: 5/10
- **タグ**: claude-code, vscode

---

## 2026-07-22

### Hallmark デザインスキル解説｜AI slopを拒みClaude Code・Cursorで使う

Nutlope（Together AI）が公開したClaude Code・Cursor向けのデザインスキル「Hallmark」の解説記事。「AI slop（AIっぽい生成物）」を回避し、色ではなく構造から作り分けることを目的とする。build（新規生成）に加え、audit（採点）、redesign（再設計）、study（デザインDNA抽出）の4操作を提供し、57のスロップ検査ゲートと6軸採点でAIの既定値UIを避ける仕組みを持つ。GitHubスター14,933でMITライセンス。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/hallmark-anti-ai-slop-design-skill)
- **重要度**: 6/10
- **タグ**: claude-code, cursor, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-22 | 自動生成 |
