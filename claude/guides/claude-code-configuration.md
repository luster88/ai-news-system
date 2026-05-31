---
title: Claude Code Configuration
category: guides
subcategory: claude-code-configuration
tags:
- claude-code
- prompt
- setup
- 新機能
date: '2026-05-12'
updated: '2026-05-31'
sources:
- url: https://qiita.com/Tadashi_Kudo/items/80a6a0c8fe73bd9450c3
  title: 104kスターのKarpathy CLAUDE.mdを試したら、手元に既にあった話——グローバルCLAUDE.mdで全PJ適用済みの実態
  date: '2026-05-12'
- url: https://qiita.com/Tadashi_Kudo/items/56efa02ba181e0094ec9
  title: Claude CodeチームがMarkdownにHTMLを持ち込んだ理由——そして自分はHTMLすら読まないという現実
  date: '2026-05-19'
- url: https://qiita.com/goki602/items/8af4792b8e8794173e7c
  title: Claude Code の CLAUDE.md と Skills を使い分ける ― 常時ルールとタスク別手順の設計
  date: '2026-05-31'
---




# Claude Code Configuration

---

## 2026-05-31

### Claude Code の CLAUDE.md と Skills を使い分ける ― 常時ルールとタスク別手順の設計

Claude Code の CLAUDE.md と Skills の使い分けを解説。CLAUDE.md は毎セッション読み込まれる常時ルール（500行以下推奨）、Skills は条件付きで発動するタスク別手順書として設計されている。v2.1.152 から /reload-skills コマンドや disallowed-tools フィールドが追加され、スキル管理が強化された。description の前半 250 文字にトリガー条件を凝縮することが自動発動の鍵となる。

- **ソース**: [Qiita claudecode](https://qiita.com/goki602/items/8af4792b8e8794173e7c)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 2026-05-31

### Claude Code の CLAUDE.md と Skills を使い分ける ― 常時ルールとタスク別手順の設計

Claude Code における CLAUDE.md と Skills の使い分けを解説。CLAUDE.md は毎セッション読み込まれる常時ルール（500行以下推奨）、Skills は条件付きで発動するタスク別手順という役割分担を明確化。/init コマンドでの初期化、description フィールドによる自動発動制御、v2.1.152 の /reload-skills や disallowed-tools などの新機能も紹介している。

- **ソース**: [Qiita claude](https://qiita.com/goki602/items/8af4792b8e8794173e7c)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-05-19

### Claude CodeチームがMarkdownにHTMLを持ち込んだ理由——そして自分はHTMLすら読まないという現実

Claude CodeのCLAUDE.mdファイルにおけるHTMLコメント機能の仕様変更について解説。HTMLコメント内のテキストは自動注入時にClaudeからは隠され、人間だけが読める層となった。しかし筆者は書いたコメントを読み返さない問題に直面し、定期的なレビューや期限設定の重要性を指摘している。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/56efa02ba181e0094ec9)
- **重要度**: 6/10
- **タグ**: claude-code, setup, prompt

---

## 2026-05-12

### 104kスターのKarpathy CLAUDE.mdを試したら、手元に既にあった話——グローバルCLAUDE.mdで全PJ適用済みの実態

Andrej Karpathy氏の104kスターのCLAUDE.mdテンプレートを検証した結果、その原則の多くが既にグローバル設定で実装済みだったという実例報告。プロジェクトごとにテンプレートをコピペするのではなく、~/.claude/CLAUDE.mdにコア原則を集約し、プロジェクト固有の設定のみローカルに記述する運用方法を解説。「小さく正確な変更（Surgical Changes）」「仕様が曖昧なら質問させる」など5つのコア原則と、200行以下に抑える実践的なメンテナンス手法を紹介。

- **ソース**: [Qiita claudecode](https://qiita.com/Tadashi_Kudo/items/80a6a0c8fe73bd9450c3)
- **重要度**: 7/10
- **タグ**: claude-code, prompt, setup

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-12 | 自動生成 |
