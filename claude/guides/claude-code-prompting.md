---
title: Claude Code Prompting
category: guides
subcategory: claude-code-prompting
tags:
- claude-code
- cowork
- opus
- prompt
date: '2026-07-25'
updated: '2026-11-12'
sources:
- url: https://qiita.com/chiba_hiro0514/items/eac3c952a7937a6f121c
  title: Claude Opus 5を使う上で、調整すべきclaude.md
  date: '2026-07-25'
- url: https://qiita.com/suwa_nobu/items/1dd9df248ee6f4c9dfd4
  title: CLAUDE.md に「このコードはあなたのもの」と書くと、重複したコードをまとめてくれるのか。Claude Code・Codex・Gemini
    CLI で132回試したら、まとめたのは Claude だけだった
  date: '2026-11-12'
---


# Claude Code Prompting

---

## 2026-11-12

### CLAUDE.md に「このコードはあなたのもの」と書くと、重複したコードをまとめてくれるのか。Claude Code・Codex・Gemini CLI で132回試したら、まとめたのは Claude だけだった

Claude Code の CLAUDE.md に「このコードはあなたのもの」という一文を書くと、重複コードを共通関数にまとめるようになることを132回の実験で検証。Claude は日本語・英語どちらでも効果があり、既存出力を壊さず共通化したが、Codex と Gemini CLI は指示ファイルを読んでいるにも関わらず全てコピーで対応した。ただし「No drive-by refactors」を前に置くと Claude も共通化しなくなり、コストは1.8倍に増加した。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/1dd9df248ee6f4c9dfd4)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-07-25

### Claude Opus 5を使う上で、調整すべきclaude.md

Claude Opus 5向けのclaude.md調整方法を解説。Opus 5は自動的に検証・自己修正を行うため、「再確認せよ」「検証せよ」などの従来の指示は削除すべき。長いシステムプロンプトでは終わり近くにリマインダーを配置し、ナレーション調整は肯定的な例で示す。思考機能はオフではなくlow effortで使う方がコスト効率が良い。

- **ソース**: [Qiita claudecode](https://qiita.com/chiba_hiro0514/items/eac3c952a7937a6f121c)
- **重要度**: 7/10
- **タグ**: opus, claude-code, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-25 | 自動生成 |
