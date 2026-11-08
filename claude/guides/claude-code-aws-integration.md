---
title: Claude Code Aws Integration
category: guides
subcategory: claude-code-aws-integration
tags:
- claude-code
- setup
- vscode
- 新機能
date: '2026-05-18'
updated: '2026-11-08'
sources:
- url: https://qiita.com/daitak/items/daf289a8e75e0bd4044d
  title: Agent Toolkit for AWS を使ってClaude CodeからEKSクラスタを作成してみる!
  date: '2026-05-18'
- url: https://qiita.com/emptybaba/items/ef9370aa4f9038aeecd9
  title: 一人でできることの範囲が、変わってしまった｜個人開発SaaS「fuSen」第十七話
  date: '2026-10-31'
- url: https://ai-heartland.com/explain/claude-code-output-style
  title: Claude Code出力スタイルの使い方｜Conciseで応答が短くなる仕組みと設定の落とし穴
  date: '2026-11-08'
---



# Claude Code Aws Integration

---

## 2026-11-08

### Claude Code出力スタイルの使い方｜Conciseで応答が短くなる仕組みと設定の落とし穴

Claude Codeの出力スタイル機能（Concise）を使うと応答が約36%短くなる。コマンドで設定可能だが、settings.jsonに手動で書く場合は大文字小文字を厳密に区別する必要がある（"concise"は無効で"Concise"が正しい）。設定は.claude/settings.local.jsonに保存され、この端末のみで有効。重要な警告やエラーは省略されない設計。

- **ソース**: [AI Heartland](https://ai-heartland.com/explain/claude-code-output-style)
- **重要度**: 6/10
- **タグ**: claude-code, setup, vscode

---

## 2026-10-31

### 一人でできることの範囲が、変わってしまった｜個人開発SaaS「fuSen」第十七話

個人開発者がClaude Codeを活用してWebサイト校正ツール「fuSen」を開発する経験談。ユーザー要望を当日中に実装できる環境が生まれたこと、20年間のWeb制作経験者が「デプロイって何？」状態から本番環境へのデプロイを当たり前にできるようになった変化、そして技術的な実装だけでなくユーザーとの信頼関係構築にもつながっている実感を語る。Claude Codeにより「一人でできることの範囲」が劇的に拡大した開発体験の記録。

- **ソース**: [Qiita claude](https://qiita.com/emptybaba/items/ef9370aa4f9038aeecd9)
- **重要度**: 6/10
- **タグ**: claude-code, 新機能

---

## 2026-05-18

### Agent Toolkit for AWS を使ってClaude CodeからEKSクラスタを作成してみる!

2026年5月6日にリリースされたAgent Toolkit for AWSを使い、Claude CodeからEKSクラスタを作成する手順を紹介。aws-coreプラグインをインストールし、VS Code上で対話形式でS3バケットやEKSクラスタ、ノードグループを構築。Claude Codeがバケット名の命名規則違反を自動修正したり、CloudFormationテンプレートからVPCを作成するなど、インテリジェントな動作を実証した実践記事。

- **ソース**: [Qiita claudecode](https://qiita.com/daitak/items/daf289a8e75e0bd4044d)
- **重要度**: 7/10
- **タグ**: claude-code, setup, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-05-18 | 自動生成 |
