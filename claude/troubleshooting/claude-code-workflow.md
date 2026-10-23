---
title: Claude Code Workflow
category: troubleshooting
subcategory: claude-code-workflow
tags:
- bugfix
- claude-code
- cowork
- prompt
- 新機能
date: '2026-05-29'
updated: '2026-10-23'
sources:
- url: https://zenn.dev/tokium_dev/articles/human-discipline-for-ai-colleague
  title: Claude のテスト設計が信用できないので ── 振り返りと試運転SkillをAIに盛り込んだ
  date: '2026-05-29'
- url: https://zenn.dev/n314/articles/6becd34ddbe6ad
  title: Claude CodeのTeamCreateが廃止され、Plan Modeが変わったのでワークフローを見直す
  date: '2026-06-18'
- url: https://qiita.com/kaiyaku_iyada/items/a197d44386369b15d248
  title: Claude Code のスキルに人間への指示書を書かせたら、3日とも「何を報告するか」が抜けた
  date: '2026-10-23'
---



# Claude Code Workflow

---

## 2026-10-23

### Claude Code のスキルに人間への指示書を書かせたら、3日とも「何を報告するか」が抜けた

Claude Code のスキル daily-ops を使って人間向け指示書を作成する実験の記録。3日間連続で「何を報告するか」の指定が抜けるという問題が発生。指示書の書き方、バージョン履歴、実際の運用での課題（見積もり時間と実績の乖離、人間に判断を委ねる書き方が残る問題）を詳細に記録している。

- **ソース**: [Qiita claude](https://qiita.com/kaiyaku_iyada/items/a197d44386369b15d248)
- **重要度**: 4/10
- **タグ**: claude-code, prompt, cowork

---

## 2026-06-18

### Claude CodeのTeamCreateが廃止され、Plan Modeが変わったのでワークフローを見直す

Claude CodeのTeamCreate機能がv2.1.178で廃止され、Plan Modeの動作も大きく変更された。Plan Modeは独自のワークフローを最優先するため、スキルと併用すると競合する問題が発生。これに対応してサブエージェントのモデルをinheritに変更し、複数ブランチを比較するスキルやカスタムinsightsコマンドを開発してワークフローを見直した。AIによる優劣判断には限界があるものの、手動判断の補助として活用している。

- **ソース**: [Zenn claude](https://zenn.dev/n314/articles/6becd34ddbe6ad)
- **重要度**: 6/10
- **タグ**: claude-code, bugfix, 新機能

---

## 2026-05-29

### Claude のテスト設計が信用できないので ── 振り返りと試運転SkillをAIに盛り込んだ

TOKIUM の QA チームが Claude Code を使ったテスト自動化に取り組む中で、セッションをまたぐと記憶が消える問題や、完了報告と実態の食い違いといった課題に直面。人間の振り返り会と試運転の習慣を AI に適用することで、ミスパターンの抑制と課題の可視化を実現した実践記録。

- **ソース**: [Zenn claude](https://zenn.dev/tokium_dev/articles/human-discipline-for-ai-colleague)
- **重要度**: 6/10
- **タグ**: claude-code, cowork, prompt

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-29 | 自動生成 |
