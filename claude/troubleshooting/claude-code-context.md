---
title: Claude Code Context
category: troubleshooting
subcategory: claude-code-context
tags:
- bugfix
- claude-code
- haiku
- performance
- prompt
- 新機能
date: '2026-04-17'
updated: '2026-11-23'
sources:
- url: https://zenn.dev/genda_jp/articles/9228f64c472e98
  title: 'Claude Code: スラッシュコマンドの `model` 指定が /compact を誤発火させる落とし穴'
  date: '2026-04-17'
- url: https://qiita.com/suwa_nobu/items/b465ef863f8d8608f497
  title: Claude Code はサブエージェントにも CLAUDE.md を渡していた。18回測った
  date: '2026-09-15'
- url: https://zenn.dev/ojisan_ai_lab/articles/claude-code-compact-stack-20261122
  title: Claude Codeの /compact を重ねると何が消える？ 決まり10個は残り、最初の表30行は作業を挟むと2回目で0行でした
  date: '2026-11-23'
---



# Claude Code Context

---

## 2026-11-23

### Claude Codeの /compact を重ねると何が消える？ 決まり10個は残り、最初の表30行は作業を挟むと2回目で0行でした

Claude Codeの/compactコマンドを連続実行した実験記事。会話で伝えた決まり10個は10回の圧縮後も全て保持されたが、最初に渡した経費表30行は作業を挟んだ2回目の圧縮で完全に消失した。作業を挟まずに/compactを3回続けると圧縮が拒否される。公式ドキュメントでは重要な決まりはCLAUDE.mdに記載することが推奨されている。

- **ソース**: [Zenn claude](https://zenn.dev/ojisan_ai_lab/articles/claude-code-compact-stack-20261122)
- **重要度**: 6/10
- **タグ**: claude-code, performance, prompt

---

## 2026-09-15

### Claude Code はサブエージェントにも CLAUDE.md を渡していた。18回測った

Claude Code 2.1.271で、サブエージェントに対してCLAUDE.mdを渡さない設定（omitClaudeMd）が追加されたことを18回の実測で検証した記事。以前はサブエージェント起動時に毎回CLAUDE.mdが全てコンテキストに積まれていたが、新バージョンではこれを抑制できる。--agents JSONでの定義方法と、公式ドキュメントにまだ記載がない点も指摘している。

- **ソース**: [Qiita claude](https://qiita.com/suwa_nobu/items/b465ef863f8d8608f497)
- **重要度**: 7/10
- **タグ**: claude-code, bugfix, 新機能

---

## 2026-04-17

### Claude Code: スラッシュコマンドの `model` 指定が /compact を誤発火させる落とし穴

Claude Codeのスラッシュコマンドで`model: haiku`を指定すると、Opus 1Mセッションで誤って/compactが発火する問題を報告。原因はコマンド実行時にコンテキストウィンドウが一時的に200Kに縮小するため。v2.1.76で部分的に修正されたが、Haikuは1M変種が存在しないため昇格されず問題が残存。Sonnetは429エラーに形を変えて問題が継続している。

- **ソース**: [Zenn claude](https://zenn.dev/genda_jp/articles/9228f64c472e98)
- **重要度**: 6/10
- **タグ**: claude-code, haiku, bugfix

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-04-17 | 自動生成 |
