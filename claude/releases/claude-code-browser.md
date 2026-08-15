---
title: Claude Code Browser
category: releases
subcategory: claude-code-browser
tags:
- bugfix
- claude-code
- cowork
- release
- 新機能
date: '2026-07-12'
updated: '2026-08-15'
sources:
- url: https://the-decoder.com/claude-code-now-has-a-built-in-browser-that-lets-the-ai-read-click-and-type-on-external-websites
  title: Claude Code now has a built-in browser that lets the AI read, click, and
    type on external websites
  date: '2026-07-12'
- url: https://qiita.com/moha0918_/items/5acf087c20983cff5f7c
  title: Claude Code v2.1.227〜v2.1.229｜Write の read 必須が新モデルで外れる｜毎日Changelog解説
  date: '2026-08-12'
- url: https://www.reddit.com/r/ClaudeAI/comments/1vndhg6/finally_claude_code_has_autocontinue_when_limits
  title: Finally, Claude Code has “Auto-continue when limits reset”
  date: '2026-08-13'
- url: https://qiita.com/picnic/items/ec718a60bd314c5d8c90
  title: Claude Code v2.1.232まとめ：PowerShell権限バイパス等の重大修正と新機能
  date: '2026-08-14'
- url: https://qiita.com/moha0918_/items/b604352231f9a8a76a38
  title: Claude Code v2.1.233｜TodoWrite が Fable 5 / Sonnet 5 で無効に｜毎日Changelog解説
  date: '2026-08-15'
---





# Claude Code Browser

---

## 2026-08-15

### Claude Code v2.1.233｜TodoWrite が Fable 5 / Sonnet 5 で無効に｜毎日Changelog解説

Claude Code v2.1.233 で、Opus 4.8・Sonnet 5・Fable 5・Mythos 5 以降のモデルでは TodoWrite / TaskCreate などの Todo 系ツールがデフォルトで無効化されました。これにより PostToolUse hook や statusline で TodoWrite を参照している設定が動作しなくなります。CLAUDE_CODE_ENABLE_TODO_TOOLS=1 で有効化可能ですが、今後の維持は要検討です。Windows 版では v2.1.232 の Bash コマンド承認問題と NTLM 認証情報漏洩の脆弱性が修正され、GitLab マージリクエスト対応や MCP v2 の接続安定性向上も含まれます。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/b604352231f9a8a76a38)
- **重要度**: 7/10
- **タグ**: claude-code, release, bugfix

---

## 2026-08-14

### Claude Code v2.1.232まとめ：PowerShell権限バイパス等の重大修正と新機能

Claude Code v2.1.232がリリースされ、PowerShellとWindows Git Bashにおける2件の重大な権限バイパス脆弱性（critical/high）が修正されました。サブエージェントのフォーク機能がデフォルト化され、セッション間メッセージング機能が追加されています。GitLabトークンの秘匿化強化やRemote Control機能の安定化も実施されており、Windows環境のユーザーは早急なアップデートが推奨されます。

- **ソース**: [Qiita claude](https://qiita.com/picnic/items/ec718a60bd314c5d8c90)
- **重要度**: 9/10
- **タグ**: claude-code, bugfix, 新機能

---

## 2026-08-13

### Finally, Claude Code has “Auto-continue when limits reset”

Claude Code に「使用制限がリセットされた際に自動継続」する新機能が追加されました。この機能により、使用制限に達した後、制限が解除されると自動的にセッションを再開できるようになり、長時間のコーディングセッションがより快適になります。ユーザーからは便利な改善として評価されています。

- **ソース**: [Reddit r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/comments/1vndhg6/finally_claude_code_has_autocontinue_when_limits)
- **重要度**: 7/10
- **タグ**: claude-code, 新機能, cowork

---

## 2026-08-12

### Claude Code v2.1.227〜v2.1.229｜Write の read 必須が新モデルで外れる｜毎日Changelog解説

Claude Code v2.1.227〜v2.1.229のChangelog解説。v2.1.228で新モデルに限りWriteツールの「同セッション内でReadしてから書く」制約が撤廃され、未読ファイルの上書きが可能に。一方で安全性が低下する側面もある。/commit-push-prの危険フラグ自動承認廃止、claude.ai同期スキルの挙動制限、セッション後始末のバグ修正なども含まれる。

- **ソース**: [Qiita claude](https://qiita.com/moha0918_/items/5acf087c20983cff5f7c)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

### Claude Code v2.1.227〜v2.1.229｜Write の read 必須が新モデルで外れる｜毎日Changelog解説

Claude Code v2.1.227〜v2.1.229のアップデートで、Writeツールの「Read必須」制約が新モデルでは撤廃され、未読ファイルの上書きが可能になった。一方、/commit-push-prコマンドの危険フラグ自動承認が廃止され、claude.ai同期スキルのローカルコマンド実行も制限された。これらは利便性と安全性のバランスを調整する重要な変更である。

- **ソース**: [Qiita claudecode](https://qiita.com/moha0918_/items/5acf087c20983cff5f7c)
- **重要度**: 7/10
- **タグ**: claude-code, release, 新機能

---

## 2026-07-12

### Claude Code now has a built-in browser that lets the AI read, click, and type on external websites

Anthropic が Claude Code に統合ブラウザ機能を追加。AI が外部ウェブサイトを直接開き、読み取り、クリック、入力が可能に。ドキュメントサイトや課題トラッカーへのアクセスに対応し、タブベースで動作。書き込み操作には安全性チェックが適用され、購入・アカウント作成・CAPTCHA回避は同意なしでは実行されない。組織はアクセス制限やブラウザツールの無効化が可能で、ログインセッション内での操作には Chrome 拡張機能の使用を推奨。

- **ソース**: [The Decoder Claude](https://the-decoder.com/claude-code-now-has-a-built-in-browser-that-lets-the-ai-read-click-and-type-on-external-websites)
- **重要度**: 8/10
- **タグ**: claude-code, 新機能, release

---

## 関連リンク

- [Claude Info トップ](../README.md)

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-12 | 自動生成 |
