---
title: Claude Code Security
category: releases
subcategory: claude-code-security
tags:
- bugfix
- claude-code
- release
- 新機能
date: '2026-07-23'
updated: '2026-09-01'
sources:
- url: https://www.reddit.com/r/ClaudeAI/comments/1v48e9x/claude_code_just_added_native_codebase_security
  title: Claude Code just added native codebase security scanning
  date: '2026-07-23'
- url: https://qiita.com/picnic/items/ba95f05d2b78799f238b
  title: 'Claude Code v2.1.257: Fable 5.1追加と権限すり抜け修正まとめ'
  date: '2026-09-01'
---


# Claude Code Security

---

## 2026-09-01

### Claude Code v2.1.257: Fable 5.1追加と権限すり抜け修正まとめ

Claude Code v2.1.257がリリースされ、新モデルClaude Fable 5.1が追加されました。今回は権限バイパスの無効化という破壊的変更を含む、セキュリティ修正が中心です。プロジェクト設定ファイルでの権限スキップが無視されるようになり、複数の権限チェック回避の脆弱性が修正されました。autoモードにコンテナ脱出防止ルールが追加され、Bedrock/Vertex/Foundry等のサードパーティプロバイダの認証問題も修正されています。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/ba95f05d2b78799f238b)
- **重要度**: 8/10
- **タグ**: claude-code, release, bugfix

---

## 2026-07-23

### Claude Code just added native codebase security scanning

Claude Code に新機能としてネイティブのコードベースセキュリティスキャン機能が追加されました。この機能により、開発者はコードの脆弱性やセキュリティリスクを直接 Claude Code 内で検出できるようになります。開発ワークフロー内でのセキュリティチェックが統合され、より安全なコード開発が可能になります。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1v48e9x/claude_code_just_added_native_codebase_security)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-23 | 自動生成 |
